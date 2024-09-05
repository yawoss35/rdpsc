import os
import subprocess
import tkinter as tk
from tkinter import messagebox

def connect_rdp():
    host = entry_host.get()
    user = entry_user.get()
    password = entry_password.get()

    if not host or not user or not password:
        messagebox.showwarning("Eksik Bilgi", "Lütfen tüm bilgileri doldurun!")
        return

    
    os.system(f"cmdkey /add:{host} /user:{user} /pass:{password}")

    
    subprocess.run(f"mstsc /v:{host}", shell=True)

    
    os.system(f"cmdkey /delete:{host}")


root = tk.Tk()
root.title("RDP Bağlantısı")


root.geometry("300x200")


label_host = tk.Label(root, text="Host:")
label_host.pack(pady=5)
entry_host = tk.Entry(root)
entry_host.pack(pady=5)


label_user = tk.Label(root, text="Kullanıcı Adı:")
label_user.pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack(pady=5)


label_password = tk.Label(root, text="Şifre:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)


button_connect = tk.Button(root, text="Bağlan", command=connect_rdp)
button_connect.pack(pady=10)


root.mainloop()

#bu kod windowsta çalışır