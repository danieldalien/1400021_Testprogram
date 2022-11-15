#!/usr/bin/env python3

#----TO DO----#
#
# 3 Pos Enable Switch (H) (Fuer Sicherheitskreis)
# Handguiding Enable Switch (H)
#
#
#
#
#
#----Ende TO DO----#

import socket
import time

HOST = '0.0.0.0'    # All local IPs
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

conn = 0
addr = 0

#----Variabeln----#
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
global System_Point_21
global System_Point_22
global System_Point_23
global System_Point_24
global System_Point_25
global System_Point_26
global System_Point_27
global System_Point_28
global System_Point_29
global System_Point_30
global System_Point_31
global System_Point_32
global System_Point_33
global System_Point_34
global System_Point_35
global System_Point_36
global System_Point_37
global System_Point_38
global System_Point_39
global System_Point_40
global System_Point_41
global System_Point_42
global System_Point_43
global System_Point_44
global System_Point_45
global System_Point_46
global System_Point_47
global System_Point_48
global System_Point_49
global System_Point_50
global System_Point_51
global System_Point_52
global System_Point_53
global System_Point_54
global System_Point_55
global System_Point_56
global System_Point_57
global System_Point_58
global System_Point_59
global System_Point_60
global System_Point_61
global System_Point_62
global System_Point_63
global System_Point_64
global System_Point_65
global System_Point_66
global System_Point_67
global System_Point_68
global System_Point_69
global System_Point_70
global System_Point_71
global System_Point_72
global System_Point_73
global System_Point_74
global System_Point_75
global System_Point_76
global System_Point_77
global System_Point_78
global System_Point_79
global System_Point_80
global System_Point_81
global System_Point_82
global System_Point_83
global System_Point_84
global System_Point_85
global System_Point_86
global System_Point_87
global System_Point_88
global System_Point_89
global System_Point_90
global System_Point_91
global System_Point_92
global System_Point_93
global System_Point_94
global System_Point_95
global System_Point_96
global System_Point_97
global System_Point_98
global System_Point_99
global System_Point_100
global System_Point_101
global System_Point_102
global System_Point_103
global System_Point_104
global System_Point_105
global System_Point_106
global System_Point_107
global System_Point_108
global System_Point_109
global System_Point_110
global System_Point_111
global System_Point_112
global System_Point_113
global System_Point_114
global System_Point_115
global System_Point_116
global System_Point_117
global System_Point_118
global System_Point_119
global System_Point_120
global System_Point_121
global System_Point_122
global System_Point_123
global System_Point_124
global System_Point_125
global System_Point_126
global System_Point_127
global System_Point_128
global System_Point_129
global System_Point_130
global System_Point_131
global System_Point_132
global System_Point_133
global System_Point_134
global System_Point_135
global System_Point_136
global System_Point_137
global System_Point_138
global System_Point_139
global System_Point_140
global System_Point_141
global System_Point_142
global System_Point_143
global System_Point_144
global System_Point_145
global System_Point_146
global System_Point_147
global System_Point_148
global System_Point_149
global System_Point_150
global System_Point_151
global System_Point_152
global System_Point_153
global System_Point_154
global System_Point_155
global System_Point_156
global System_Point_157
global System_Point_158
global System_Point_159
global System_Point_160
global System_Point_161
global System_Point_162
global System_Point_163
global System_Point_164
global System_Point_165
global System_Point_166
global System_Point_167
global System_Point_168
global System_Point_169
global System_Point_170
global System_Point_171
global System_Point_172
global System_Point_173
global System_Point_174
global System_Point_175
global System_Point_176
global System_Point_177
global System_Point_178
global System_Point_179
global System_Point_180
global System_Point_181
global System_Point_182
global System_Point_183
global System_Point_184
global System_Point_185
global System_Point_186
global System_Point_187
global System_Point_188
global System_Point_189
global System_Point_190
global System_Point_191
global System_Point_192
global System_Point_193
global System_Point_194
global System_Point_195
global System_Point_196
global System_Point_197
global System_Point_198
global System_Point_199


global System_Pr_1
global System_Pr_2
global System_Pr_3
global System_Pr_4
global System_Pr_5
global System_Pr_6
global System_Pr_7
global System_Pr_8
global System_Pr_9
global System_Pr_10
global System_Pr_11
global System_Pr_12
global System_Pr_13
global System_Pr_14
global System_Pr_15
global System_Pr_16
global System_Pr_17
global System_Pr_18
global System_Pr_19
global System_Pr_20
global System_Pr_21
global System_Pr_22
global System_Pr_23
global System_Pr_24
global System_Pr_25
global System_Pr_26
global System_Pr_27
global System_Pr_28
global System_Pr_29
global System_Pr_30


global Global_F_Touch #Kraft 
global Global_Einfahrtiefe_Wait_Touch
global Global_Tastgeschwindigkeit
global Global_Fahrgeschwindigkeit
global Global_rad_zu_grad
global Global_Breite_Schrank 
global Global_Hoehe_Schrank
global Global_Max_Tiefe_Schrank 
global Global_Dist_Schrank #Abstand bis zum Schaltschrank fuer gefahrenloses fahren.

global Global_P_Top
global Global_P_Side
global Global_P_Front
global System_Origin_Coord #Origin von Schaltschrank

#--Helfer--#
global Global_Total_Points
global Global_Total_Program
global Global_gelenke_ff
#--Ende Helfer--#

global System_P_Side_1
global System_P_Side_2
global System_P_Top_1
global System_P_Top_2
global System_winkel_x
global System_winkel_y

#----Ende Variabeln----#

#----Funktionen----#

def wait_touch(Axis) :
    #
    #wait_touch: Checkt ob die Kraft Global_F_Touch erreicht wurde

    #:param Axis: Definiert die Axe auf welcher nach der Kraft gemessen werden soll.
    #
	force = True 
	while force:
		force = check_force_condition(axis=Axis, max =Global_F_Touch , ref = DR_TOOL)

def relative_bewegung( pos_ini , deltaX , deltaY , deltaZ ):
    #
    #relative_bewegung: Berechnet punkt von relativer Bewegung mit angegebenen deltas

    #:param pos_ini: Punkt von dem aus brechnet werden soll.
    #:param delta_x: Verschiebung auf der X-Axe
    #:param delta_y: Verschiebung auf der Y-Axe
    #:param delta_z: Verschiebung auf der Z-Axe
    #:return: Berechneten Punkt
    #
    delta = [ deltaX , deltaY , deltaZ , 0 , 0 , 0 ]
    pos = add_pose(pos_ini , delta)

    return pos 

def fahren( pos , offset , ausrichtung , teach_mode = False ) : 
    #
    #fahren: Fährt den Punkt "pos" in Abhängigkeit von der Ausrichtung an

    #:param pos: Punkt der angefahren werden soll.
    #:param offset: Distanz von Vorposition zur Position 
    #:param ausrichtung: Ob Punkt gerade oder angewinkelt angefahren werden soll
    #:param teach_mode (optional) : Muss nur in der Funktion New_Cabinet auf Wahr gesetzt werden.
    #:return: /
    #:return (Teach Mode) : Wahr = Position als korrekt vom Benutzer bestaetigt 

    if ausrichtung :

        if pos[0] != 0 and pos[1] != 0 and pos[2] != 0 :

            movel(relative_bewegung( pos , 0 , 0 , -offset ))
            movel(pos)
            if teach_mode == False :
                movel(relative_bewegung( pos , 0 , 0 , -offset ))
            elif teach_mode == True :
                correct_position = tp_get_user_input("Position correct ?", input_type=DR_VAR_BOOL)
                
                return correct_position
    else :

        posi_base = coord_transform( pos , 101 , DR_BASE )
        overwrite_user_cart_coord( 102, posi_base, ref=DR_BASE )
        set_ref_coord(102)
        posi = posx( 0 , 0 , 0 , 0 , 0 , 0)
        movel(relative_bewegung( posi , 0 , 0 , -offset ))
        movel(posi)

        if teach_mode == False :
            movel(relative_bewegung( posi , 0 , 0 , -offset ))
            set_ref_coord(101)
        elif teach_mode == True :
            correct_position = tp_get_user_input( "Position correct ?", input_type=DR_VAR_BOOL )
            set_ref_coord( 101 )
            return correct_position

def plausibilitaets_pruefung( pos ):
    #
    #plausibilitaets_pruefung: Checkt ob die Position sich innerhalb des Cabinets befindet 

    #:param pos: Punkt der angefahren werden soll.
    #:return: T = Punkt befindet sich im Cabinet ; F = Punkt befindet sich nicht im Cabinet 
    #
    plausibilitaet = False
    x_wert = False
    y_wert = False
    z_wert = False

    coord_101 = posx( System_Origin_Coord[0] - 118.102 , System_Origin_Coord[1] , System_Origin_Coord[2] , 0 , 0 , 0 )
    posi = coord_transform( pos , 101 , DR_BASE )

    if ( coord_101[0] - 50 <= posi[0] <= coord_101[0] + Global_Breite_Schrank + 50 ) :
        x_wert = True
    if ( coord_101[1] - 50 <= posi[1] <= coord_101[1] +  Global_Max_Tiefe_Schrank + 50 ) : 
        y_wert = True   
    if ( coord_101[2] + 50 >= posi[2] >= coord_101[2] - Global_Hoehe_Schrank - 50 ) : 
        z_wert = True 

    if ( x_wert == True and y_wert == True and z_wert == True ) :
        plausibilitaet = True 

    return plausibilitaet

def barcode_id_pruefer(ID_Cabinet):
    #
    #barcode_id_pruefer: Prueft ob die vom User eingebene barcode_id schon vergeben wurde

    #:param ID_Cabinet: Vom Benutzer, beim einlernen eines neuen Cabinetes, eingegebene ID-Cabinet 
    #:return: T = Frei ; F = Schon vergeben
    #
    tester = True
    for x in range( 1 , int(Global_Total_Program) ): #Hier wird erset freie Programm gefunden 

        point = globals()['System_Pr_%s' % x]

        if point[1] == ID_Cabinet :

            tester = False
            break

    return tester

def check_ausrichtung(pos):
    #
    #check_ausrichtung: Prueft ob Punkt schraeg oder gerade angefahren werden soll

    #:param pos: Punkt der angefahren werden soll.

    #:return: T = Pos soll gerade angefahren werden ; F = Punkt soll schraeg angefahren werden.
    #    
    if(pos[4] == 0 ):
        ausrichtung_gerade = True # Punkt wird gerade angefahren 
    else :
        ausrichtung_gerade = False #Punkt wurde mit einem Winkel eingelernt
    
    return ausrichtung_gerade

#----Ende Funktionen----#

def Orientation_Cabinet():
    #
    #Orientation_Cabinet: Tastet Cabinet ab und überschreibt das Koordinatensystem 101 mit der neuen Ausrichtung

    #:return: /
    #
    set_ref_coord(DR_BASE)

    #---Job 1 : Z herausfinden
    
    movel( Global_P_Top )
    movel(pos = relative_bewegung(Global_P_Top , 0 , 105 , 0 ) ) #
    P_Touch =   relative_bewegung(Global_P_Top , 0 , 105 , -1*Global_Einfahrtiefe_Wait_Touch )
    set_velx(Global_Tastgeschwindigkeit)
    amovel(P_Touch)
    wait_touch(DR_AXIS_X)
    stop(DR_SSTOP)
    set_velx(Global_Fahrgeschwindigkeit)
    P_Touch,sol = get_current_posx()
    System_Origin_Coord[2] = P_Touch[2] #Z Wert vom Origin gespeichert
    movel( relative_bewegung(P_Touch , 0 , 0 , 5 ) )
    movel( Global_P_Top )

    #---Ende Job 1

    #---Job 2 : X herausfinden  

    movel( Global_P_Side )
    movel(pos = relative_bewegung(Global_P_Side , 0 , 105 , 0 ) ) #
    P_Touch = relative_bewegung(Global_P_Side , Global_Einfahrtiefe_Wait_Touch , 105 , 0 )
    set_velx(Global_Tastgeschwindigkeit)
    amovel(P_Touch)
    wait_touch(DR_AXIS_Y)
    stop(DR_SSTOP)
    set_velx(Global_Fahrgeschwindigkeit)
    P_Touch,sol = get_current_posx()
    System_Origin_Coord[0] = P_Touch[0] + 118.102 #Z Wert vom Origin gespeichert ; 15 = radius werkzeug
    movel( Global_P_Side )
    
    #---Ende Job 2
    
    #---Job 3 : winkel herausfinden 

    set_velx( Global_Fahrgeschwindigkeit ) 
    
    movel( Global_P_Front )
    new_front = posx( System_Origin_Coord[0]  , Global_P_Front[1] , System_Origin_Coord[2] - 30 , Global_P_Front[3] , Global_P_Front[4] , Global_P_Front[5] )
    movel( new_front )
    
    P_Touch = relative_bewegung(new_front , 0 , Global_Einfahrtiefe_Wait_Touch , 0 )
    set_velx( Global_Tastgeschwindigkeit )
    amovel( P_Touch )
    wait_touch(DR_AXIS_Z)
    stop( DR_SSTOP )
    set_velx( Global_Fahrgeschwindigkeit ) 
    P_Touch,sol = get_current_posx()
    
    x_1 = P_Touch
    
    movel( new_front )
    front_2 = relative_bewegung(new_front , 300 , 0 , 0 )
    movel(front_2)
    P_Touch = relative_bewegung(front_2 , 0 , Global_Einfahrtiefe_Wait_Touch , 0 )
    set_velx(Global_Tastgeschwindigkeit)
    amovel(P_Touch)
    wait_touch(DR_AXIS_Z)
    stop(DR_SSTOP)
    set_velx(Global_Fahrgeschwindigkeit)
    P_Touch,sol = get_current_posx()
    
    movel( relative_bewegung( P_Touch , 0 , -50 , 0 ) )
    x_2 = P_Touch
    
    winkel_y = ( atan( ( x_1[1] - x_2[1]) / (x_1[0] - x_2[0]) ) ) * Global_rad_zu_grad
    m_2 = ( ( x_2[1] - x_1[1] ) / ( x_2[0] - x_1[0] ) )
    b = (x_2[1]) - m_2*(x_2[0] + abs(System_Origin_Coord[0]))
    System_Origin_Coord[1] = b
    System_Origin_Coord[3] = 90 + winkel_y
    System_Origin_Coord[4] = 90
    System_Origin_Coord[5] = 90
    
    overwrite_user_cart_coord(101, System_Origin_Coord, ref=DR_BASE)

    #---Ende Job 3

def Test_Cabinet(barcode): #Testet angewähltes Cabinet
    #
    #Test_Cabinet: Testet ein Cabinet

    #:param barcode: ID vom Cabinet welches getestet werden soll.

    #:return: /
    #
    overwrite_user_cart_coord(101, System_Origin_Coord, ref=DR_WORLD)
    set_ref_coord(101)
    ini = 0
    end = 0 

    for x in range( 1 , int(Global_Total_Program) ):

        programm = globals()['System_Pr_%s' % x]
        barcode = 123
        if programm[1] == int(barcode) :
            ini = programm[2]
            end = programm[3]
            break

    for x in range( ini , end ) :
        pos = globals()['System_Point_%s' % x]
        check_plausibilitaet = plausibilitaets_pruefung(pos)

        if check_plausibilitaet == True :
        
            fahren(pos , 100 , check_ausrichtung(pos))

        else :
            tp_popup("The Position {0} is not inside of the Cabinet".format('System_Point_%s' % x), DR_PM_MESSAGE)



def New_Cabinet(): #Kreiirt ein neues Cabinet
    #
    #New_Cabinet: Erstellt ein neues Cabinet mithilfe vom User

    #:return: /
    #
    overwrite_user_cart_coord(101, System_Origin_Coord, ref=DR_BASE)
    set_ref_coord(101)
    Name_Cabinet = tp_get_user_input(" Name of the Cabinet ?" , input_type = DR_VAR_STR )

    try:
        while True :
            ID_Cabinet   = tp_get_user_input(" Identifier of the Cabinet ?" , input_type = DR_VAR_INT )
            if barcode_id_pruefer(ID_Cabinet) == True :
                break
            else :
                tp_popup("The ID = {0} is already in use ".format(ID_Cabinet), DR_PM_MESSAGE)
    except Exception as e : 

        tp_popup("Fehler={0}".format(e), DR_PM_MESSAGE)

    while True :
        try:
            Nbr_Teaching_Points = tp_get_user_input("How many points you want to teach? (INTEGER)", input_type = DR_VAR_INT)
            break
        except Exception as e : 

            tp_popup("Fehler={0}".format(e), DR_PM_MESSAGE)

    Positionen = []

    for x in range(Nbr_Teaching_Points): #Hier werden alle Punkte vom Operator eingelernt.

        correct_position = False
        t = tp_get_user_input("Straight Position ?", input_type = DR_VAR_BOOL)
        if t == True :
            Grad = 0 
        else :
            try:
                while True :
                    Grad   = tp_get_user_input(" Angle in degree ?" , input_type = DR_VAR_FLOAT )
                    if Grad > -60 and Grad < 60 :
                        break
                    else:
                        tp_get_user_input("Angle = ]-60° ; 60°[", input_type = DR_VAR_BOOL)

            except Exception as e : 

                tp_popup("Fehler={0}".format(e), DR_PM_MESSAGE)

        while correct_position == False :
            wait_manual_guide()
            posi,sol = get_current_posx(ref=101)
            if Grad == 0 :
                ausrichtung = True 
            else:
                ausrichtung = False 

            posi[3] = 0
            posi[4] = Grad
            posi[5] = 0

            test = plausibilitaets_pruefung(posi)
            if test == False :

                posi_base = coord_transform(posi , 101 , DR_BASE )
                tp_popup("The Position = {0} is not in the limits".format(posi_base), DR_PM_MESSAGE)
                tp_popup(" {0} <= {6} <= {1} AND {2} <= {7} <= {3} AND {4} >= {8} >= {5} ".format( round(System_Origin_Coord[ 0 ] - 118.102 - 50 , 2 ) , round( System_Origin_Coord[ 0 ] - 118.102 + Global_Breite_Schrank + 50 , 2 ) , round( System_Origin_Coord[ 1 ] - 50 , 2 ) , round( System_Origin_Coord[ 1 ] + Global_Max_Tiefe_Schrank + 50 , 2 ) , round( System_Origin_Coord[ 2 ] + 50 , 2 ) , round( System_Origin_Coord[ 2 ] - Global_Hoehe_Schrank - 50 , 2 ) , round( posi_base[0] , 2 ) , round( posi_base[1] , 2 ) , round( posi_base[2] , 2 )  ), DR_PM_MESSAGE)

            elif test == True :

                correct_position = fahren( posi , 150 , ausrichtung , True )

                if correct_position == False :
                    tp_get_user_input(" Teach Position again", input_type=DR_VAR_BOOL)

        Positionen.append(posi)




    for x in range( 1 , int(Global_Total_Points) ): #Hier wird erset freie Position gefunden 

        point = globals()['System_Point_%s' % x]

        if point[0] == 0 and point[1] == 0 and point[2] == 0 :

            ini = x
            break

    for x in range( 1 , int(Global_Total_Program) ): #Hier wird erset freie Programm gefunden 

        point = globals()['System_Pr_%s' % x]

        if point[0] == 0 :

            globals()['System_Pr_%s' % x] = [ Name_Cabinet , ID_Cabinet , ini , ini + Nbr_Teaching_Points ]
            break

        
    for x in  (Positionen):  # Hier werden alle Positionen in eine System Variabel gespeichert
    
        globals()['System_Point_%s' % ini] = x
        ini = ini + 1 

def validateCommand(command):
    # We just check if we received the proper command
    command = command.decode()
    found = False
    for x in range( 1 , 5 ):

        programm = globals()['System_Pr_%s' % x]

        if int(programm[1]) == int(command) or int(command) == 0000:

            found = True
            return True

    if found == False :

        return False 

def doSomething(command):
    # Here we perform the actual job required

    Orientation_Cabinet()

    if( int(command) == 0000):
        New_Cabinet()
    else:
        Test_Cabinet(command)

    #time.sleep(3)
    movej( Global_gelenke_ff )
    print('Processing done, replying')
    conn.sendall('Processing completed - here is the result'.encode())
    return

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # AF_INET is the Internet address family for IPv4. 
    s.bind((HOST, PORT)) #SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport messages in the network.
    s.listen(100) # Hier musste eine Zahl eingefügt werden, die zahl gibt an nach wieviel nicht akzeptierten Verbinungen keine mehr angenommen werden 
    while True:
        print('Waiting for connection...')
        conn, addr = s.accept() #new socket object 
        with conn:
            print('Connection accepted from ', addr)
            while True:
                data = conn.recv(4096) #reads whatever the client sends , 4096 = recv_size
                print('Data received: ' + str(data))
                if not data:
                    break
                if validateCommand(data):
                    conn.sendall('ACK: '.encode() + data)
                    print('Command accepted, perform it')
                    doSomething(data)
                else :
                    conn.sendall('NACK: '.encode() + data)
                    print('Invalid command, rejecting it')
            print('Connection with ' + str(addr) + " lost")




