Below is the SQL script and the Dockerfile to run a MySQL container with the provided script.

### SQL Script
```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root';
FLUSH PRIVILEGES;
CREATE DATABASE mydatabase;
USE mydatabase;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(100) NOT NULL,
    city VARCHAR(100),
    data TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Dockerfile
```Dockerfile
# Use the official MySQL image from the Docker Hub
FROM mysql:latest

# Set the MySQL root password
ENV MYSQL_ROOT_PASSWORD=root

# Set the MySQL database name
ENV MYSQL_DATABASE=mydatabase

# Copy the SQL script to the Docker container
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the default MySQL port
EXPOSE 3306
```

### Steps to Build and Run the Docker Container
1. Save the SQL script to a file named `init.sql`.
2. Save the Dockerfile to a file named `Dockerfile`.
3. Open a terminal and navigate to the directory where the `init.sql` and `Dockerfile` are saved.
4. Build the Docker image using the following command:
   ```sh
   docker build -t my-mysql-image .
   ```
5. Run the Docker container using the following command:
   ```sh
   docker run -d -p 3306:3306 --name my-mysql-container my-mysql-image
   ```

This will start a MySQL container with the database and table set up according to your script. 
