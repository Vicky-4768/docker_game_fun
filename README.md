# Simple Number Game

This is a simple web application for playing a number guessing game. The application is built with Flask and uses MySQL for the database.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/Vicky-4768/docker_game_fun.git
   cd docker_game_fun
   ```

2. Build and run the Docker containers:

   ```sh
   docker-compose up --build -d
   ```

3. Visit in your browser to access the application.
   ```
   localhost:5000
   ``` 

## Clean Up

To delete all containers and images, run:

```sh
. dq.sh
```

## Directory Structure

```
Simple_Number_Game/
├── app.py
├── Dockerfile
├── req.txt
├── templates/
│   ├── game.html
│   ├── index.html
│   └── reveal.html
└── sup_sql/
    ├── Dockerfile
    └── init.sql
```

## Additional Information

- The MySQL database is initialized using the `init.sql` script located in the `sup_sql` directory.
- Ensure Docker and Docker Compose are installed on your machine before running the setup commands.


