#!/usr/bin/bash python3
"""Inserts  a new document in a collection based on kwargs"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    for key, value in kwargs.items():
        data = mongo_collection.insert_one({key: value})
        return data.inserted_id
