#!/usr/bin/bash python3
"""function that changes all topics of a school document based on the name
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Based on the name all topics of the school document are changed
    """
    return mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}}
        )
