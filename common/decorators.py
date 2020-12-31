import redis
from common.custom_redis import CustomCashe
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta
import json


def cache(cache_time):

    def wrapper(func):

        def cash_reload(*args, **kwargs):
            r = CustomCashe()
            result = r.get(f'lst_{func.__name__}')
            if result:

                return Response(json.loads(result), status=status.HTTP_200_OK)
            else:
                result = func(*args, **kwargs)
                r.setex(f'lst_{func.__name__}', timedelta(seconds=cache_time), json.dumps(result.data))
                return result

        return cash_reload

    return wrapper
