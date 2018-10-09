#  Cheat sheet - Familiarize with Docker and Docker Hub:

Commands that helped me to iteract with docker and create a public repository on DockerHub.

```bash
docker #Show all comands
docker search ubuntu #Search image
docker pull ubuntu #Download image
docker run ubuntu #Run an image
docker images #Show all images already downloaded
docker ps #Show activated images
docker ps -a #Show activated and desactivated images
docker run -it ubuntu #Acess to terminal inside container
sudo docker commit -m "message" -a "Author" 996cc7227002 finid/ubuntu-nodejs #Save image after doing changes
docker stop container-id 

docker login -u mrsequeira
docker tag finid/ubuntu-nodejs:latest mrsequeira/ubuntu-nodejs:myfirstimagepush #Tag created image to docker hub repository
docker push mrsequeira/ubuntu-nodejs:myfirstimagepush
``` 

The objective was to make an image using Ubuntu with node.js already installed.
Ref: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04