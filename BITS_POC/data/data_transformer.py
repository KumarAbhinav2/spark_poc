def normalizer(data, mean, std):
    """
    Normalize features by standard deviation
    data is a ndarray
    """
    return (data - mean) / std