#!/bin/bash

sudo apt-get update

# Instalamos vagrant
sudo wget https://releases.hashicorp.com/vagrant/1.8.6/vagrant_1.8.6_i686.deb
sudo dpkg -i vagrant_1.8.6_i686.deb

# Instalar plugin para azure
sudo vagrant plugin install vagrant-azure

# Instalación Ansible
sudo apt-get install ansible


# Despliegue en Azure
sudo vagrant up --provider=azure

#Instalamos Fabric
sudo apt-get install fabric

# Despliegue de la aplicación con Fabric

# Actualiza el supervisor
fab -p Abecedario1234# -H sergio@comunibot.cloudapp.net recargar
#Inicia el supervisor
#fab -p Abecedario1234# -H sergio@comunibot.cloudapp.net iniciar

#Inicia con nohup
fab -p Abecedario1234# -H sergio@comunibot.cloudapp.net iniciar_hup
