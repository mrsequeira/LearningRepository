#  Cheat sheet - Familiarize with Docker and Docker Hub:

Commands that helped me to iteract with docker and create a public repository on DockerHub.

## Basics
```bash
docker #Show all comands
docker search ubuntu #Search image
docker pull ubuntu #Download image
docker run ubuntu #Run an image
docker images #Show all images already downloaded
docker ps #Show activated images and more info
docker ps -a #Show activated and desactivated images
docker stop container-id 
docker run -it ubuntu #Acess to terminal inside container(foreground mode, allocating pseudo-tty)
    #Options
    -v <host-dir>:<container-dir> #Persisting Data
    -d  # Detached mode
    --name <NAME> #run and give a new name VERIFY
    -p <specific-port>:<specific-port> <container-name|container-id> # Run image to specified port and name

sudo docker commit -m "message" -a "Author" 996cc7227002 finid/ubuntu-nodejs #Save image after doing changes
docker login -u mrsequeira
docker tag finid/ubuntu-nodejs:latest mrsequeira/ubuntu-nodejs:myfirstimagepush #Tag created image to docker hub repository
docker push mrsequeira/ubuntu-nodejs:myfirstimagepush
``` 

## Debug
```bash
docker ps #Show activated images and more info(port, name, status, etc)
docker logs <container-name|container-id>
docker inspect <container-name|container-id> #details about a running container.
docker port container-name <port>
``` 

## Dockerfile
```bash
FROM <container-name:tag>
COPY <src> <dest>
EXPOSE <port>

CMD ["example", "-a", "finish this;"]#If the command requires arguments then it's recommended to use an array
``` 
## Turning dockerfile into an image
```bash
docker build -t <name-image:tag> <build-directory> #use tags to reference a version number, 
``` 

## ex
```bash

``` 
## ex
```bash

``` 





Refs:
https://docs.docker.com/engine/reference/builder/
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04

Where to learn:
https://www.katacoda.com/ 
