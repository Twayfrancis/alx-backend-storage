#!/usr/bin/env python3
"""
create a cache class
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class for storing data in a Redis database.
    Attributes:
        _redis (Redis): Instance of the Redis client.
    """
    def __init__(self):
        """
        Cache class constructor.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key and return the key.
        Args:
            data (Union[str, bytes, int, float]): The data to be stored.
        Returns:
            str: The key under which the data is stored in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
