# -*- coding: utf-8 -*-
import telebot
from ComunioPy import Comunio
from telebot import types
import os
import sqlite3
import modificaciones
import psycopg2, psycopg2.extras


#bot = telebot.TeleBot(os.environ["TOKENBOT"])
TOKEN = '287783764:AAGiiRJgG4cKfgGOKbTMCLbqtzA4AsEyprE' #Ponemos nuestro TOKEN generado con el @BotFather
bot = telebot.TeleBot(TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	cid = message.chat.id # Guardamos el ID de la conversacion para poder responder.
	bot.send_message(cid, "Introduzca acción que desea realizar, usuario de comunio y contraseña\nAcciones: \n1. /Alineacion: Devuelve la alineación con la que se jugó la última jornada\n2. /Noticias: Devuelve las dos últimas noticias\n3. /Mercado: Devuelve el mercado de fichajes de la comunidad\n4. /Ofertas: Devuelve las ofertas que me han hecho\n5. /Traspasos: Devuelve las ofertas que yo he hecho\n\nEjemplo: /Alineacion,usuario,contraseña \n\nUna vez que introduzca sus datos correctamente, solo debera introducir la acción deseada")
	con_bd = sqlite3.connect('datos.db')#psycopg2.connect(database='test',user='postgres',password='pass', host='localhost')
	cursor_cid = con_bd.cursor()

	valor = (cid, )
	cursor_cid.execute("DELETE FROM usuarios WHERE cid=?", valor)
	con_bd.commit()

	cursor_cid.close()
	con_bd.close()

@bot.message_handler(commands=['Alineacion', 'alineacion'])
def send_alineacion(m):
	con_bd = sqlite3.connect('datos.db') #psycopg2.connect(database='test',user='postgres',password='pass', host='localhost')
	cursor_cid = con_bd.cursor()
	cid = modificaciones.cid_(m)
	vector_comprobar = []
	vector_comprobar = "(" + str(cid) + ",)"
		
	vector_cc = sqlite3.Cursor
	vector_cc = cursor_cid.execute("SELECT cid FROM usuarios")
	existe = False
	for i in vector_cc:
		if existe != True:
			if str(i) == vector_comprobar:		#Encontramos el cid en la bd 			
				existe = True
				variable_aux = 1				
				break
			else:
				variable_aux = 0		

	if variable_aux == 0:
		cadena_usuario_contrasenia = modificaciones.comprobar(m)
	
		user = cadena_usuario_contrasenia[1]				#Insertamos cid, nombre y passwd en la BD
		passwd = cadena_usuario_contrasenia[2]
		reg = (cid, user, passwd)
		cursor_cid.execute("INSERT INTO usuarios VALUES (?,?,?)", reg)
		con_bd.commit()
	else:
		cadena_usuario_contrasenia = modificaciones.comprobar_con_bd(m)
	
	if cadena_usuario_contrasenia == -1:
		return(-1)
	else:
		test = modificaciones.asignar_valores(cadena_usuario_contrasenia,variable_aux,cid)
				
		if hasattr(test, 'myid') != True:
			valor = (cid, )
			bot.send_message(cid, "Usuario o contraseña incorrecta. Vuelve a intentarlo")
			cursor_cid.execute("DELETE FROM usuarios WHERE cid=?", valor)
			con_bd.commit()
		else:
			uid = test.get_myid() #Saco el uid del usuario
			modificaciones.get_nombre(test,uid)
			resultado_alineacion = modificaciones.alineacion_(test,uid)
			bot.send_message(cid,resultado_alineacion)
			
	cursor_cid.close()
	con_bd.close()

@bot.message_handler(commands=['Noticias', 'noticias'])
def send_noticias(m):
	con_bd = sqlite3.connect('datos.db') #psycopg2.connect(database='test',user='postgres',password='pass', host='localhost')
	cursor_cid = con_bd.cursor()
	cid = modificaciones.cid_(m)
	vector_comprobar = []
	vector_comprobar = "(" + str(cid) + ",)"
		
	vector_cc = sqlite3.Cursor
	vector_cc = cursor_cid.execute("SELECT cid FROM usuarios")
	existe = False
	for i in vector_cc:
		if existe != True:
			if str(i) == vector_comprobar:		#Encontramos el cid en la bd 			
				existe = True
				variable_aux = 1				
				break
			else:
				variable_aux = 0		

	if variable_aux == 0:
		cadena_usuario_contrasenia = modificaciones.comprobar(m)
	
		user = cadena_usuario_contrasenia[1]				#Insertamos cid, nombre y passwd en la BD
		passwd = cadena_usuario_contrasenia[2]
		reg = (cid, user, passwd)
		cursor_cid.execute("INSERT INTO usuarios VALUES (?,?,?)", reg)
		con_bd.commit()
	else:
		cadena_usuario_contrasenia = modificaciones.comprobar_con_bd(m)
	
	if cadena_usuario_contrasenia == -1:
		return(-1)
	else:
		test = modificaciones.asignar_valores(cadena_usuario_contrasenia,variable_aux,cid)
				
		if hasattr(test, 'myid') != True:
			valor = (cid, )
			bot.send_message(cid, "Usuario o contraseña incorrecta. Vuelve a intentarlo")
			cursor_cid.execute("DELETE FROM usuarios WHERE cid=?", valor)
			con_bd.commit()

		else:
			uid = test.get_myid() #Saco el uid del usuario
			noticias = modificaciones.noticias_(test)
			bot.send_message(cid, noticias)
			
	cursor_cid.close()
	con_bd.close()	

@bot.message_handler(commands=['Mercado', 'mercado'])
def send_mercado(m):
	con_bd = sqlite3.connect('datos.db') #psycopg2.connect(database='test',user='postgres',password='pass', host='localhost')
	cursor_cid = con_bd.cursor()
	cid = modificaciones.cid_(m)
	vector_comprobar = []
	vector_comprobar = "(" + str(cid) + ",)"
		
	vector_cc = sqlite3.Cursor
	vector_cc = cursor_cid.execute("SELECT cid FROM usuarios")
	existe = False
	for i in vector_cc:
		if existe != True:
			if str(i) == vector_comprobar:		#Encontramos el cid en la bd 			
				existe = True
				variable_aux = 1				
				break
			else:
				variable_aux = 0		

	if variable_aux == 0:
		cadena_usuario_contrasenia = modificaciones.comprobar(m)
	
		user = cadena_usuario_contrasenia[1]				#Insertamos cid, nombre y passwd en la BD
		passwd = cadena_usuario_contrasenia[2]
		reg = (cid, user, passwd)
		cursor_cid.execute("INSERT INTO usuarios VALUES (?,?,?)", reg)
		con_bd.commit()
	else:
		cadena_usuario_contrasenia = modificaciones.comprobar_con_bd(m)
	
	if cadena_usuario_contrasenia == -1:
		return(-1)
	else:
		test = modificaciones.asignar_valores(cadena_usuario_contrasenia,variable_aux,cid)
				
		if hasattr(test, 'myid') != True:
			valor = (cid, )
			bot.send_message(cid, "Usuario o contraseña incorrecta. Vuelve a intentarlo")
			cursor_cid.execute("DELETE FROM usuarios WHERE cid=?", valor)
			con_bd.commit()

		else:
			uid = test.get_myid() #Saco el uid del usuario
			mercado_fichajes = modificaciones.mercado_(test)
			bot.send_message(cid, "[Nombre, Equipo, Precio_min, Precio_mercado, Puntos, Fecha, Propietario, Posición]")
			bot.send_message(cid, mercado_fichajes)
			
	cursor_cid.close()
	con_bd.close()
		
	
			

@bot.message_handler(commands=['Ofertas', 'ofertas'])	
def send_ofertas(m):
	con_bd = sqlite3.connect('datos.db') #psycopg2.connect(database='test',user='postgres',password='pass', host='localhost')
	cursor_cid = con_bd.cursor()
	cid = modificaciones.cid_(m)
	vector_comprobar = []
	vector_comprobar = "(" + str(cid) + ",)"
		
	vector_cc = sqlite3.Cursor
	vector_cc = cursor_cid.execute("SELECT cid FROM usuarios")
	existe = False
	for i in vector_cc:
		if existe != True:
			if str(i) == vector_comprobar:		#Encontramos el cid en la bd 			
				existe = True
				variable_aux = 1				
				break
			else:
				variable_aux = 0		

	if variable_aux == 0:
		cadena_usuario_contrasenia = modificaciones.comprobar(m)
	
		user = cadena_usuario_contrasenia[1]				#Insertamos cid, nombre y passwd en la BD
		passwd = cadena_usuario_contrasenia[2]
		reg = (cid, user, passwd)
		cursor_cid.execute("INSERT INTO usuarios VALUES (?,?,?)", reg)
		con_bd.commit()
	else:
		cadena_usuario_contrasenia = modificaciones.comprobar_con_bd(m)
	
	if cadena_usuario_contrasenia == -1:
		return(-1)
	else:
		test = modificaciones.asignar_valores(cadena_usuario_contrasenia,variable_aux,cid)
				
		if hasattr(test, 'myid') != True:
			valor = (cid, )
			bot.send_message(cid, "Usuario o contraseña incorrecta. Vuelve a intentarlo")
			cursor_cid.execute("DELETE FROM usuarios WHERE cid=?", valor)
			con_bd.commit()

		else:
			uid = test.get_myid() #Saco el uid del usuario
			ofertas_hacia_mi = modificaciones.ofertas_hacia_mi_(test)
			bot.send_message(cid, "[Jugador,Propietario,Equipo,Dinero,Fecha,Fecha de cambio ,Estatus]")
			bot.send_message(cid, ofertas_hacia_mi)
			
	cursor_cid.close()
	con_bd.close()

				

@bot.message_handler(commands=['Traspasos', 'traspasos'])	
def send_traspasos(m):
	con_bd = sqlite3.connect('datos.db') #psycopg2.connect(database='test',user='postgres',password='pass', host='localhost')
	cursor_cid = con_bd.cursor()
	cid = modificaciones.cid_(m)
	vector_comprobar = []
	vector_comprobar = "(" + str(cid) + ",)"
		
	vector_cc = sqlite3.Cursor
	vector_cc = cursor_cid.execute("SELECT cid FROM usuarios")
	existe = False
	for i in vector_cc:
		if existe != True:
			if str(i) == vector_comprobar:		#Encontramos el cid en la bd 			
				existe = True
				variable_aux = 1				
				break
			else:
				variable_aux = 0		

	if variable_aux == 0:
		cadena_usuario_contrasenia = modificaciones.comprobar(m)
	
		user = cadena_usuario_contrasenia[1]				#Insertamos cid, nombre y passwd en la BD
		passwd = cadena_usuario_contrasenia[2]
		reg = (cid, user, passwd)
		cursor_cid.execute("INSERT INTO usuarios VALUES (?,?,?)", reg)
		con_bd.commit()
	else:
		cadena_usuario_contrasenia = modificaciones.comprobar_con_bd(m)
	
	if cadena_usuario_contrasenia == -1:
		return(-1)
	else:
		test = modificaciones.asignar_valores(cadena_usuario_contrasenia,variable_aux,cid)
				
		if hasattr(test, 'myid') != True:
			valor = (cid, )
			bot.send_message(cid, "Usuario o contraseña incorrecta. Vuelve a intentarlo")
			cursor_cid.execute("DELETE FROM usuarios WHERE cid=?", valor)
			con_bd.commit()

		else:
			uid = test.get_myid() #Saco el uid del usuario
			ofertas_hacia_otro = modificaciones.ofertas_hacia_otro_(test)
			bot.send_message(cid, "[Jugador,Propietario,Equipo,Dinero,Fecha,Fecha de cambio ,Estatus]")
			bot.send_message(cid, ofertas_hacia_otro)
			
	cursor_cid.close()
	con_bd.close()

#bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.

bot.polling() # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.


