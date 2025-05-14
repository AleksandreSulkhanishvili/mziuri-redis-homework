import time


class FakeRedis:
    def __init__(self):
        self.store = {}

    def set(self, key, value, ex=None):
        expiration_time = time.time() + ex
        if ex is not None:
            self.store[key] = (value, expiration_time)
        else:
            None

    def get(self, key):
        if key not in self.store:
            return None

        value, expiration_time = self.store[key]
        if expiration_time is not None and time.time() > expiration_time:
            del self.store[key]
            return None
        return value


# Usage example:
if __name__ == "__main__":
    r = FakeRedis()
    r.set("temp", "123", ex=3)
    time.sleep(4)
    print(r.get("temp"))
