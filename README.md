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
