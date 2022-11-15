


def barcode_id_pruefer():

    Global_Total_Program = 6
    ID_Cabinet = 'test'
    tester = True
    for x in range( 1 , int(Global_Total_Program) ): #Hier wird erset freie Programm gefunden 

        point = globals()['System_Pr_%s' % x]
        tp_popup("={0}".format(x),DR_PM_ALARM)


test = barcode_id_pruefer()