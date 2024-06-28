from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for n in range(randint(8, 10))]
    password_numbers = [choice(numbers) for n in range(randint(2, 4))]
    password_symbols = [choice(symbols) for n in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    #Can be done in more pythonic way: join()
    password = "".join(password_list)

    pw_input.insert(END, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_input.get()
    email_data = email_input.get()
    pw_data = pw_input.get()

    # 실제로 데이터 파일에 저장하기 이전에, 유저에게 확인 메시지 띄우기
    ## 공란인 경우 데이터 저장하지 않고 유저에게 안내하기
    if len(website_data) == 0 or len(email_data) == 0 or len(pw_data) == 0:
        messagebox.showinfo(title="Wait!", message="Please don't leave any fields empty!")

    else:
        ## boolean 변수로 둔다.
        is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered.\n\nEmail: {email_data}\n"
                                                           f"password: {pw_data}\nIs it ok to save?")
        if is_ok:
            # 입력된 데이터를 txt파일에 저장하기
            with open("data.txt", mode="a") as file:
                file.write(f"Website: {website_data} | Email/ID: {email_data} | Password: {pw_data}\n")

            website_input.delete(0, END)
            pw_input.delete(0, END)

        # in case of 'not is_ok:', nothing happens, which means user can go back.

# ---------------------------- UI SETUP ------------------------------- #
## window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

## canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(column=1, row=0)

## label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

## entry
website_input = Entry(width=36)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

email_input = Entry(width=36)
email_input.insert(0, "HelloWorld@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

pw_input = Entry(width=21)
pw_input.grid(column=1, row=3)

## button
generate_label = Button(text="Generate Password", width=11, command=generate)
generate_label.grid(column=2, row=3)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()