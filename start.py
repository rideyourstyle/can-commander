import time

"""
ID DLC Data
5C1 1 06 Vol up
5C1 1 07 Vol Down
5C1 1 0A Menu
5C1 1 1A Phone
5C1 1 22 Arrow Up
5C1 1 23 Arrow Down
5C1 1 28 OK
5C1 1 2B Mute
5C1 1 00 Button is released
"""



if 0:
  import can
  test = can.interface.Bus(bustype='socketcan', channel='vcan0')

  msg1 = can.Message(arbitration_id=0x4de, extended_id=False, data=[1,2,3])
  test.send(msg1)

else:
  from mfl import Mfl

  mfl = Mfl('vcan0')
  mfl.start_listener()

  time.sleep(20)


