# PROJECT ON PASSWORD MANAGER

from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR --------------- #

symbols_list = []

for i in range(33,39):
    symbols_list += chr(i)
    
for i in range(63,65):
    symbols_list += chr(i)

symbols_list.remove(chr(34))


def generate_password():

    password_entry.delete(0,END)

    character = randint(10,12)
    uppercase = randint(2,3)
    numbers = randint(2,3)
    symbols = randint(2,3)
    lowercase = character - (uppercase+symbols+numbers)

    uppercase_password = [chr(randint(65,90)) for i in range(0,uppercase)]

    lowercase_password = [chr(randint(97,122)) for i in range(0,lowercase)]

    numbers_password = [chr(randint(48,57)) for i in range(0,numbers)]

    symbols_password = [symbols_list[randint(0, len(symbols_list)-1)] for i in range(0,symbols)]

    password = uppercase_password + lowercase_password + symbols_password + numbers_password

    shuffle(password)

    password_generated = "".join(password)

    password_entry.insert(0, password_generated)
    pyperclip.copy(password_generated)


# ---------------------------- SAVE PASSWORD ------------------------- #

def save_data():

    website_data = website_entry.get().lower()
    email_data = email_entry.get()
    password_data = password_entry.get()

    new_data = {
        website_data : {
            "Email" : email_data ,
            "Password" : password_data
        }
    }


    if len(website_data)==0 or len(email_data)==0 or len(password_data)==0:
        messagebox.showinfo(title="ERROR!" , message="Do not leave any field empty.")

    else:

        answer = messagebox.askyesno(title=f"{website_data}" , message=f"DETAILS ENTERED :-\n\nEmail/Username : {email_data}\nPassword : {password_data}\n\nSave Data to the file ?")

        # return true if yes is clicked and false if no is clicked


        if answer:
        #     with open("C:/Users/Ayushi Aggarwal/Desktop/MAYANK/PYTHON PROGRAMMING/GRAPHICS/PASSWORD MANAGER/data.txt" , "a") as file:
        #         file.write(f'''Data :-
        # Website : {website_data}
        # Email/Username : {email_data}
        # Password : {password_data}\n\n''')

            try:
                with open("C:/Users/Mayank Aggarwal/Software Development/MAYANK/PYTHON PROGRAMMING/GRAPHICS/PASSWORD MANAGER/data.json" , "r") as file:
                    data = json.load(file)

            except:
                with open("C:/Users/Mayank Aggarwal/Software Development/MAYANK/PYTHON PROGRAMMING/GRAPHICS/PASSWORD MANAGER/data.json" , "w") as file:
                    json.dump(new_data, file , indent=4)

            else:
                data.update(new_data)

                with open("C:/Users/Mayank Aggarwal/Software Development/MAYANK/PYTHON PROGRAMMING/GRAPHICS/PASSWORD MANAGER/data.json" , "w") as file:
                    json.dump(data, file , indent=4)

            finally:
                website_entry.delete(0,END)
                email_entry.delete(0,END)
                password_entry.delete(0,END)


# -------------------- SEARCH DATA --------------------- #


def search_data():

    website_data = website_entry.get().lower()

    try :
        with open("C:/Users/Mayank Aggarwal/Software Development/MAYANK/PYTHON PROGRAMMING/GRAPHICS/PASSWORD MANAGER/data.json" , "r") as file:
            data = json.load(file)

    except : 
        messagebox.showinfo(title="ERROR!" , message="NO DATA FILE FOUND!")

    else:
        if website_data in data.keys():

            email_data = data[website_data]["Email"]
            password_data = data[website_data]["Password"]

            messagebox.showinfo(title=website_data , message=f"DATA FOUND :- \n\n Email : {email_data}\n Password : {password_data}")

        else:
            messagebox.showinfo(title="OOPS!" , message=f"No Details for the {website_data} exists.")
                    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("POMODORO APP")
window.config(padx=70 , pady=50 , bg="cyan")


canvas = Canvas(width=250, height= 250 , bg="cyan" , highlightthickness=0)
logo_img = PhotoImage(file="C:/Users/Mayank Aggarwal/Software Development/MAYANK/PYTHON PROGRAMMING/GRAPHICS/PASSWORD MANAGER/logo.png")
canvas.create_image(125 , 125 , image=logo_img)
canvas.grid(row=1 , column=0 , columnspan=3)

manager_label = Label(text="PASSWORD MANAGER" , font=("Cambria" , 30 , "bold") , fg="blue" , bg="cyan")
manager_label.grid(row=0, column=0,columnspan=3)


website_label = Label(text="Website :" , font=("Calibri" , 17 , "bold") , fg="black" , bg="cyan")
website_label.grid(row=2 , column=0)
website_label.config(padx=10,pady=20)

email_label = Label(text="Email/Username :" , font=("Calibri" , 17 , "bold") , fg="black" , bg="cyan")
email_label.grid(row=3 , column=0)
email_label.config(padx=10,pady=20)

password_label = Label(text="Password :" , font=("Calibri" , 17 , "bold") , fg="black" , bg="cyan")
password_label.grid(row=4 , column=0)
password_label.config(padx=10,pady=20)


website_entry = Entry(width=36 , font=("Arial" , 15), highlightthickness=2 , highlightcolor="blue" , borderwidth=3 , highlightbackground="black")
website_entry.grid(row=2,column=1)


email_entry = Entry(width=60 , font=("Arial" , 15), highlightthickness=2 , highlightcolor="blue" , borderwidth=3 , highlightbackground="black")
email_entry.grid(row=3,column=1 , columnspan=2)

password_entry = Entry(width=36 , font=("Arial" , 15) , highlightthickness=2 , highlightcolor="blue" , borderwidth=3 , highlightbackground="black")
password_entry.grid(row=4,column=1)


generate = Button(text="Generate Password" , font=("Calibri" , 17 , "bold") , bd=5 , width=20 , command=generate_password)
generate.grid(row=4,column=2)

add = Button(text="Add" , font=("Calibri" , 17 , "bold") , bd=5 , width=55 , command=save_data)
add.grid(row=5,column=1,columnspan=2)

search = Button(text="Search" , font=("Calibri" , 17 , "bold") , bd=5 , width=20 , command=search_data)
search.grid(row=2,column=2)




window.mainloop()