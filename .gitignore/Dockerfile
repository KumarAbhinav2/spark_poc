FROM aturner/java-python

USER root
COPY ./code
ARG spark_version=3.1.1
ARG hadoop_version=3.2

RUN mkdir spark-3.1.1-bin-hadoop3.2/logs
RUN mv sparkk-3.1.1-bin-hadoop3.2 /opt/app-root
RUN chmod -R 777 /opt/app-root/spark-3.1.1-bin-hadoop3.2/*
RUN chmod -R 777 /opt/app-root/spark-3.1.1-bin-hadoop3.2/bin/*
RUN chmod -R 777 /opt/app-root/spark-3.1.1-bin-hadoop3.2/logs/

ENV SPARK_HOME /opt/app-root/spark-${spark_version}-bin-hadoop${hadoop_version}
ENV SPARK_MASTER_PORT 7077
ENV PYSPARK_PYTHON python3

WORKDIR ${SPARK_HOME}
ARG spark_worker_web_ui=8081
EXPOSE ${spark_worker_web_ui}

CMD bin/spark-class org.apache.spark.deploy.worker.Worker spark://10.130.34.160:7077 >> logs/spark-worker.out

