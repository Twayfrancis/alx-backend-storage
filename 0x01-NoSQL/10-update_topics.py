#!/usr/bin/env python3
"""function that changes all topics of school doc based on name"""


def update_topics(mongo_collection, name, topics):
    """ Update all topics of a school document based on the name """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
