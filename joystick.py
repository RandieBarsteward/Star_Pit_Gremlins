"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

              (Joystick Gremlin Profile/Scripts for Star Citizen)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
from gremlin.spline import CubicSpline
from vjoy.vjoy import AxisName
from scmap import *
from hotas import *
from throtjoystick import *
import time

joystick = gremlin.input_devices.JoystickDecorator("Joystick - HOTAS Warthog", "{9250BC30-9941-11EA-8001-444553540000}",
                                                   "Default")


default_curve = CubicSpline(
        [(-1.0, -1.0), (1.0, 1.0), (0.772, 0.552), (-0.772, -0.552)]
)

precision_curve = CubicSpline(
        [(-1.0, -0.5), (0.0, 0.0), (1.0, 0.5)]
)

active_weapon_groups = {}
active_curve = default_curve

mousetoggle = 1

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

# Warthog Joystick Axis
@joystick.axis(1)
def pitch(event, vjoy):
    vjoy[3].axis(Pitch).value = active_curve(event.value)

@joystick.axis(2)
def yaw(event, vjoy):
    vjoy[3].axis(Yaw).value = active_curve(event.value)


#Warthog Trigger and Missile (Red)

@joystick.button(JOYBTN_Trigger)
def trigger_stage_1(event, vjoy):
    if not vjoy[1].button(7).is_pressed: #checks vJoy button output

        vjoy[3].button(FireWeaponGroup1).is_pressed = event.is_pressed
    else:
        vjoy[3].button(FireWeaponGroup1).is_pressed = False

@joystick.button(JOYBTN_TriggerSecondStage)
def trigger_stage_2(event, vjoy):

    if not vjoy[1].button(7).is_pressed: #checks vJoy button output
        vjoy[3].button(FireWeaponGroup2).is_pressed = event.is_pressed
    else:
        vjoy[3].button(FireWeaponGroup2).is_pressed = False

@joystick.button(JOYBTN_RedBtn)
def missile_red(event, vjoy):
    if not vjoy[1].button(8).is_pressed: #checks vJoy button output
        vjoy[3].button(LockFireMissiles).is_pressed = event.is_pressed
    else:
        vjoy[3].button(LockFireMissiles).is_pressed = False

#Warthog PINKY Trigger
@joystick.button(JOYBTN_PinkyBtn)
def pinky_button(event, vjoy):
    vjoy[3].button(CycleCounterMeasures).is_pressed = event.is_pressed

# Warthog PINKY Button
@joystick.button(JOYBTN_PinkyLever)
def pinky_trigger(event, vjoy):
    if vjoy[1].button(10).is_pressed: #checks vJoy button output
        vjoy[3].button(CounterMeasures).is_pressed = False
    else:
        vjoy[3].button(CounterMeasures).is_pressed = event.is_pressed

# mouse mode toggle - Grey button next to trigger
@joystick.button(JOYBTN_IndexBtn)
def mousemode(event, vjoy):
        vjoy[3].button(MouseMode).is_pressed = event.is_pressed

# 4 way Hat - Hostile Target Management
@joystick.button(JOYBTN_4WayUp)
def mousemode(event, vjoy):
        vjoy[3].button(TgtReticle).is_pressed = event.is_pressed

@joystick.button(JOYBTN_4WayRight)
def mousemode(event, vjoy):
        vjoy[3].button(TgtCycle).is_pressed = event.is_pressed

@joystick.button(JOYBTN_4WayDown)
def mousemode(event, vjoy):
        vjoy[3].button(TgtNearHostile).is_pressed = event.is_pressed

@joystick.button(JOYBTN_4WayLeft)
def mousemode(event, vjoy):
        vjoy[3].button(TgtCycleBack).is_pressed = event.is_pressed

# 8 way Hat - Pin and friendly target cycle
@joystick.button(JOYBTN_8WayUp)
def mousemode(event, vjoy):
        vjoy[3].button(PinTarget).is_pressed = event.is_pressed

@joystick.button(JOYBTN_8WayRight)
def mousemode(event, vjoy):
        vjoy[3].button(FriendlyCycle).is_pressed = event.is_pressed

@joystick.button(JOYBTN_8WayDown)
def mousemode(event, vjoy):
        vjoy[3].button(FriedlyCycleBack).is_pressed = event.is_pressed

@joystick.button(JOYBTN_8WayLeft)
def mousemode(event, vjoy):
        vjoy[3].button(CyclePin).is_pressed = event.is_pressed

# Shields - Grey Thumb Joystick

@joystick.button(JOYBTN_GreyJoyForward)
def mousemode(event, vjoy):
        vjoy[3].button(ShieldFront).is_pressed = event.is_pressed

@joystick.button(JOYBTN_GreyJoyBack)
def mousemode(event, vjoy):
        vjoy[3].button(ShieldBack).is_pressed = event.is_pressed

@joystick.button(JOYBTN_GreyJoyLeft)
def mousemode(event, vjoy):
        vjoy[3].button(ShieldLeft).is_pressed = event.is_pressed

@joystick.button(JOYBTN_GreyJoyRight)
def mousemode(event, vjoy):
        vjoy[3].button(ShieldRight).is_pressed = event.is_pressed

@joystick.button(JOYBTN_GreyJoyPress)
def mousemode(event, vjoy):
        vjoy[3].button(ShieldEqual).is_pressed = event.is_pressed

#allows all direction on HAT 1
@joystick.hat(JOYHAT)
def onJoystickHat_Zoom(event, vjoy, joy):
    vjoy[3].hat(1).direction = (event.value)
