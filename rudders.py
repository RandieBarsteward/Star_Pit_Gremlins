"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

              (Joystick Gremlin Profile/Scripts for Star Citizen)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
from gremlin.spline import CubicSpline
from vjoy.vjoy import AxisName
from scmap import *
from hotas import *


rudders = gremlin.input_devices.JoystickDecorator("Saitek Pro Flight Combat Rudder Pedals", "{C792F720-9912-11EA-8001-444553540000}",
                                                   "Default")
default_curve = CubicSpline(
        [(-1.0, -1.0), (0.0, 0.0), (1.0, 1.0)]
)
precision_curve = CubicSpline(
        [(-1.0, -0.5), (0.0, 0.0), (1.0, 0.5)]
)

active_weapon_groups = {}
active_curve = default_curve

@rudders.axis(1)
def LeftPedal(event, vjoy):
    vjoy[3].axis(StrafeDown).value = active_curve(event.value)

@rudders.axis(2)
def RightPedal(event, vjoy):
    vjoy[3].axis(StrafeUp).value = active_curve(event.value)

@rudders.axis(6)
def roll(event, vjoy):
    vjoy[3].axis(Roll).value = active_curve(event.value)
