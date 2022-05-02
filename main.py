from gui import *


def main():
    window: Tk = Tk()
    window.geometry('300x300')
    window.title('Television')
    window.resizable(False,False)

    widgets = GUI(window)
    window.mainloop()



if __name__=='__main__':
    main()
