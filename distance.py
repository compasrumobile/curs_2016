class Distance:

    def __init__(self, meters=0, km=0):
        self.meters = meters + km * 1000

    def __add__(self, b):
        if type(b) == Distance:
            self.meters += b.meters
        else:
            self.meters += b
        return self

    def km(self):
        return self.meters / 1000


d1 = Distance(300)

print(d1.meters)

