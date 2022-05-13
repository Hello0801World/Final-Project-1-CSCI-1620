from gui import *


def main():
    """
    Function to create window conditions such as size,title, etc.
    """
    window: Tk = Tk()
    window.geometry('250x400')
    window.title('Television')
    window.resizable(False,False)

    widgets = GUI(window)
    window.mainloop()


if __name__=='__main__':
    main()
