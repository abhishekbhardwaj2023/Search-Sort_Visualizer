import tkinter as tk
import Codes.Start_Threading

from Codes.type_Searching import *
from Codes.type_Sorting import *


class Window:
    def __init__(self, root):

        # Main Window
        self.root = root

        # Warning sign for close
        self.root.protocol("WM_DELETE_WINDOW", self.Close)

        # Main Window Size and Center Aligned in the screen
        self.wx, self.wy = 400, 350
        self.wxs, self.wys = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.WINDOW_X, self.WINDOW_Y = (self.wxs / 2) - (self.wx / 2), (self.wys / 2) - (self.wy / 2)
        self.root.geometry('%dx%d+%d+%d' % (self.wx, self.wy, self.WINDOW_X, self.WINDOW_Y))
        self.root.config(bg="LightSkyBlue1")
        self.root.resizable(False, False)

        # Title And Icon
        self.root.title("Algorithm Visualizer")
        self.root.iconbitmap("Images/algorithm.ico")
        

        # Heading of the main window
        self.MainLabel = Label(self.root, text='Algorithm Visualizer', bg="LightSkyBlue1", fg="red",
                               font=("Times new roman", 25,"bold"))
        self.MainLabel.pack(pady=15)

        def show():
            if (ch1.get() == 1) & (ch2.get() == 1):
                   messagebox.showerror("Error!", "Please choose only 1 type!!")
                   
            elif (ch1.get() == 1) & (ch2.get() == 0):

                self.root.destroy()
                search_window = Tk()
                type_Searching(search_window)
                search_window.mainloop()


            elif (ch1.get() == 0) & (ch2.get() == 1):

                self.root.destroy()
                sort_window = Tk()
                type_Sorting(sort_window)
                sort_window.mainloop()

            elif (ch1.get() == 0) & (ch2.get() == 0):
                   messagebox.showerror("Error!", "Please choose the type of algorithm !!")
                
               
        label = Label(self.root, text='Choose the type of algorithm:', fg="blue",bg="LightSkyBlue1",
                               font=("Times new roman", 15,"bold"))
        label.pack(pady=15)


        #checkbuttons
        ch1=tk.IntVar()  
        check1=tk.Checkbutton(self.root, text="Searching", variable=ch1,font=("Times new roman", 15,"bold"))  
        check1.deselect()  
        check1.pack(pady=5, expand=YES)  
          
        ch2=tk.IntVar()  
        check2=tk.Checkbutton(self.root, text="Sorting", variable=ch2,font=("Times new roman", 15,"bold"))  
        check2.deselect()  
        check2.pack(pady=5, expand=YES)

        button1=Button(self.root, text="Next >>",bg="green2", activebackground="lime green",
                                 font=("calibri", 20,"bold"),command=show).pack(expand=YES)   
        


    # Exit button
    def Exit(self):
        self.root.destroy()

    # Close warning
    def Close(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.root.destroy()
            exit()

    # Secondary window back button
    def Back(self):
        self.root.destroy()
        Process = Codes.Start_Threading.START()
        Process.start()
