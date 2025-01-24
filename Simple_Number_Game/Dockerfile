# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY req.txt .

# Install the required packages
RUN pip install --no-cache-dir -r req.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Set the environment variables for Flask and SQL
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production
ENV MYSQL_HOST=-my-mysql-container
ENV MYSQL_PORT=3306
ENV MYSQL_USER=your-root
ENV MYSQL_PASSWORD=root
ENV MYSQL_DB=your-mydatabase

# Command to run the app
CMD ["python", "app.py"]

