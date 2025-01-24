FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=mydatabase

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306



















# Use the official MySQL image from the Docker Hub
#FROM mysql:latest

# Set the MySQL root password
#ENV MYSQL_ROOT_PASSWORD=root

# Set the MySQL database name
#ENV MYSQL_DATABASE=mydatabase

# Copy the SQL script to the Docker container
#COPY init.sql /docker-entrypoint-initdb.d/

# Expose the default MySQL port
#EXPOSE 3306

