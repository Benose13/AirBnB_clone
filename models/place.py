#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """place:
        city_id: The City id.
        user_id: The User id.
        name: name.
        description: description
        number_rooms:number of rooms.
        number_bathrooms:number of bathrooms.
        max_guest :maximum number of guests
        price_by_night: price per night of the place.
        latitude: latitude of the place.
        longitude :longitude of the place.
        amenity_ids: list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
