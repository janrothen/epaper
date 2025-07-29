#!/usr/bin/env python3

"""
Main application script for controlling RGB LED strips on Raspberry Pi.

This script provides the entry point for the LED strip controller application.
It initializes the LED hardware, handles graceful shutdown signals, and manages
the main application lifecycle including fade-in effects and cleanup operations.

The application runs continuously until interrupted by SIGINT (Ctrl+C) or SIGTERM,
at which point it performs cleanup by turning off the LED strip before exiting.

Usage:
    python3 run.py

Dependencies:
    - ledstrip: LED strip control logic
    - graceful_shutdown: Signal handling for clean shutdown
    - Raspberry Pi with GPIO pins connected to RGB LED strip
    - pigpio daemon running for hardware control
"""

import time

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from config.config_manager import ConfigManager
from led.profile_manager import ProfileManager
from led.color import Color
from led.effects import breathing_effect, fade_effect, random_color_effect, color_cycle_effect
from led.gpio_service import GPIOService
from led.ledlightstrip_controller import LEDLightstripController
from utils.graceful_shutdown import GracefulShutdown

def main():
    killer = GracefulShutdown()
    config_manager = ConfigManager()
    pins = config_manager.get_all_pin_assignments()
    gpio_service = GPIOService()
    strip = LEDLightstripController(pins, gpio_service=gpio_service)
    strip.switch_off()

    profile_manager = ProfileManager(config_manager)

    logging.info("App started. Press Ctrl+C to stop.")

    color = profile_manager.get_active_profile_color()
    strip.run_sequence(fade_effect, strip, Color.BLACK, color, 10000)

    while not killer.kill_now:
        logging.info("Running...")
        time.sleep(1)

    strip.stop_current_sequence()
    strip.switch_off()
    logging.info("App exited cleanly.")

if __name__ == '__main__':
    main()