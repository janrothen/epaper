#!/usr/bin/env python3

import random

MIN_COLOR_VALUE = 0
MAX_COLOR_VALUE = 255


class Color:
    """
    Represents an RGB color with validation and utility methods.
    
    Provides a clean interface for working with RGB colors, including
    predefined color constants, validation, and conversion methods.
    
    Usage:
        red = Color(255, 0, 0)
        green = Color.GREEN
        custom = Color.from_hex("#FF5733")
        r, g, b = red.rgb  # Unpack as tuple
    """
    
    def __init__(self, red=0, green=0, blue=0):
        self.red = self._clamp(red)
        self.green = self._clamp(green)
        self.blue = self._clamp(blue)
    
    def _clamp(self, value):
        """Clamp color value between MIN and MAX."""
        return max(MIN_COLOR_VALUE, min(MAX_COLOR_VALUE, int(value)))

    @property
    def rgb(self):
        """Return color as (red, green, blue) tuple."""
        return (self.red, self.green, self.blue)
    
    @classmethod
    def from_tuple(cls, rgb_tuple):
        """Create Color from (r, g, b) tuple."""
        return cls(*rgb_tuple)
    
    @classmethod
    def from_hex(cls, hex_string):
        """Create Color from hex string like '#FF0000' or 'FF0000'."""
        hex_string = hex_string.lstrip('#')
        if len(hex_string) != 6:
            raise ValueError("Hex string must be 6 characters")
        
        try:
            r = int(hex_string[0:2], 16)
            g = int(hex_string[2:4], 16)
            b = int(hex_string[4:6], 16)
            return cls(r, g, b)
        except ValueError:
            raise ValueError("Invalid hex color string")
    
    @classmethod
    def random(cls):
        """Create a random color with RGB values between 0-255."""
        red = random.randint(MIN_COLOR_VALUE, MAX_COLOR_VALUE)
        green = random.randint(MIN_COLOR_VALUE, MAX_COLOR_VALUE)
        blue = random.randint(MIN_COLOR_VALUE, MAX_COLOR_VALUE)
        return cls(red, green, blue)
    
    @classmethod
    def random_bright(cls, min_brightness=100):
        """Create a random bright color with minimum brightness per channel."""
        red = random.randint(min_brightness, MAX_COLOR_VALUE)
        green = random.randint(min_brightness, MAX_COLOR_VALUE)
        blue = random.randint(min_brightness, MAX_COLOR_VALUE)
        return cls(red, green, blue)
    
    @classmethod
    def random_pastel(cls):
        """Create a random pastel color (lighter, softer colors)."""
        red = random.randint(150, MAX_COLOR_VALUE)
        green = random.randint(150, MAX_COLOR_VALUE)
        blue = random.randint(150, MAX_COLOR_VALUE)
        return cls(red, green, blue)

    def __str__(self):
        return f"Color(R={self.red}, G={self.green}, B={self.blue})"
    
    def __repr__(self):
        return f"Color({self.red}, {self.green}, {self.blue})"
    
    def __eq__(self, other):
        if isinstance(other, Color):
            return self.rgb == other.rgb
        return False

    # Predefined colors
    BLACK = None
    WHITE = None
    RED = None
    GREEN = None
    BLUE = None
    YELLOW = None
    CYAN = None
    MAGENTA = None
    ORANGE = None
    PURPLE = None
    PINK = None
    WARM_WHITE = None
    COOL_WHITE = None

# Initialize predefined colors
Color.BLACK = Color(0, 0, 0)
Color.WHITE = Color(255, 255, 255)
Color.RED = Color(255, 0, 0)
Color.GREEN = Color(0, 255, 0)
Color.BLUE = Color(0, 0, 255)
Color.YELLOW = Color(255, 255, 0)
Color.CYAN = Color(0, 255, 255)
Color.MAGENTA = Color(255, 0, 255)
Color.ORANGE = Color(255, 165, 0)
Color.PURPLE = Color(128, 0, 128)
Color.PINK = Color(255, 192, 203)
Color.WARM_WHITE = Color(255, 200, 100)
Color.COOL_WHITE = Color(200, 220, 255)