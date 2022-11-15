#Liftkit Positionieren Pos1 Oben __ Liftkit vers position du haut pos1

#define
t_timeout_Com_Liftkit = 1 		#Timeout in [s]
t_timeout_Mvt_Liftkit = 5 		#Timeout in [s]

#pos_Unten = 3
#pos_Mitte = 2
pos_Oben = 1

serObj = serial.Serial(port='/dev/ttyS1',baudrate=38400,writeTimeout=0.1,timeout=0.1) # For PC and RS232 Port COM2 (Linux Adressierung)

#serObj.setRTS=True #Wenn Werkseinstellung nicht ON ist
#serObj.setDTR=True #Wenn Werkseinstellung nicht ON ist

t = 0	
while True:
	if getCurrentEncSum(serObj) != 0:   #Abfrage Kommunikation Liftkit __ Demande communication Liftkit 
		Global_Stoerung = 0			#Interface Thread Stoerungsmanagement
		break		
	wait (0.1)
	t += 0.1
	if t > t_timeout_Com_Liftkit:
		Global_Stoerung = 1			#Interface Thread Stoerungsmanagement
		set_digital_outputs([11,-12,14])		#Förderband ansteuern damit kein Stau am Eingang entsteht __ activer bande pour qu'il n'y a pas de bouchon à l'entrée
		tp_popup("Keine Kommunikation mit Liftkit __ Liftkit n'a pas de communication", DR_PM_ALARM)

goToPos(serObj, pos_Oben)       #Pos anfahren

t = 0	
while True:
	if Global_enc_LK_MinPos_Oben <= getCurrentEncSum(serObj) <= Global_enc_LK_MaxPos_Oben:      #Abfrage Position Liftkit __ Demande position Liftkit 
		Global_Pos_Liftkit = 1
		Global_Stoerung = 0			#Interface Thread Stoerungsmanagement
		break		
	wait (0.1)
	t += 0.1
	if t > t_timeout_Mvt_Liftkit:
		Global_Stoerung = 1			#Interface Thread Stoerungsmanagement
		set_digital_outputs([11,-12,14])    #Förderband ansteuern damit kein Stau am Eingang entsteht __ activer bande pour qu'il n'y a pas de bouchon à l'entrée
		tp_popup("Liftkit hat Position Oben nicht erreicht __ Liftkit n'atteint pas position en haut, {0} <= Actual {1} <= {2}".format(Global_enc_LK_MinPos_Oben, getCurrentEncSum(serObj), Global_enc_LK_MaxPos_Oben), DR_PM_ALARM)

#enc = getCurrentEncSum(serObj)
#print("Current height (mm): " + str(convertEncToMm(enc)) + ", encoders sum: " + str(enc))

serObj.close()      #For PC