import tkinter as tk
from tkinter import messagebox
import myMSGenerator
import myMSViewer
import myMSCorrector

def generate_marksheets():
    myMSGenerator.MSMaker()

def correct_marksheets():
    myMSCorrector.CorrectorMS()

def view_marksheets():
    student_name = name_entry.get()
    student_roll_no = roll_entry.get()
    if student_name and student_roll_no:
        myMSViewer.FetchMarkSheet(student_name, student_roll_no)
    else:
        messagebox.showwarning("Warning", "Please enter student's name and roll number.")

def on_close():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Marksheet Generator and Corrector")

menu_frame = tk.Frame(root)
menu_frame.pack(padx=20, pady=20)

generate_button = tk.Button(menu_frame, text="Generate Marksheets", command=generate_marksheets)
generate_button.grid(row=0, column=0, padx=10, pady=10)

correct_button = tk.Button(menu_frame, text="Correct Marksheets", command=correct_marksheets)
correct_button.grid(row=0, column=1, padx=10, pady=10)

view_button = tk.Button(menu_frame, text="View Marksheets", command=view_marksheets)
view_button.grid(row=0, column=2, padx=10, pady=10)

view_frame = tk.Frame(root)
view_frame.pack(padx=20, pady=20)

name_label = tk.Label(view_frame, text="Enter Student's Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(view_frame)
name_entry.grid(row=0, column=1, padx=10, pady=10)

roll_label = tk.Label(view_frame, text="Enter Student's Roll No:")
roll_label.grid(row=1, column=0, padx=10, pady=10)
roll_entry = tk.Entry(view_frame)
roll_entry.grid(row=1, column=1, padx=10, pady=10)

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
