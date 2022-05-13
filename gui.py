from tkinter import *
from classes import *
from PIL import ImageTk, Image


class GUI:
    """
    class to create a GUI and have some methods to function buttons
    """
    def __init__(self,window):
        """
        Constructor to create a user interface
        :param window: window parameter from main class
        """
        self.window =window

        self.channel_val=1
        self.volume_val =0
        self.tv = Television(self.channel_val, self.volume_val)



        self.frame_top=Frame(self.window)
        self.TorF = BooleanVar(self.window)
        self.check=Checkbutton(self.frame_top,text='On/Off', variable =self.TorF, command =self.change_button_state)
        self.check.pack()
        self.frame_top.pack(pady=5)

        self.frame_channel = Frame(self.window)
        self.label_channel = Label(self.frame_channel, text='Channel')
        self.label_channel.pack(padx=5, pady=10, side=LEFT)
        self.frame_channel.pack()

        self.frame_middle=Frame(self.window)
        #self.label_channel=Label(self.frame_middle,text='Channel')
        self.button_channel_up = Button(self.frame_middle,text='Up',state = DISABLED, command=self.Cha_up_clicked)
        self.button_channel_down = Button(self.frame_middle,text='Down',state = DISABLED, command= self.Cha_down_clicked)
        self.label_num_channel = Label(self.frame_middle, text=self.channel_val)

        self.label_channel.pack(padx=5, pady=10, side=LEFT)
        self.button_channel_up.pack(padx=5, pady=10, side=LEFT)
        self.label_num_channel.pack(padx=5, pady=10, side=LEFT)
        self.button_channel_down.pack(padx=5, pady=10, side=LEFT)
        #self.label_channel.pack(padx=5, pady=10, side=LEFT)
        #self.label_num_channel.pack(padx=5, pady=10, side=LEFT)
        self.frame_middle.pack()

        self.frame_channel_img = Frame(self.window)
        self.channel_image = Image.open('tim-gouw-VvQSzMJ_h0U-unsplash.jpg')
        self.resized_img = self.channel_image.resize((100,50), Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(self.resized_img)
        self.label_channel_desc = Label(self.frame_channel_img,text=' ',state='disable')
        self.label_channel_img = Label(self.frame_channel_img,image=self.new_image,state='disable')

        self.label_channel_desc.pack()
        self.label_channel_img.pack(padx=5,pady=5,side=LEFT)
        self.frame_channel_img.pack()

        self.frame_volume = Frame(self.window)
        self.label_volume = Label(self.frame_volume, text='Volume')
        self.label_volume.pack(padx=5, pady=10, side=LEFT)
        self.frame_volume.pack()


        self.frame_bottom = Frame(self.window)
        #self.label_volume = Label(self.frame_bottom, text='Volume')
        self.button_volume_up = Button(self.frame_bottom, text='Up', state = DISABLED,command = self.Vol_up_clicked)
        self.button_volume_down = Button(self.frame_bottom, text='Down',state = DISABLED,command = self.Vol_down_clicked)
        self.label_num_volume = Label(self.frame_bottom, text='0')

        #self.label_volume.pack(padx=5, pady=10, side=LEFT)
        self.button_volume_up.pack(padx=5, pady=10, side=LEFT)
        self.label_num_volume.pack(padx=5, pady=10, side=LEFT)
        self.button_volume_down.pack(padx=5, pady=10, side=LEFT)
        self.label_volume.pack(padx=5, pady=10, side=LEFT)
        #self.label_num_volume.pack(padx=5, pady=10, side=LEFT)
        self.frame_bottom.pack()

        self.instruction = Label(self.window, text='Make check box marked to turn a tv on\n'
                                                   'Channel is range from 1 to 4\n'
                                                   'Volume is range from 0 to 5')

        self.instruction.pack(padx=5,pady=10)

    def change_button_state(self):
        """
        Function to change a state of buttons based on if CheckButton is marked or not
        """
        if self.TorF.get():
            self.button_channel_up['state'] = 'active'
            self.button_channel_down['state'] = 'active'
            self.button_volume_up['state'] = 'active'
            self.button_volume_down['state'] = 'active'
            self.label_channel_img['state']='active'
            self.label_channel_desc['state'] = 'active'

            if self.channel_val==1:
                self.label_channel_desc.config(text='Sports')
            elif self.channel_val==2:
                self.label_channel_desc.config(text='Movie')
            elif self.channel_val==3:
                self.label_channel_desc.config(text='Comedy')
            elif self.channel_val==4:
                self.label_channel_desc.config(text='Drama')
        else:
            self.button_channel_up["state"] = 'disable'
            self.button_channel_down["state"] = 'disable'
            self.button_volume_up["state"] = 'disable'
            self.button_volume_down["state"] = 'disable'
            self.label_channel_img['state'] = 'disable'
            self.label_channel_desc['state'] = 'disable'
            self.label_channel_desc.config(text=' ')

    def Cha_up_clicked(self):
        """
        Function to call channel_up method when button_channel_up is clicked
        """
        self.channel_val = self.tv.channel_up()
        self.label_num_channel.config(text=f'{self.channel_val}')

        if self.channel_val==1:
            self.channel_image = Image.open('tim-gouw-VvQSzMJ_h0U-unsplash.jpg')
            self.resized_img = self.channel_image.resize((100, 50), Image.ANTIALIAS)
            self.new_image = ImageTk.PhotoImage(self.resized_img)
            self.label_channel_img.config(image=self.new_image)

            self.label_channel_desc.config(text='Sports')
        elif self.channel_val==2:
            self.channel_image = Image.open('tamara-gak-1vZAezBEADw-unsplash.jpg')
            self.resized_img = self.channel_image.resize((100, 50), Image.ANTIALIAS)
            self.new_image = ImageTk.PhotoImage(self.resized_img)
            self.label_channel_img.config(image =self.new_image)

            self.label_channel_desc.config(text='Movie')
        elif self.channel_val==3:
            self.channel_image = Image.open('stewart-munro-XuFOXH9bCK8-unsplash.jpg')
            self.resized_img = self.channel_image.resize((100, 50), Image.ANTIALIAS)
            self.new_image = ImageTk.PhotoImage(self.resized_img)
            self.label_channel_img.config(image=self.new_image)

            self.label_channel_desc.config(text='Comedy')
        elif self.channel_val==4:
            self.channel_image = Image.open('gr-stocks-q8P8YoR6erg-unsplash.jpg')
            self.resized_img = self.channel_image.resize((100, 50), Image.ANTIALIAS)
            self.new_image = ImageTk.PhotoImage(self.resized_img)
            self.label_channel_img.config(image=self.new_image)

            self.label_channel_desc.config(text='Drama')


    def Cha_down_clicked(self):
        """
        Function to call channel_down method when button_channel_down is clicked
        """
        self.channel_val=self.tv.channel_down()
        self.label_num_channel.config(text=f'{self.channel_val}')

        if self.channel_val==1:
            self.channel_image = Image.open('tim-gouw-VvQSzMJ_h0U-unsplash.jpg')
            self.resized_img = self.channel_image.resize((100, 50), Image.ANTIALIAS)
            self.new_image = ImageTk.PhotoImage(self.resized_img)
            self.label_channel_img.config(image=self.new_image)

            self.label_channel_desc.config(text='Sports')
        elif self.channel_val==2:
            self.channel_image = Image.open('tamara-gak-1vZAezBEADw-unsplash.jpg')
            self.resized_img = self.channel_image.resize((100, 50), Image.ANTIALIAS)
            self.new_image = ImageTk.PhotoImage(self.resized_img)
            self.label_channel_img.config(image =self.new_image)

            self.label_channel_desc.config(text='Movie')
        elif self.channel_val==3:
            self.channel_image = Image.open('stewart-munro-XuFOXH9bCK8-unsplash.jpg')
            self.resized_img = self.channel_image.resize((100, 50), Image.ANTIALIAS)
            self.new_image = ImageTk.PhotoImage(self.resized_img)
            self.label_channel_img.config(image=self.new_image)

            self.label_channel_desc.config(text='Comedy')
        elif self.channel_val==4:
            self.channel_image = Image.open('gr-stocks-q8P8YoR6erg-unsplash.jpg')
            self.resized_img = self.channel_image.resize((100, 50), Image.ANTIALIAS)
            self.new_image = ImageTk.PhotoImage(self.resized_img)
            self.label_channel_img.config(image=self.new_image)

            self.label_channel_desc.config(text='Drama')

    def Vol_up_clicked(self):
        """
        Function to call volume_up method when button_volume_up is clicked
        """
        self.volume_val=self.tv.volume_up()
        self.label_num_volume.config(text=f'{self.volume_val}')

    def Vol_down_clicked(self):
        """
        Function to call volume_down method when button_volume_down is clicked
        """
        self.volume_val = self.tv.volume_down()
        self.label_num_volume.config(text=f'{self.volume_val}')





