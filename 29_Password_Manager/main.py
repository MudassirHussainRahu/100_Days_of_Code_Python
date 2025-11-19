import tkinter as tk
from tkinter import messagebox
import random
import pyperclip


FONT_NAME = "Courier"

def hard():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    num_letters, num_symbols, num_numbers = 4,4,4

    password = []

    characters = [ random.choice(letters) for _ in range(num_letters) ]
    symbols_selected = [ random.choice(symbols) for _ in range(num_symbols) ]
    numbers_selected = [ random.choice(numbers) for _ in range(num_numbers)]

    password.extend(characters)
    password.extend(symbols_selected)
    password.extend(numbers_selected)

    random.shuffle(password)
    password = ''.join(password)
    pyperclip.copy(password)
    password_entry.insert(tk.END, password)    



def save_data():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        print("Invalid Entry")
        messagebox.showinfo(title="Info", message="Please don't leave any fields empty!")
        # operaion.configure(text="Invalid Arguments")
        return
    
    is_okay = messagebox.askokcancel(title=website, message=f"Details entered: \nEmail:{email_username}\nPassword:{password}\nIs it okay to save.")
    if is_okay:
        txt = website + " | " + email_username + " | " +password + '\n'
        with open("data.txt", "a") as file:
            file.write(txt)
            
        operaion.configure(text="Password Added Successfully")
        website_entry.delete(first=0, last=tk.END)
        password_entry.delete(first=0, last=tk.END)


window = tk.Tk()
window.title("Password Manager")
window.configure(padx=50 ,pady=50)
img = tk.PhotoImage(file="logo.png")

canvas = tk.Canvas(height=200, width=200)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)


website_label = tk.Label(text="Website:", font=(FONT_NAME, 10))
website_label.grid(column=0, row=1)

website_entry = tk.Entry(width=60)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()


email_username_label = tk.Label(text="Email/Username:", font=(FONT_NAME, 10))
email_username_label.grid(column=0, row=2)

email_username_entry = tk.Entry(width=60)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(tk.END, string="name@example.com")

password_label = tk.Label(text="Password:", font=(FONT_NAME, 10))
password_label.grid(column=0, row=3)

password_entry = tk.Entry(width=32)
password_entry.grid(column=1, row=3, padx=0)

genreate_password_button = tk.Button(text="Generate Password", font=(FONT_NAME, 10), width=19, command=hard)
genreate_password_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", font=(FONT_NAME, 10), width=45, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, padx=0)

operaion = tk.Label(text="", font=(FONT_NAME, 10))
operaion.grid(column=1, row=5)


window.mainloop()