FROM abhinav85/bits_cluster_base

# -- Layer: JupyterLab

USER root

ARG spark_version=3.1.1
ARG jupyterlab_version=3.0.10

RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    chmod -R 777 / && \ 
    pip3 install wget pyspark==${spark_version} jupyterlab==${jupyterlab_version}

# -- Runtime

EXPOSE 8888
WORKDIR ${SHARED_WORKSPACE}
CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=
