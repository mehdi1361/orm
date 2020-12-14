import redis
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta
import json
from functools import wraps

def cache(**kwargs):

    def wrapper(func):

        def cash_reload(*args, **kwargs):
            r = redis.Redis(host='127.0.0.1', port=6379)
            result = r.get(f'lst_{func.__name__}')
            if result:

                return Response(json.loads(result), status=status.HTTP_200_OK)
            else:
                result = func(*args, **kwargs)
                r.setex(f'lst_{func.__name__}', timedelta(minutes=kwargs['time']), json.dumps(result.data))
                return result

        return cash_reload

    return wrapper
