from tkinter import*

def add():

	name = name_input.get()
	phone = phone_input.get()
	email = email_input.get()

	f = open("output.txt", "a")
	f.writelines('Name: ' + name + '\n' + 'Phone: ' + phone + '\n' + 'Email: ' + email + '\n\n\n')
	f.close()

root = Tk()
root.title("PhoneBook")

label1 = Label(text = "Contacts List")
label1.grid(row = 0, columnspan = 2, sticky = W, pady = 5, padx = 5)

label2 = Label(text="Name:")
label2.grid(row = 1, column = 0)
name = StringVar()
name_input = Entry(textvariable = name)
name_input.grid(row = 1, column = 1, padx = 5)

label3 = Label(text = "Phone:")
label3.grid(row = 2, column = 0)
telephone = StringVar()
phone_input = Entry(textvariable = telephone)
phone_input.grid(row = 2, column = 1)

label4 = Label(text = "Email:")
label4.grid(row = 3, column = 0)
email = StringVar()
email_input = Entry(textvariable = email)
email_input.grid(row = 3, column = 1)

button1 = Button(text = "Add to list", command = add)
button1.grid(row = 4, columnspan = 2, sticky = E, pady = 5, padx = 5)

root.mainloop()
