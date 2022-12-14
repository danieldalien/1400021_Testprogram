import serial

D1 = {
    "X1" : 1  ,
    "X2" : 2  , 
    "X3" : 4  ,
    "X4" : 8  ,
    "X5" : 16 ,
    "X6" : 32 ,
    "X7" : 64 ,
    "X8" : 128
}

pneumatic = {
    "first_block" : "MPA_Outputs_40003" ,
    "second_block" : "2_Outputs_40004"
}

DI_Signals = {
    "first_block" : "1_DI_45395" ,
    "second_block" :"2_DI_45397" , 
    "third_block" : "3_DI_45399"            
}

handpress_clam = {
    "go_bp" : [ pneumatic["first_block"] , 1 ]  ,
    "go_wp" : [ pneumatic["first_block"] , 2 ]  , 
    "status_bp" : [ DI_Signals["first_block"] , 2 ] ,
    "status_wp" : [ DI_Signals["first_block"] , 1 ] 
}

rotary_gripper_turn = {
    "go_bp" : [ pneumatic["first_block"] , 4 ]  ,
    "go_wp" : [ pneumatic["first_block"] , 8 ]  , 
    "status_bp" : [ DI_Signals["first_block"] , 4 , 8 ] ,
    "status_wp" : [ DI_Signals["first_block"] , 16 , 32 ] 
}

rotary_gripper = {
    "go_bp" : [ pneumatic["first_block"] , 16 ]  ,
    "go_wp" : [ pneumatic["first_block"] , 32 ]  , 
    "status_bp" : [ DI_Signals["first_block"] , 4 , 16 ] ,
    "status_wp" : [ DI_Signals["first_block"] , 8 , 32 ] 
}

rotary_gripper_grip_and_turn = {

  "turn_bp_open" : [ pneumatic["first_block"] , 20 ] ,
  "turn_bp_closed" : [ pneumatic["first_block"] , 36 ] ,
  "turn_wp_open" : [ pneumatic["first_block"] , 24 ] ,
  "turn_wp_closed" : [ pneumatic["first_block"] , 40 ] ,

  "status_turn_bp_open" : [ DI_Signals["first_block"] , 16 ] ,
  "status_turn_bp_closed" : [ DI_Signals["first_block"] , 32 ] ,
  "status_turn_wp_open" : [ DI_Signals["first_block"] , 4 ] ,
  "status_turn_wp_closed" : [ DI_Signals["first_block"] , 8 ] 

}

stroke_horizontal_cylinder = {
    "go_bp" : [ pneumatic["first_block"] , 128 ]  ,
    "go_wp" : [ pneumatic["first_block"] , 64 ]  , 
    "status_bp" : [ DI_Signals["first_block"] , 64 ] ,
    "status_wp" : [ DI_Signals["first_block"] , 128 ] 
}

stroke_verticale_cylinder = {
    "go_bp" : [ pneumatic["second_block"] , 32 ]  ,
    "go_wp" : [ pneumatic["second_block"] , 16 ]  , 
    "status_bp" : [ DI_Signals["second_block"] , 2 ] ,
    "status_wp" : [ DI_Signals["second_block"] , 1 ] 
}

transfer_cylinder = {
    "go_bp" : [ pneumatic["second_block"] , 2 ]  ,
    "go_wp" : [ pneumatic["second_block"] , 1 ]  , 
    "status_bp" : [ DI_Signals["second_block"] , 4 ] ,
    "status_wp" : [ DI_Signals["second_block"] , 8 ] 
}

taster_cylinder = {
  "status_bp" : [ DI_Signals["second_block"] , 16 ] , 
  "status_wp" : [ DI_Signals["second_block"] , 32 ]
}

test_head = {
  "status_bp" : -1 , 
  "status_wp" : [ DI_Signals["second_block"] , 64 ]
}

inlet_sensor_left = {
  "status_bp" : -1 , 
  "status_wp" : [ DI_Signals["third_block"] , 1 ]
}

inlet_sensor_right = {
  "status_bp" : -1 , 
  "status_wp" : [ DI_Signals["third_block"] , 2 ]
}

venturi_vacuum_1 = {
  "status_bp" : -1 , 
  "status_wp" : [ DI_Signals["third_block"] , 4 ]
}

venturi_vacuum_2 = {
  "status_bp" : -1 , 
  "status_wp" : [ DI_Signals["third_block"] , 8 ]
}

venturi_vacuum_3 = {
  "status_bp" : -1 , 
  "status_wp" : [ DI_Signals["third_block"] , 16 ]
}

venturi_vacuum_4 = {
  "status_bp" : -1 , 
  "status_wp" : [ DI_Signals["third_block"] , 32 ]
}



  
#####################################  
     
class modbus( ):


    def __init__(self , D1 , pneumatic , DI_Signals , handpress_clam , rotary_gripper_turn , rotary_gripper , rotary_gripper_grip_and_turn , stroke_horizontal_cylinder , stroke_verticale_cylinder , transfer_cylinder , taster_cylinder , test_head , inlet_sensor_left , inlet_sensor_right , venturi_vacuum_1 , venturi_vacuum_2 , venturi_vacuum_3 , venturi_vacuum_4) :

        self.id_handpress_clam = "handpress_clam"
        self.id_rotary_gripper_turn = "rotary_gripper_turn"
        self.id_rotary_gripper = "rotary_gripper"
        self.id_rotary_gripper_grip_and_turn = "rotary_gripper_grip_and_turn" 
        self.id_stroke_horizontal_cylinder = "stroke_horizontal_cylinder"
        self.id_stroke_verticale_cylinder = "stroke_verticale_cylinder"
        self.id_transfer_cylinder = "transfer_cylinder"
        self.id_taster_cylinder = "taster_cylinder"
        self.id_test_head = "test_head"
        self.id_inlet_sensor_left = "inlet_sensor_left"
        self.id_inlet_sensor_right = "inlet_sensor_right"
        self.id_venturi_vacuum_1 = "venturi_vacuum_1"
        self.id_venturi_vacuum_2 = "venturi_vacuum_2"
        self.id_venturi_vacuum_3 = "venturi_vacuum_3"
        self.id_venturi_vacuum_4 = "venturi_vacuum_4"


        self.handpress_clam = handpress_clam
        self.rotary_gripper_turn = rotary_gripper_turn
        self.rotary_gripper = rotary_gripper
        self.rotary_gripper_grip_and_turn = rotary_gripper_grip_and_turn
        self.stroke_horizontal_cylinder = stroke_horizontal_cylinder
        self.stroke_verticale_cylinder = stroke_verticale_cylinder
        self.transfer_cylinder = transfer_cylinder
        self.taster_cylinder = taster_cylinder
        self.test_head = test_head
        self.inlet_sensor_left = inlet_sensor_left
        self.inlet_sensor_right = inlet_sensor_right
        self.venturi_vacuum_1 = venturi_vacuum_1
        self.venturi_vacuum_2 = venturi_vacuum_2
        self.venturi_vacuum_3 = venturi_vacuum_3
        self.venturi_vacuum_4 = venturi_vacuum_4
        self.D1 = D1
        self.pneumatic = pneumatic
        self.DI_Signals = DI_Signals
        
        self.timeout = 3

    def stop_at_signal( self , id , signal):
        """"
        signal = Stop at bp or stop at wp 
        """
        t = 0 
        while True :
            wp , bp = self.get_status_signal(id)

            if signal == "bp":
                if bp:
                    stop(DR_SSTOP)
                    break
            elif signal == "wp":
                if wp:
                    stop(DR_SSTOP)
                    break   
                         
            if t > self.timeout+15:
                tp_popup("timeout at stop_at_signal()",DR_PM_ALARM)
                exit()
            else:
                wait(0.01)
                t = t + 0.01
    
    def get_cylinder( self , id ):

        #if id == self.rotary_gripper_turn or self.rotary_gripper :
        #  tp_popup("Diese id = {0} ist nicht Konfiguriert".format(id), DR_PM_ALRAM)
        #  exit()

        cylinder = {}

        if id == self.id_handpress_clam :
            cylinder = self.handpress_clam

        elif id == self.id_rotary_gripper_turn:
            cylinder = self.rotary_gripper_turn

        elif id == self.id_rotary_gripper:
            cylinder = self.rotary_gripper

        elif id == self.id_stroke_horizontal_cylinder:
            cylinder = self.stroke_horizontal_cylinder

        elif id == self.id_stroke_verticale_cylinder:
            cylinder = self.stroke_verticale_cylinder

        elif id == self.id_transfer_cylinder:
            cylinder = self.transfer_cylinder

        else:
            tp_popup("Kenne diese id = {0} nicht".format(id), DR_PM_ALARM)

        return cylinder

    def get_signal( self , id ):

        status = {}

        if id == self.id_taster_cylinder:
            status = self.taster_cylinder

        elif id == self.id_test_head:
            status = self.test_head

        elif id == self.id_inlet_sensor_left:
            status = self.inlet_sensor_left

        elif id == self.id_inlet_sensor_right:
            status = self.inlet_sensor_right

        elif id == self.id_venturi_vacuum_1:
            status = self.venturi_vacuum_1

        elif id == self.id_venturi_vacuum_2:
            status = self.venturi_vacuum_2

        elif id == self.id_venturi_vacuum_3:
            status = self.venturi_vacuum_3

        elif id == self.id_venturi_vacuum_4:
            status = self.venturi_vacuum_4

        elif id == self.id_handpress_clam:
            status = self.handpress_clam

        elif id == self.id_stroke_horizontal_cylinder:
            status = self.stroke_horizontal_cylinder

        elif id == self.id_stroke_verticale_cylinder:
            status = self.stroke_verticale_cylinder

        elif id == self.id_transfer_cylinder:
            status = self.transfer_cylinder

    
        else:
            tp_popup("Kenne diese id = {0} nicht".format(id), DR_PM_ALARM)

        return status 

    def get_status_rotary_gripper ( self ):

        if self.rotary_gripper_grip_and_turn["status_turn_bp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]) != 0 :
            status = "bp_open"
        elif self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][0]) != 0 :
            status = "bp_closed"
        elif self.rotary_gripper_grip_and_turn["status_turn_wp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_open"][0]) != 0 :
            status = "wp_open"
        elif self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][0]) != 0 :
            status = "wp_closed"
        else :
            status = "Unknown"
            tp_popup("Unknown status at rotary gripper" , DR_PM_ALARM)
        
        return status 

    def cylinder_to_bp( self , id ) :      

      if id == self.id_rotary_gripper_turn or id == self.id_rotary_gripper :

        status = self.get_status_rotary_gripper()
        #tp_popup("status rotary gripper =  {0}".format(status) , DR_PM_ALARM)

        if id == self.id_rotary_gripper_turn :

          if status == "wp_open":
            set_modbus_output(self.rotary_gripper_grip_and_turn["turn_bp_open"][0] , self.rotary_gripper_grip_and_turn["turn_bp_open"][1] )
            t = 0
            while True :
                if self.rotary_gripper_grip_and_turn["status_turn_bp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]) != 0 :
                    break
                else : 
                    if t > self.timeout :
                        #TBC       
                        tp_popup("timeout cylinder_bp: {0}".format(id) , DR_PM_ALARM)
                    elif t == self.timeout / 2 :
                      set_modbus_output(self.rotary_gripper_grip_and_turn["turn_bp_open"][0] , self.rotary_gripper_grip_and_turn["turn_bp_open"][1] )
                    else :
                        wait( 0.1 )
                        t = t + 0.1

          elif status == "wp_closed":
            set_modbus_output(self.rotary_gripper_grip_and_turn["turn_bp_closed"][0] , self.rotary_gripper_grip_and_turn["turn_bp_closed"][1] )
            t = 0
            while True :
                if self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][0]) != 0 :
                    break
                else : 
                    if t > self.timeout :
                        #TBC       
                        tp_popup("timeout cylinder_bp: {0}".format(id) , DR_PM_ALARM)
                    elif t == self.timeout / 2 :
                      set_modbus_output(self.rotary_gripper_grip_and_turn["turn_bp_closed"][0] , self.rotary_gripper_grip_and_turn["turn_bp_closed"][1] )
                    else :
                        wait( 0.1 )
                        t = t + 0.1
        
        elif id == self.id_rotary_gripper :

          if status == "bp_closed" :
            set_modbus_output(self.rotary_gripper_grip_and_turn["turn_bp_open"][0] , self.rotary_gripper_grip_and_turn["turn_bp_open"][1] )
            t = 0
            while True :
                if self.rotary_gripper_grip_and_turn["status_turn_bp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]) != 0 :
                    break
                else : 
                    if t > self.timeout :
                        #TBC       
                        tp_popup("timeout cylinder_bp: {0}".format(id) , DR_PM_ALARM)
                    elif t == self.timeout / 2 :
                      set_modbus_output(self.rotary_gripper_grip_and_turn["turn_bp_open"][0] , self.rotary_gripper_grip_and_turn["turn_bp_open"][1] )
                    else :
                        wait( 0.1 )
                        t = t + 0.1
          
          elif status == "wp_closed" :
            set_modbus_output(self.rotary_gripper_grip_and_turn["turn_wp_open"][0] , self.rotary_gripper_grip_and_turn["turn_wp_open"][1] )
            t = 0
            while True :
                if self.rotary_gripper_grip_and_turn["status_turn_wp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_open"][0]) != 0 :
                    break
                else : 
                    if t > self.timeout :
                        #TBC       
                        tp_popup("timeout cylinder_bp: {0}".format(id) , DR_PM_ALARM)
                    elif t == self.timeout / 2 :
                      set_modbus_output(self.rotary_gripper_grip_and_turn["turn_wp_open"][0] , self.rotary_gripper_grip_and_turn["turn_wp_open"][1] )
                    else :
                        wait( 0.1 )
                        t = t + 0.1

      else :
        cylinder = self.get_cylinder(id)
        tp_popup("Input modbus = {0}".format(get_modbus_input(cylinder["status_bp"][0])) , DR_PM_ALARM)
        if cylinder["status_bp"][1] & get_modbus_input(cylinder["status_bp"][0]) != 0 :
            tp_popup("Cylinder already in basic position",DR_PM_MESSAGE)
        else :
            set_modbus_output(cylinder["go_bp"][0] , cylinder["go_bp"][1] )
            t = 0
            while True :
                if cylinder["status_bp"][1] & get_modbus_input(cylinder["status_bp"][0]) != 0 :
                    break
                else : 
                    if t > self.timeout :
                        #TBC       
                        tp_popup("timeout cylinder_bp: {0}".format(id) , DR_PM_ALARM)
                    elif t == self.timeout / 2 :
                      set_modbus_output(cylinder["go_bp"][0] , cylinder["go_bp"][1] )
                    else :
                        wait( 0.1 )
                        t = t + 0.1

    def cylinder_to_wp( self , id ) :

      cylinder = self.get_cylinder(id)


      if id == self.id_rotary_gripper_turn or id == self.id_rotary_gripper :

        status = self.get_status_rotary_gripper()
        #tp_popup("status rotary gripper =  {0}".format(status) , DR_PM_ALARM)

        if id == self.id_rotary_gripper_turn :

          if status == "bp_open":
            set_modbus_output(self.rotary_gripper_grip_and_turn["turn_wp_open"][0] , self.rotary_gripper_grip_and_turn["turn_wp_open"][1] )
            t = 0
            while True :
                if self.rotary_gripper_grip_and_turn["status_turn_wp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_open"][0]) != 0 :
                    break
                else : 
                    if t > self.timeout :
                        #TBC       
                        tp_popup("timeout cylinder_bp: {0}".format(id) , DR_PM_ALARM)
                    elif t == self.timeout / 2 :
                      set_modbus_output(self.rotary_gripper_grip_and_turn["turn_wp_open"][0] , self.rotary_gripper_grip_and_turn["turn_wp_open"][1] )
                    else :
                        wait( 0.1 )
                        t = t + 0.1

          elif status == "bp_closed":
            set_modbus_output(self.rotary_gripper_grip_and_turn["turn_wp_closed"][0] , self.rotary_gripper_grip_and_turn["turn_wp_closed"][1] )
            t = 0
            while True :
                if self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][0]) != 0 :
                    break
                else : 
                    if t > self.timeout :
                        #TBC       
                        tp_popup("timeout cylinder_bp: {0}".format(id) , DR_PM_ALARM)
                    elif t == self.timeout / 2 :
                      set_modbus_output(self.rotary_gripper_grip_and_turn["turn_wp_closed"][0] , self.rotary_gripper_grip_and_turn["turn_wp_closed"][1] )
                    else :
                        wait( 0.1 )
                        t = t + 0.1
        
        elif id == self.id_rotary_gripper :

          if status == "bp_open" :
            set_modbus_output(self.rotary_gripper_grip_and_turn["turn_bp_closed"][0] , self.rotary_gripper_grip_and_turn["turn_bp_closed"][1] )
            t = 0
            while True :
                if self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][0]) != 0 :
                    break
                else : 
                    if t > self.timeout :
                        #TBC       
                        tp_popup("timeout cylinder_bp: {0}".format(id) , DR_PM_ALARM)
                    elif t == self.timeout / 2 :
                      set_modbus_output(self.rotary_gripper_grip_and_turn["turn_bp_closed"][0] , self.rotary_gripper_grip_and_turn["turn_bp_closed"][1] )
                    else :
                        wait( 0.1 )
                        t = t + 0.1
          
          elif status == "wp_open" :
            set_modbus_output(self.rotary_gripper_grip_and_turn["turn_wp_closed"][0] , self.rotary_gripper_grip_and_turn["turn_wp_closed"][1] )
            t = 0
            while True :
                if self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][0]) != 0 :
                    break
                else : 
                    if t > self.timeout :
                        #TBC       
                        tp_popup("timeout cylinder_bp: {0}".format(id) , DR_PM_ALARM)
                    elif t == self.timeout / 2 :
                      set_modbus_output(self.rotary_gripper_grip_and_turn["turn_wp_closed"][0] , self.rotary_gripper_grip_and_turn["turn_wp_closed"][1] )
                    else :
                        wait( 0.1 )
                        t = t + 0.1

      else:

        if cylinder["status_wp"][1] & get_modbus_input(cylinder["status_wp"][0]) != 0 :
            tp_popup("Cylinder already in basic position",DR_PM_MESSAGE)
        else :
            set_modbus_output(cylinder["go_wp"][0] , cylinder["go_wp"][1] )
            t = 0
            while True :
                if cylinder["status_wp"][1] & get_modbus_input(cylinder["status_wp"][0]) != 0 :
                    break
                else : 
                    if t > self.timeout :
                        #TBC
                        tp_popup("timeout cylinder: {0}".format(id) , DR_PM_ALARM)

                    elif t == self.timeout / 2 :
                      set_modbus_output(cylinder["go_wp"][0] , cylinder["go_wp"][1] )

                    else :
                        wait( 0.1 )
                        t = t + 0.1

    def move_all( self , position = "bp" ):
      
      if position == "bp" :

        set_modbus_output(self.pneumatic["first_block"] , 149 )
        set_modbus_output(self.pneumatic["second_block"] , 18 )

      if position == "wp" :
        set_modbus_output(self.pneumatic["first_block"] , 106 )
        set_modbus_output(self.pneumatic["second_block"] , 33 )        

    def get_status_signal( self , id ):

        id_signal = self.get_signal(id)
        wp = False
        bp = False

        if id == self.id_taster_cylinder or id == self.id_handpress_clam or id == self.id_stroke_horizontal_cylinder or id == self.id_stroke_verticale_cylinder or id == self.id_taster_cylinder:

            if id_signal["status_wp"][1] & get_modbus_input(id_signal["status_wp"][0]) != 0 :
                wp = True 
            if id_signal["status_bp"][1] & get_modbus_input(id_signal["status_bp"][0]) != 0 : 
                bp = True 
            return wp , bp 
        else : 

            if id_signal["status_wp"][1] & get_modbus_input(id_signal["status_wp"][0]) != 0 :
                wp = True 
            else :
                bp = True

            return wp , bp

    def get_set_output( self , id = 0 , status = 0 ):   

        # First Block 
        first_block_output = 0 

        if self.handpress_clam["status_bp"][1] & get_modbus_input(self.handpress_clam["status_bp"][0]) != 0 :
      
            first_block_output = first_block_output + self.handpress_clam["go_bp"][1]
        elif self.handpress_clam["status_wp"][1] & get_modbus_input(self.handpress_clam["status_wp"][0]) != 0 :
            first_block_output = first_block_output + self.handpress_clam["go_wp"][1]
        else:
            tp_popup("problem at handpress_clam" , DR_PM_ALARM)

        #tp_popup("output = {0}".format(first_block_output), DR_PM_ALARM)

        if self.rotary_gripper_grip_and_turn["status_turn_bp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]) != 0 :
            first_block_output = first_block_output + self.rotary_gripper_grip_and_turn["turn_bp_open"][1]
        elif self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][0]) != 0 :
            first_block_output = first_block_output + self.rotary_gripper_grip_and_turn["turn_bp_closed"][1]
        elif self.rotary_gripper_grip_and_turn["status_turn_wp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_open"][0]) != 0 :
            first_block_output = first_block_output + self.rotary_gripper_grip_and_turn["turn_wp_open"][1]
        elif self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][0]) != 0 :
            first_block_output = first_block_output + self.rotary_gripper_grip_and_turn["turn_wp_closed"][1]
        else:
            tp_popup("problem at rotary_gripper_turn" , DR_PM_ALARM)

        #tp_popup("output = {0}".format(first_block_output), DR_PM_ALARM)

        if self.stroke_horizontal_cylinder["status_bp"][1] & get_modbus_input(self.stroke_horizontal_cylinder["status_bp"][0]) != 0 :
            first_block_output = first_block_output + self.stroke_horizontal_cylinder["go_bp"][1]
        elif self.stroke_horizontal_cylinder["status_wp"][1] & get_modbus_input(self.stroke_horizontal_cylinder["status_wp"][0]) != 0 :
            first_block_output = first_block_output + self.stroke_horizontal_cylinder["go_wp"][1]
        else:
            tp_popup("stroke_horizontal_cylinder" , DR_PM_ALARM)
   

        # Second Block
        second_block_output = 0 

        if self.stroke_verticale_cylinder["status_bp"][1] & get_modbus_input(self.stroke_verticale_cylinder["status_bp"][0]) != 0 :
            second_block_output = second_block_output + self.stroke_verticale_cylinder["go_bp"][1]
        elif self.stroke_verticale_cylinder["status_wp"][1] & get_modbus_input(self.stroke_verticale_cylinder["status_wp"][0]) != 0 :
            second_block_output = second_block_output + self.stroke_verticale_cylinder["go_wp"][1]
        else:
            tp_popup("problem at stroke_verticale_cylinder" , DR_PM_ALARM)

        if self.transfer_cylinder["status_bp"][1] & get_modbus_input(self.transfer_cylinder["status_bp"][0]) != 0 :
            second_block_output = second_block_output + self.transfer_cylinder["go_bp"][1]
        elif self.transfer_cylinder["status_wp"][1] & get_modbus_input(self.transfer_cylinder["status_wp"][0]) != 0 :
            second_block_output = second_block_output + self.transfer_cylinder["go_wp"][1]
        else:
            tp_popup("problem at transfer_cylinder" , DR_PM_ALARM)


        if id != self.id_rotary_gripper_grip_and_turn : 
            cylinder = self.get_cylinder(id)
            id_block = cylinder["status_bp"][0]
            merker = 0
        else :
            id_block = self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]
            merker = 1


        if id_block == self.DI_Signals["first_block"] :

            if merker == 0 :
                if status == "go_bp":
                    if cylinder["status_bp"][1] & get_modbus_input(cylinder["status_bp"][0]) != 0 :
                        first_block_output = first_block_output 
                    elif cylinder["status_wp"][1] & get_modbus_input(cylinder["status_wp"][0]) != 0 :
                        first_block_output = first_block_output - cylinder["go_wp"][1] + cylinder["go_bp"][1]
                    else:
                        tp_popup("Problem at get_set_output" , DR_PM_ALARM)

                elif status == "go_wp":
                    if cylinder["status_bp"][1] & get_modbus_input(cylinder["status_bp"][0]) != 0 :
                        first_block_output = first_block_output - cylinder["go_bp"][1] + cylinder["go_wp"][1]
                    elif cylinder["status_wp"][1] & get_modbus_input(cylinder["status_wp"][0]) != 0 :
                        first_block_output = first_block_output 
                    else:
                        tp_popup("Problem at get_set_output" , DR_PM_ALARM)

            elif merker == 1 :
                if status == "turn_bp_open":
                    if self.rotary_gripper_grip_and_turn["status_turn_bp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]) != 0 :
                        first_block_output = first_block_output 
                    elif self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_bp_closed"][1] + self.rotary_gripper_grip_and_turn["turn_bp_open"][1]
                    elif self.rotary_gripper_grip_and_turn["status_turn_wp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_open"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_wp_open"][1] + self.rotary_gripper_grip_and_turn["turn_bp_open"][1]
                    elif self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_wp_closed"][1] + self.rotary_gripper_grip_and_turn["turn_bp_open"][1]
                    else:
                        tp_popup("Problem at get_set_output" , DR_PM_ALARM)

                elif status == "turn_bp_closed":
                    if self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][0]) != 0 :
                        first_block_output = first_block_output 
                    elif self.rotary_gripper_grip_and_turn["status_turn_bp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_bp_open"][1] + self.rotary_gripper_grip_and_turn["turn_bp_closed"][1]
                    elif self.rotary_gripper_grip_and_turn["status_turn_wp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_open"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_wp_open"][1] + self.rotary_gripper_grip_and_turn["turn_bp_closed"][1]
                    elif self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_wp_closed"][1] + self.rotary_gripper_grip_and_turn["turn_bp_open"][1]
                    else:
                        tp_popup("Problem at get_set_output" , DR_PM_ALARM)

                elif status == "turn_wp_open":
                    if self.rotary_gripper_grip_and_turn["status_turn_wp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_open"][0]) != 0 :
                        first_block_output = first_block_output 
                    elif self.rotary_gripper_grip_and_turn["status_turn_bp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_bp_open"][1] + self.rotary_gripper_grip_and_turn["turn_wp_open"][1]
                    elif self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_bp_closed"][1] + self.rotary_gripper_grip_and_turn["turn_wp_open"][1]
                    elif self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_wp_closed"][1] + self.rotary_gripper_grip_and_turn["turn_wp_open"][1]
                    else:
                        tp_popup("Problem at get_set_output" , DR_PM_ALARM)

                elif status == "turn_wp_closed":
                    if self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][0]) != 0 :
                        first_block_output = first_block_output 
                    elif self.rotary_gripper_grip_and_turn["status_turn_bp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_bp_open"][1] + self.rotary_gripper_grip_and_turn["turn_wp_closed"][1]
                    elif self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_bp_closed"][1] + self.rotary_gripper_grip_and_turn["turn_wp_closed"][1]
                    elif self.rotary_gripper_grip_and_turn["status_turn_wp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_open"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_wp_open"][1] + self.rotary_gripper_grip_and_turn["turn_wp_closed"][1]
                    else:
                        tp_popup("Problem at get_set_output" , DR_PM_ALARM)

        elif id_block == self.DI_Signals["second_block"] :
            if status == "go_bp":
                if cylinder["status_bp"][1] & get_modbus_input(cylinder["status_bp"][0]) != 0 :
                    second_block_output = second_block_output 
                elif cylinder["status_wp"][1] & get_modbus_input(cylinder["status_wp"][0]) != 0 :
                    second_block_output = second_block_output - cylinder["go_wp"][1] + cylinder["go_bp"][1]
                else:
                    tp_popup("Problem at get_set_output" , DR_PM_ALARM)

            elif status == "go_wp":
                if cylinder["status_bp"][1] & get_modbus_input(cylinder["status_bp"][0]) != 0 :
                    second_block_output = second_block_output - cylinder["go_bp"][1] + cylinder["go_wp"][1]
                elif cylinder["status_wp"][1] & get_modbus_input(cylinder["status_wp"][0]) != 0 :
                    second_block_output = second_block_output 
                else:
                    tp_popup("Problem at get_set_output" , DR_PM_ALARM)

        elif id_block == self.DI_Signals["third_block"] :
            pass
        

        set_modbus_output(self.pneumatic["first_block"] , first_block_output )
        set_modbus_output(self.pneumatic["second_block"] , second_block_output )

        while True :
            t = 0
            if id != self.id_rotary_gripper_grip_and_turn : 
                if status == "go_bp":

                    if cylinder["status_bp"][1] & get_modbus_input(cylinder["status_bp"][0]) != 0 :
                        break 
                    else:
                        if t > self.timeout:
                            tp_popup("Timeout get_set_output",DR_PM_ALARM)
                        elif t > self.timeout/2:
                            set_modbus_output(self.pneumatic["first_block"] , first_block_output )
                            set_modbus_output(self.pneumatic["second_block"] , second_block_output )
                        else:
                            t = t + 0.1
                            wait(0.1)

                if status == "go_wp":

                    if cylinder["status_wp"][1] & get_modbus_input(cylinder["status_wp"][0]) != 0 :
                        break 
                    else:
                        if t > self.timeout:
                            tp_popup("Timeout get_set_output",DR_PM_ALARM)
                        elif t > self.timeout/2:
                            set_modbus_output(self.pneumatic["first_block"] , first_block_output )
                            set_modbus_output(self.pneumatic["second_block"] , second_block_output )
                        else:
                            t = t + 0.1
                            wait(0.1)
            else :

                if status == "turn_bp_open":

                    if self.rotary_gripper_grip_and_turn["status_turn_bp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]) != 0 :
                        break 
                    else:
                        if t > self.timeout:
                            tp_popup("Timeout get_set_output",DR_PM_ALARM)
                        elif t > self.timeout/2:
                            set_modbus_output(self.pneumatic["first_block"] , first_block_output )
                            set_modbus_output(self.pneumatic["second_block"] , second_block_output )
                        else:
                            t = t + 0.1
                            wait(0.1)

                elif status == "turn_bp_closed":

                    if self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][0]) != 0 :
                        break 
                    else:
                        if t > self.timeout:
                            tp_popup("Timeout get_set_output",DR_PM_ALARM)
                        elif t > self.timeout/2:
                            set_modbus_output(self.pneumatic["first_block"] , first_block_output )
                            set_modbus_output(self.pneumatic["second_block"] , second_block_output )
                        else:
                            t = t + 0.1
                            wait(0.1)

                elif status == "turn_wp_open":

                    if self.rotary_gripper_grip_and_turn["status_turn_wp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_open"][0]) != 0 :
                        break 
                    else:
                        if t > self.timeout:
                            tp_popup("Timeout get_set_output",DR_PM_ALARM)
                        elif t > self.timeout/2:
                            set_modbus_output(self.pneumatic["first_block"] , first_block_output )
                            set_modbus_output(self.pneumatic["second_block"] , second_block_output )
                        else:
                            t = t + 0.1
                            wait(0.1)


                elif status == "turn_wp_closed":

                    if self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][0]) != 0 :
                        break 
                    else:
                        if t > self.timeout:
                            tp_popup("Timeout get_set_output",DR_PM_ALARM)
                        elif t > self.timeout/2:
                            set_modbus_output(self.pneumatic["first_block"] , first_block_output )
                            set_modbus_output(self.pneumatic["second_block"] , second_block_output )
                        else:
                            t = t + 0.1
                            wait(0.1)


        return first_block_output , second_block_output

    def set_digital_output_wait_input(self , output , set_status ):
        """
        Sets digital output and waits for modbus signal for confirmation 

        output = Integer 
        set_status = "go_wp" or "go_bp"
        """

        if output == 6 : # Greifer Vertikal
            signal = self.id_venturi_vacuum_1
        elif output == 8 : # Greifer Horizontal
            signal = self.id_venturi_vacuum_2
        elif output == 10 : # S1
            signal = self.id_venturi_vacuum_3
        elif output == 12 :
            signal = self.id_taster_cylinder
        elif output == 13 : # SP
            signal = self.id_venturi_vacuum_4
        else :
            signal = "unkown"
            tp_popup("Kenne output:  {0} nicht ! (set_digital_output_wait_input) ".format(output) , DR_PM_ALARM)
            exit()

        if signal != "unkown":
            if set_status == "go_bp":
                set_digital_output(-(output))
                t = 0
                while True: 
                    wp , bp = self.get_status_signal(signal)

                    if bp == True and wp == False :
                        break
                    else:
                        if t > self.timeout:
                            tp_popup("Timeout at output {0}".format(output) , DR_PM_ALARM)
                            exit()
                        else:
                            wait(0.1)
                            t = t + 0.1

            elif set_status == "go_wp":
                set_digital_output((output))
                t = 0
                while True: 
                    wp , bp = self.get_status_signal(signal)

                    if wp == True and bp == False :
                        break
                    else:
                        if t > self.timeout:
                            tp_popup("Timeout at output {0}".format(output) , DR_PM_ALARM)
                            exit()
                        else:
                            wait(0.1)
                            t = t + 0.1

            else :
                tp_popup("Wrong set status " , DR_PM_ALARM)
                exit()

##################################### 
##################################### 

class drive():

    def __init__(self) -> None:
        self.no_blendRadius = 0 
        self.small_blendRadius = 0
        self.big_blendRadius = 0 
        self.v_slow = 50
        self.v_speed = 100
        self.c_hyamp = Hyamp()
        self.c_modbus = modbus(
                    D1 , 
                    pneumatic , 
                    DI_Signals , 
                    handpress_clam , 
                    rotary_gripper_turn , 
                    rotary_gripper , 
                    rotary_gripper_grip_and_turn ,
                    stroke_horizontal_cylinder , 
                    stroke_verticale_cylinder , 
                    transfer_cylinder , 
                    taster_cylinder , 
                    test_head ,
                    inlet_sensor_left , 
                    inlet_sensor_right ,
                    venturi_vacuum_1 , 
                    venturi_vacuum_2 , 
                    venturi_vacuum_3 , 
                    venturi_vacuum_4 ) 
        pass

    def relative_mvt(self , pose_ini = 0 , ref = "DR_WORLD" , deltaX = 0 , deltaY = 0 , deltaZ = 50 , Rx = 0 , Ry = 0 , Rz = 0):
        """
        relative_mvt calculate relative mvt .

        param id: id of the component where vacuum should be set or reset  
        param pose_ini : Positon of which relative movement should be executed (only in DR_BASE)
        param ref : DR_TOOL or DR_WORLD 
        
        return: DR_WORLD: posx  , DR_TOOL : moves directly
        """ 
        
        if ref == "DR_TOOL" :
            Prel = posx(deltaX,deltaY,-1*deltaZ,Rx,Ry,Rz)
            movel(Prel, ref=DR_TOOL, mod=DR_MV_MOD_REL)

        elif ref == "DR_WORLD" :
            if pose_ini == 0 :
                print("[relative_mvt] Unsupported position: {0} ".format(pose_ini))
                tp_popup("[relative_mvt] Unsupported position: {0} ".format(pose_ini), DR_PM_ALARM)
            else:
                delta = [ deltaX , deltaY , deltaZ , Rx , Ry , Rz ]
                pos = [pose_ini[0] + delta[0] , pose_ini[1] + delta[1] , pose_ini[2] + delta[2] , pose_ini[3] + delta[3] , pose_ini[4] + delta[4] , pose_ini[5] + delta[5] ]
                #pos = add_pose(pose_ini , delta)
                return pos
        else :
            print("[relative_mvt] Unsupported reference: {0} ".format(ref))
            tp_popup("[relative_mvt] Unsupported reference: {0} ".format(ref), DR_PM_ALARM)

    def fahren( self , pos , ausrichtung , teach_mode = False ) : 
        """
        This funtion drives to the teached point and will do the -hyamp Test
        """
        if teach_mode:
            if ausrichtung :

                if pos[0] != 0 and pos[1] != 0 and pos[2] != 0 :

                    movel(self.relative_mvt( pos ) , v = self.v_slow , r = self.no_blendRadius)
                    movel(pos , v = self.v_slow , r = self.no_blendRadius)

                    correct_position = tp_get_user_input("Position correct ?", input_type=DR_VAR_BOOL)
                        
                    return correct_position
            else :

                #posi_base = coord_transform(pos , 101 , DR_WORLD )
                overwrite_user_cart_coord(102, pos, ref=DR_WORLD)
                set_ref_coord(102)
                posi = posx( 0 , 0 , 0 , 0 , 0 , 0)
                movel(posi , v = self.v_slow , r = self.no_blendRadius  )
                movel(self.relative_mvt( posi , deltaZ= -50 ), v = self.v_slow , r = self.no_blendRadius)
                movel(posi , v = self.v_slow , r = self.no_blendRadius)


                correct_position = tp_get_user_input("Position correct ?", input_type=DR_VAR_BOOL)
                if correct_position :
                    for x in range (1 , 20)  :
                        cur_pos , sol = get_current_posx(DR_WORLD)
                        home_L = fkin(Global_Home , ref = DR_WORLD)
                        safe_y = home_L[1]
                        
                        if cur_pos[1] > safe_y:
                            movel(self.relative_mvt( posi , deltaZ= -50*x ), v = self.v_slow , r = self.no_blendRadius)
                        else :
                            break
                    
                    movej(Global_Home , r = self.small_blendRadius)

                return correct_position
        else: 
            pos_world = coord_transform(pos , 101 , DR_WORLD )
            overwrite_user_cart_coord(102, pos_world, ref=DR_WORLD)
            set_ref_coord(102)
            posi = posx( 0 , 0 , 0 , 0 , 0 , 0)
            
            movel(self.relative_mvt( posi , deltaZ= -200 ) , r = self.small_blendRadius)
            movel(self.relative_mvt( posi , deltaZ= -50 ) , v = self.v_speed , r = self.no_blendRadius)
            amovel(self.relative_mvt( posi , deltaZ= +20 ) , v = self.v_slow / 2 )
            self.c_modbus.stop_at_signal(self.c_modbus.id_test_head , "wp")
            #tp_popup("Mache Test....",DR_PM_ALARM)
            self.c_hyamp.test_point()
            

            for x in range (1 , 20)  :
                cur_pos , sol = get_current_posx(DR_WORLD)
                home_L = fkin(Global_Home , ref = DR_WORLD)
                safe_y = home_L[1]
               
                if cur_pos[1] > safe_y:
                    movel(self.relative_mvt( posi , deltaZ= -50*x ), v = self.v_slow , r = self.no_blendRadius)
                else :
                    break

            movej(Global_Home , r = self.small_blendRadius)

    def check_home( self ):
        """
        Checks if Roboter is near homeposition 
        """

##################################### 
##################################### 

class functions() :

    global Global_Total_Points
    global Global_Total_Program
    global Global_Breite_Schrank
    global Global_Max_Tiefe_Schrank
    global Global_Hoehe_Schrank

    Global_Total_Points = 20
    Global_Total_Program = 10
    Global_Breite_Schrank = 90
    Global_Max_Tiefe_Schrank = 1500
    Global_Hoehe_Schrank = 50 

    def __init__(self) -> None:

        pass
    
    def plausibilitaets_pruefung(self,pos):
        """
       plausibilitaets_pruefung checks if teached points is inside the cabinet limits .

        param pos: position which needs to be checked  
        
        return: true/false
        """
        plausibilitaet = False
        x_wert = False
        y_wert = False
        z_wert = False

        #coord_101 = posx( System_Origin_Coord[ 0 ] - 118.102 , System_Origin_Coord[ 1 ] , System_Origin_Coord[ 2 ] , 0 , 0 , 0  )
        #posi = coord_transform( pos , 101 , DR_WORLD )

        if ( 420 <= pos[0] <= 1265 ) :
            x_wert = True
        if ( 640 <= pos[1] <= 1800 ) : 
            y_wert = True   
        if ( -900 <= pos[2] <= 1500 ) : 
            z_wert = True 

        if ( x_wert == True and y_wert == True and z_wert == True ) :
            plausibilitaet = True 

        return plausibilitaet

    def barcode_id_pruefer(self,ID_Cabinet):
        """
        barcode_id_pruefer checks if introduced barcode already exists and if its valid  .

        param ID_Cabinet: Introduced Id which needs to be checked  
        
        return: true/false
        """
        tester = True
        for x in range( 1 , int(Global_Total_Program) ): #Hier wird erset freie Programm gefunden 

            point = globals()['System_Pr_%s' % x]

            if point[1] == ID_Cabinet :

                tester = False
                break

        return tester

    def check_ausrichtung(self,pos):
        """
        check_ausrichtung checks whether it is a straight point to be approached or not   .

        param pos: position which needs to be checked    
        
        return: bool: ausrichtung_gerade (True = straight)
        """
        if(pos[4] == 0 ):

            ausrichtung_gerade = True # Punkt wird gerade angefahren 
        else :
            ausrichtung_gerade = False #Punkt wurde mit einem Winkel eingelernt
        
        return ausrichtung_gerade
    
    def create_dictionary( self , Points , Programms ):
        """
        create_dictionary creates dictionarry with all Points / Program variables inside the Doosan  

        param Point: When True creates dictionary os System_Points  
        param Program: When True creates dictionary os System_Proramms     
        
        return: dict
        """
        if Points == True :

            dict_points = {}

            for x in range( 1 , int(Global_Total_Points) + 1 ): #Hier wird erset freie Position gefunden 
                
                point = globals()['System_Point_%s' % x]
                dict_points[x] = point

                
        elif Programms == True :

            dict_programms = {}
            for x in range( 1 , int(Global_Total_Program) + 1 ): #Hier wird erset freie Position gefunden 

                programm = globals()['System_Pr_%s' % x]
                dict_programms[x] = programm 

        if Points == True and Programms == False:
            return dict_points
        elif Programms == True and Points == False :
            return dict_programms
        elif Programms == True and Points == True:
            return dict_points , dict_programms

    def calc_points(self):
        """
        Calc waypoints
        """

        global Global_P_Top
        global Global_P_Side

##################################### 
##################################### 

class Hyamp():

    def __init__(self) -> None:
        pass

    def serialWrite(self,serial, data):
        return serial.write(data)               
    
    def serialRead(self,serial, length):  
        return serial.read(length)        

    def enable_Remote(self):

        try :
            serObj = serial.Serial(port='/dev/ttyUSB0',baudrate=38400, bytesize=DR_EIGHTBITS, parity=DR_PARITY_NONE, stopbits=DR_STOPBITS_ONE,writeTimeout=3,timeout=3) # For PC and RS232 Port COM2 (Linux Adressierung)
        except Exception as e:
            tp_popup("Turn ON HYAMP AND connect USB to Doosan and HYAMP", DR_PM_ALARM)
            return False

        check_remote = self.serialWrite(serObj , b'SPR?\n')
        time.sleep(1)
        serialread = self.serialRead(serObj , check_remote )

        if int(serialread) == 0 :
            msg = b'SPR{1}\n'
            write = self.serialWrite(serObj , msg)
            time.sleep(1)
            serialread = self.serialRead(serObj , write )

            check_remote = self.serialWrite(serObj , b'SPR?\n')
            time.sleep(1)
            serialread = self.serialRead(serObj , check_remote )
            if int(serialread) == 0 :
                tp_popup("Could not enable Remote Connection")
                serObj.close()
                return False

        #serObj.close()
        return serObj 

    def get_test_results(self , serObj):
        global System_test
        global System_test_hyamp

        try:

            #serObj = self.enable_Remote()

            #serObj = serial.Serial(port='/dev/ttyUSB0',baudrate=38400, bytesize=DR_EIGHTBITS, parity=DR_PARITY_NONE, stopbits=DR_STOPBITS_ONE,writeTimeout=3,timeout=3) # For PC and RS232 Port COM2 (Linux Adressierung)

            msg = b'TD?\n , RD<1>\n , RD<2>\n , RD<3>\n , RD<4>\n , RD<5>\n '
        
        
            test = self.serialWrite(serObj , msg)
            time.sleep(1)
            serialread = self.serialRead(serObj , test )
            test_res = str(serialread)
            result = test_res.split("\\n")
            System_test_hyamp = result[1].split(",")

            tp_popup("Result={0}".format(System_test_hyamp), DR_PM_MESSAGE)


        except Exception as e: 
            tp_popup("Fehler={0}".format(e), DR_PM_MESSAGE)

    def test_point(self):

        try:

            serObj = self.enable_Remote()

            #serObj = serial.Serial(port='/dev/ttyUSB0',baudrate=38400, bytesize=DR_EIGHTBITS, parity=DR_PARITY_NONE, stopbits=DR_STOPBITS_ONE,writeTimeout=3,timeout=3) # For PC and RS232 Port COM2 (Linux Adressierung)
            
            msg = b'TEST\n'
            test = self.serialWrite(serObj , msg)
            res = wait_digital_input(15 , ON , 10)
            if res == 0:
                res = wait_digital_input(15 , OFF , 10)
                if res == 0 : 
                    pass
                else:
                    tp_popup("Problem while Processing" , DR_PM_ALARM)
            else :
                tp_popup("Problem while Processing" , DR_PM_ALARM)

            if get_digital_input(13):
                tp_popup("TEST SUCCEDED", DR_PM_MESSAGE)

                self.get_test_results(serObj)
                serObj.close()

            elif get_digital_input(14):

                tp_popup("TEST FAILED", DR_PM_MESSAGE)
                set_digital_output( 15 , ON, 0.5 , OFF)
                wait(0.1)
                set_digital_output( 15 , ON, 0.5 , OFF)
                serObj.close()


            #serialread = self.serialRead(serObj , test )
            #tp_popup("TEST={0}".format(serialread), DR_PM_MESSAGE)
            

        except Exception as e: 
            try:

                serObj = self.enable_Remote()

                #serObj = serial.Serial(port='/dev/ttyUSB0',baudrate=38400, bytesize=DR_EIGHTBITS, parity=DR_PARITY_NONE, stopbits=DR_STOPBITS_ONE,writeTimeout=3,timeout=3) # For PC and RS232 Port COM2 (Linux Adressierung)
                
                msg = b'TEST\n'
                test = self.serialWrite(serObj , msg)
                res = wait_digital_input(15 , ON , 10)
                if res == 0:
                    res = wait_digital_input(15 , OFF , 10)
                    if res == 0 : 
                        pass
                    else:
                        tp_popup("Problem while Processing" , DR_PM_ALARM)
                else :
                    tp_popup("Problem while Processing" , DR_PM_ALARM)

                if get_digital_input(13):
                    tp_popup("TEST SUCCEDED", DR_PM_MESSAGE)

                    self.get_test_results(serObj)
                    serObj.close()

                elif get_digital_input(14):

                    tp_popup("TEST FAILED", DR_PM_MESSAGE)
                    set_digital_output( 15 , ON, 0.5 , OFF)
                    wait(0.1)
                    set_digital_output( 15 , ON, 0.5 , OFF)
                    serObj.close()


                #serialread = self.serialRead(serObj , test )
                #tp_popup("TEST={0}".format(serialread), DR_PM_MESSAGE)
                

            except Exception as e: 
                tp_popup("Fehler_test_point={0}".format(e), DR_PM_MESSAGE)

##################################### 
##################################### 

class runtime():  

    def __init__(self) -> None:
        self.c_functions = functions()
        self.c_drive = drive()
        self.no_blendRadius = 0 
        self.small_blendRadius = 0
        self.big_blendRadius = 0
        self.tastgeschwindigkeit = 10 
        self.c_modbus = modbus(
                    D1 , 
                    pneumatic , 
                    DI_Signals , 
                    handpress_clam , 
                    rotary_gripper_turn , 
                    rotary_gripper , 
                    rotary_gripper_grip_and_turn ,
                    stroke_horizontal_cylinder , 
                    stroke_verticale_cylinder , 
                    transfer_cylinder , 
                    taster_cylinder , 
                    test_head ,
                    inlet_sensor_left , 
                    inlet_sensor_right ,
                    venturi_vacuum_1 , 
                    venturi_vacuum_2 , 
                    venturi_vacuum_3 , 
                    venturi_vacuum_4 ) 
  
    def New_Cabinet(self):

        global System_Am_Lernen
        global System_New_Cabinet
        global System_Grad
        Global_Total_Program = 5
        Global_Total_Points = 20

        overwrite_user_cart_coord( 101, System_Origin_Coord, ref=DR_WORLD )
        #set_ref_coord(101)
        set_ref_coord(DR_WORLD)

        if System_New_Cabinet == True :

            self.Orientation_Cabinet()

            while True : 

                Name_Cabinet = tp_get_user_input(" Name of the Cabinet ?" , input_type = DR_VAR_STR )
                if not Name_Cabinet :

                    tp_popup(" Empty String, please enter a name  ", DR_PM_MESSAGE)

                else :
                    break

            while True :
                
                try:

                    ID_Cabinet   = tp_get_user_input(" Identifier of the Cabinet ?" , input_type = DR_VAR_INT )
                    if self.c_functions.barcode_id_pruefer(ID_Cabinet) == True :              
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
            points = self.c_functions.create_dictionary( True , False )
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

        while True :

            id_last_programm = 0
            id_last_point = 0
            programms = self.c_functions.create_dictionary( False , True )
            for x , y in programms.items(): #Findet das letzte freie Programm array

                if y[0] == 0 :

                    id_last_programm = x - 1
                    break
                

            points = self.c_functions.create_dictionary( True , False )
            for x , y in points.items(): # Findet den Letzten freien Punkt in den Systemvariabeln

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
                #Neues Programm wurde nicht fertig eingelernt. N??chsten Punkt einlernen.
                einlernen = True
        
            if einlernen == True:

                if System_Am_Lernen == False: # Neuen Punkt einlernen

                    tp_popup( "Program will close now, position robot and start program again ", DR_PM_ALARM )
                    System_Am_Lernen = 1
                    System_Grad = 5
                    exit()
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
                                    tp_get_user_input( "Angle = ]-60?? ; 60??[", input_type = DR_VAR_BOOL )

                        except Exception as e : 

                            tp_popup( "Fehler={0}".format(e), DR_PM_MESSAGE )

                elif System_Am_Lernen == True :

                    posi,sol = get_current_posx(ref=DR_WORLD)

                    if System_Grad == 0 :

                        ausrichtung = True 
                        posi[3] = 90
                        posi[4] = 90
                        posi[5] = 90

                    else:

                        ausrichtung = False 

                    

                    test = self.c_functions.plausibilitaets_pruefung(posi)
                    if test == False :

                        posi_base = coord_transform(posi , 101 , DR_WORLD )
                        tp_popup("The Position = {0} is not in the limits".format(posi_base), DR_PM_MESSAGE)
                        tp_popup(" {0} <= {6} <= {1} AND {2} <= {7} <= {3} AND {4} >= {8} >= {5} ".format( round(System_Origin_Coord[ 0 ] - 118.102 - 50 , 2 ) , round( System_Origin_Coord[ 0 ] - 118.102 + Global_Breite_Schrank + 50 , 2 ) , round( System_Origin_Coord[ 1 ] - 50 , 2 ) , round( System_Origin_Coord[ 1 ] + Global_Max_Tiefe_Schrank + 50 , 2 ) , round( System_Origin_Coord[ 2 ] + 50 , 2 ) , round( System_Origin_Coord[ 2 ] - Global_Hoehe_Schrank - 50 , 2 ) , round( posi_base[0] , 2 ) , round( posi_base[1] , 2 ) , round( posi_base[2] , 2 )  ), DR_PM_MESSAGE)
                        tp_get_user_input(" Teach Position again and restart programm", input_type=DR_VAR_BOOL) 
                        exit()

                    elif test == True :

                        correct_position = self.c_drive.fahren( posi , ausrichtung , True )
                        
                        if correct_position == False :

                            tp_get_user_input(" Teach Position again and restart programm ", input_type=DR_VAR_BOOL) 
                            exit()
                        else:
                            pos_101 = coord_transform(posi , DR_WORLD , 101 )
                            globals()['System_Point_%s' % id_last_point] = pos_101
                            System_Am_Lernen = 0

    def Orientation_Cabinet(self):
        """
        Orientation_Cabinet: Tastet Cabinet ab und ??berschreibt das Koordinatensystem 101 mit der neuen Ausrichtung
        :return: /
        
        set_ref_coord(DR_BASE)
        """
        global System_Origin_Coord
        global System_test_x1
        global System_test_x2
        global System_test_winkel
        global System_Cur_Pos

        tiefe_p2_winkel = 720

        test = set_ref_coord(DR_WORLD)
        
        #---Job 1 : Z herausfinden
        
        #self.c_modbus.set_digital_output_wait_input(12 , "go_bp")
        set_digital_output(-12)

        movej( Global_Home , r = self.small_blendRadius )
        System_Cur_Pos = 1000

        # Move Pre Pos 
        pre_pos,sol = get_current_posx(DR_WORLD)
        pre_pos[2] = Global_P_Top[2]
        pre_pos[3] = Global_P_Top[3]
        pre_pos[4] = Global_P_Top[4]
        pre_pos[5] = Global_P_Top[5]
        movel( pre_pos , r = self.small_blendRadius )
        System_Cur_Pos = 1001


        movel( Global_P_Top , r = self.small_blendRadius )
        System_Cur_Pos = 1005
        self.c_modbus.set_digital_output_wait_input(12 , "go_wp")

        #Get Cabinet Height
        amovel(self.c_drive.relative_mvt(Global_P_Top , deltaZ = -100 ) , v = self.tastgeschwindigkeit ) #
        self.c_modbus.stop_at_signal(self.c_modbus.id_taster_cylinder , "bp")

        P_Touch,sol = get_current_posx()
        System_Cur_Pos = 1006

        System_Origin_Coord[2] = P_Touch[2] #Z Wert vom Origin gespeichert
        #self.c_modbus.set_digital_output_wait_input(12 , "go_bp")
        set_digital_output(-12)
        movel( Global_P_Top , r = self.small_blendRadius )
        System_Cur_Pos = 1005 

        movel(self.c_drive.relative_mvt(pre_pos , deltaY = -200 , deltaZ=0 ) , r = self.small_blendRadius ) #
        System_Cur_Pos = 1007

        #Home_L = fkin(Global_Home , DR_WORLD)
        #pre_pos,sol = get_current_posx(DR_WORLD)
        #pre_pos[1] = Home_L[1] 
        #pre_pos[3] = Global_P_Top[3]
        #pre_pos[4] = Global_P_Top[4]
        #pre_pos[5] = Global_P_Top[5]
        #movel( pre_pos , r = self.small_blendRadius )        
        #movej( Global_Home , r = self.small_blendRadius )
        
        #---Ende Job 1
        
        #--Job 2 : Y herausfinden
        
        movej( Global_Home , r = self.small_blendRadius )
        Home_L = fkin(Global_Home , DR_WORLD)
        pre_pos,sol = get_current_posx(DR_WORLD)
        pre_pos[1] = Home_L[1] - 50
        pre_pos[2] = System_Origin_Coord[2] - 45.681 - 10
        pre_pos[3] = 90
        pre_pos[4] = 7
        pre_pos[5] = -156
        movel( pre_pos , r = self.small_blendRadius )

        pre_pos[2] = pre_pos[2] + 140.4
        pre_pos[1] = pre_pos[1] + 150
        movel( pre_pos , r = self.small_blendRadius )
        #tp_popup("??re_pos = {0}".format(pre_pos),DR_PM_ALARM)
        #tp_popup("pos = {0}".format(self.c_drive.relative_mvt(pre_pos , deltaY = 500 , deltaZ=0 )),DR_PM_ALARM)
        self.c_modbus.set_digital_output_wait_input(12 , "go_wp")
        amovel(self.c_drive.relative_mvt(pre_pos , deltaY = 300 , deltaZ=0 ) , v = self.tastgeschwindigkeit ) #
        self.c_modbus.stop_at_signal(self.c_modbus.id_taster_cylinder , "bp")
        #set_digital_output(-12)

        P_Touch,sol = get_current_posx(DR_WORLD)
        System_Origin_Coord[1] = P_Touch[1] #Z Wert vom Origin gespeichert
        #self.c_modbus.set_digital_output_wait_input(12 , "go_bp")
        set_digital_output(-12)
        pre_pos = posx(P_Touch)
        pre_pos[1] = pre_pos[1] - 150 
        movel(pre_pos , r = self.small_blendRadius)

        movej(Global_Home , r = self.small_blendRadius)
        
        #---Ende Job 2
        
        #---Job 2 : X herausfinden  

        #movej( Global_Home , r = self.small_blendRadius )

        #self.c_modbus.set_digital_output_wait_input(12 , "go_bp")
        set_digital_output(-12)
        movej( Global_pre_Side , r = self.small_blendRadius )

        pre_pos,sol = get_current_posx(DR_WORLD)
        pre_pos[1] = System_Origin_Coord[1] + 140.4 + 55
        pre_pos[2] = pre_pos[2] + 300
        movel( pre_pos , r = self.small_blendRadius)

        pre_pos[0] = 460
        pre_pos[3] = Global_P_Side[3] - 4
        pre_pos[4] = Global_P_Side[4]
        pre_pos[5] = Global_P_Side[5]
        movel( pre_pos , r = self.small_blendRadius)
        self.c_modbus.set_digital_output_wait_input(12 , "go_wp")
        amovel(self.c_drive.relative_mvt(pre_pos , deltaX = 200 , deltaZ=0 ) , v = self.tastgeschwindigkeit ) #
        self.c_modbus.stop_at_signal(self.c_modbus.id_taster_cylinder , "bp")
        # set_digital_output(-12)
        P_Touch,sol = get_current_posx(DR_WORLD)
        System_test_x1 = posx(P_Touch)
        System_Origin_Coord[0] = P_Touch[0] #Z Wert vom Origin 

        #self.c_modbus.set_digital_output_wait_input(12 , "go_bp")
        set_digital_output(-12)

        pre_pos = posx(P_Touch)
        pre_pos[0] = pre_pos[0] - 50 
        movel(pre_pos , r = self.small_blendRadius)

        pre_pos[1] = pre_pos[1] + tiefe_p2_winkel
        movel(pre_pos , r = self.small_blendRadius)
        self.c_modbus.set_digital_output_wait_input(12 , "go_wp")
        amovel(self.c_drive.relative_mvt(pre_pos , deltaX = 200 , deltaZ=0 ) , v = self.tastgeschwindigkeit ) #
        self.c_modbus.stop_at_signal(self.c_modbus.id_taster_cylinder , "bp")
        P_Touch,sol = get_current_posx(DR_WORLD)
        System_test_x2 = posx(P_Touch)
        #self.c_modbus.set_digital_output_wait_input(12 , "go_bp")
        set_digital_output(-12)

        pre_pos = posx(P_Touch)
        pre_pos[0] = pre_pos[0] - 50 
        movel(pre_pos , r = self.small_blendRadius)

        # Winkel Berechnen :

        ankathete = System_test_x1[0] - System_test_x2[0]
        gegenkathete=  System_test_x1[1] - System_test_x2[1]
        System_test_winkel = r2d(atan(gegenkathete/ankathete))

        if System_test_winkel < 0:
            System_test_winkel = 90 + System_test_winkel
            System_test_winkel = 90 + System_test_winkel
        elif System_test_winkel >=0:
            System_test_winkel = 90 - System_test_winkel
            System_test_winkel = 90 - System_test_winkel

        System_Origin_Coord[3] = System_test_winkel
        System_Origin_Coord[4] = 90
        System_Origin_Coord[5] = 90
        
        overwrite_user_cart_coord(101, System_Origin_Coord, ref=DR_WORLD)        
        #Berechnung Origin :

        m1 = (( System_test_x2[1] - System_test_x1[1] ) / System_test_x2[0] - System_test_x1[0])
        b1 = System_test_x2[1] - m1*System_test_x2[0]

        m2 = -1*m1
        b2 = 0

        movej( Global_pre_Side , r = self.small_blendRadius )
        movej(Global_Home , r = self.small_blendRadius)


        #P_Touch = relative_bewegung(Global_P_Side , Global_Einfahrtiefe_Wait_Touch , 105 , 0 )
        #set_velx(Global_Tastgeschwindigkeit)
        #amovel(P_Touch)
        #wait_touch(DR_AXIS_Y)
        #stop(DR_SSTOP)
        #set_velx(Global_Fahrgeschwindigkeit)
        #P_Touch,sol = get_current_posx()
        #System_Origin_Coord[0] = P_Touch[0] + 118.102 #Z Wert vom Origin gespeichert ; 15 = radius werkzeug
        #movel( Global_P_Side )
        
        #---Ende Job 2

        
        #---Job 3 : winkel herausfinden 
        """
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
        
        overwrite_user_cart_coord(101, System_Origin_Coord, ref=DR_WORLD)
        """

    def Test_Cabinet(self , barcode ): #Testet angew??hltes Cabinet
        #
        #Test_Cabinet: Testet ein Cabinet

        #:param barcode: ID vom Cabinet welches getestet werden soll.

        #:return: /
        #
        self.Orientation_Cabinet()
        overwrite_user_cart_coord(101, System_Origin_Coord, ref=DR_WORLD)
        set_ref_coord(101)
        ini = 0
        end = 0 

        for x in range( 1 , int(Global_Total_Program) ):

            programm = globals()['System_Pr_%s' % x]
            
            if programm[1] == int(barcode) :
                ini = programm[2]
                end = programm[3] 
                break

        for x in range( ini , end ) :
            pos = globals()['System_Point_%s' % x]
            #check_plausibilitaet = self.c_functions.plausibilitaets_pruefung(pos)
            check_plausibilitaet = True

            if check_plausibilitaet == True :
            
                self.c_drive.fahren(pos ,ausrichtung=False , teach_mode=False)

            else :
                tp_popup("The Position {0} is not inside of the Cabinet".format('System_Point_%s' % x), DR_PM_MESSAGE)

    def restart(self):
        #Sick umschalten damit Position von Schrank auch gepr??ft wird
        set_digital_output(2)
        
##################################### 


new_cabinet = runtime()
#new_cabinet.New_Cabinet()
#new_cabinet.Test_Cabinet("123")

System_test = 0 
System_test_hyamp = 0 

test_hyamp = Hyamp()
test_hyamp.test_point()