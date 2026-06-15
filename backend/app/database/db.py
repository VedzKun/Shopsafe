class Database:
    def __init__(self):
        self.connected = False
    def connect(self):
        self.connected = True
    def disconnect(self):
        self.connected = False
        