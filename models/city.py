#!/usr/bin/python3
""" inherit Basemodel"""
from models.base_model import BaseModel


class City(BaseModel):
    """city with state id
    state_id: id for state
    name: name of state"""
    state_id = ""
    name = ""
