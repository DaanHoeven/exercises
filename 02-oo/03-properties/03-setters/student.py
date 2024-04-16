# Write your code here
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        if value < 0 or value > 23:
            raise ValueError("Unvalid value")
        else:
            self.__hours = value

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        if value < 0 or value > 59:
            raise ValueError("Unvalid value")
        else:
            self.__minutes = value

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        if value < 0 or value > 59:
            raise ValueError("Unvalid value")
        else:
            self.__seconds = value
