class Television:
    """
    Class to represent television object
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 5     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 5      # Maximum TV volume

    def __init__(self, channel, volume):
        """
        Constructor to create a television object
        :param channel: channel of television object
        :param volume: volume of television object
        """
        self.__channel = channel
        self.__volume = volume

    def channel_up(self):
        """
        Function to channel up for a tv object
        :return: value of channel
        """

        if self.__channel >=self.MIN_CHANNEL and self.__channel <self.MAX_CHANNEL:
            self.__channel+=1
        elif self.__channel==self.MAX_CHANNEL:
            self.__channel=self.MIN_CHANNEL

        return self.__channel


    def channel_down(self):
        """
        Function to channel down for a tv object
        :return: value of channel
        """

        if self.__channel>self.MIN_CHANNEL and self.__channel<=self.MAX_CHANNEL:
            self.__channel-=1
        elif self.__channel ==self.MIN_CHANNEL:
            self.__channel=self.MAX_CHANNEL

        return self.__channel



    def volume_up(self):
        """
        Function to volume up for a tv object
        :return: value of volume
        """

        if self.__volume>=self.MIN_VOLUME and self.__volume < self.MAX_VOLUME:
            self.__volume+=1
        elif self.__volume == self.MAX_VOLUME:
            pass

        return self.__volume


    def volume_down(self):
        """
        Function to volume up
        :return: value of volume
        """

        if self.__volume>self.MIN_VOLUME and self.__volume<=self.MAX_VOLUME:
            self.__volume-=1
        elif self.__volume==self.MIN_VOLUME:
            pass

        return self.__volume

