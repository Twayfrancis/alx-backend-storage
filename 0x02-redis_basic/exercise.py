#!/usr/bin/env python3
"""
create a cache class
"""
import redis
import uuid
from typing import Union, Callable, Optional
import functools


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a method

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(f"{key}:outputs", str(result))
        return result
    return wrapper


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

    @call_history
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


def replay(method: Callable):
    """
    function to display the history of calls of a particular method.
    Args:
        method (Callable): the method to display the history for.
    """
    key = method.__qualname__
    inputs = method.__self__._redis.lrange(f"{key}:inputs", 0, -1)
    outputs = method.__self__._redis.lrange(f"{key}:outputs", 0, -1)
    print(f"{key} was called {len(inputs)} times:")
    for inp, out in zip(inputs, outputs):
        inp_str = inp.decode('utf-8')
        out_str = out.decode('utf-8')
        print(f"{key}{inp_str} -> {out_str}")
