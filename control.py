from pymavlink import mavutil
import keyboard as kb
import time

PITCH_ANGLE = 0
ROLL_ANGLE = 0
YAW_ANGLE = 0

MAX_ANGLE = 180


def handleLeftKey(ROLL_ANGLE):
    return max(ROLL_ANGLE - 10, -MAX_ANGLE)

def handleRightKey(ROLL_ANGLE):
    return min(ROLL_ANGLE + 10, MAX_ANGLE)

def handleWKey(PITCH_ANGLE):
    return min(PITCH_ANGLE + 10, MAX_ANGLE)

def handleSKey(PITCH_ANGLE):
    return max(PITCH_ANGLE - 10, -MAX_ANGLE)

def handleAKey(YAW_ANGLE):
    return max(YAW_ANGLE - 10, -MAX_ANGLE)

def handleDKey(YAW_ANGLE):
    return min(YAW_ANGLE + 10, MAX_ANGLE)

def move_gimbal(conn, PITCH_ANGLE, ROLL_ANGLE=0, YAW_ANGLE=0):
    """
    Moves gimbal to given position
    Args:
        PITCH_ANGLE (float): tilt angle in centidegrees (0 is forward)
        ROLL_ANGLE (float, optional): pan angle in centidegrees (0 is forward)
        YAW_ANGLE  (float, optional): pan angle in centidegrees (0 is forward)
    """
    conn.mav.command_long_send(
        conn.target_system,
        conn.target_component,
        mavutil.mavlink.MAV_CMD_DO_MOUNT_CONTROL,
        1,
        PITCH_ANGLE,
        ROLL_ANGLE,
        YAW_ANGLE,
        0, 0, 0,
        mavutil.mavlink.MAV_MOUNT_MODE_MAVLINK_TARGETING)



devloc = '/dev/ttyACM0'
print('connecting to device on: ', devloc)
conn = mavutil.mavlink_connection(devloc)
conn.wait_heartbeat()
print(conn.recv_match(blocking=True))
# master.wait_heartbeat()
print('heartbeat found')


while True:
    if kb.is_pressed("left"):
        ROLL_ANGLE = handleLeftKey(ROLL_ANGLE)
    elif kb.is_pressed("right"):
        ROLL_ANGLE = handleRightKey(ROLL_ANGLE)
    elif kb.is_pressed('w'):
        PITCH_ANGLE = handleWKey(PITCH_ANGLE)
    elif kb.is_pressed("s"):
        PITCH_ANGLE = handleSKey(PITCH_ANGLE)
    elif kb.is_pressed("a"):
        YAW_ANGLE = handleAKey(YAW_ANGLE)
    elif kb.is_pressed("d"):
        YAW_ANGLE = handleDKey(YAW_ANGLE)
    else:
        continue
    print('pitch: ', PITCH_ANGLE, 'roll: ', ROLL_ANGLE, 'yaw: ', YAW_ANGLE)
    print("sending command")
    move_gimbal(conn, PITCH_ANGLE, ROLL_ANGLE, YAW_ANGLE)
    print(" ")
    time.sleep(0.1)