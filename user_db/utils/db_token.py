from cachetools import TTLCache
from common.constants import ttl
from threading import Lock

class CacheDBKey:
    _instance = None
    _lock = Lock()  # Ensure thread safety for singleton initialization


    # Ensure that new class instance is not created if one already exists
    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(CacheDBKey, cls).__new__(cls)
                cls._instance.key_store = TTLCache(maxsize=1000, ttl=ttl)
        return cls._instance

    def storeKey(self, user_id, key_db_token):
        """Store key_db_token in the TTLCache."""
        self.key_store[user_id] = key_db_token

    def getKey(self, user_id):
        """Retrieve key_db_token from the TTLCache."""
        return self.key_store.get(user_id)