FROM abhinav85/bits_spark_base

# -- Runtime

USER root
ARG spark_version=3.1.1
ARG hadoop_version=3.2

RUN chmod -R 777 /usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}/ 
RUN chmod -R 777 /usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}/logs
RUN chmod -R 777 /usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}/bin
RUN chgrp root /etc/passwd && chmod ug+rw /etc/passwd
ARG spark_worker_web_ui=8082

EXPOSE ${spark_worker_web_ui}

ADD ep.sh /opt/
RUN chmod -R 777 /opt/ep.sh
ENTRYPOINT ["/opt/ep.sh"]
CMD bin/spark-class org.apache.spark.deploy.worker.Worker spark://${SP_MASTER_HOST}:7077 >> logs/spark-worker.out
