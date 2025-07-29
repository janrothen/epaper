#!/usr/bin/env python3

import datetime
from .color import Color

PROFILE_MORNING = 'profile.morning'
PROFILE_EVENING = 'profile.evening'


class ProfileManager:
    """
    Manages color profiles for different times of day.
    
    Handles the logic for determining which profile should be active
    based on the current time and retrieving color configurations
    from the configuration manager.
    
    Usage:
        profile_mgr = ProfileManager(config_manager)
        active_profile = profile_mgr.get_active_profile()
        colors = profile_mgr.get_profile_colors(active_profile)
    """
    
    def __init__(self, config_manager):
        self._config = config_manager
    
    def get_active_profile(self):
        """Get the currently active profile based on time of day."""
        now = datetime.datetime.now()
        return PROFILE_MORNING if self.is_morning(now) else PROFILE_EVENING
    
    def is_morning(self, now):
        """Check if the given time is considered morning (before 12:00)."""
        return now.time() < datetime.time(12)
    
    def get_profile_colors(self, profile_name):
        """Get RGB color tuple for a specific profile."""
        return self._config.get_profile_colors(profile_name)
    
    def get_profile_color_value(self, profile_name, color):
        """Get specific color value from a profile."""
        return self._config.get_profile_color_value(profile_name, color)

    def get_profile_color_object(self, profile_name) -> Color:
        """Get Color object for a specific profile."""
        colors = self.get_profile_colors(profile_name)
        return Color.from_tuple(colors)
    
    def get_active_profile_color(self) -> Color:
        """Get Color object for the currently active profile."""
        active_profile = self.get_active_profile()
        return self.get_profile_color_object(active_profile)