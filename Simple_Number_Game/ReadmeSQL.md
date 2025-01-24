! Let's get you set up with a root password and create a new user.

### Setting a Password for the Root User
1. **Log in to MySQL as the root user:**
    ```bash
    sudo mysql
    ```

2. **Set a new password for the root user:**
    ```sql
    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'new_password';
    FLUSH PRIVILEGES;
    ```

Replace `new_password` with your desired password.

### Creating a New User
1. **Log in to MySQL as the root user:**
    ```bash
    sudo mysql -u root -p
    ```

2. **Create a new user:**
    ```sql
    CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'user_password';
    ```

Replace `new_user` with your desired username and `user_password` with your desired password.

3. **Grant privileges to the new user:**
    ```sql
    GRANT ALL PRIVILEGES ON mydatabase.* TO 'new_user'@'localhost';
    FLUSH PRIVILEGES;
    ```

This will give the new user full access to the `mydatabase` database.

### Checking User Belonging
To check which users belong to the MySQL server, you can run the following command:

```sql
SELECT user, host FROM mysql.user;
```

This will display a list of all users and their associated hosts.

If you don't have a users table yet, you can create one with the following command:
```sql
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

Feel free to customize the commands according to your needs. Let me know if you need any more help!
