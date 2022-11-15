#!/usr/bin/env python3

import socket
import time
import json
import random
import string

HOST = '0.0.0.0'    # Listen on all local IPs
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

conn = 0
addr = 0

# Generates a random lowercase string of requested length
def getRandomString(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

# Validates the command request we received first
def validateCommand(command):
    # Validation is super simplistic in this example
    return command.decode() == 'ValidCommand' 

# Perform whatever the valid command submitted earlier means
def doSomething(command):
    time.sleep(0.5) # For demo
    print('Processing done, replying')
    # We just populated a JSON reply containing various data types
    # with random values
    data = {}
    data['RandomFloat'] = random.uniform(0, 100)
    data['RandomInt'] = random.randrange(100)
    data['RandomBool'] = bool(random.getrandbits(1))
    data['RandomString'] = getRandomString(1+random.randrange(10))
    json_data = json.dumps(data)
    print(json_data)
    # Send it over to the client
    conn.sendall(json_data.encode())
    conn.sendall('\r\n'.encode())
    return

# Main program: wait for incoming TCP connections and deal with them
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(100)
    while True:
        print('Waiting for connection...')
        conn, addr = s.accept()
        with conn:
            print('Connection accepted from ', addr)
            i = 0
            while True:
                i = i+1
                data = conn.recv(8192)
                print('Data received (' + str(i) + ') ' + str(data))
                if not data:
                    break
                if validateCommand(data):
                    conn.sendall('ACK: '.encode() + data)
                    conn.sendall('\r\n'.encode())
                    print('Command accepted, perform it')
                    doSomething(data);
                else :                    
                    conn.sendall('NACK: '.encode() + data)
                    conn.sendall('\r\n'.encode())
                    print('Invalid command, rejecting it')
                    #conn.shutdown(socket.SHUT_RDWR)
                    conn.close()
                    break
                time.sleep(1)    
            print('Connection with ' + str(addr) + " lost")
            
