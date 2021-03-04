#coded by Mr. Robot
import sys, os, webbrowser, platform, subprocess

import webbrowser

def __limpiar():
	if os.name == 'nt':
            os.system('cls')
	else:
            os.system('clear')
def menu():
	__limpiar()

	print """

\033[1;31m                                ____            _
\033[1;31m                               |  _ \  _____  _(_)_ __   __ _
\033[1;37m                               | | | |/ _ \ \/ / | '_ \ / _` |
\033[1;37m                               | |_| | (_) >  <| | | | | (_| |
\033[1;31m                               |____/ \___/_/\_\_|_| |_|\__, |
\033[1;31m                                                        |___/

					  \033[1;31mHacking Live\033[1;m
			  \033[1;34mHecho por:\033[1;m Byron Duval & Mr.Robot
  				       \033[1;35mVersion: Beta 1.0
  				      
"""
	print '''
\033[1;32m 1. webmii 	\033[1;32m 7. Dato2        \033[1;32m 13. IpOsito       \033[1;32m19. TinfoLeak         \033[1;32m 25. MentionMap
\033[1;32m 2. RCivl	 \033[1;32m 8. EcLegal       \033[1;32m 14. GrabifiIp    \033[1;32m   20. SleepingTime 	\033[1;32m 26. SkypeIp
\033[1;32m 3. Ruc    	\033[1;32m 9. Celulares    \033[1;32m  15. GeoIp        \033[1;32m   21. SocialBear  	 \033[1;32m 27. Intelligence
\033[1;32m 4. Direccion  \033[1;32m 10. Numeros     \033[1;32m 16. IpLocation    \033[1;32m 22. IdTwitter        \033[1;32m     28. Username
\033[1;32m 5. Siturin    \033[1;32m 11. GeoImagen   \033[1;32m 17. Cabeceras  	 \033[1;32m23. StalkScan         \033[1;32m  29. Zqtwitter
\033[1;32m 6. Datos      \033[1;32m 12. TelfLegal   \033[1;32m 18. FotoForens    \033[1;32m  24. IdFacebook      \033[1;32m 30. Exit

		'''
	d = raw_input("\033[1;30m Doxing > ")

	if d == "1":
		webbrowser.open('https://webmii.com/')

		menu()
	elif d == "2":
		webbrowser.open('http://si.secap.gob.ec/sisecap/servicioObtieneDatosRegistroCivil.php?num_doc=1715318661')
		menu()
	elif d == "3":
		webbrowser.open('https://coresalud.msp.gob.ec/coresalud/app.php/publico/registrounico/obtenerwsruc/1002164190001')
		menu()
	elif d == "4":
		webbrowser.open('https://coresalud.msp.gob.ec/coresalud/app.php/publico/registrounico/establecimiento')
		menu()
	elif d == "5":
		webbrowser.open('https://siturin.turismo.gob.ec/register')
		menu()
	elif d == "6":
		webbrowser.open('https://diego.ec/servicios/reg_civil/?ci=1002637435&key=xcv8900*')
		menu()
	elif d == "7":
		webbrowser.open('https://diego.ec/servicios/reg_civil_new/?ci=1002637435&key=xcv8900*')
		menu()
	elif d == "8":
		webbrowser.open('http://www.ecuadorlegalonline.com/consultas/consultar-numero-cedula/')
		menu()
	elif d == "9":
		webbrowser.open('https://www.imei.info/')
		menu()
	elif d == "10":
		webbrowser.open('https://www.truecaller.com/')
		menu()
	elif d == "11":
		webbrowser.open('http://exif.regex.info/exif.cgi')
		menu()
	elif d == "12":
		webbrowser.open('http://tucelularlegal.arcotel.gob.ec/tucelularlegal/consulta_Imeis.aspx')
		menu()
	elif d == "13":
		webbrowser.open('https://area51space.000webhostapp.com/osito/osito.php')
		menu()
	elif d == "14":
		webbrowser.open('https://grabify.link/')
		menu()
	elif d == "15":
		webbrowser.open('https://tools.tracemyip.org/')
		menu()
	elif d == "16":
		webbrowser.open('https://www.iplocation.net/')
		menu()
	elif d == "17":
		webbrowser.open('https://toolbox.googleapps.com/apps/messageheader/?lang=es')
		menu()
	elif d == "18":
		webbrowser.open('http://fotoforensics.com/')
		menu()
	elif d == "19":
		webbrowser.open('https://tinfoleak.com/')
		menu()
	elif d == "20":
		webbrowser.open('http://sleepingtime.org/')
		menu()
	elif d == "21":
		webbrowser.open('https://socialbearing.com/')
		menu()
	elif d == "22":
		webbrowser.open('https://tweeterid.com/')
		menu()
	elif d == "23":
		webbrowser.open('https://stalkscan.com/')
		menu()
	elif d == "24":
		webbrowser.open('https://es.piliapp.com/facebook/id/')
		menu()
	elif d == "25":
		webbrowser.open('https://mentionmapp.com/')
		menu()
	elif d == "26":
		webbrowser.open('http://mostwantedhf.info/')
		menu()
	elif d == "27":
		webbrowser.open('https://intelx.io/')
		menu()
	elif d == "28":
		webbrowser.open('https://namechk.com/')
		menu()
	elif d == "29":
		webbrowser.open('https://zqdatarecovery.com/zqtwitter_new/')
		menu()
	elif d == "30":
		sys.exit()

menu()
