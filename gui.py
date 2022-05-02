from tkinter import *
from classes import *


class GUI:
    def __init__(self,window):
        self.window =window

        self.channel_val=0
        self.volume_val =0
        self.tv = Television(self.channel_val, self.volume_val)


        self.frame_top=Frame(self.window)
        self.TorF = BooleanVar(self.window)
        self.check=Checkbutton(self.frame_top,text='On/Off', variable =self.TorF, command =self.change_button_state)
        self.check.pack()
        self.frame_top.pack(pady=5)

        self.frame_middle=Frame(self.window)
        self.label_channel=Label(self.frame_middle,text='Channel')
        self.button_channel_up = Button(self.frame_middle,text='Up',state = DISABLED, command=self.Cha_up_clicked)
        self.button_channel_down = Button(self.frame_middle,text='Down',state = DISABLED, command= self.Cha_down_clicked)
        self.label_num_channel = Label(self.frame_middle, text='0')

        self.label_channel.pack(padx=5, pady=10, side=LEFT)
        self.button_channel_up.pack(padx=5, pady=10, side=LEFT)
        self.button_channel_down.pack(padx=5, pady=10, side=LEFT)
        self.label_channel.pack(padx=5, pady=10, side=LEFT)
        self.label_num_channel.pack(padx=5, pady=10, side=LEFT)
        self.frame_middle.pack()

        self.frame_bottom = Frame(self.window)
        self.label_volume = Label(self.frame_bottom, text='volume')
        self.button_volume_up = Button(self.frame_bottom, text='Up', state = DISABLED,command = self.Vol_up_clicked)
        self.button_volume_down = Button(self.frame_bottom, text='Down',state = DISABLED,command = self.Vol_down_clicked)
        self.label_num_volume = Label(self.frame_bottom, text='0')

        self.label_volume.pack(padx=5, pady=10, side=LEFT)
        self.button_volume_up.pack(padx=5, pady=10, side=LEFT)
        self.button_volume_down.pack(padx=5, pady=10, side=LEFT)
        self.label_volume.pack(padx=5, pady=10, side=LEFT)
        self.label_num_volume.pack(padx=5, pady=10, side=LEFT)
        self.frame_bottom.pack()

        self.instruction = Label(self.window, text='Make check box marked to turn a tv on\n'
                                                   'Channel is range from 0 to 5\n'
                                                   'Volume is range from 0 to 5')

        self.instruction.pack(padx=5,pady=10)


    def change_button_state(self):
        if self.TorF.get():
            self.button_channel_up['state'] = 'active'
            self.button_channel_down['state'] = 'active'
            self.button_volume_up['state'] = 'active'
            self.button_volume_down['state'] = 'active'
        else:
            self.button_channel_up["state"] = 'disable'
            self.button_channel_down["state"] = 'disable'
            self.button_volume_up["state"] = 'disable'
            self.button_volume_down["state"] = 'disable'

    def Cha_up_clicked(self):
        channel = self.tv.channel_up()
        self.label_num_channel.config(text=f'{channel}')

    def Cha_down_clicked(self):
        channel=self.tv.channel_down()
        self.label_num_channel.config(text=f'{channel}')

    def Vol_up_clicked(self):
        volume=self.tv.volume_up()
        self.label_num_volume.config(text=f'{volume}')

    def Vol_down_clicked(self):
        volume = self.tv.volume_down()
        self.label_num_volume.config(text=f'{volume}')



