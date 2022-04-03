import numpy as np
import cv2
import os
import gtuner
import time
from licensing.methods import Key, Helpers


# ENTER YOUR LICENSE KEY HERE
license_key = "XXXX-XXXX-XXXX-XXXX"

##################################################
# TO DEACTIVATE THE JUMPSHOT MODS, PRESS:

# R2 + L2 + R1 + L1 (Playstation)
# RT + LT + RB + LB (Xbox)
##################################################

CURRENT_GEN = False

# Change this to True if you want to use the current gen configurations. 
# Change it to False if you want to use the next gen configurations

##################################################
# USER SETTINGS YOU MOST DEFINITELY HAVE TO CHANGE

SHOT_STICK_SHOOTING = True 

# Make this True if you want to take shots with your shot stick.
# Make this False if you do not want to take shots with your shot stick. Note: you may want to do this if you 
# want to use a dribble script or your own dribble moves along with this script.

##################################################


SHOT_TIMING = 150
FADE_TIMING = 345
STEP_BACK_TIMING = 367


# If you are getting lates for still shots, press L2 + Left to decrease timing by 5.
# If you are getting early's for still shots, press L2 + Right to increase timing by 5.
# If you are getting lates for fades, press R2 + Left to decrease timing by 5.
# If you are getting early's for fades, press R2 + Right to increase timing by 5.
# If you are getting lates for step backs, press L2 + R2 + Left to decrease timing by 5.
# If you are getting early's for step backs, press L2 + R2 + Right to increase timing by 5.


THRESHOLD = 0.8

# The higher the threshold, the less it detects
# The lower the threshold, the more it detects
# There are trade-offs to putting it too low. It may detect something you don't want it to detect
# I usually increase/decrease by 0.05



dil = None


class GCVWorker:
    def __init__(self, width, height):
        global dil
        os.chdir(os.path.dirname(__file__))
        self.shot_timing = SHOT_TIMING
        self.fade_timing = FADE_TIMING
        self.step_back_timing = STEP_BACK_TIMING
        self.threshold = THRESHOLD
        self.current_gen = CURRENT_GEN
        self.SHOT_STICK_SHOOTING = SHOT_STICK_SHOOTING
        self.license_key = license_key
        dil = __import__('dilemma')
        dil.init(self)





    def __del__(self):
        del self
    
    def process(self, frame):
        global dil 
        self.gcvdata = bytearray([0x00])
        self.gcvdata[0] = False
        (frame, self.gcvdata) = dil.activate(frame, self.gcvdata, self)

        return (frame, self.gcvdata)