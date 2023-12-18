#!/usr/bin/env python3
"""function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """_summary_

    Args:
        mongo_collection (_type_): _description_
    """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
