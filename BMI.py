from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("BMI Calculator")
root.geometry("700x600")
root.config(bg="#346ab3")
header = Label(root, text='IDEAL BODY MASS INDEX CALCULATOR', bg='#9ccb3b', fg='black')
header.place(x=220, y=20)
# Frame
frame = Frame(root, width=500, height=200, relief='raised', bg='#9ccb3b')
frame.place(relx=0.15, rely=0.1)

# Weight label
weight = Label(frame, text="Weight(kg):", bg='#9ccb3b', fg='black')
weight.place(relx=0.1, rely=0.1)
weight_entry = Entry(frame)
weight_entry.place(relx=0.4, rely=0.1)

# Height Label
height = Label(frame, text="Height(cm):", bg='#9ccb3b', fg='black')
height.place(relx=0.1, rely=0.3)
height_entry = Entry(frame)
height_entry.place(relx=0.4, rely=0.3)

# Gender Label
gender = Label(frame, text="Gender:", bg='#9ccb3b', fg='black')
gender.place(rely=0.53, relx=0.1)

# Age Label
age = Label(frame, text="Age:", bg='#9ccb3b', fg='black')
age.place(rely=0.8, relx=0.1)
age_entry = Entry(frame, state='readonly')
age_entry.place(rely=0.8, relx=0.4)
# Selecting either male or female
options = ['Select...', 'Male', "Female"]
variable = StringVar(frame)
variable.set(options[0])


# Defining Functions
def activate(value):
    variable.set(value)
    if value != "Select...":
        age_entry.config(state='normal')
    else:
        age_entry.config(state='readonly')


gender_menu = OptionMenu(frame, variable, *options, command=activate)
gender_menu.place(relx=0.4, rely=0.5)


# Defining Calculation formula
def bmi_calc():
    global result_bmi
    try:
        float(weight_entry.get())
        float(height_entry.get())
        float(age_entry.get())
        if variable.get() == "Select...":
            raise ValueError
        elif variable.get() == "Male":
            result = ((0.5 * float(weight_entry.get())) / ((float(height_entry.get()) / 100) ** 2)) + 11.5
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(weight_entry.get()) / ((float(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
        elif variable.get() == "Female":
            result = ((0.5 * float(weight_entry.get())) / ((float(height_entry.get()) / 100) ** 2)) + (
                    0.03 * float(age_entry.get())) + 11
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(weight_entry.get()) / ((float(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
        if result_bmi < 18.5:
            category.config(text='Underweight')
        elif 18.5 <= result_bmi < 25:
            category.config(text='Normal weight')
        elif 25 <= result_bmi < 30:
            category.config(text='Overweight')
        elif result_bmi >= 30:
            category.config(text='Obese')
    # Error if no value was entered
    except ValueError:
        messagebox.showerror(title=None, message='Gender was not specified or invalid entry was given')
        delete()


# Calculation Button
calculate = Button(root, text="Calculate your Ideal Body Mass Index", width=50, command=bmi_calc)
calculate.place(rely=0.45, relx=0.2)

bmi = Label(root, text="BMI:", bg='#9ccb3b', fg="black")
bmi.place(rely=0.55, relx=0.1)
bmi_field = Entry(root, state='readonly')
bmi_field.place(rely=0.55, relx=0.2)
ideal_bmi = Label(root, text='Ideal BMI:', bg='#9ccb3b', fg="black")
ideal_bmi.place(rely=0.55, relx=0.5)
ideal_field = Entry(root, state='readonly')
ideal_field.place(rely=0.55, relx=0.65)


# Delete Function
def delete():
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    age_entry.config(state='normal')
    bmi_field.config(state='normal')
    ideal_field.config(state='normal')
    age_entry.delete(0, END)
    bmi_field.delete(0, END)
    ideal_field.delete(0, END)
    age_entry.config(state='readonly')
    bmi_field.config(state='readonly')
    ideal_field.config(state='readonly')
    weight_entry.focus()
    variable.set(options[0])


# Stating which category BMI falls into (underweight, normal, overweight, obese)
category_head = Label(root, text="Category:", bg='#9ccb3b', fg='black')
category = Label(root, width=20, bg='#9ccb3b', fg='black')
category.place(relx=0.38, rely=0.72)
category_head.place(relx=0.45, rely=0.67)
clear = Button(root, text='Clear', command=delete)
clear.place(rely=0.85, relx=0.1)
quit = Button(root, text='Exit', command='exit')
quit.place(rely=0.85, relx=0.83)
root.mainloop()
