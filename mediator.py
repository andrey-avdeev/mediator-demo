class Mediator:
    def __init__(self):
        self._delegates = {}

    def subscribe(self, key, delegate):
        if key not in self._delegates:
            self._delegates[key] = []

        self._delegates[key].append(delegate)

    def publish(self, key, data):
        if key in self._delegates:
            for delegate in self._delegates[key]:
                delegate(data)
