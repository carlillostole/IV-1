# -*- coding: utf-8 -*-
import telebot
from ComunioPy import Comunio
from telebot import types
import os
import sqlite3
import modificaciones

bot = telebot.TeleBot(os.environ["TOKENBOT"])

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	cid = message.chat.id # Guardamos el ID de la conversacion para poder responder.
	bot.send_message(cid, "Introduzca acción que desea realizar, usuario de comunio y contraseña\nAcciones: \n1. /Alineacion: Devuelve la alineación con la que se jugó la última jornada\n2. /Noticias: Devuelve las dos últimas noticias\n3. /Mercado: Devuelve el mercado de fichajes de la comunidad\n4. /Ofertas: Devuelve las ofertas que me han hecho\n5. /Traspasos: Devuelve las ofertas que yo he hecho\n\nEjemplo: /Alineacion,usuario,contraseña")


@bot.message_handler(commands=['Alineacion', 'alineacion'])
def send_alineacion(m):
	cid = cid_(m)
	cadena_usuario_contrasenia = comprobar(m)

	if cadena_usuario_contrasenia == -1:
		return(-1)
	else:
		#con_bd = sqlite3.connect('base_datos_bot.db')
		#cursor_cid = con_bd.cursor()
		#Por hacer
		#reg = (cid, cadena_usuario_contrasenia[1], cadena_usuario_contrasenia[2])
		#cursor_cid.execute("INSERT INTO tabla_bot VALUES(?,?,?)", reg)
		#con_bd.commit()
		

		test = asignar_valores(cadena_usuario_contrasenia)
				
		if hasattr(test, 'myid') != True:
			bot.send_message(cid, "Usuario o contraseña incorrecta. Vuelve a intentarlo")

		else:
			uid = test.get_myid() #Saco el uid del usuario
			modificaciones.get_nombre(test,uid)
			resultado_alineacion = modificaciones.alineacion_(test,uid)
			bot.send_message(cid,resultado_alineacion)
			#cursor_cid.execute("SELECT * FROM tabla_bot")
			#for i in cursor_cid: print(i)
			#print "Hola"
		#cursor_cid.close()
		#con_bd.close()
@bot.message_handler(commands=['Noticias', 'noticias'])
def send_noticias(m):
	cid = cid_(m)
	cadena_usuario_contrasenia = comprobar(m)

	if cadena_usuario_contrasenia == -1:
		return(-1)
	else:
		test = asignar_valores(cadena_usuario_contrasenia)
				
		if hasattr(test, 'myid') != True:
			bot.send_message(cid, "Usuario o contraseña incorrecta. Vuelve a intentarlo")

		else:
			uid = test.get_myid() #Saco el uid del usuario

			noticias = noticias_(test)
			bot.send_message(cid, noticias)

@bot.message_handler(commands=['Mercado', 'mercado'])
def send_mercado(m):
	cid = cid_(m)
	cadena_usuario_contrasenia = comprobar(m)

	if cadena_usuario_contrasenia == -1:
		return(-1)
	else:
		test = asignar_valores(cadena_usuario_contrasenia)
				
		if hasattr(test, 'myid') != True:
			bot.send_message(cid, "Usuario o contraseña incorrecta. Vuelve a intentarlo")

		else:
			uid = test.get_myid() #Saco el uid del usuario
	
			mercado_fichajes = mercado_(test)
			bot.send_message(cid, "[Nombre, Equipo, Precio_min, Precio_mercado, Puntos, Fecha, Propietario, Posición]")
			bot.send_message(cid, mercado_fichajes)

@bot.message_handler(commands=['Ofertas', 'ofertas'])	
def send_ofertas(m):
	cid = cid_(m)
	cadena_usuario_contrasenia = comprobar(m)

	if cadena_usuario_contrasenia == -1:
		return(-1)
	else:
		test = asignar_valores(cadena_usuario_contrasenia)
				
		if hasattr(test, 'myid') != True:
			bot.send_message(cid, "Usuario o contraseña incorrecta. Vuelve a intentarlo")

		else:
			uid = test.get_myid() #Saco el uid del usuario

			ofertas_hacia_mi = ofertas_hacia_mi_(test)
			bot.send_message(cid, "[Jugador,Propietario,Equipo,Dinero,Fecha,Fecha de cambio ,Estatus]")
			bot.send_message(cid, ofertas_hacia_mi)	

@bot.message_handler(commands=['Traspasos', 'traspasos'])	
def send_traspasos(m):
	cid = cid_(m)
	cadena_usuario_contrasenia = comprobar(m)

	if cadena_usuario_contrasenia == -1:
		return(-1)
	else:
		test = asignar_valores(cadena_usuario_contrasenia)
				
		if hasattr(test, 'myid') != True:
			bot.send_message(cid, "Usuario o contraseña incorrecta. Vuelve a intentarlo")

		else:
			uid = test.get_myid() #Saco el uid del usuario

			ofertas_hacia_otro = ofertas_hacia_otro_(test)
			bot.send_message(cid, "[Jugador,Propietario,Equipo,Dinero,Fecha,Fecha de cambio ,Estatus]")
			bot.send_message(cid, ofertas_hacia_otro)
#--------------------------------------------------------------------------
def asignar_valores(cadena_usuario_contrasenia):
	accion = cadena_usuario_contrasenia[0]
	usuario = cadena_usuario_contrasenia[1]
	contrasenia = cadena_usuario_contrasenia[2]
	test = Comunio(usuario,contrasenia,"BBVA") 
	return test

def comprobar(m):
	cid = m.chat.id
	cadena_usuario_contrasenia = m.text.split(" ")
	if len(cadena_usuario_contrasenia) != 3 :
		bot.send_message(cid, "Cadena errónea. Inténtalo de nuevo")
		return(-1)
		
	else:
		if (cadena_usuario_contrasenia[1].find("_")) == 1: #Tiene _
			cadena = ""
			cadena = cadena_usuario_contrasenia[1].replace("_"," ")
			cadena_usuario_contrasenia[1] = cadena

		return cadena_usuario_contrasenia

def cid_(m):
	cid = m.chat.id
	return cid


#Noticias
def noticias_(test):
	news = []
	news = test.get_news()
	vector_noticias = []
	vector_resultado = " "
	vector_noticias = news[0] + news[1]
	vector_resultado = vector_noticias
	
	for i in range(len(vector_resultado)):
		index = vector_resultado.find('.A')+1 #Localizo donde se encuentra el .A
		
		if vector_resultado[i] == '.' and vector_resultado[i+1] == 'A':
			vector_noticias = vector_noticias[:index] + '\n' + vector_noticias[index:]

		vector_resultado = vector_noticias
	
	return vector_resultado


def mercado_(test):
	venta = [] #Almaceno los jugadores en venta
	venta = test.players_onsale("4495491",False) #Funcion que saca los jugadores en venta con el uid de la liga
	
	mercado = " "
	posicion_mercado = ""
	mercado = venta
	contador = 0
	for i in range(len(mercado)):
		for j in range(len(mercado[i])):
			contador+=1
			
			posicion_mercado += mercado[i][j]
			if contador%8 == 0:
				posicion_mercado += '\n' + '\n'
			else:
				posicion_mercado += ', '
			
	return posicion_mercado

def ofertas_hacia_mi_(test):

	ofertas_hacia_mi = []
	ofertas_hacia_mi = test.bids_to_you()

	ofertas = " "
	ofertas = ofertas_hacia_mi
	devolver_ofertas = ""
	contador = 0

	for i in range(0,2):
    		for j in range(len(ofertas[i])):
        		contador+=1
			
			if contador == 4:
				ofertas[i][j] = str(ofertas[i][j])

			devolver_ofertas += ofertas[i][j]
			if contador%7 == 0:
				devolver_ofertas += '\n'
				contador = 0
			else:
				devolver_ofertas += ', '
	return devolver_ofertas

def ofertas_hacia_otro_(test):

	ofertas_hacia_otro = []
	ofertas_hacia_otro = test.bids_from_you()

	ofertas = " "
	ofertas = ofertas_hacia_otro
	devolver_ofertas = ""
	contador = 0

	for i in range(0,2):
    		for j in range(len(ofertas[i])):
        		contador+=1
			
			if contador == 4:
				ofertas[i][j] = str(ofertas[i][j])

			devolver_ofertas += ofertas[i][j]
			if contador%7 == 0:
				devolver_ofertas += '\n'
				contador = 0
			else:
				devolver_ofertas += ', '
	return devolver_ofertas
#----------------------------------------------------------------------------
"""
					else:
						bot.send_message(cid, "Acción no valida. Vuelve a introducir usuario, contraseña y una acción valida")
"""


#bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.

bot.polling() # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.


