#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import unittest
import sqlite3

class Test(unittest.TestCase):
	def test_bd(self):
        	conectar = sqlite3.connect('datos.db')
		with conectar:
			cur = conectar.cursor()
			cur.execute("INSERT INTO usuarios VALUES ('3','testeando','12345678')")
			ult_fila = cur.lastrowid
			cur.execute("DELETE FROM usuarios WHERE cid = '3'")
			self.assertEqual(ult_fila,2)
	

if __name__ == '__main__':
    unittest.main() 
