FROM abhinav85/bits_cluster_base

# -- Layer: Apache Spark

USER root
ARG spark_version=3.1.1
ARG hadoop_version=3.2

RUN apt-get update -y && \
    apt-get install -y curl && \
    curl https://archive.apache.org/dist/spark/spark-${spark_version}/spark-${spark_version}-bin-hadoop${hadoop_version}.tgz -o spark.tgz && \
    tar -xf spark.tgz && \
    mv spark-${spark_version}-bin-hadoop${hadoop_version} /usr/bin/ && \
    mkdir /usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}/logs && \
    chmod -R 777 /usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}/logs && \
    chmod -R 777 /opt/ && \
    #chgrp root /etc/passwd && chmod ug+rw /etc/passwd && \
    rm spark.tgz

ENV SPARK_HOME /usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}
ENV SP_MASTER_HOST sp-master
ENV SP_MASTER_PORT 7077
ENV PYSPARK_PYTHON python3

WORKDIR ${SPARK_HOME}

