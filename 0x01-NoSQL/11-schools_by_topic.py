#!/usr/bin/bash python3
"""function that returns the list of school having a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """The topic is what is searched
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})
