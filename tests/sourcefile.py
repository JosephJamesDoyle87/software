#!/usr/bin/env python3
"""
-One Million lights in a 1000x1000 grid. 

-Lights in the grid are numbered from 0 to 999 in each direction;

The lights at each corner are at 0,0, 0,999, 999,999, and 999,0.

Instructions include whether to turn on, turn off, or toggle various
inclusive ranges given as coordinate pairs. 

-Coordinate pairs represent opposite corners of a rectangle, inclusive; 

-Lights start all turned On..
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
        
def parse_and_update(lights, string):
   
    positions = try_parse_turn_on(string)
    if positions:
        lights.turn_on(*positions)
        return

    positions = try_parse_turn_off(string)
    if positions:
        lights.turn_off(*positions)
        return

    positions = try_parse_toggle(string)
    if positions:
        lights.toggle(*positions)
        return

    raise ValueError("Unrecognized command")

def try_parse_positions(string):
    """This function tries to parse the range or return None"""
    
    match = re.match(r'(\d+),(\d+) through (\d+),(\d+)', string)
    if not match:
        return None

    (top, left, bottom, right) = map(int, match.groups())

    return (top, left, bottom, right)

def try_parse_turn_on(string):
    """This function tries to parse the turn on command or return None
    >>> try_parse_turn_on("turn on 0,0 through 999,999")
    (0, 0, 999, 999)
    >>> try_parse_turn_on("turn off 0,0 through 999,999") is None
    True
    >>> try_parse_turn_on("turn on 0,0 through 999,") is None
    True
    """
    turn_on = re.match(r'turn on ', string)
    if not turn_on:
        return None

    positions = try_parse_positions(string[turn_on.end():])

    return positions

def try_parse_turn_off(string):
    """This function tries to parse the turn off command or return None
    >>> try_parse_turn_off("turn off 0,0 through 999,999")
    (0, 0, 999, 999)
    >>> try_parse_turn_off("turn on 0,0 through 999,999") is None
    True
    >>> try_parse_turn_off("turn off 0,0 through 999,") is None
    True
    """
    turn_off = re.match(r'turn off ', string)
    if not turn_off:
        return None

    positions = try_parse_positions(string[turn_off.end():])

    return positions

def try_parse_toggle(string):
    """This Tfunction tries to parse the toggle command or return None
    >>> try_parse_toggle("toggle 0,0 through 999,999")
    (0, 0, 999, 999)
    >>> try_parse_toggle("turn off 0,0 through 999,999") is None
    True
    >>> try_parse_toggle("toggle 0,0 through 999,") is None
    True
    """
    toggle = re.match(r'toggle ', string)
    if not toggle:
        return None

    positions = try_parse_positions(string[toggle.end():])

    return positions

def main(filename):
    """Read instructions for lights and count lit ones"""
    lights = Lights(1000)
    with open(filename, 'r') as f:
        for line in f:
            parse_and_update(lights, line)

    count = lights.count_lit()
    print(count)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    main(**vars(args))
