import tkinter as tk
from tkinter import ttk
import Codes.Start_Threading
from Codes.type_Searching import *
from Codes.Start_Searching import *


class type_Searching:
    def __init__(self, root):

        # Sorting window
        self.root = root

        # warning for close/exit
        self.root.protocol("WM_DELETE_WINDOW", self.Close)

       

        # Window Size
        self.wx, self.wy = 400, 350

        # Screen Size
        self.wxs, self.wys = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        # Aligning the window in the center of the screen
        self.WINDOW_X, self.WINDOW_Y = (self.wxs / 2) - (self.wx / 2), (self.wys / 2) - (self.wy / 2)

        # Sorting canvas size
        self.CANVAS_X, self.CANVAS_Y = 950, 700

        # Left side information frame size
        self.FRAME1_X, self.FRAME1_Y = 250, 700

        # Apply changes to window
        self.root.geometry('%dx%d+%d+%d' % (self.wx, self.wy, self.WINDOW_X, self.WINDOW_Y))
        self.root.config(bg="Lightskyblue1")
        self.root.wm_resizable(False, False)

        # Title And Icon
        self.root.title("Algorithm Visualizer")
        self.root.iconbitmap("Images/searching.ico")

        def show1():
            if (ch1.get() == 1) & (ch2.get() == 1):
                   messagebox.showerror("Error!", "Please choose exactly 1 type!!")
                   
            elif (ch1.get() == 1) & (ch2.get() == 0):

                self.root.destroy()
                linear_search = Tk()
                Searching(linear_search,"Linear Search")
                linear_search.mainloop()

            elif (ch1.get() == 0) & (ch2.get() == 1):

                self.root.destroy()
                binary_search = Tk()
                Searching(binary_search,"Binary Search")
                binary_search.mainloop()

            else:
                messagebox.showerror("Error!", "Please choose the type of algorithm !!")

        self.MainLabel2 = Label(self.root, text='Choose the type of searching algorithm:', bg="LightSkyBlue1", fg="red",
                               font=("Times new roman", 14,"bold"))
        self.MainLabel2.pack(pady=15)

        ch1=tk.IntVar()  
        check1=tk.Checkbutton(self.root, text="Linear search", variable=ch1,font=("Times new roman", 14))  
        check1.deselect()  
        check1.pack(pady=5, expand=YES)  
          
        ch2=tk.IntVar()  
        check2=tk.Checkbutton(self.root, text="Binary search", variable=ch2,font=("Times new roman", 14))  
        check2.deselect()  
        check2.pack(pady=5, expand=YES)

        button1=Button(self.root, text="Submit",bg="green2", activebackground="lime green",
                                 font=("calibri", 20,"bold"),command=show1).pack(expand=YES)   


        


       


    def Exit(self):
        self.root.destroy()
      
    # Function for back button to main window
    def Back(self):
        self.root.destroy()
        Process = Codes.Start_Threading.START()
        Process.start()

    # Function for exit
    def Close(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.root.destroy()
            quit()




