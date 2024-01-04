FROM mysql
COPY ./src/database/init.sql /docker-entrypoint-initdb.d/