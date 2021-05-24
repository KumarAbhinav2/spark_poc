FROM abhinav85/bits_spark_base

# -- Runtime
USER root
RUN chgrp root /etc/passwd && chmod ug+rw /etc/passwd
ARG spark_master_web_ui=8080

EXPOSE ${spark_master_web_ui} ${SP_MASTER_PORT}
ADD ep.sh /opt/
RUN chmod -R 777 /opt/ep.sh
ENTRYPOINT ["/opt/ep.sh"]
CMD bin/spark-class org.apache.spark.deploy.master.Master >> logs/spark-master.out
