from __future__ import division, print_function

import math
import pygrafix
import random

import function

class BuildingSentryRenderer(object):
    def __init__(self):
        self.depth = 1
        self.sprites = list([pygrafix.image.load("sprites/ingameelements/sentryred/{0}.png".format(i)) for i in range(10)])
        
    def render(self, renderer, game, state, sentry):
        self.sprite = self.sprites[min(int(sentry.animation_frame), 9)] # TODO, get rid of this min and figure out how to cap an image index
        sprite = pygrafix.sprite.Sprite(self.sprite)

        # TODO: Sprite offset correctly
        sprite.position = renderer.get_screen_coords(sentry.x, sentry.y)

        renderer.world_sprites.append(sprite)
