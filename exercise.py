#!/usr/bin/env python3
"""
Class that connects to the database and flushes when complete
The class has a method store that updates redis
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """:param method: The method to be decorated.
       :return: A new Callable that wraps the
                original method and counts its calls.
    """
    key = method.__qualname__

    @wraps(method)
    def increment(self, *args, **kwargs):
        """Councts the increments
           :param self: The instance of the Cache class.
           :param args: Any positional arguments passed
                        to the decorated method.
           :param kwargs: Any keyword arguments passed
                          to the decorated method.
           :return: The result of the decorated method.
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return increment


def call_history(method: Callable) -> Callable:

    @wraps(method)
    def history(self, *args, **kwargs):
        """Customised inputs
           Returns:
                  result of the method
        """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return history


def replay(method: Callable) -> Callable:
    """
    display the history of calls of a particular function
    """
    key = method.__qualname__
    redis = int(Cache()._redis.get(key))
    print(f"{key} was called {redis} times:")
    for i, (input_key, output_key) in enumerate(
        zip(redis._redis.lrange(f"{key}:inputs", 0, -1), redis._redis.lrange(
            f"{key}:outputs", 0, -1))):
        input_str = input_key.decode('utf-8')
        output_str = output_key.decode('utf-8')
        inputs = eval(input_str) if input_str != 'None' else ()
        output = eval(output_str) if output_str != 'None' else None
    print(f"{key}(*{inputs}) -> {output_key.decode('utf-8')}")


class Cache():
    """Define  instance variable called redis
       Attributes:
                  _redis: Aredis client instance.
       Methods:
               store: Inputs data in redis.
    """
    def __init__(self):
        """
           creates the redis instance
           flushes it afterwards
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Deals with data storage
           Args:
                data:Can be str, byte, int, float
           Returns:
                  key: generated using the uuid
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """Takes a value and converts it to its required formart
           Args:
                key: string from redis
                fn: callable which converts to the other formarts
           Returns:
                str, bytes, int, float, None(if key does not exist)
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """Returns the string
           in utf-8
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Returns the integer values
        only
        """
        return self.get(key, fn=int)
