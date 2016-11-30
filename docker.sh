#!/bin/bash

#Descarga docker
sudo apt-get update
sudo apt-get install -y docker.io
# Inicia el servicio docker
sudo service docker start
sudo docker -d &
#Descarga la imagen
sudo docker pull sergiocaceres/iv
#Ejecuta la imagen
sudo docker run -i -t sergiocaceres/iv /bin/bash 

#Tras ejecutar el script ejecutar "cd IV && make execute"
