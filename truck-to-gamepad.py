import sys
import time

import vgamepad as vg
import ecal.core.core as ecal_core
from ecal.core.subscriber import ProtoSubscriber

import VehicleDynamics_pb2
import Brake_pb2
import CanButton_pb2

steering_wheel_min = -0.25
steering_wheel_max = 0.12

def vehicle_dynamics_callback(topic_name, vehicle_dynamics_pb, time):
    steering_wheel_value = vehicle_dynamics_pb.signals.steering_wheel_angle

    if (steering_wheel_value > steering_wheel_max):
        steering_wheel_value = steering_wheel_max
    elif (steering_wheel_value < steering_wheel_min):
        steering_wheel_value = steering_wheel_min

    relative_joystick = (steering_wheel_value - steering_wheel_min) / (steering_wheel_max - steering_wheel_min)
    relative_joystick = -((relative_joystick * 2) - 1.0)

    gamepad.left_joystick_float(x_value_float=relative_joystick, y_value_float=0.0)  # values between -1.0 and 1.0
    gamepad.update()

def brake_in_callback(topic_name, brake_in_pb, time):
    is_brake_applied = brake_in_pb.signals.is_brake_applied
    if (is_brake_applied):
        gamepad.right_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
    else:
        gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
    gamepad.update()

def button_callback(topic_name, button_state_pb, time):
    is_button_pressed = (button_state_pb.ActStatForButton == 1)
    if is_button_pressed:
        gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
    else:
        gamepad.left_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
    
if __name__ == "__main__":

    ecal_core.initialize(sys.argv, "TruckGamepad")
    gamepad = vg.VX360Gamepad()


    vehicle_dynamics_sub = ProtoSubscriber("VehicleDynamicsInPb", VehicleDynamics_pb2.VehicleDynamics)
    vehicle_dynamics_sub.set_callback(vehicle_dynamics_callback) 

    brake_sub = ProtoSubscriber("BrakeInPb", Brake_pb2.Brake)
    brake_sub.set_callback(brake_in_callback) 

    button_sub = ProtoSubscriber("HMI_CAN_Button_State", CanButton_pb2.ButtonState)
    button_sub.set_callback(button_callback) 

    is_pressed = False;

    while ecal_core.ok():
        # if not is_pressed:
        #     gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # press the A button
        #     gamepad.left_trigger(value=100)  # value between 0 and 255
        #     print("press")
        #     is_pressed = True
        # else:
        #     gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        #     gamepad.left_trigger(value=200)  # value between 0 and 255
        #     print("release")
        #     is_pressed = False
        gamepad.update()

        # gamepad.left_joystick(x_value=-10000, y_value=0)  # values between -32768 and 32767
        # gamepad.right_joystick(x_value=-32768, y_value=15000)  # values between -32768 and 32767
        # Sleep 500 ms
        time.sleep(0.5)

