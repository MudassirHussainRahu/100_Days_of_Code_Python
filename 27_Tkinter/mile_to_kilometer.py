import tkinter as tk

window = tk.Tk()
window.minsize(width=400, height=400)
window.title("Mile to Kilometer Converter")


label = tk.Label(text="Miles", font=("Arial", 12))
label.grid(column=2, row=0)

miles = tk.Entry(width=20)
miles.insert(tk.END, "0")
miles.grid(column=1, row=0)

is_equal_to = tk.Label(text="is equal to", font=("Arial", 12))
is_equal_to.grid(column=0, row=1)


kilometer = tk.Label(text="0", font=("Arial", 12))
kilometer.grid(column=1, row=1)

km_label = tk.Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)
def convert_used():
    miles_entry = miles.get()
    try:
        m = float(miles_entry)
        k = m*1.6
        kilometer.configure(text=f"{k}")
    except:
        kilometer.configure(text=f"Invalid Input")

convert = tk.Button(text="Convert", command=convert_used)
convert.grid(column=1, row=2)





window.mainloop()


