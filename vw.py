import can


try:
  c_bus = can.interface.Bus(bustype='socketcan', channel='vcan0')

except:
  c_bus = can.interface.Bus(bustype='virtual')
  print('No can interface available, switch to virtual can bus')


# print all messages
def bus_print(number_of_messages):

  i = 0
  while(i < number_of_messages):
    print(c_bus.recv(timeout=1))
    #i += 1


