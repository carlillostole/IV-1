# Repositorio de las prácticas

Aún no tengo decidido cuál será el proyecto en cuestión, por lo que en el siguiente hito tomaré una decisión.

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
