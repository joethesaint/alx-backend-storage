#!/usr/bin/python3
""" 8-main """
from pymongo import Mongoclient
list_all = __import__("8-all").list_all

if __name__ == "__main__":
    client = Mongoclient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
