import tkinter as tk
# *args ( unlimited positional arguments )
def add(*args):
    total = 0
    for n in args:
        total += n

    return total


# **kwargs ( unlimited key-word arguments )

def calculate(n, **kwargs):
    print(kwargs)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")



def main():
    print("playground.py")
    print(add(1,2,3,4,6))

    # calculate(add=3, multiply=5)

    my_car = Car(make="Toyota")

    print(my_car.make)

    # Text box
    text = tk.Text(height=10, width=30)
    text.focus()
    text.insert(tk.END,"Example of multi-line text.")
    text.get("1.0", tk.END)
    text.pack()


    # spinbox 
    def spinbox_used():
        print(spinbox.get())
    spinbox = tk.Spinbox(from_=0, to=100, width=5, command=spinbox_used)
    spinbox.pack()

    # scale
    def scale_used(value):
        print(value)
    scale = tk.Scale(from_=0, to=50, command=scale_used)
    scale.pack()

    # check button
    def checkbutton_used():
        print(checked_state.get())

    checked_state = tk.IntVar()
    chekbuton = tk.Checkbutton(text="Is It On", variable=checked_state, command=checkbutton_used)
    checked_state.get()
    chekbuton.pack()
    
    # RadioButton
    def radio_used():
        print(radio_state.get())

    radio_state = tk.IntVar()
    radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
    radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
    radiobutton3 = tk.Radiobutton(text="Option3", value=3, variable=radio_state, command=radio_used)
    radiobutton1.pack()
    radiobutton2.pack()
    radiobutton3.pack()


    # listbox
    def listbox_used(event):
        print(listbox.get(listbox.curselection()))

    listbox = tk.Listbox(height=4)
    fruits = [
        "Apple", "Pear", "Orange", "Banana"
    ]
    for item in fruits:
        listbox.insert(fruits.index(item), item)
    listbox.bind("<<ListboxSelect>>", listbox_used)
    listbox.pack()


if __name__ == "__main__":
    main()