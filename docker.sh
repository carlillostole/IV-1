#!/bin/bash

#Tras ejecutar el script no olvidar de ejecutar "cd IV && make run"

#Descarga la imagen
sudo docker pull sergiocaceres/iv
#Ejecuta la imagen
sudo docker run -i -t sergiocaceres/iv /bin/bash 
