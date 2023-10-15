#!/usr/bin/python3
"""State that ingerit basemodel"""
from models.base_model import BaseModel


class State(BaseModel):
    """inherite name and data frome basemodel
    namw: state name"""
    name = ""
