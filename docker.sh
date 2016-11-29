#!/bin/bash

#Descarga la imagen
sudo docker pull sergiocaceres/iv
#Ejecuta la imagen
sudo docker run -i -t sergiocaceres/iv /bin/bash 

#Tras ejecutar el script ejecutar "cd IV && make execute"
