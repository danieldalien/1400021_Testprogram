#----Orientation Cabinet----#

#----TO DO----#
#
# 
# 
# 
# 
#
#
#
#
#
#
#----Ende TO DO----#

#----Variabeln----#
global Global_positionen
global Global_positionen_1
global Global_positionen_2
global Global_positionen_3
global System_positione
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

global System_Pr_1
global System_Pr_2
global System_Pr_3
global System_Pr_4
global System_Pr_5

global Global_F_Touch #Kraft 
global Global_Einfahrtiefe_Wait_Touch
global Global_Tastgeschwindigkeit
global Global_Fahrgeschwindigkeit
global Global_rad_zu_grad

global Global_Tiefe_Schrank
global Global_Breite_Schrank 

global Global_Home
global Global_P_Top
global Global_P_Side
global Global_P_Front
global Global_ausgangs_pos #Home
global System_P_Coord_1 #Erster Punkt Ausrichtung TOP
global System_P_Coord_2 #Zweiter Punkt Ausrichtung Side_1 , danach mit einer relativen bewegung den 2 finden um den Winkel zu bestimmen.
global System_P_Coord_3 #Dritter Punkt Front
global System_P_Coord_4 #Vierter
global System_Origin_Coord #Origin von Schaltschrank

#--Helfer--#
global Global_Server_Info
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
    timeout_wait_touch = 5
    Global_F_Touch = 1

    t = 0
    while force:
        force = check_force_condition(axis=Axis, min = Global_F_Touch , max = Global_F_Touch + 10 , ref = DR_TOOL)
        if t > timeout_wait_touch:
            break
        else:
            wait( 0.01 )
            t = t + 0.01


def relative_bewegung( pos_ini , deltaX , deltaY , deltaZ ):
   
    delta = [ deltaX , deltaY , deltaZ , 0 , 0 , 0 ]
    pos = add_pose(pos_ini , delta)

    return pos     


#----Ende Funktionen----#

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
#400
#---Job 2 : X herausfinden  
#P_Side = relative_bewegung(P_Touch , -400 , 0 , 5 )
#movel(P_Side)
#movel(relative_bewegung(P_Side , 0 , 0 , -60 ))
#P_Touch = relative_bewegung(P_Side , Global_Einfahrtiefe_Wait_Touch , 0 , -60 )
#tp_popup("Fehler={0}".format(P_Touch), DR_PM_MESSAGE)

movel( Global_P_Side )
movel(pos = relative_bewegung(Global_P_Side , 0 , 105 , 0 ) ) #
P_Touch = relative_bewegung(Global_P_Side , Global_Einfahrtiefe_Wait_Touch , 105 , 0 )
set_velx(Global_Tastgeschwindigkeit)
amovel(P_Touch)
wait_touch(DR_AXIS_Y)
stop(DR_SSTOP)
set_velx(Global_Fahrgeschwindigkeit)
P_Touch,sol = get_current_posx()
System_Origin_Coord[0] = P_Touch[0] + 118.102 
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
