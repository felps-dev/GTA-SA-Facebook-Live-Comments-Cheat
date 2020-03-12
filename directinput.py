import sys,time,ctypes, random

SendInput = ctypes.windll.user32.SendInput

PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def executar_cheat(cheat):
    cont = 0
    exletra = 0x53
    for i in range(len(cheat)):
        letra = converterKBCommand(cheat[i])
        if letra != 0x53:
            PressKey(letra)
            #time.sleep(random.randint(80,200)/1000)
            time.sleep(0.050)
            ReleaseKey(letra)
            time.sleep(0.050)
            cont = cont + 1
    if cont == len(cheat):
        return True
    else:
        return False


def converterKBCommand(input):
    if input == 'Q':
        return 0x10
    elif input== 'W':
        return 0x11
    elif input == 'E':
        return 0x12
    elif input == 'R':
        return 0x13
    elif input == 'T':
        return 0x14
    elif input == 'Y':
        return 0x15
    elif input == 'U':
        return 0x16
    elif input == 'I':
        return 0x17
    elif input == 'O':
        return 0x18
    elif input == 'P':
        return 0x19
    elif input == 'A':
        return 0x1E
    elif input == 'S':
        return 0x1F
    elif input == 'D':
        return 0x20
    elif input == 'F':
        return 0x21
    elif input == 'G':
        return 0x22
    elif input == 'H':
        return 0x23
    elif input == 'J':
        return 0x24
    elif input == 'K':
        return 0x25
    elif input == 'L':
        return 0x26
    elif input == 'Z':
        return 0x2C
    elif input == 'X':
        return 0x2D
    elif input == 'C':
        return 0x2E
    elif input == 'V':
        return 0x2F
    elif input == 'B':
        return 0x30
    elif input == 'N':
        return 0x31
    elif input == 'M':
        return 0x32
    else:
        return 0x53

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
