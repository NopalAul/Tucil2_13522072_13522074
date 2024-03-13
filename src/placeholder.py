import tkinter as tk

def on_entry_click(event):
    if entry.get() == 'Masukkan teks di sini...':
        entry.delete(0, tk.END)  # Hapus teks saat diklik
        entry.config(fg='black')  # Ganti warna teks menjadi hitam

def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Masukkan teks di sini...')  # Tambahkan teks placeholder kembali
        entry.config(fg='grey')  # Ganti warna teks menjadi abu-abu

root = tk.Tk()
root.title("Entry Placeholder")

# Fungsi untuk mengeksekusi perintah saat tombol Enter ditekan
def on_enter(event):
    print(entry.get())

# Membuat Entry widget
entry = tk.Entry(root, width=30, fg='grey')
entry.insert(0, 'Masukkan teks di sini...')
entry.bind('<FocusIn>', on_entry_click)  # Event binding saat entry ditekan
entry.bind('<FocusOut>', on_focusout)    # Event binding saat entry kehilangan fokus
entry.bind('<Return>', on_enter)         # Event binding saat tombol Enter ditekan
entry.pack(pady=10)

root.mainloop()
