class Hospital:

    def __init__(self, spaciousness=0):
        self.spaciousness = spaciousness

    def get_t(self):
        return self.__spaciousness

    def set_t(self, value):

        if value > 1000:
            self.__spaciousness = 1000
        else:
            self.__spaciousness = value

    spaciousness = property(get_t, set_t)

h = Hospital(1200)
print(h.spaciousness)

class Ward:

    def __init__(self, spaciousness=0):
        self.spaciousness = spaciousness

    def get_t(self):
        return self.__spaciousness

    def set_t(self, value):

        if value > 4:
            self.__spaciousness = 4
        else:
            self.__spaciousness = value

    spaciousness = property(get_t, set_t)

h = Ward(10)
print(h.spaciousness)



