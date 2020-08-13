
"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
              (Joystick Gremlin Profile/Scripts for Star Citizen)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

                          ###########################
                          # HOTAS PHYSICAL MAPPINGS #
                          ###########################

# The following variables are initialized to the physical axes and buttons on
# the HOTAS. The included scripts' logic utilize these values to know what
# inputs to "listen" for to do particular actions and maneuvers.

USING_RUDDER_PEDALS = True
RUDDER_PEDALS_INVERT = -1.0 # must be -1.0 or 1.0 (negative for invert)
##############################################################################
# Rudder Pedals Information
RUD_Name = "Saitek Pro Flight Combat Rudder Pedals"
RUD_Id = "{C792F720-9912-11EA-8001-444553540000}"

# Set the following actions to the physical axes on your rudder (sc_throttle.py)
RUDAXIS_Reverse = 1  # Z Axis                   L PEDAL(sc_throttle.py)
RUDAXIS_Boost = 2    # WORKING   vJoy 8        R PEDAL(sc_throttle.py)
RUDAXIS_Roll = 3     # Rz Axis                  PIVOT     (sc_throttle.py)
RUDAXISBTN_Threshold = -0.5         # Less than = no press

##############################################################################

# Joystick Information
JOY_Name = "Joystick - HOTAS Warthog"
JOY_Id = "{9250BC30-9941-11EA-8001-444553540000}"


JOY_Rotation = 0

# Set the following actions to the physical axes on the joystick
JOYAXIS_Yaw = 1
JOYAXIS_Pitch = 2

# Set the following actions to the physical buttons on the joystick

# Trigger
JOYBTN_Trigger = 1
JOYBTN_TriggerSecondStage = 6

#Weapon Release Button
JOYBTN_RedBtn = 2

#Stick Pinky Button

JOYBTN_PinkyBtn = 3
JOYBTN_PinkyLever = 4

#mouse mode toggle - Grey button next to trigger
JOYBTN_IndexBtn = 5

#Hostile Target Managment
JOYBTN_4WayUp = 7
JOYBTN_4WayRight = 8
JOYBTN_4WayDown = 9
JOYBTN_4WayLeft = 10

#Hostile Target Managment
JOYBTN_8WayUp = 11
JOYBTN_8WayRight = 12
JOYBTN_8WayDown = 13
JOYBTN_8WayLeft = 14

#Shield Managment Thumb
JOYBTN_GreyJoyForward = 15
JOYBTN_GreyJoyBack = 17
JOYBTN_GreyJoyLeft = 18
JOYBTN_GreyJoyRight = 16
JOYBTN_GreyJoyPress = 19

#Hat
JOYHAT = 1

##############################################################################

# Thottle Joystick Information
THROTJOY_Name = "T.16000M"
THROTJOY_Id = "{955E0FD0-9F6E-11EA-8001-444553540000}"

# Set the following actions to the physical axes on the joystick
THROTJOYAXIS_Yaw = 1
THROTJOYAXIS_Pitch = 2

#trigger
LeftJOYBTN_Trigger = 1 #Space Break

# Hat Face - 3 buttons
LeftJOYBTN_FaceBottom = 2 #Afterburner
LeftJOYBTN_FaceLeft = 3 #Match Target Speed
LeftJOYBTN_FaceRight = 4 #Cruise Control

# Right cluster - 6 buttons
LeftJOYBTN_Panel = 8 #HT


#Hat
LeftJOYHAT = 1

##############################################################################

# MFD Information - MFD Outputs to vJoy device 2

MFD_Name = "vJoy Device"
MFD_Id = "{732BD260-A024-11EA-8002-444553540000}"

# MFD - Weapons page

MFDBTN_WpnGrp1_Safe = 3
MFDBTN_WpnGrp2_Safe = 7
MFDBTN_Missile_Safe = 8
MFDBTN_Bomb_Doors = 11



'''
##############################################################################
# Throttle Information
THR_Name = "Throttle - HOTAS Warthog"
THR_Id = 72287236

THRAXIS_ThrottleAbs = 4                # Right throttle (sc_throttle.py)
THRAXIS_StrafeThrustAmt = 5            # An unused slider is a good choice. (sc_throttle.py)
THRAXIS_ThrusterPower = 128
# Set the following actions to the physical switches on the throttle. Switches
# are buttons in the virtual sense, but the logic that uses them assumes they
# can easily be held down indefinitely


#FUEL NORM SWITCHES
SWITCH_CycleFire = 17                  # ##WORKING No vJoy binding needed ##  EFRNORM (Right Fuel Norm Switch)
#SWITCH_XXX = 16                       # EFRNORM (Left Fuel Norm Switch)

#ENGINE OPERATE SWITCHES
#THRBTN_ShieldRaise = 31               #ENGINE OPERATE LEFT FORWARD (MOMENT)
#SWITCH_XXX = 18                       #ENGINE OPERATE LEFT BACK (SWITCH)
#SWITCH_XXX = 32                       #ENGINE OPERATE RIGHT FORWARD (MOMENT)
#SWITCH_XXX = 19                       #ENGINE OPERATE LEFT BACK (SWITCH)

#FLAPS (sc_throttle.py)
SWITCH_FlapsUp = 22                    # ##WORKING vJoy 10          FLAPU (flaps up Quantum) (sc_throttle.py)
SWITCH_FlapsDown = 23                  # ##WORKING No vJoy          FLAPD (flaps down Precision Thrusters) (sc_throttle.py)

#ENGINE IDLE
SWITCH_EngineOff = 29                 # ##WORKING vJoy 45           Engine Idle R (sc_throttle.py)
#SWITCH_EngineOff = 30                #

#APU ON (sc_cockpit.py)
SWITCH_Power = 20                      # ##WORKING vJoy 44          APU ON (SWITCH)(sc_cockpit.py)

#THROTTLE FRICTION
#JOYAXIS_FRICTION =                    # THROTTLE FRICTION SLIDER

#L/G WRN SILENCE (sc_throttle.py)
THRBTN_LandingGear = 21                # ##WORKING vJoy 9           LDGH (Landing Gear button) (sc_throttle.py)

#EAC ON/OFF
SWITCH_PowerOn = 24                     # ##WORKING vJoy 38           EAC ON/OFF (SWITCH) (sc_throttle.py)
#SWITCH_FlightSystemsReady = 24         # ##WORKING vJoy 38           EAC ON/OFF (SWITCH) (sc_throttle.py)

#RDR ALTM
SWITCH_ShieldsOn = 25                   # ##WORKING vJoy 37           RDR ALTM (SWITCH) (sc_throttle.py)

#AUTOPILOT (sc_autopilot.py)
THRBTN_AutopilotEngage = 26            # ##WORKING vJoy 12 / 11 (APALT DOWN)             APENG (Autopilot engage) (sc_autopilot.py)
SWITCH_AutopilotUp = 27              #                                                APALT (Autopilot switch in "PATH") (sc_autopilot.py)
SWITCH_AutopilotDown = 28               # ##WORKING No vJoy                               APALT (Autopilot switch in "ALT") (sc_autopilot.py)

####################
####################
####################
# Set the following actions to the physical buttons on the throttle
#THROTTLE PINKY  ###CHANGE THIS. WASTE OF KEYS###
SWITCH_ModeOnFoot = 13                 # PSF (Pinky switch forward)
SWITCH_ModeVehicle = 14                # PSB (Pinky switch backward)

#THROTTLE RIGHT THUMB SWITCH (sc_throttle.py)
THRBTN_StrafeUp = 3                    # Y Axis                     MSU (thumb hat up) (sc_throttle.py)
THRBTN_StrafeDown = 5                  # Y Axis                     MSD (thumb hat down) (sc_throttle.py)
THRBTN_StrafeRight = 4                 # X Axis                     MSR (thumb hat right) (sc_throttle.py)
THRBTN_StrafeLeft = 6                  # X Axis                     MSL (thumb hat left) (sc_throttle.py)
THRBTN_ResetZoom = 2                   # ##NO vJoy BINDING          MSP (thumb hat press) (sc_throttle.py)

#RED THUMB SWITCH / CHINA HAT (sc_gunnery.py)
THRBTN_CycleCounterMeasure = 11        # ##WORKING vJoy 5          CHF (red two way forward) (sc_gunnery.py)
THRBTN_LaunchCounterMeasures = 12      # ##WORKING vJoy 3          CHB (red two way backward) (sc_gunnery.py)

#SPEED BRAKE
THRBTN_Afterburner = 7                 # ##WORKING vJoy 13         SPDF (Fat two way forward) (locks) (sc_throttle.py)
THRBTN_LookBehind = 8                  # ##WORKING vJoy 14         SPDB (Fat two way backward) (sc_camera.py)

#LEFT THROTTLE BUTTON (RED) (sc_throttle.py)
THRBTN_MatchTarget = 15                # ##WORKING vJoy 48                    LTB (red pinky button) (sc_throttle.py)


#RIGHT BOAT SWITCH
THRBTN_DecoupledModeToggle = 10        # ##WORKING vJoy 15          BOAT (Boat back) (sc_throttle.py)



#THRBTN_IncreaseCoolerRate
#THRBTN_DecreaseCoolerRate
#
#THRBTN_OpenAllDoors
#THRBTN_CloseAllDoors
#THRBTN_LockAllDoors
#THRBTN_UnlockAllDoors

THRHAT_StrafeUpDown = 1                # HAT 1 (up/down) (sc_throttle.py)
THRHAT_Roll = 1                        # HAT 1 (left/right) (sc_throttle.py)
'''
'''
##############################################################################
# Button Box Information
BUT_Name = "BU0836X Interface"
BUT_Id = 500305921

BUT_Key = 1
BUT_PowerOn = 2
BUT_EngineOn = 3
BUT_ShieldsOn = 4
BUT_ShipLights = 5
BUT_IFCS = 6
BUT_AutoLand = 7
BUT_VTOL = 8
BUT_ModeStealth = 9
BUT_ModeCombat = 10
BUT_ModePrecision = 11
BUT_ScanModeToggle = 12
BUT_Scan = 13
BUT_GunArm = 14
BUT_MissileArm = 15
BUT_ESPToggle = 16
BUT_LandGear = 17
BUT_ShipLock = 18
BUT_ShipDoors = 19
BUT_DestructArm = 20
BUT_SelfDestruct = 21

BUT_WpnGroupThreeSafe = 22
BUT_WpnGroupFourSafe = 23
BUT_LandGear = 24
BUT_ShipLock = 25
BUT_ShipDoors = 26
BUT_DestructArm = 27
BUT_SelfDestruct = 28
BUT_Pedal = 29
BUT_HeadTrack = 30
'''
