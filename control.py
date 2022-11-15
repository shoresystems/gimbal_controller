import pymavlink as pmav
import keyboard as kb
import time

PITCH_ANGLE = 0
ROLL_ANGLE = 0
YAW_ANGLE = 0


def handleLeftKey(e):
    YAW_ANGLE += 10
    return YAW_ANGLE

while True:

    kb.onpress_key("left", handleLeftKey)
    print('yaw', YAW_ANGLE)
    time.sleep(0.1)