global Global_test_touch
global Global_test_touch2

def wait_touch() :

    while True:
        if (get_digital_input(13) == False):

            stop(DR_SSTOP)
            P_Touch,sol = get_current_posx()
            tp_popup("Position={0}".format(P_Touch), DR_PM_MESSAGE)
            break

def relative_bewegung( pos_ini , deltaX , deltaY , deltaZ ):
   
    delta = [ deltaX , deltaY , deltaZ , 0 , 0 , 0 ]
    pos = add_pose(pos_ini , delta)

    return pos 

for x in range (0,15):
    movel(Global_test_touch)
    amovel(relative_bewegung(Global_test_touch , 0 , 0 , -7))
    wait_touch()
    movel(Global_test_touch)
    movel(Global_test_touch2)
