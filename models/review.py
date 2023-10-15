#!/usr/bin/python3
"""Basemofw."""
from models.base_model import BaseModel


class Review(BaseModel):
    """review
        place_id: Place id.
        user_id:User id.
        text:text for the review.
    """

    place_id = ""
    user_id = ""
    text = ""
