from tkinter import *

window = Tk()

def ScalePrinter(text):
    print(text)

Scale(window,
      label='sss',        # Lable
      from_=0,            # Minimize Value
      to=100,             # Maximize Value
      resolution=1,       # Step
      orient=HORIZONTAL,  # Direction
      command=ScalePrinter
      ).pack()

window.mainloop()
