from __future__ import division, print_function

import math, pygame
from pygame.locals import *

import function

# this file contains all kinds of constants

PHYSICS_TIMESTEP = 1/50 # always update physics in these steps
INPUT_SEND_FPS = 1/30 # we send input to the server at this rate