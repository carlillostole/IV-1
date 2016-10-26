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


