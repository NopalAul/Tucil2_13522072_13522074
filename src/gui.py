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

# Quadratic
quadratic_path = resource_path("assets/quadratic.png")
quadratic_img = PhotoImage(file=quadratic_path)
quadratic_button = Button(page1, image=quadratic_img, bg='#FBFEFE', bd=0, command=lambda: show_frame(page2)).place(relx=0.5, rely=0.63, anchor=CENTER)


############## PAGE 2: TXT INPUT ##############
def on_entry_click(event):
    if tawal_input.get() == 'X':
        tawal_input.delete(0, END)  # Hapus teks saat diklik
        tawal_input.config(fg='black')  # Ganti warna teks menjadi hitam

def on_focusout(event):
    if tawal_input.get() == '':
        tawal_input.insert(0, 'X')  # Tambahkan teks placeholder kembali
        tawal_input.config(fg='grey')  # Ganti warna teks menjadi abu-abu
# Background
page2.configure(bg='#FBFEFE')

# Title
title2_path = resource_path("assets/3titik.png")
title2_img = PhotoImage(file=title2_path)
Label(page2, image=title2_img, bg='#FBFEFE').pack(pady=(61, 0))

# Titik awal
tawal_path = resource_path("assets/tawal.png")
tawal_img = PhotoImage(file=tawal_path)
Label(page2, image=tawal_img, bg='#FBFEFE').place(x=60.8, y=171)
tawal_input = Entry(page2, width=2, border=0, font=('Arial', 14))
tawal_input.insert(0, 'X')
tawal_input.bind('<FocusIn>', on_entry_click)  # Event binding saat entry ditekan
tawal_input.bind('<FocusOut>', on_focusout)    # Event binding saat entry kehilangan fokus
tawal_input.place(x=199, y=181)

# Titik kontrol
tkontrol_path = resource_path("assets/tkontrol.png")
tkontrol_img = PhotoImage(file=tkontrol_path)
Label(page2, image=tkontrol_img, bg='#FBFEFE').place(x=60.8, y=240)

# Titik akhir
takhir_path = resource_path("assets/takhir.png")
takhir_img = PhotoImage(file=takhir_path)
Label(page2, image=takhir_img, bg='#FBFEFE').place(x=60.8, y=309)

# Generate button
generate_path = resource_path("assets/generate.png")
generate_img = PhotoImage(file=generate_path)
generate_button = Button(page2, image=generate_img, bg='#FBFEFE', bd=0).place(x=81.81, y=460)

# Back button
back_path = resource_path("assets/back.png")
back_img = PhotoImage(file=back_path)
back_button = Button(page2, image=back_img, bg='#FBFEFE', bd=0, command=lambda: show_frame(page1)).place(x=81.81, y=523)


# Container hasil
hasil_path = resource_path("assets/hasil.png")
hasil_img = PhotoImage(file=hasil_path)
Label(page2, image=hasil_img, bg='#FBFEFE').place(x=339, y=162)

# Waktu eksekusi
time_path = resource_path("assets/time.png")
time_img = PhotoImage(file=time_path)
Label(page2, image=time_img, bg='#FBFEFE').place(x=523, y=595)


# END
window.mainloop()