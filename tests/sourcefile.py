#!/usr/bin/env python3
"""
-One Million lights in a 1000x1000 grid. 

-Lights in the grid are numbered from 0 to 999 in each direction;

The lights at each corner are at 0,0, 0,999, 999,999, and 999,0.

Instructions include whether to turn on, turn off, or toggle various
inclusive ranges given as coordinate pairs. 

-Coordinate pairs represent opposite corners of a rectangle, inclusive; 

-Lights start all turned On
"""

import enum
import re
import numpy as np

class LightState(enum.IntEnum):
    OFF = 0
    ON = 1

class Lights(object):
    """Wrapper for manipulating lights
    The wrapper is constructed with the size of the (square) grid,
    with all lights initially off. It then supports several operations
    on slices of the lights, where a slice is defined as a range from
    the top left to the bottom right (in a 4-tuple (top, left, bottom,
    right)). The bottom-right range is inclusive, meaning the range
    (0, 0, 2, 2) represents a 3x3 grid of 9 lights.
    The operations supported are:
    - func:`turn_on` set all of the lights in the slice to on
    - func:`turn_off` set all of the lights in the slice to off
    - func:`toggle` set all of the lights that were on to off, and all
      the ones that were off to on.
    """
    def __init__(self, size=1000):
        """This function creates the grid and sets every light to off"""
        self.size = size
        self.lights = LightState.OFF * np.ones((self.size, self.size))

    def __eq__(self, other):
        return np.all(self.lights == other.lights)

    def copy(self):
        """This function creates a copy of the current state of the lights"""
        lights = Lights(self.size)
        lights.lights[:] = self.lights

        return lights

    def count_lit(self):
        """This function returns the number of lights that are on"""
        return int(np.sum(self.lights))

    def toggle(self, top, left, bottom, right):
        """This function toggles lights in the given range"""
        self._multiply_add_and_clamp(top, left, bottom, right, -1, 1)

    def turn_on(self, top, left, bottom, right):
        """This function turns on lights in the given range"""
        self._multiply_add_and_clamp(top, left, bottom, right, 0, 1)

    def turn_off(self, top, left, bottom, right):
        """This function turns off lights in the given range"""
        self._multiply_add_and_clamp(top, left, bottom, right, 0, 0)

    def _multiply_add_and_clamp(self, top, left, bottom, right, mult, addend):
        """This function performs operations on the given range and clamp values"""
        self.lights[top:bottom+1, left:right+1] *= mult
        self.lights[top:bottom+1, left:right+1] += addend

        mask = self.lights < LightState.OFF
        self.lights[mask] = LightState.OFF