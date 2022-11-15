#----Variabeln----#
global Global_positionen
global Global_positionen_1
global Global_positionen_2
global Global_positionen_3
global System_positione
global Global_ausgangs_pos
global System_Point_1
global System_Point_2
global System_Point_3
global System_Point_4
global System_Point_5
global System_Point_6
global System_Point_7
global System_Point_8
global System_Point_9
global System_Point_10
global System_Point_11
global System_Point_12
global System_Point_13
global System_Point_14
global System_Point_15
global System_Point_16
global System_Point_17
global System_Point_18
global System_Point_19
global System_Point_20

#----Ende----#

#----Korrektur Ausrichtung----#
A = 56.58
B = 90 
C = -90
#----Ende----#


Nbr_Teaching_Points = tp_get_user_input("Wieviele Punkte wollen Sie einlernen? (GANZZAHL)", input_type= DR_VAR_INT)
Global_positionen = dict()
Positionen = []
start_position = posx(590.04,722.11,1152.38,48.07,154.95,-173.09)
''' 
i = 1
for x in range(Nbr_Teaching_Points):
    #test = "System_Point_"+str(i) 
    Global_positionen[test] = posx(590.04,722.11,1152.38 - i*100,48.07,154.95,-173.09)
    Positionen.append(posx(590.04,722.11,1152.38 - i*100,48.07,154.95,-173.09))
    i = i + 1

#tp_popup("test={0}".format(Positionen), DR_PM_MESSAGE)

'''
for x in range(Nbr_Teaching_Points): #Hier werden alle Punkte vom Operator eingelernt eingelernt.
    wait_manual_guide()
    posi,sol = get_current_posx(ref=DR_BASE)
    posi[3] = A
    posi[4] = B
    posi[5] = C

    Positionen.append(posi)

i = 1 
for x in  (Positionen):  # Hier werden alle Positionen in eine System Variabel gespeichert

    globals()['System_Point_%s' % i] = x
    i = i + 1 


#System_positionen = ["Ford", "Volvo", "BMW"]
tp_popup("test={0}".format(Global_positionen), DR_PM_MESSAGE)
movej(Global_ausgangs_pos)
movel(System_Point_1)
movel(System_Point_2)
movel(System_Point_3)
