import sqlite3 # esta importando la libreria de base datos
con = sqlite3.connect('banco.db', timeout=10)# esta estableciendo la conexion a la base de datos que se llama banco.db
cursor = con.cursor()# el cursor para utilizar varias funciones con relacion a la base de datos 
table ="""CREATE TABLE IF NOT EXISTS USUARIO(NUMERO INT, NIP INT, DINERO INT);"""# esta creando una tabla que se llama usuario
cursor.execute(table)

class Cuenta: # la clase tiene la funcion retirar, depositar y ver balance dentro de ella y crear usuario . O sea cuando veo cuenta.balance es llamandola porque ya esta aqui
    def __init__(self): # Esta declarando por primera vez el self, esta como inicializando los atributos de self
        self.dinero = 0 # esto para poder utilizarlo luego y lo llamarlo abajo donde el quiera.
        self.disponible = 500
        

    def crearUsuario(self, numero_id, nip_id, dinero = 0): # aqui estamos insertando el usuario en la base de datos, aqui esta la logica que se uso para gr
        # grabar el usuario en la base datos
    	self.numero_id = numero_id # aqui lo esta declarando
    	self.nip_id = nip_id # aqui lo esta declarando
    	self.dinero +=dinero # aqui lo esta declarando
    	cursor.execute(f'''INSERT INTO USUARIO (NUMERO, NIP, DINERO) VALUES ({self.numero_id}, {self.nip_id}, {self.dinero})''')
    	con.commit()
    	print('-'*20)
    def depositar(self, nuevoDinero, numero_id):# aqui se grabar el deposito del usuario. 
    	self.dinero +=nuevoDinero
    	cursor.execute(f'''UPDATE USUARIO SET DINERO = {self.dinero} WHERE NUMERO = {self.numero_id};''')
    	con.commit()# eso sirve para grabar la instruccion de la base datos  en la tabla
    	print('-'*20)
    def retirar(self, nuevoDinero, numero_id): 
    	self.dinero -=nuevoDinero
    	self.disponible -= nuevoDinero
    	cursor.execute(f'''UPDATE USUARIO SET DINERO = '{self.dinero}' WHERE NUMERO = {self.numero_id};''')
    	con.commit()
    	print('-'*20)
    def balance(self, numero_id):
    	lst = ['Numero de identificación', 'NIP', 'Saldo'] # la funcion lst es un arreglo de tres posiciones empezando en 0,1,2
    	cursor.execute(f'''SELECT * FROM USUARIO WHERE NUMERO="{self.numero_id}"''')
    	con.commit()
    	mensaje = ''
    	for c in enumerate(cursor.fetchall()): # el lst es para mostrar la informacion en la pantalla en el orden, ver el programa para saber.
    		print(f"{lst[c[0]]}: {c[1][0]}")
    		print(f"{lst[1]}: {c[1][1]}")
    		print(f"{lst[2]}: ${c[1][2]}")
    		print('-'*20)# eso son las rayitas que aparecen 20 veces 
    		break # eso para que no recorra mas 
    	print('-'*20)	
if __name__ == '__main__':
	def main(): # esta es la funcion principal
		def iniciarSesion():
			opcion = 0
			numero = int(input('Escriba su número de cuenta de 5 digitos: '))# input es para escribir en el teclado
			nip = int(input('Escriba su NIP de 5 digitos: '))
			if len(str(numero)) == 5 and len(str(nip)) == 5: # esto es una valiadacion para saber 5 digitos en el numero de cuenta y nip
				cuenta = Cuenta()  # len es la cantidad de digitos 
				cuenta.crearUsuario(numero,nip)
			while len(str(numero)) != 5 or len(str(nip)) != 5: # el signo de exclamacion igual quiere decir que no es igual te lo pide nuevo

				numero = int(input('Escriba su número de cuenta de 5 digitos: '))
				nip = int(input('Escriba su NIP de 5 digitos: '))
				if len(str(numero)) == 5 and len(str(nip)) == 5:
					cuenta = Cuenta()
					cuenta.crearUsuario(numero,nip) # se hace esto para que si esta bien se grabe la cuenta del usuario 

			while opcion != 4: # esto para que cuando no se seleccione la opcion 4 entre a esta condicion que esta debajo

				print('Bienvenido!')
				if len(str(numero)) == 5 and len(str(nip)) == 5:
					print(f'Menú principal:\n\t1 - Ver mi saldo\n\t2 - Retirar efectivo\n\t3 - Depositar fondos\n\t4 - Salir\n')
					opcion = int(input('Escriba una opción (4 para salir): '))
					if opcion == 1: cuenta.balance(numero)# si lo que pusiste es igual a 1 es para saber el balance 
					elif opcion == 2: # si tu le presionas 2 es para retirar dinero y te aparece las opciones debajo
						print('Opciones de retiro: ')
						print(f'1 - $20\t\t4 - $100\n2 - $40\t\t5 - $200\n3 - $60\t\t6 - Cancelar tansacción')
						dinero = int(input('introduzca opción entre 1 a 6: '))
						if dinero == 1 and cuenta.disponible >= 20 and cuenta.dinero >= 20: cuenta.retirar(20, numero)# si presiono 1 verifica que lo que tengo en la cuenta sea mayor que 20 para poder retirarlo
						elif dinero == 2 and cuenta.disponible >= 40 and cuenta.dinero >= 40: cuenta.retirar(40, numero)
						elif dinero == 3 and cuenta.disponible >= 60 and cuenta.dinero >= 60: cuenta.retirar(60, numero)
						elif dinero == 4 and cuenta.disponible >= 100 and cuenta.dinero >= 100: cuenta.retirar(100, numero)
						elif dinero == 5 and cuenta.disponible >= 200 and cuenta.dinero >= 200: cuenta.retirar(200, numero)
						elif dinero == 6: pass 
						else: print(f'Usted esta retirando más dinero del disponible o no tiene suficiente saldo. Disponible: ${cuenta.disponible}\n{"-"*20}')# eso es para que si pones mas dinero de lo disponible te diga eso
					elif opcion == 3:
						dinero = int(input('introduzca dinero a depositar: '))
						cuenta.depositar(dinero, numero) # va a funcion depositar que esta en la clase cuenta.
                        # en la funcion en cuenta tenemos ver mi balance, retirar y depositar. 

			else: print('Gracias por utilizar nuestros servicios')
			cursor.close()# esto es para cerrar todas las funciones de la base de datos 
		iniciarSesion()

	main()