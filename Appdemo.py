import tkinter as tk
from tkinter import messagebox

def submit_info():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    phone_number = entry_phone_number.get()
    student_id = entry_student_id.get()

    message = f"First Name: {first_name}\nLast Name: {last_name}\nPhone Number: {phone_number}\nStudent ID: {student_id}"
    messagebox.showinfo("Submitted Information", message)

root = tk.Tk()
root.title("Computer Club Inquiry Form")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_first_name = tk.Label(frame, text="First Name:")
label_first_name.grid(row=0, column=0, padx=(0, 10))
entry_first_name = tk.Entry(frame)
entry_first_name.grid(row=0, column=1)

label_last_name = tk.Label(frame, text="Last Name:")
label_last_name.grid(row=1, column=0, padx=(0, 10))
entry_last_name = tk.Entry(frame)
entry_last_name.grid(row=1, column=1)

label_phone_number = tk.Label(frame, text="Phone Number:")
label_phone_number.grid(row=2, column=0, padx=(0, 10))
entry_phone_number = tk.Entry(frame)
entry_phone_number.grid(row=2, column=1)

label_student_id = tk.Label(frame, text="Student ID:")
label_student_id.grid(row=3, column=0, padx=(0, 10))
entry_student_id = tk.Entry(frame)
entry_student_id.grid(row=3, column=1)

button_submit_info = tk.Button(frame, text="Submit Info", command=submit_info)
button_submit_info.grid(row=4, columnspan=2, pady=(10, 0))

root.mainloop()