import os
import tkinter
import tkinter.messagebox

print('App is runtime' + str(__name__))

def gen_talk_message():
    tkinter.messagebox.showinfo('warn','the message send to python3')
    print('message send:)')

def printSend():
    root=tkinter.Tk()
    root.title('the gui runtiem in python3')
    root.geometry('800x600') # window w-h
    root.resizable(False, False)
    tkinter.Button(
        root, 
        text='hello button',
        command=gen_talk_message
    ).pack()
    root.mainloop() # the window loop is state..

if __name__ == '__main__':
    printSend()