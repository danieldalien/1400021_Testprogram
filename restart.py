#Restart

#----TO DO----#
# Wenn die Zelle definiert ist noch andere Grenzwerte eingeben fuer sicheres Rausfahren
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

curr_pos,sol = get_current_posx(DR_BASE)

while True :

    if curr_pos[1] > Global_Dist_Schrank :
        
        tp_popup("Please move the Robot out of the Cabinet !", DR_PM_ALARM)
        wait_manual_guide()
        curr_pos,sol = get_current_posx(DR_BASE)

    else :
        movej(Global_gelenke_ff)
        break



