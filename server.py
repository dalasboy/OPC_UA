from opcua import Server
from random import randint
from time import sleep

server = Server()

url = 'opc.tcp://127.0.0.1:4840/server'
server.set_endpoint(url)

namespace = 'OPC_Simulation_Server'
addspace = server.register_namespace(namespace)

node = server.get_objects_node()

Param = node.add_object(addspace, 'Paramiters')

Temp = Param.add_variable(addspace, 'Temperature',0)
Press = Param.add_variable(addspace, 'Pressure',0)

Temp.set_writable()
Press.set_writable()

server.start()

print('server Started at {}'.format(url))

while True:
    Temperature =  randint(10,50)
    Pressure = randint(200,900)
    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    print(Temperature, Pressure)
    sleep(1)