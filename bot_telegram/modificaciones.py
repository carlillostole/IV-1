# -*- coding: utf-8 -*-
import telebot
from ComunioPy import Comunio
from telebot import types
import os
import sqlite3

#bot = telebot.TeleBot(os.environ["TOKENBOT"])
TOKEN = '287783764:AAGiiRJgG4cKfgGOKbTMCLbqtzA4AsEyprE' #Ponemos nuestro TOKEN generado con el @BotFather
bot = telebot.TeleBot(TOKEN)

#Alineacion
def alineacion_(test,uid):
	alineacion = []
	alineacion = test.lineup_user(uid) #Alineacion del usuario
	vecto1 = invertir(alineacion)
	vecto = ', '.join(vecto1)
	return vecto

#Invertir la cadena
def invertir(var):
	return var[::-1]

#Devuelve el nombre de la liga
def get_nombre(test,uid):
	title = []
	title = test.get_title()
	return title

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

def comprobar_con_bd(m):
	cid = m.chat.id
	cadena_usuario_contrasenia = m.text.split(" ")
	if len(cadena_usuario_contrasenia) != 1 :
		bot.send_message(cid, "Solo debe introducir la acción. Su nombre y contraseña están guardadas")
		return(-1)
		
	else:
		return cadena_usuario_contrasenia

def cid_(m):
	cid = m.chat.id
	return cid


def asignar_valores(cadena_usuario_contrasenia,variable_aux,cid):
	if variable_aux == 0:
		accion = cadena_usuario_contrasenia[0]
		usuario = cadena_usuario_contrasenia[1]
		contrasenia = cadena_usuario_contrasenia[2]
		test = Comunio(usuario,contrasenia,"BBVA") 
	else:
		con_bd = sqlite3.connect('datos.db')
		cursor_cid = con_bd.cursor()
		vector_comprobar = []
		accion = cadena_usuario_contrasenia[0]
		vector_comprobar = int(cid)
		valor = (cid, )
		vector_cj = cursor_cid.execute("SELECT usuario,contrasenia FROM usuarios WHERE cid=?", valor)
		for i in vector_cj:
			user = i[0]
			passwd = i[1]
		test = Comunio(user, passwd,"BBVA")    #Meter los parametros de esa lista con una consulta a la BD
		cursor_cid.close()
		con_bd.close()

	return test


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


