# GUI (Graphical User Interface)
# CLI ( Command Line Interface )
# keyword arguments (def my_function(a,b,c):)
# 
# Advanced Python arguments ()

# arguments (*args) ( unlimited positional arguments )
# keyword arguments (**kwargs)

# Tkinter Layout Managers
# pack, place grid

import tkinter as tk


def button_clicked():
    print("I got clicked")

def main():
    # creating new window 
    window = tk.Tk()
    window.title("My First GUI Program")
    window.minsize(width=500, height=500)

    # creating label (writing text)
    my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
    my_label.grid(column=0, row=0)

    def change_label():
        print("I got clicked")
        my_label["text"] = entry.get()

    # creating button
    button = tk.Button(text="Click Me", command=change_label)
    button.grid(column=1, row=1)

    # Input
    entry = tk.Entry(width=40)
    entry.insert(tk.END, string="Input")
    entry.grid(column=3,row=2)

    new_button = tk.Button(text="New_Button")
    new_button.grid(column=2, row=0)
    

    # keep window running
    window.mainloop()




if __name__ == "__main__":
    main()