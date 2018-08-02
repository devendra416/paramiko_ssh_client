#!/usr/bin/python3

import paramiko, getpass, time, json
#store IP addresses of devices in devices.json
#with open('devices.json', 'r') as f:
#    devices = json.load(f) */

with open('commands.txt', 'r') as f: 
    commands = [line for line in f.readlines()]

with open('uname_pass.txt','r') as f:
   
        user_pass = {k:v for k,v in (line.split() for line in f) }
        
max_buffer = 65535

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)

# Starts the loop for devices
for device in devices.keys(): 
  outputFileName = device + '_output.txt'
  for user in user_pass:
  	connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if connection.connect(devices[device]['ip'], username=user, password=user_pass[user], look_for_keys=False, allow_agent=False):
      new_connection = connection.invoke_shell()
      output = clear_buffer(new_connection)
      time.sleep(2)
      new_connection.send("terminal length 0\n")
      output = clear_buffer(new_connection)
      with open(outputFileName, 'wb') as f:
        for command in commands:
            new_connection.send(command)
            time.sleep(2)
            output = new_connection.recv(max_buffer)
            print(output)
            f.write(output
    else 
        print connection not establishe to %s with %s and %s ,  devices[device]['ip'], username=user, password=user_pass[user]
  new_connection.close()      
               	
