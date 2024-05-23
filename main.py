from tkinter import *
from passwordbrain import *
from csv import *

# --------------------------SETUP AND FUNCTIONALITY--------
password_brain = Pb()


# ------Static Functions------------
# Calls the "generate_password" function from the passwordbrain and displays in the entry
def display_generated_password():
    generated_password = password_brain.generate_password()
    password_entry.delete(0, END)
    password_entry.insert(END, generated_password)


# Saves the website, email, and password to a CSV file
def save_password():
    with open('passwords.csv', 'a') as file:
        file.write(f"{website_entry.get()},{email_entry.get()},{password_entry.get()}\n")
    website_entry.delete(0, END)
    password_entry.delete(0,END)
    email_entry.delete(0, END)


# Retrieves credentials from the CSV file based on the website
def retrieve_credentials(website):
    with open('passwords.csv', 'r') as file:
        if website:
            contents = reader(file)
            for row in contents:
                if row[0] == website:
                    return row[1], row[2]


# Takes retrieved credentials and places in the entry boxes
def populate_entry_fields():
    credentials = retrieve_credentials(website_entry.get())
    if credentials is not None:
        email = str(credentials[0])
        password = str(credentials[1])
        email_entry.insert(0, email)
        password_entry.insert(0, password)

    else:
        pass


# Function to hide or show the password
def toggle_password_visibility():
    visibility = password_entry.cget('show')
    if visibility == '*':
        password_entry.config(show='')
        hide_button.config(text="Hide Password")
    if visibility == '':
        password_entry.config(show='*')
        hide_button.config(text="Show Password")


# -------------------------------UI----------------------
# Main window


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas with the logo image
canvas = Canvas(height=200, width=200)
photo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_img)
canvas.grid(row=0, column=1, sticky="nsew")

# Entry boxes, labels, and buttons
website_label = Label(text="Website: ", width=15)
email_label = Label(text="Email/Username: ", width=15)
password_label = Label(text="Password: ", width=15)
website_entry = Entry(width=35)
email_entry = Entry(width=35)
password_entry = Entry(width=21)
generate_button = Button(text="Generate Password", width=15, command=display_generated_password)
add_button = Button(text="Save", width=20, command=save_password)
retrieve_button = Button(text="Find Credentials", width=15, command=populate_entry_fields)
hide_button = Button(text="Hide Password", width=15, command=toggle_password_visibility)


# Organize the UI with a grid
website_label.grid(row=1, column=0, sticky="nsew")
email_label.grid(row=2, column=0, sticky="nsew")
password_label.grid(row=3, column=0, sticky="nsew")
website_entry.grid(row=1, column=1, columnspan=2, sticky="nsew")
email_entry.grid(row=2, column=1, columnspan=2, sticky="nsew")
password_entry.grid(row=3, column=1, sticky="nsew")
generate_button.grid(row=4, column=0, sticky="nsew")
add_button.grid(row=4, column=1)
retrieve_button.grid(row=4, column=2, sticky="nsew")
hide_button.grid(row=3, column=2, sticky="nsew")

# Main event loop
window.mainloop()
