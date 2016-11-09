#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from ComunioPy import Comunio
import unittest
import sqlite3
from info_test import *
import modificaciones
import psycopg2
import os

usr_bd = (os.environ["USR_BD"])
pass_bd = (os.environ["PASS_BD"])

test = Comunio("bot_iv","12345678",'BBVA') 
class Test(unittest.TestCase):
	def test_bd(self):
        	conectar = psycopg2.connect(database='d6f0n6kc34qjo7',user=(os.environ["USR_BD"]),password=(os.environ["PASS_BD"]),host='ec2-54-225-117-56.compute-1.amazonaws.com')
		with conectar:
			cur = conectar.cursor()
			cur.execute("INSERT INTO usuarios VALUES ('3','testeando','12345678')")
			ult_fila = cur.lastrowid
			cur.execute("DELETE FROM usuarios WHERE cid = '3'")
			self.assertEqual(ult_fila,ult_fila)
	
	def test_get_alineacion(self):
        	alineacion_obtenida = modificaciones.alineacion_(test,test.get_myid())
        	self.assertEqual(alineacion_obtenida, vecto)

	def test_get_title(self):
		title_obtenido = modificaciones.get_nombre(test,test.get_myid())
		self.assertEqual(title_obtenido, nombre_comunidad)

	
if __name__ == '__main__':
    unittest.main() 
