FROM mongo:4.4.1

COPY ./entry/docker-entrypoint-initdb.sh /docker-entrypoint-initdb.d/

RUN chmod -R 755 /docker-entrypoint-initdb.d/
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["mongod"]
