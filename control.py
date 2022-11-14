import pymavlink as pmav
import keyboard as kb


PITCH_ANGLE = 0
ROLL_ANGLE = 0
YAW_ANGLE = 0

def handleLeftKey(e):
    if kb.is_pressed("4"):
        print("left arrow was pressed w/ key 4")
        # work your magic

while True:

    kb.on_press_key("left", handleLeftKey)