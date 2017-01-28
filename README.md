# Repositorio de las prácticas



##Práctica 0: Git y Github

###Prerrequisitos

- [x] 	Haber rellenado en la hoja de cálculo correspondiente la equivalencia entre nombre real y nick en GitHub

- [x]	Haber cumplimentado los objetivos de la primera sesión

###Objetivos

#### Creación de par de claves y añadirlo a Github

Debemos realizar los siguientes pasos:

1. ``ssh-keygen -t rsa -C "sergiocaceres@correo.ugr.es"``
2. Una vez creada la clave, debemos copiarla. Para ello hacemos lo siguiente: ``cat /home/sergio/.ssh/id_rsa.pub`` Copiamos lo que nos imprime por pantalla y eso lo pegamos en la configuración de SSH que se encuentra en nuestro perfil de Github.
3. Una vez hecho esto, ya tendremos lista nuestro par de claves y podremos subir archivos sin necesidad de poner nuestro usuario y contraseña de Github

#### Creación correcta del nombre y correo electrónico 

Para que aparezcan en los commits nuestro nombre y correo debemos poner las siguientes órdenes:

``git config --global user.name "Sergio Cáceres" `` para el nombre

``git config --global  user.email"sergiocaceres@correo.ugr.es"`` para el correo.

#### Edición del perfil de Github

Simplemente ingresamos en nuestro Github y pulsamos sobre "Edit Profile". Una vez dentro podemos observar como existen diversos campos para completar según queramos

#### Creación de la rama hito0

Nos dirigimos a nuestro repositorio creado para esta asignatura, en mi caso IV, y en el desplegable donde pone Branch, añadimos uno nuevo.

#### Realizar el fork de la carpeta de la asignatura

Acudimos al repositorio del que queremos hacer el fork y pulsamos sobre el botón "Fork".

#### Licencias y fichero Readme

Añadimos las licencias una vez creado nuestro repositorio. Modificamos el archivo Readme para incluir información relavante de nuestro proyecto.
Para poder añadirlos a nuestro repositorio basta con hacer ``git add nombre_fichero_a_subir``

``git commit -m "Descripción de lo que hemos subido``

``git push origin hito0``

#### Pull Request

Para finalizar esta práctica, debemos hacer un Pull Request para que nuestros archivos se suban al repositorio común de la asignatura



##Primer hito: Estructuración y tema del proyecto.

###Prerrequisitos

- [x] Tener aprobado el hito 0 de proyecto
- [x] Haber alcanzado el 80% de los objetivos del tema introductorio 
- [x] Haber realizado los ejercicios propuestos.

#### Proyecto elegido y breve descripción

Para el proyecto de esta asignatura he decidido realizar un bot de Telegram. Con este bot se pretende resolver el problema de los jugadores de Comunio(una página web en la que se juegan ligas internas en la que existen una serie de puntuaciones para cada jugador según haya jugado en dicha jornada de liga) en la que se podrá consultar el mercado de fichajes, la alineación que tiene para esa jornada y muchas más opciones que se irán indicando en hitos posteriores.

#### Servicios necesarios

- Servidor de base de datos
- Python para la creación del bot
- Despliegue en la nube
- API para el bot de Telegram
- API para acceso a Comunio
- Monitorización


##Segundo hito: Integración continua

###Prerequisitos

- [x] Haber alcanzado el 80% de los objetivos del tema introductorio tras haber realizado los ejercicios propuestos.

En este hito hemos visto como añadir integración continua a nuestro proyecto.

Deberemos subir nuestro proyecto y sincronizarlo con Travis-CI para que realice la integración continua. Primero necesitamos enlazar la cuenta de GitHub al servicio, una vez realizado esto, debemos indicarle que repostorios queremos que controle y una vez hecho esto, indicarle como se compila, las dependencias que debe usar y la ejecución del test. Esto es simplemente añadir un fichero .travis.yml con lo descrito anteriormente. Mi archivo .travis.yml es el siguiente:

```
language: python
python:
  - "2.7"

# command to install dependencies
install: make install

# command to run tests
script: make test
```

Le estamos indicando el lenguaje que usamos, la instalación de las dependencias y la ejecución mediante un fichero Makefile. Dicho fichero es el siguiente:

```
install:
	pip install -r requirements.txt

test:
	cd bot_telegram && python test.py

execute:
	cd bot_telegram && python bot.py
```

Nos fijamos en cada opción del Makefile. La primera opción "install" nos instala las dependencias que necesitamos, las cuales las tenemos en el fichero requirements.txt (más adelante lo mostraré). La siguiente opción es "test", llamando a test.py que es donde lo tenemos definido. Por último la opción "execute" que nos ejecutaría el bot

Por tanto, Travis analizará cada commit que se realice al repositorio y realizará un test para ver si está correcto o no (por ahora un test de prueba).

![Imagen 1](http://i68.tinypic.com/htd0ur.png)

Y travis nos dice lo siguiente:

![Imagen 2](http://i63.tinypic.com/1z64n6c.png)

![Imagen 3](http://i67.tinypic.com/2evck13.png)

Podemos ver que ha funcionado correctamente y por eso se nos genera el icono en verde que pone "build passing", insertado al inicio de este documento.

![Imagen 4](http://i66.tinypic.com/6gvh8j.png)

También le hemos dicho a travis que tenemos una variable de entorno y que queremos que guarde su valor. Para ello, accedemos a los ajustes del repositorio donde lo queremos y añadimos el nombre y su valor. Quedaría algo asi:

![Imagen 5](http://i64.tinypic.com/rkos42.png)


##Tercer hito: Despliegue en un PaaS

###Prerequisitos
- [x]	Haber alcanzado el 60% de los objetivos del tema correspondiente tras haber realizado los ejercicios propuestos. Haber superado el hito anterior de la práctica.

En este hito hemos visto como desplegar nuestra aplicación en un PaaS. 

Para este hito he decidido realizar el despliegue en Heroku. Para ello, nos hemos tenido que registrar en la web y a partir de ahi crear una aplicación con una base de datos. La base de datos que he usado ha sido la propia de Heroku (PostgreSQL) y que está alojada en AmazonAWS. Para acceder a dicha base de datos realizamos lo siguiente (en el código de nuestro botesta hecho):

```
con_bd = psycopg2.connect(database='d6f0n6kc34qjo7',user=(os.environ["USR_BD"]),password=(os.environ["PASS_BD"]),host='ec2-54-225-117-56.compute-1.amazonaws.com')
```
donde, para ello, nos hemos definido dos variables de entorno, llamadas ```USR_BD y PASS_BD``` para no mostrarlo públicamente y que alguien nos pueda modificar las tablas.

He hecho exactamente lo mismo con el Token del Bot. 

Añadir que para que Travis pase los test y Heroku funcione correctamente, en el apartado Settings de ambos servicios debemos configurar estas variables con su valor.

Una vez hecho esto, accedemos a la web de Heroku y seleccionamos la casilla que dice que tras pasar los test de Travis nuestra aplicación se subirá a Heroku. Esto es marcando simplemente esta casilla:

![Imagen 6](http://i68.tinypic.com/2m4ocab.png)

Por tanto, cada vez que hagamos un push a nuestro repositorio se esperará a que pase los test de Travis. Si lo logra, la aplicación se despliegue en Heroku.

Para el despliegue necesitaremos un fichero llamada Procfile, cuyo contenido es el siguiente:

```
worker: cd bot_telegram && python bot.py 
```

Como se trata de un bot de Telegram, necesitamos poner "worker" o "bot" para que a los 60 segundos sin recibir peticiones no se caiga. SI tuviesemos páginas webs simplemente con poner web bastaría.

Este fichero debe encontrarse en la raíz y es el archivo que Heroku ejecuta, por tanto, debemos decirle que ejecute el bot, en mi caso el fichero bot.py.

A parte, he creado un archivo llamado runtime.txt que contiene la versión de Python que estamos usando. El contenido de dicho fichero es el siguiente:

```
python-2.7.12 
```

Una vez que tengamos nuestros ficheros de forma correcta, nos disponemos a subirlo a Heroku. Para ello simplemente nos creamos una nuesva aplicación, le damos el nombre que queramos y configuramos su despliegue como expliqué anteriormente, sincronizado con GitHub.

Para acceder a la base de datos y ahi poder crear las tablas que deseemos, tenemos que poner la orden 

```
heroku logs --tail --ps postgres --app <nombre_app>
```
o, podemos acceder a las características de nuestra base de datos(que se encuentra en la página de Heroku), y copiar la url que aparece en Heroku CLI en nuestra terminal. 

Una vez que tenemos el bot listo, solo falta comprobar que está lanzado y ejecutándose. Lo vemos en los logs:

![Imagen 7](http://i67.tinypic.com/35brp7b.png)

Ahi podemos ver que nuestro bot está lanzado y funcionando.

En definitiva, hemos visto como configurar el despliegue en Heroku, usar la base de datos que Heroku nos proporciona como es PostgreSQL y los diferentes archivos de configuración que necesitamos para que la aplicación funcione correctamente. 

Podremos probar nuestra aplicación hablando al bot por el nombre de **@Comuni_bot**. Veamos simplemente un /start para ver que nos responde:

![Imagen 8](http://i66.tinypic.com/r0nq50.jpg)


##Cuarto hito: Entorno de pruebas

###Prerequisitos

- [x] Haber alcanzado el 70% de los objetivos de las sesiones hasta este hito. En el caso de que no se haya hecho, no se calificará este hito del proyecto.

- [x] Haber superado el hito anterior.

Para ver como sincronizar DockerHub con nuestro GitHub es bastante simple. Antes de nada hay que crearse una cuenta en dockerhub.

![Imagen 9](http://i67.tinypic.com/2ytrx1z.png)

Una vez creado iniciamos sesión y vamos a la pestaña Settings -> Linked Accounts & Services

![Imagen 10](http://i63.tinypic.com/2r7yiw0.png)

Una vez ahí, tenemos que enlazar nuestro GitHub (vemos que yo ya lo tengo asociado)

![Imagen 11](http://i65.tinypic.com/2uj7gcp.png)

Si no lo tenemos aún asociado, tenemos que clickar sobre dicha opción, pulsaremos sobre Create y elegimos la opción Create Automated Build. Nos da la opción de crearla mediante GitHub y deberemos elegir el repositorio de nuestro proyecto. 

Se puede ver como la construcción se realiza cada vez que se haga un push en la rama master
![Imagen 12](http://i65.tinypic.com/34osj95.png)

![Imagen 13](http://i67.tinypic.com/sosb9h.png)

Con estos pasos ya tendriamos asociado nuestro GitHub a nuestro contenedor Docker. Realizariamos un sudo docker pull sergiocaceres/iv y ya lo tendriamos descargado, tan solo habría que hacer lo siguiente:

####Probando docker

Una vez hayamos realizado la orden "sudo docker pull sergiocaceres/iv" tendremos que lanzar el contenedor. Para ello tenemos que asignarle valor a las variables de entorno declaradas, pero que por motivos de seguridad se ve borrado en la siguiente imagen. Tras realizar esa orden ejecutamos ```cd IV/ && make execute ``` y ya lanzará el bot

![Imagen 14](http://i63.tinypic.com/znv3w0.png)

Podemos ver como funciona correctamente y el bot está funcionando


##Quinto hito: Diseño del soporte virtual para el despliegue de una aplicación

###Prerequisitos

- [x] Haber alcanzado el 50% de los objetivos del tema de gestión de infraestructuras y uso de sistemas.

- [x] Haber superado todos los hitos anteriores.

####Instalación Azure, Vagrant y Ansible

Hemos desplegado en Azure ya que disponía de una cuenta gratuita proporcionada por el profesor de la asignatura, [Juan Julián Merelo Guervós](https://github.com/JJ). Por lo tanto no tenía duda de alojar el bot en el IaaS Azure.
####
Empezaremos descargando [Vagrant](https://www.vagrantup.com/downloads.html), en mi caso, me he descargado la versión [1.8.6](https://releases.hashicorp.com/vagrant/1.8.6/). Una vez instalado, procedemos a instalar Ansible. Para ello bastaría ejecutar la siguiente orden:
```
sudo apt-get install ansible
```

Hemos instalado tanto Vagrant como Ansible, nos quedaría instalar los plugins de Azure. Lo hacemos con la siguiente orden:
```
vagrant plugin install vagrant-azure
```

Ya estaríamos listos para empezar a usar Azure, vamos a ver que procesos hay que seguir.

Primero, tenemos que crearnos los certificados de servidor para enlazar nuestra máquina a la de Azure. Esto lo hacemos con las siguientes ordenes:
```
openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout azure.pem -out azure.pem
openssl x509 -inform pem -in azure.pem -outform der -out azure.cer
chmod 600 azure.pem
```

Una vez generado el certificado, tendremos que insertarlo en la página web de Azure. Para ello, nos vamos al portal antiguo de [Azure](https://manage.windowsazure.com/). Una vez estemos logueados tendremos que irnos al apartado Configuración -> Certificados y Administración -> Cargamos el fichero llamado .cer. Vemos en la siguiente imagen como nos debería quedar.

![Imagen 1](http://i67.tinypic.com/2pocrdd.png)

Una vez hecho esto, ya podremos realizar el fichero Vagrantfile. Para ello, primero debemos ejecutar 
```
vagrant init
```
Esto nos genera el fichero Vagrantfile, ahora debemos ponerlo acorde para que ejecute Ansible con unas determinadas credenciales,.. (esto se explicará a continuación)

####Vagranfile

Nuestro fichero [Vagrantfile](https://github.com/sergiocaceres/IV/blob/master/Vagrantfile) es el siguiente:
```
# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "azure"
	config.vm.network "public_network" 
	config.vm.provider :azure do |azure, override|
		azure.mgmt_certificate = File.expand_path("azure.pem")
		azure.mgmt_endpoint    = "https://management.core.windows.net"
		azure.subscription_id = "6b38da11-0190-4ca3-81f2-7cd3cd7a9e0b"
		azure.vm_name     = "comunibot"
		azure.cloud_service_name = 'comunibot'
		azure.vm_image    = "b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_2-LTS-amd64-server-20150506-en-us-30GB" 
		azure.vm_size     = "Small"
    		config.vm.box_url = "https://github.com/msopentech/vagrant-azure/raw/master/dummy.box"

		azure.vm_user = "sergio" # defaults to 'vagrant' if not provided
    		azure.vm_password = "Abecedario1234#"
		azure.vm_location = "Central US"
		azure.tcp_endpoints = '80:80'
		azure.ssh_port = "22"
  	end
	config.vm.synced_folder ".", "/vagrant",disabled: true
	config.ssh.username = 'sergio'
	config.ssh.password = 'Abecedario1234#'

	config.vm.provision "ansible" do |ansible|
		ansible.raw_arguments=["-vvvv"]
		ansible.sudo = true        
		ansible.playbook = "configuracion_ansible.yml"
		ansible.verbose = "v"
  	end

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
end
```

Ahora vamos a ver qué significa cada orden:
- config.vm.box = "azure" -> Decimos que la box de la máquina virtual es la de azure
- azure.mgmt_certificate = File.expand_path("azure.pem") -> Le pasamos el certificado
- azure.mgmt_endpoint = "https://management.core.windows.net" -> Ubicación del portal de administración de la máquina
- azure.subscription_id = "" -> ID de la suscripción de Azure. Se puede encontrar en la web mencionada anteriormente
- azure.vm_name = "comunibot" -> Nombre de la máquina virtual
- azure.cloud_service_name = 'comunibot' -> Nombre del servicio web en la nube
- azure.vm_image = "" -> Imagen del SO que instalamos
- azure.vm_size = "Small" -> Tamaño de la máquina virtual
- config.vm.box_url = "https://github.com/msopentech/vagrant-azure/raw/master/dummy.box" -> Configuración de la box utilizada
- zure.vm_user = "sergio" -> Nombre de usuario de la máquina
- azure.vm_password = "Abecedario1234#" -> Contraseña de acceso para el usuario creado
- azure.ssh_port = "22" -> Puerto para conexiones SSH
- config.ssh.username = 'sergio' -> Usuario para la conexión SSH
- config.ssh.password = 'Abecedario1234#' -> Clave para la conexión SSH

Ahora configuraremos ansible:
- ansible.raw_arguments=["-vvvv"] -> Ansible imprime todo lo que ocurra
- ansible.sudo = true -> Esto hace que todos los comandos de ansible sean tipo superusuario
- ansible.playbook = "configuracion_ansible.yml" -> Ubicación del archivo de configuración de ansible


####Configuración ansible
Ahora veremos nuestro fichero de ansible, el cual se encarga de instalar todas las dependencias necesarias. Para ello vamos a ver nuestro fichero [configuracion_ansible.yml](https://github.com/sergiocaceres/IV/blob/master/configuracion_ansible.yml):

```
---
- hosts: default
  remote_user: sergio
  sudo: yes
  vars:
   TOKENBOT: "{{ lookup('env','TOKENBOT') }}"
   USR_BD: "{{ lookup('env','USR_BD') }}"
   PASS_BD: "{{ lookup('env','PASS_BD') }}"
  tasks:
  - name: Update
    command: apt-get update
  - name: essential
    command: apt-get install -y build-essential
  - name: Install git 
    command: apt-get install -y git
  - name: Instalar pip
    apt: name=python-pip state=present
  - name: Instalar supervisor
    apt: name=supervisor state=present
  - name: Instalar libpq-dev
    apt: name=libpq-dev state=present
  - name: Descargar repositorio sergiocaceres 
    shell: rm -rf IV && git clone https://github.com/sergiocaceres/IV
  - name: Configurar programa para el supervisor
    template: src=comuni_bot.conf dest=/etc/supervisor/conf.d/comuni_bot.conf
  - name: Instalar python setuptools
    apt: name=python-setuptools state=present
  - name: Instalar python-dev
    apt: name=python-dev state=present
  - name: Instalar librerias necesarias
    apt: name=libgdbm-dev state=present
  - name: Instalar libncurses
    apt: name=libncurses5-dev state=present
  - name: Instalar libgdbm-dev
    apt: name=libgdbm-dev state=present
  - name: Instalar postgresql
    apt: name=postgresql state=present
  - name: Instalar postgresql-contrib
    apt: name=postgresql-contrib state=present
  - name: Instalar psycopg2
    command: pip install -U pip
  - name: Instalar python-dev
    command: sudo apt-get install -y python-dev
  - name: Instalar requirements
    command: sudo pip install -r IV/requirements.txt
  - name: Ejecutar supervisor
    service: name=supervisor state=started
```

Aquí le tenemos que pasar las variables de entorno para no ponerlas públicas. Ahí podemos ver como se realiza. Vamos a ver que significa cada etiqueta:

- hosts: default -> Servidor en el que se harán las órdenes. Se pone por defecto
- sudo:Yes -> Órdenes como sudo
- remote_user -> Usuario remoto con el que se ejecutarán las órdenes
- tasks: -> Tareas a ejecutar
- name: -> Nombre de la tarea a ejecutar
- apt -> Ejecuta con apt para descargar dependencias
- shell -> Ejecuta la orden

Una vez listo, procedemos al despliegue ejecutando la orden:
```
vagrant up --provider=azure
```

Si queremos actualizar algunos paquetes sin tener que eliminar la máquina y volver a crearla, bastaría con hacer

```
vagrant provision
```
Una vez hecho esto, tan solo tendríamos que esperar a que se termine de crear la máquina en Azure y configurada con los paquetes dichos en el fichero de Ansible.

####Supervisor

Como se trata de un bot de Telegram, necesitamos que esté siempre ejecutándose, a pesar de que cerremos la terminal. Para ello nos creamos un fichero de configuración, llamado [comuni_bot.conf](https://github.com/sergiocaceres/IV/blob/master/comuni_bot.conf). Es el siguiente:
```
[program:comuni_bot]
autostart=false
command=python bot_telegram/bot.py
user=sergio
directory=/home/sergio/IV
environment=
	TOKENBOT="{{TOKENBOT}}",
	USR_BD="{{USR_BD}}",
	PASS_BD="{{PASS_BD}}",
redirect_stderr=true
stdout_logfile=/var/log/supervisor/comuni_bot.log
stderr_logfile=/var/log/supervisor/comuni_bot-error.log
```

Le decimos el nombre que usaremos, el comando a ejecutar, el directorio donde se van a almacenar los logs y los más importante, nuestras variables de entorno.

####Fabric

Fabric es una herramienta con la que podremos administrar una máquina remota una vez haya sido creada y aprovisionada con todo lo necesario. Una vez creado el fichero mencionado anteriormente, usaremos el fichero de Fabric [fabfile.py]() para redactar una serie de funciones que podremos ejecutar con Fabric. Vemos el fichero:
```
from fabric.api import *
import os

def descargar():
    run ('sudo rm -rf IV')
    run ('sudo git clone https://github.com/sergiocaceres/IV')

def detener():
    run ("sudo supervisorctl stop comuni_bot")

def borrar():
    run ('sudo rm -rf IV')

def instalar():
    run ('cd IV && make install')

def recargar():
    run("sudo supervisorctl reload")

def iniciar():
    with shell_env(TOKENBOT=os.environ['TOKENBOT'], USR_BD=os.environ['USR_BD'], PASS_BD=os.environ['PASS_BD']):
        run('sudo supervisorctl start comuni_bot')

def iniciar_no_supervisor():
    with shell_env(TOKENBOT=os.environ['TOKENBOT'], USR_BD=os.environ['USR_BD'], PASS_BD=os.environ['PASS_BD']):
        run('cd IV && make execute')
```	
Vemos que tenemos una serie de funciones que podremos ejecutar. Vemos que hacen:
- descargar() -> Nos descarga el repositorio de GitHub
- detener() -> Para la ejecución, en nuestro caso, del bot (supervisor)
- borrar() -> Nos borra la carpeta IV que es donde se aloja todo el contenido
- instalar() -> Nos instala los requirements
- def recargar() -> Actualiza el supervisor por si hemos hecho algún cambio en el fichero comuni_bot.conf mencionado anteriormente
- iniciar() -> Inicia la ejecución del bot con supervisor, pasándole las variables de entorno
- iniciar_no_supervisor() -> Como el propio nombre indica, inicia la ejecución del bot pero sin supervisor, es decir, que si cerramos nuesra terminal, el proceso se pararía.

Una vez explicado el fichero, vamos a ver como se lanza nuestro bot usando Fabric. Es simple, debemos poner la siguiente orden:
```
fab -p CONTRASEÑA -H usuario@host ORDEN
```

Donde ORDEN es una de la función explicada justo arriba. Veamos una imagen de la ejecución:

![Imagen 2](http://i64.tinypic.com/2wrmcdy.png)
![Imagen 3](http://i63.tinypic.com/10h0j7t.png)

Ahora vemos que responde sin ningún problema

![Imagen 4](http://i65.tinypic.com/dt9au.jpg)
![Imagen 5](http://i67.tinypic.com/1zvd849.jpg)

Con todo este proceso, podemos ver como hemos instalado los requisitos para poder realizar este hito. Vemos su ejecución con Fabric y su funcionamiento con las últimas capturas de pantalla. Si queremos empezar a hablarle al bot, tan solo tendremos que pinchar [aquí](https://telegram.me/comuni_bot)
