#----Test Cabinet----#

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

def fahren( pos , offset , ausrichtung ) : 

    if ausrichtung :

        if pos[0] != 0 and pos[1] != 0 and pos[2] != 0 :

            movel(relative_bewegung( pos , 0 , 0 , -offset ))
            movel(pos)
            movel(relative_bewegung( pos , 0 , 0 , -offset ))
    else :

        posi_base = coord_transform(pos , 101 , DR_BASE )
        overwrite_user_cart_coord(102, posi_base, ref=DR_BASE)
        set_ref_coord(102)
        posi = posx( 0 , 0 , 0 , 0 , 0 , 0)
        movel(relative_bewegung( posi , 0 , 0 , -offset ))
        movel(posi)
        movel(relative_bewegung( posi , 0 , 0 , -offset ))

        set_ref_coord(101)

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

def check_ausrichtung(pos):
    
    if(pos[4] == 0 ):
        ausrichtung_gerade = True # Punkt wird gerade angefahren 
    else :
        ausrichtung_gerade = False #Punkt wurde mit einem Winkel eingelernt
    
    return ausrichtung_gerade

#----Ende Funktionen----#

overwrite_user_cart_coord(101, System_Origin_Coord, ref=DR_WORLD)
set_ref_coord(101)
ini = 0
end = 0 

for x in range( 1 , int(Global_Total_Program) ):

    programm = globals()['System_Pr_%s' % x]
    #barcode = 123456
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


