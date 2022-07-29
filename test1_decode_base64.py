import base64
from colorama import Fore as a
from time import sleep
import os




def al():
	
	print(a.BLUE+"""cloneneg . . . . . . . 
	
	
	""")
	sleep(1.1)

	os.system("clear")
	
	print(a.RED+"""___________________________
	
	 """+a.GREEN+"""           ******************************
	 """+a.RED+"""
	            name is shayq jam 
	           
	         """+a.GREEN+"""   ******************************"""+a.RED+"""
	            fone is 09934388986
	            """+a.GREEN+"""******************************"""+a.RED+"""
	            _____________________________
	            """)
	            
	
	print(a.GREEN+"[1] "+a.RED+"=  "+a.CYAN+"encrypt : ")
	
	print(a.GREEN+"[2] "+a.RED+"=  "+a.CYAN+"decrypt : ")
	
	
	dat=int(input("inte yor add  :  "))
	
	w="_"
	
	
	
	def ali():
		ds=input("inter encrept file name : ")
		encod=ds.encode("utf-8")
		b16=base64.b16encode(encod)
		print(b16)
		
		
		
	def shayq():
		ds=input("enter nem file   :?   ")
		print(base64.b16decode(ds).decode("utf-8"))
		
		
	if dat==1:
		sleep(1.5)
		os.system("clear")
		ali()
		
		print("welvom to encodeng file ")
		
	if dat==2:
		sleep(1.5)
		os.system("clear")
		
		print("""
		
		welcom to ghenel  
		
		""")
		print(w*400)
		
		shayq()
		
		
		
		
		
		print("""
		
		""")

		
		
		
		
	
	
	
	
	
	
	
al()
	