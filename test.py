# TEST '

import serial  

def serialWrite(serial, data):
    return serial.write(data)               
    
def serialRead(serial, length):  
    return serial.read(length)        

def enable_Remote():

    try :
        serObj = serial.Serial(port='/dev/ttyUSB0',baudrate=38400, bytesize=DR_EIGHTBITS, parity=DR_PARITY_NONE, stopbits=DR_STOPBITS_ONE,writeTimeout=3,timeout=3) # For PC and RS232 Port COM2 (Linux Adressierung)
    except Exception as e:
        tp_popup("Turn ON HYAMP AND connect USB to Doosan and HYAMP", DR_PM_ALARM)
        return False

    check_remote = serialWrite(serObj , b'SPR?\n')
    time.sleep(1)
    serialread = serialRead(serObj , check_remote )

    if int(serialread) == 0 :
        msg = b'SPR{1}\n'
        write = serialWrite(serObj , msg)
        time.sleep(1)
        serialread = serialRead(serObj , write )

        check_remote = serialWrite(serObj , b'SPR?\n')
        time.sleep(1)
        serialread = serialRead(serObj , check_remote )
        if int(serialread) == 0 :
            tp_popup("Could not enable Remote Connection")
            serObj.close()
            return False

    serObj.close()
    return True 
try:

    Remote = enable_Remote()

    serObj = serial.Serial(port='/dev/ttyUSB0',baudrate=38400, bytesize=DR_EIGHTBITS, parity=DR_PARITY_NONE, stopbits=DR_STOPBITS_ONE,writeTimeout=3,timeout=3) # For PC and RS232 Port COM2 (Linux Adressierung)
    
    #msg = b'TEST\n'
    #test = serialWrite(serObj , msg)
    #time.sleep(1)
    #serialread = serialRead(serObj , test )
    #tp_popup("TEST={0}".format(serialread), DR_PM_MESSAGE)

    msg = b'TD?\n , RD<1>\n , RD<2>\n , RD<3>\n , RD<4>\n , RD<5>\n '
    msg = b'TEST\n'
    test = serialWrite(serObj , msg)
    time.sleep(1)
    serialread = serialRead(serObj , test )
    tp_popup("Result={0}".format(serialread), DR_PM_MESSAGE)


except Exception as e: 
    tp_popup("Fehler={0}".format(e), DR_PM_MESSAGE)


