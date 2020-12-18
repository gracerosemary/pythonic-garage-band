class Band:
    """Band instance requires attribute of name (string) and members (list). The play_solos method asks each member to play a solo, in the order they were added to the band. The to_list method returns a list of previously created Band instances."""
    instances = []
    def __init__(self, name: str, members=None):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"
    
    def play_solos(self):
        solos = []
        members = self.members
        for solo in members:
            solo = solo.play_solo()
            solos.append(solo)
        return solos

        # one-liner solution from code review
        # return [solo.play_solo() for solo in self.members]

    @classmethod
    def to_list(cls):
        return cls.instances

class Musician:
    """get_instrument method returns a string. play_solo method also returns a string."""
    def __init__(self, name, instrument, solo, title):
        self.name = name
        self.instrument = instrument
        self.solo = solo
        self.title = title

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f'{self.title} instance. Name = {self.name}'
        # returns name of that class and refer to its name
        # return f'{self.__class__.__name__} instance. Name = {self.name}'

    def get_instrument(self):
            return f"{self.instrument}"

    def play_solo(self):
        return f"{self.solo}"

class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar", "face melting guitar solo", "Guitarist")

class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, "bass", "bom bom buh bom", "Bassist")

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "drums", "rattle boom crash", "Drummer")


if __name__ == "__main__":
    musician = Musician("joe", "flute", "solo", "title")
    print(musician)
    # print(repr(musician))

    guitarist = Guitarist("jane")
    print(guitarist)

# Attribution - Super: https://realpython.com/python-super/