class FakeRandom:
    def __init__(self):
        self.palautus = 1

    def randint(self, eka, toka):
        return self.palautus
