# Workaround for ASUS EeeBook X205TA Japanese Keyboard(Yen and Backslash) on Linux

## introduction
this python script is a work-around for a issue that ASUS EeeBook X205TA
Japanese Keyboard is not inputtable some keys (such as yen, pipe, underscore, ..).

these keys are recognized by kernel's HID (you can watch /dev/hidraw0 and input these keys),
but hid-input driver doesn't have mapping from hid input to scancode.

this python script has running on userland, reading /dev/hidraw0, if detect yen or backslash,
this script fire key event via uinput,

## prerequisite

load uinput kernel module 

`# modprobe uinput`

## dependencies

python-evdev (for uinput)

## installation

1. clone this
2. create virtualenv
`$ virtualenv .`
3. activate virtualenv
`$ source bin/activate`
4. install dependencies
`$ pip install -r requirements.txt
5. exec on root privilege
`$ sudo python main.py`


## license

this script has distributed under MIT License



