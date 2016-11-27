FROM ubuntu:14.04
MAINTAINER Sergio Cáceres Pintor <sergiocaceres@correo.ugr.es>

#Instalamos git
RUN sudo apt-get -y update
RUN sudo apt-get install -y git

#Clonamos el repositorio
RUN sudo git clone https://github.com/sergiocaceres/IV.git

#Instalamos las herramientas de python necesarias
#Instalamos las herramientas de python necesarias
RUN sudo apt-get -y install python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip

#Instalamos los requerimientos necesarios
RUN cd IV/ && make install

ENV TOKENBOT="287783764:AAGiiRJgG4cKfgGOKbTMCLbqtzA4AsEyprE"
ENV PASS_BD="2BhNndeKPkBdn7K3jfSvrou0M_"
ENV USR_BD="ersdwrualbmqkz"

CMD cd IV/ && make execute

