import struct
from evdev import UInput, ecodes as e


ui = UInput();

fp = open("/dev/hidraw0", mode='rb')

usflagstate = False
ynflagstate = False

while True:
  buf = fp.read(9)
  usflag = False
  ynflag = False
  for i in range(3, 9):
    if buf[i] == 0x87:
      usflag = True
    elif buf[i] == 0x89:
      ynflag = True

  if usflagstate == False and usflag == True:
    ui.write(e.EV_KEY, e.KEY_RO, 1)
    usflagstate = True
    print("RO press")
  elif usflagstate == True and usflag == False:
    ui.write(e.EV_KEY, e.KEY_RO, 0)
    usflagstate = False
    print("RO release")

  if ynflagstate == False and ynflag == True:
    ui.write(e.EV_KEY, e.KEY_YEN, 1)
    ynflagstate = True
    print("YEN press")
  elif ynflagstate == True and ynflag == False:
    ui.write(e.EV_KEY, e.KEY_YEN, 0)
    ynflagstate = False
    print("YEN release")
  ui.syn()
