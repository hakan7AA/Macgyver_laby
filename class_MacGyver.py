"""Pygame importation."""
import pygame
from pygame.locals import *
from class_Coordinates import *


class MacGyver:
    """
    Description.

    A class to define the attributes of Macgyver.
    """

    def __init__(self):
        """Constructor. Sets blank coordinates and 'player.png' as sprite."""
        self.coord = Coordinates(None, None)
        self.sprite = pygame.image.load(
            'ressource/MacGyver.png'
            ).convert_alpha()

    def get_coord(self):
        """Return Macgyver's position as a Coordinate type object."""
        return self.coord

    def set_coord(self, coord):
        """Set Macgyver's coordinates.
        Uses a Coordinate type object as argument."""
        self.coord = coord

    def get_sprite(self):
        """Return macgyver's sprite."""
        return self.sprite

    def empty(self):
        """Only for aesthetical purposes :
        makes Macgyver's sprite invisible when he loses."""
        self.sprite = pygame.image.load('ressource/exit.png').convert_alpha()
