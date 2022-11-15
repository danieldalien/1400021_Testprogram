#----New Cabinet V2----#
#
# Wir konnten kein Lichtgitter im Automatikmodus einbinden, was 
# manual guiding erlauben würde. Deswegen habe 
# ich das einlernen verändert. Ziel ist es den Punkt einzulernen,
# das Program  zu stoppen. Nun kann der Benutzer den 
# Roboter verfahren. Hat der Roboter die gewünschte Position
# so startet der Benutzer das Programm wieder und wartet auf 
# die nächste Anweisung vom Roboter
# 
#----TO DO----#
#
# 
# 
# 
#
#----Ende TO DO----#


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

global Global_P_Top
global Global_P_Side
global Global_P_Front
global System_Origin_Coord #Origin von Schaltschrank

#--Helfer--#
global Global_Total_Points
global Global_Total_Program
global Global_gelenke_ff
global System_New_Cabinet #Merker ob gerade ein neuer Schrank eingelernt wird
global System_Grad # Merker der ausrichtung 
global System_Am_Lernen # Merker ob er eine neue Position lernt oder eine einspeichert nach programm stopp
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
	force = True 
	while force:
		force = check_force_condition(axis=Axis, max =Global_F_Touch , ref = DR_TOOL)

def relative_bewegung( pos_ini , deltaX , deltaY , deltaZ ):
   
    delta = [ deltaX , deltaY , deltaZ , 0 , 0 , 0 ]
    pos = add_pose(pos_ini , delta)

    return pos     

def plausibilitaets_pruefung(pos):

    plausibilitaet = False
    x_wert = False
    y_wert = False
    z_wert = False

    coord_101 = posx( System_Origin_Coord[ 0 ] - 118.102 , System_Origin_Coord[ 1 ] , System_Origin_Coord[ 2 ] , 0 , 0 , 0  )
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

    tester = True
    for x in range( 1 , int(Global_Total_Program) ): #Hier wird erset freie Programm gefunden 

        point = globals()['System_Pr_%s' % x]

        if point[1] == ID_Cabinet :

            tester = False
            break
    return tester

def check_ausrichtung(pos):
    
    if(pos[4] == 0 ):

        ausrichtung_gerade = True # Punkt wird gerade angefahren 
    else :
        ausrichtung_gerade = False #Punkt wurde mit einem Winkel eingelernt
    
    return ausrichtung_gerade

def fahren( pos , offset , ausrichtung , teach_mode = False ) : 

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

        posi_base = coord_transform(pos , 101 , DR_BASE )
        overwrite_user_cart_coord(102, posi_base, ref=DR_BASE)
        set_ref_coord(102)
        posi = posx( 0 , 0 , 0 , 0 , 0 , 0)
        movel(posi)
        movel(relative_bewegung( posi , 0 , 0 , -offset ))
        movel(posi)

        if teach_mode == False :

            movel(relative_bewegung( posi , 0 , 0 , -offset ))
            set_ref_coord(101)

        elif teach_mode == True :

            correct_position = tp_get_user_input("Position correct ?", input_type=DR_VAR_BOOL)
            set_ref_coord(101)
            return correct_position

def create_dictionary( Points , Programms ):

    if Points == True :

        dict_points = {}

        for x in range( 1 , int(Global_Total_Points) + 1 ): #Hier wird erset freie Position gefunden 
            
            point = globals()['System_Point_%s' % x]
            dict_points[x] = point

        return dict_points
             
    elif Programms == True :

        dict_programms = {}
        for x in range( 1 , int(Global_Total_Program) + 1 ): #Hier wird erset freie Position gefunden 

            programm = globals()['System_Pr_%s' % x]
            dict_programms[x] = programm

        return dict_programms 
  

#----Ende Funktionen----#

overwrite_user_cart_coord( 101, System_Origin_Coord, ref=DR_BASE )
set_ref_coord(101)

if System_New_Cabinet == True :

    while True : 

        Name_Cabinet = tp_get_user_input(" Name of the Cabinet ?" , input_type = DR_VAR_STR )
        if not Name_Cabinet :

            tp_popup(" Empty String, please enter a name  ", DR_PM_MESSAGE)

        else :
            break

    while True :
        
        try:

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

    for x in range( 1 , int(Global_Total_Points) + 1 ): #Hier wird erset freie Position gefunden 

        point = globals()['System_Point_%s' % x]

        if point[0] == 0 and point[1] == 0 and point[2] == 0 :

            ini = x
            break

        if x == int(Global_Total_Points) and point[0] != 0 : #Pruefen ob es noch einen leeren Punkt gibt in den eine Position gespeichert werden kann.
            
            tp_popup(" No more empty points, please contact Supervisor ", DR_PM_ALARM)
            exit()

    #Pruefen ob es noch genug freie Punkte gibt um das Programm einzulernen.
    points = create_dictionary( True , False )
    try:

        points[ ini + Nbr_Teaching_Points ]

    except Exception as e :

        tp_popup(" Not enough empty points to create programm, please contact Supervisor ", DR_PM_ALARM)
        exit()

    for x in range( 1 , int(Global_Total_Program) + 1 ): #Hier wird erstes freies Programm gefunden 

        point = globals()['System_Pr_%s' % x]

        if point[0] == 0 :

            globals()['System_Pr_%s' % x] = [ Name_Cabinet , ID_Cabinet , ini , ini + Nbr_Teaching_Points ]
            System_New_Cabinet = 0
            System_Am_Lernen = 0
            break

        if x == int(Global_Total_Program) and point[0] != 0 :

            tp_popup(" No more empty programms, please contact Supervisor ", DR_PM_ALARM)
            exit()

id_last_programm = 0
id_last_point = 0
  
while True :

    programms = create_dictionary( False , True )
    for x , y in programms.items(): 

        if y[0] == 0 :

            id_last_programm = x - 1
            break
        

    points = create_dictionary( True , False )
    for x , y in points.items():

        if y[0] == 0 and y[1] == 0 and y[2] == 0 :

            id_last_point = x           
            break   

    if int(id_last_point) < int(programms[id_last_programm][2]):

        #Fehlermeldung generieren, darf nicht passieren. Jemand hat Variabeln genullt 
        tp_popup("Critical Error! Position index not conform with Programm index ", DR_PM_ALARM)
        einlernen = False
        exit()

    elif int(id_last_point) >= int(programms[id_last_programm][3]):

        System_New_Cabinet = 1
        System_Am_Lernen = 0
        einlernen = False
        tp_popup("Cabinet Teaching is done ", DR_PM_MESSAGE)
        exit()

    elif int(programms[id_last_programm][3]) > int(id_last_point) >= int(programms[id_last_programm][2]) - 1:
        #Neues Programm wurde nicht fertig eingelernt. Nächsten Punkt einlernen.
        einlernen = True
 
    if einlernen == True:

        if System_Am_Lernen == False: # Neuen Punkt einlernen

            t = tp_get_user_input( "Straight Position ?", input_type = DR_VAR_BOOL )
            if t == True :

                System_Grad = 0 
                System_Am_Lernen = 1
                tp_popup( "Program will close now, position robot and start program again ", DR_PM_ALARM )
                exit()

            else :
                try:
                    while True :

                        System_Grad = tp_get_user_input(" Angle in degree ?" , input_type = DR_VAR_FLOAT )
                        if System_Grad > -60 and System_Grad < 60 :

                            System_Am_Lernen = 1 
                            tp_popup( "Program will close now, position robot and start program again ", DR_PM_ALARM )
                            exit()
                            
                        else:
                            tp_get_user_input( "Angle = ]-60° ; 60°[", input_type = DR_VAR_BOOL )

                except Exception as e : 

                    tp_popup( "Fehler={0}".format(e), DR_PM_MESSAGE )

        elif System_Am_Lernen == True :

            posi,sol = get_current_posx(ref=101)

            if System_Grad == 0 :

                ausrichtung = True 

            else:

                ausrichtung = False 

            posi[3] = 0
            posi[4] = System_Grad
            posi[5] = 0

            test = plausibilitaets_pruefung(posi)
            if test == False :

                posi_base = coord_transform(posi , 101 , DR_BASE )
                tp_popup("The Position = {0} is not in the limits".format(posi_base), DR_PM_MESSAGE)
                tp_popup(" {0} <= {6} <= {1} AND {2} <= {7} <= {3} AND {4} >= {8} >= {5} ".format( round(System_Origin_Coord[ 0 ] - 118.102 - 50 , 2 ) , round( System_Origin_Coord[ 0 ] - 118.102 + Global_Breite_Schrank + 50 , 2 ) , round( System_Origin_Coord[ 1 ] - 50 , 2 ) , round( System_Origin_Coord[ 1 ] + Global_Max_Tiefe_Schrank + 50 , 2 ) , round( System_Origin_Coord[ 2 ] + 50 , 2 ) , round( System_Origin_Coord[ 2 ] - Global_Hoehe_Schrank - 50 , 2 ) , round( posi_base[0] , 2 ) , round( posi_base[1] , 2 ) , round( posi_base[2] , 2 )  ), DR_PM_MESSAGE)
                tp_get_user_input(" Teach Position again and restart programm", input_type=DR_VAR_BOOL) 
                exit()

            elif test == True :

                correct_position = fahren( posi , 150 , ausrichtung , True )
                globals()['System_Point_%s' % id_last_point] = posi
                System_Am_Lernen = 0

                if correct_position == False :

                    tp_get_user_input(" Teach Position again and restart programm ", input_type=DR_VAR_BOOL) 
                    exit()
"""
"""