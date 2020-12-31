from redis import Redis

class CustomCashe(Redis):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CustomCashe, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        super().__init__(host='localhost', port=6379)
