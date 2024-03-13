from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import sys


# ASSETS PATH
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


################### TKINTER GUI ###################
window = Tk()
widht = 990
height = 704
x = (window.winfo_screenwidth()//2) - (widht//2) 
y = (window.winfo_screenheight()//2) - (height//2)
window.geometry(f'{widht}x{height}+{x}+{y}')
window.resizable(False, False)
window.title('BJIR - bézier curve generator')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

page1 = Frame(window)
page2 = Frame(window)

for frame in (page1, page2):
    frame.grid(row=0, column=0, sticky='nsew')

# Munculkan page lain
def show_frame(frame):
    frame.tkraise()

show_frame(page1)


############## PAGE 1: HOME ##############
# Background
page1.configure(bg='#FBFEFE')

# Title
img_path = resource_path("assets/bjirlogo.png")
img_title = PhotoImage(file=img_path)
Label(page1, image=img_title, bg='#FBFEFE').pack(pady=(150, 0))

# Subtitle
subtitle_path = resource_path("assets/bjir.png")
subtitle_img = PhotoImage(file=subtitle_path)
Label(page1, image=subtitle_img, bg='#FBFEFE').pack(pady=(16, 0))

# Try me button
try_path = resource_path("assets/tryme.png")
try_img = PhotoImage(file=try_path)
try_button = Button(page1, image=try_img, bg='#FBFEFE', bd=0, command=lambda: show_frame(page2)).place(relx=0.5, rely=0.63, anchor=CENTER)


############## PAGE 2: TXT INPUT ##############
# def on_entry_click(event):
#     if tawal_input.get() == 'X':
#         tawal_input.delete(0, END)  # Hapus teks saat diklik
#         tawal_input.config(fg='black')  # Ganti warna teks menjadi hitam

# def on_focusout(event):
#     if tawal_input.get() == '':
#         tawal_input.insert(0, 'X')  # Tambahkan teks placeholder kembali
#         tawal_input.config(fg='grey')  # Ganti warna teks menjadi abu-abu
# Background
page2.configure(bg='#FBFEFE')

# Title
title2_path = resource_path("assets/generator.png")
title2_img = PhotoImage(file=title2_path)
Label(page2, image=title2_img, bg='#FBFEFE').place(x=443, y=73)

# Back button
back_path = resource_path("assets/back2.png")
back_img = PhotoImage(file=back_path)
back_button = Button(page2, image=back_img, bg='#FBFEFE', bd=0, command=lambda: show_frame(page1)).place(x=84, y=84)

# Input X
x_input_path = resource_path("assets/x.png")
x_input_img = PhotoImage(file=x_input_path)
Label(page2, image=x_input_img, bg='#FBFEFE').place(x=84, y=170)

# Input Y
y_input_path = resource_path("assets/y.png")
y_input_img = PhotoImage(file=y_input_path)
Label(page2, image=y_input_img, bg='#FBFEFE').place(x=84, y=240)

# Add point button
add_point_path = resource_path("assets/addpoint.png")
add_point_img = PhotoImage(file=add_point_path)
add_point_button = Button(page2, image=add_point_img, bg='#FBFEFE', bd=0).place(x=73, y=297)

# Point container
point_container_path = resource_path("assets/pointcontainer.png")
point_container_img = PhotoImage(file=point_container_path)
Label(page2, image=point_container_img, bg='#FBFEFE').place(x=49, y=361)

# Iteration
iteration_path = resource_path("assets/iteration.png")
iteration_img = PhotoImage(file=iteration_path)
Label(page2, image=iteration_img, bg='#FBFEFE').place(x=84, y=620)

# Generate button
generate_path = resource_path("assets/generate.png")
generate_img = PhotoImage(file=generate_path)
generate_button = Button(page2, image=generate_img, bg='#FBFEFE', bd=0).place(x=400, y=600)


# Container hasil
hasil_path = resource_path("assets/hasil.png")
hasil_img = PhotoImage(file=hasil_path)
Label(page2, image=hasil_img, bg='#FBFEFE').place(x=339, y=162)

# Waktu eksekusi
time_path = resource_path("assets/time.png")
time_img = PhotoImage(file=time_path)
Label(page2, image=time_img, bg='#FBFEFE').place(x=658, y=599)


# END
window.mainloop()