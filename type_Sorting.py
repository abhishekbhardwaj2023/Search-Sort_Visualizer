import tkinter as tk
from tkinter import ttk
import Codes.Start_Threading
from Codes.type_Sorting import *
from Codes.Start_Sorting import *
from PIL import ImageTk,Image

# Main sorting class
class type_Sorting:
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
        self.root.iconbitmap("Images/sorting.ico")

        def show2():
            
                   
            if (ch1.get() == 1) & (ch2.get() == 0) & (ch3.get() == 0) & (ch4.get() == 0):

                self.root.destroy()
                Bubble_sort = Tk()
                Sorting(Bubble_sort,"Bubble Sort")
                Bubble_sort.mainloop()

            elif (ch1.get() == 0) & (ch2.get() == 1)& (ch3.get() == 0) & (ch4.get() == 0):

                self.root.destroy()
                merge_sort = Tk()
                Sorting(merge_sort,"Merge Sort")
                merge_sort.mainloop()

            elif (ch1.get() == 0) & (ch2.get() == 0)& (ch3.get() == 1) & (ch4.get() == 0):

                self.root.destroy()
                Insertion_sort = Tk()
                Sorting(Insertion_sort,"Insertion Sort")
                Insertion_sort.mainloop()

            elif (ch1.get() == 0) & (ch2.get() == 0)& (ch3.get() == 0) & (ch4.get() == 1):

                self.root.destroy()
                Quick_sort = Tk()
                Sorting(Quick_sort,"Quick Sort")
                Quick_sort.mainloop()

            else:  
                messagebox.showerror("Error!", "Please choose exactly 1 type!!")

        self.MainLabel3 = Label(self.root, text='Choose the type of sorting algorithm:', bg="LightSkyBlue1", fg="red",
                               font=("Times new roman", 14,"bold"))
        self.MainLabel3.pack(pady=15)

        ch1=tk.IntVar()  
        check1=tk.Checkbutton(self.root, text="Bubble sort", variable=ch1,font=("Times new roman", 14))  
        check1.deselect()  
        check1.pack(pady=5, expand=YES)  
          
        ch2=tk.IntVar()  
        check2=tk.Checkbutton(self.root, text="Merge sort", variable=ch2,font=("Times new roman", 14))  
        check2.deselect()  
        check2.pack(pady=5, expand=YES)

        ch3=tk.IntVar()  
        check3=tk.Checkbutton(self.root, text="Insertion sort", variable=ch3,font=("Times new roman", 14))  
        check3.deselect()  
        check3.pack(pady=5, expand=YES)

        ch4=tk.IntVar()  
        check2=tk.Checkbutton(self.root, text="Quick sort", variable=ch4,font=("Times new roman", 14))  
        check2.deselect()  
        check2.pack(pady=5, expand=YES)

        button1=Button(self.root, text="Submit",bg="green2", activebackground="lime green",
                                 font=("calibri", 20,"bold"),command=show2).pack(expand=YES)   


        


       


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




