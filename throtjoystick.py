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

forward_curve = CubicSpline(
        [(-1.0, -1.0), (1.0, 1.0), (0.772, 0.552), (-0.772, -0.552)]
)


Strafe_curve = CubicSpline(
        [(-1.0, -1.0), (1.0, 1.0), (0.772, 0.552), (-0.772, -0.552)]
)

ThrusterPower_Curve = CubicSpline(
        [(-1.0, -1.0), (1.0, 1.0)]
)


@tm16000.button(LeftJOYBTN_Trigger)
def weapon_group_1(event, vjoy):
    vjoy[3].button(SpaceBrake).is_pressed = event.is_pressed

@tm16000.button(LeftJOYBTN_FaceBottom)
def weapon_group_2(event, vjoy):
    vjoy[3].button(Afterburner).is_pressed = event.is_pressed

@tm16000.button(LeftJOYBTN_FaceLeft)
def weapon_group_3(event, vjoy):
    vjoy[3].button(MatchTargetSpeed).is_pressed = event.is_pressed

@tm16000.button(LeftJOYBTN_FaceRight)
def weapon_group_3(event, vjoy):
    vjoy[3].button(CruiseControl).is_pressed = event.is_pressed

@tm16000.button(LeftJOYBTN_Panel)
def HT_recalibrate(event, vjoy):
    vjoy[3].button(HTRecal).is_pressed = event.is_pressed


@tm16000.axis(1)
def pitch(event, vjoy):
    vjoy[3].axis(StrafeLeftRight).value = Strafe_curve(event.value)

@tm16000.axis(2)
def yaw(event, vjoy):
    vjoy[3].axis(StrafeForwardBack).value = forward_curve(event.value)

@tm16000.axis(6)
def yaw(event, vjoy):
    vjoy[3].axis(Roll).value = active_curve(event.value)

@tm16000.axis(7)
def yaw(event, vjoy):
    vjoy[3].axis(ThrusterPower).value = ThrusterPower_Curve(event.value)

#allows all direction on HAT 1
@tm16000.hat(LeftJOYHAT)
def onJoystickHat_Zoom(event, vjoy, joy):
    vjoy[3].hat(2).direction = (event.value)
