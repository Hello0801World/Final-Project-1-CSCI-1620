class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 5     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 5      # Maximum TV volume

    def __init__(self, channel, volume):
        """
        - Create a private variable to store the TV channel. It should be set to the minimum TV channel by default.
        - Create a private variable to store the TV volume. It should be set to the minimum TV volume by default.
        - Create a private variable to store the TV status. The TV should start when it is off.
        """
        self.__channel = channel
        self.__volume = volume


    def power(self):
        """
        - This method should be used to turn the TV on/off.
        - If called on a TV object that is off, the TV object should be turned on.
        - If called on a TV object that is on, the TV object should be turned off.
        """

        if self.__status==False:
            self.__status=True
        elif self.__status==True:
            self.__status=False


    def channel_up(self):
        """
        - This method should be used to adjust the TV channel by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
        """

        if self.__channel >=self.MIN_CHANNEL and self.__channel <self.MAX_CHANNEL:
            self.__channel+=1
        elif self.__channel==self.MAX_CHANNEL:
            self.__channel=self.MIN_CHANNEL

        return self.__channel


    def channel_down(self):
        """
        - This method should be used to adjust the TV channel by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """

        if self.__channel>self.MIN_CHANNEL and self.__channel<=self.MAX_CHANNEL:
            self.__channel-=1
        elif self.__channel ==self.MIN_CHANNEL:
            self.__channel=self.MAX_CHANNEL

        return self.__channel



    def volume_up(self):
        """
        - This method should be used to adjust the TV volume by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
        """

        if self.__volume>=self.MIN_VOLUME and self.__volume < self.MAX_VOLUME:
            self.__volume+=1
        elif self.__volume == self.MAX_VOLUME:
            pass

        return self.__volume


    def volume_down(self):
        """
        - This method should be used to adjust the TV volume by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
        """

        if self.__volume>self.MIN_VOLUME and self.__volume<=self.MAX_VOLUME:
            self.__volume-=1
        elif self.__volume==self.MIN_VOLUME:
            pass

        return self.__volume



    def __str__(self):
        """
        - This method should be used to return the TV status using the format shown in the comments of main.py
        """

        return f'TV status on ={self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


