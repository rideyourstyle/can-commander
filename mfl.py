import can

#CanListener(...)
class CanListener(can.Listener):
  def on_message_received(self, msg):

    if(msg.arbitration_id == 0x5c1):
      print("Mfl id recived")

      if(msg.



    else:
      print("Unknown id recived:")
      print(msg)


#Mfl(object)
class Mfl(object):

  notifier = None
  c_bus = None

  def __init__(self, channel):
    try:
      self.c_bus = can.interface.Bus(bustype='socketcan', channel=channel)

    except:
      self.c_bus = can.interface.Bus(bustype='virtual')
      print('No can interface available, switch to virtual can bus')

  # start listener
  def start_listener(self):
    listener = CanListener()
    self.notifier = can.Notifier(self.c_bus, [listener])

  # stop listener
  def stop_listener(self):
    self.notifier.stop()

  # print all messages
  def bus_print(self, number_of_messages):

    c_bus = self.c_bus
    i = 0

    while(i < number_of_messages):
      print(c_bus.recv(timeout=1))
      #i += 1


