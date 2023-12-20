#!/usr/bin/env python3
"""
create a cache class
"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Get the data associated with a key from Redis.

        Args:
            key (str): The key to get the data from.
            fn (Callable, optional): A callable that converts the data to the desired format.

        Returns:
            Union[str, bytes, int, float]: The data associated with the key.
        """
        data = self._redis.get(key)
        if fn is not None and data is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Get the data associated with a key from Redis and convert it to a str.

        Args:
            key (str): The key to get the data from.

        Returns:
            str: The data associated with the key.
        """
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Get the data associated with a key from Redis and convert it to an int.

        Args:
            key (str): The key to get the data from.

        Returns:
            int: The data associated with the key.
        """
        return self.get(key, fn=int)
