import gzip

import numpy

from BITS_POC.dataset import base_common
from BITS_POC.dataset.transformer import *

SOURCE_URL = 'http://yann.lecun.com/exdb/mnist/'

TRAIN_MEAN = 0.13066047740239506 * 255
TRAIN_STD = 0.3081078 * 255
TEST_MEAN = 0.13251460696903547 * 255
TEST_STD = 0.31048024 * 255


def _read32(bytestream):
    dt = numpy.dtype(numpy.uint32).newbyteorder('>')
    return numpy.frombuffer(bytestream.read(4), dtype=dt)[0]


def extract_images(f):
    """Extract the images into a 4D uint8 numpy array [index, y, x, depth].

    :param: f: A file object that can be passed into a gzip reader.
    :return: data: A 4D unit8 numpy array [index, y, x, depth].
    :raise: ValueError: If the bytestream does not start with 2051.

    """
    print('Extracting', f.name)
    with gzip.GzipFile(fileobj=f) as bytestream:
        magic = _read32(bytestream)
        if magic != 2051:
            raise ValueError(
                'Invalid magic number %d in MNIST image file: %s' %
                (magic, f.name))
        num_images = _read32(bytestream)
        rows = _read32(bytestream)
        cols = _read32(bytestream)
        buf = bytestream.read(rows * cols * num_images)
        data = numpy.frombuffer(buf, dtype=numpy.uint8)
        data = data.reshape(num_images, rows, cols, 1)
        return data


def extract_labels(f):
    print('Extracting', f.name)
    with gzip.GzipFile(fileobj=f) as bytestream:
        magic = _read32(bytestream)
        if magic != 2049:
            raise ValueError(
                'Invalid magic number %d in MNIST label file: %s' %
                (magic, f.name))
        num_items = _read32(bytestream)
        buf = bytestream.read(num_items)
        labels = numpy.frombuffer(buf, dtype=numpy.uint8)
        return labels


def read_data_sets(train_dir, data_type="train"):
    TRAIN_IMAGES = 'train-images-idx3-ubyte.gz'
    TRAIN_LABELS = 'train-labels-idx1-ubyte.gz'
    TEST_IMAGES = 't10k-images-idx3-ubyte.gz'
    TEST_LABELS = 't10k-labels-idx1-ubyte.gz'

    if data_type == "train":
        local_file = base_common.maybe_download(TRAIN_IMAGES, train_dir,
                                         SOURCE_URL + TRAIN_IMAGES)
        with open(local_file, 'rb') as f:
            train_images = extract_images(f)

        local_file = base_common.maybe_download(TRAIN_LABELS, train_dir,
                                         SOURCE_URL + TRAIN_LABELS)
        with open(local_file, 'rb') as f:
            train_labels = extract_labels(f)
        return train_images, train_labels

    else:
        local_file = base_common.maybe_download(TEST_IMAGES, train_dir,
                                         SOURCE_URL + TEST_IMAGES)
        with open(local_file, 'rb') as f:
            test_images = extract_images(f)

        local_file = base_common.maybe_download(TEST_LABELS, train_dir,
                                         SOURCE_URL + TEST_LABELS)
        with open(local_file, 'rb') as f:
            test_labels = extract_labels(f)
        return test_images, test_labels


def load_data(location="/tmp/mnist"):
    (train_images, train_labels) = read_data_sets(location, "train")
    (test_images, test_labels) = read_data_sets(location, "test")
    X_train = normalizer(train_images, TRAIN_MEAN, TRAIN_STD)
    X_test = normalizer(test_images, TRAIN_MEAN, TRAIN_STD)
    Y_train = train_labels + 1
    Y_test = test_labels + 1
    return (X_train, Y_train), (X_test, Y_test)


if __name__ == "__main__":
    train, _ = read_data_sets("/tmp/mnist/", "train")
    test, _ = read_data_sets("/tmp/mnist", "test")
    assert numpy.abs(numpy.mean(train) - TRAIN_MEAN) / TRAIN_MEAN < 1e-7
    assert numpy.abs(numpy.std(train) - TRAIN_STD) / TRAIN_STD < 1e-7
    assert numpy.abs(numpy.mean(test) - TEST_MEAN) / TEST_MEAN < 1e-7
    assert numpy.abs(numpy.std(test) - TEST_STD) / TEST_STD < 1e-7