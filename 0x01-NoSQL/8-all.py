#!/usr/bin/env python3
"""lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """mongo_collection will be the pymongo collection object
       Return an empty list if no document in the collection
    """
    if mongo_collection is None:
        return []
    return [doc for doc in mongo_collection.find()]
