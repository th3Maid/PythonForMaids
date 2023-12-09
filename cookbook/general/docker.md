# Docker and Composer CheatSheet

## Docker:

Build an image:

    docker build -t image_name:tag .

Run a container:

    docker run -d --name container_name image_name:tag

List running containers:

    docker ps

Stop a container:

    docker stop container_name

Remove a container:

    docker rm container_name

List all images:

    docker images

Remove an image:

    docker rmi image_name:tag

Execute a command in a running container:
    
    docker exec -it container_name command

View container logs:

    docker logs container_name

## Docker Compose:

Run services defined in docker-compose.yml:
    
    docker-compose up

Run services in the background:
    
    docker-compose up -d

Stop services:
    
    docker-compose down

List services status:
    
    docker-compose ps

Rebuild services:

    docker-compose up --build