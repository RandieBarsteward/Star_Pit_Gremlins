"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

              (Joystick Gremlin Profile/Scripts for Star Citizen)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
from gremlin.spline import CubicSpline
from vjoy.vjoy import AxisName
from scmap import *
from hotas import *
from joystick import *

tm16000 = gremlin.input_devices.JoystickDecorator("T.16000M", "{955E0FD0-9F6E-11EA-8001-444553540000}",
                                                   "Default")

default_curve = CubicSpline(
        [(-1.0, -1.0), (0.0, 0.0), (1.0, 1.0)]
)
precision_curve = CubicSpline(
        [(-1.0, -0.5), (0.0, 0.0), (1.0, 0.5)]
)

active_weapon_groups = {}
active_curve = default_curve

def set_weapon_group(gid, is_pressed):
    global active_curve
    global active_weapon_groups
    if is_pressed:
        active_curve = precision_curve
        active_weapon_groups[gid] = True
    else:
        active_weapon_groups[gid] = False
        if sum(active_weapon_groups.values()) == 0:
            active_curve = default_curve

@tm16000.button(LeftJOYBTN_Trigger)
def weapon_group_1(event, vjoy):
    set_weapon_group(1, event.is_pressed)
    vjoy[1].button(SpaceBrake).is_pressed = event.is_pressed

@tm16000.button(LeftJOYBTN_FaceBottom)
def weapon_group_2(event, vjoy):
    set_weapon_group(2, event.is_pressed)
    vjoy[1].button(Afterburner).is_pressed = event.is_pressed

@tm16000.button(LeftJOYBTN_FaceLeft)
def weapon_group_3(event, vjoy):
    set_weapon_group(3, event.is_pressed)
    vjoy[1].button(MatchTargetSpeed).is_pressed = event.is_pressed

@tm16000.button(LeftJOYBTN_FaceRight)
def weapon_group_3(event, vjoy):
    set_weapon_group(3, event.is_pressed)
    vjoy[1].button(CruiseControl).is_pressed = event.is_pressed

@tm16000.axis(1)
def pitch(event, vjoy):
    vjoy[1].axis(StrafeLeftRight).value = active_curve(event.value)
'''
@tm16000.axis(2)
def yaw(event, vjoy):
    vjoy[1].axis(StrafeForwardBack).value = active_curve(event.value)

@tm16000.axis(6)
def yaw(event, vjoy):
    vjoy[1].axis(Roll).value = active_curve(event.value)
'''
@tm16000.axis(7)
def yaw(event, vjoy):
    vjoy[1].axis(ThrusterPower).value = active_curve(event.value)

#allows all direction on HAT 1
@tm16000.hat(LeftJOYHAT)
def onJoystickHat_Zoom(event, vjoy, joy):
    vjoy[1].hat(2).direction = (event.value)
