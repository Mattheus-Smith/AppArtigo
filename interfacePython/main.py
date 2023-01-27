import tkinter as tk
from tkinter import ttk

tela = tk.Tk()
tela.title('MiniMapa dos Jogadores')
tela.geometry('800x600')
tela.resizable(False, False)

# configure the grid
tela.columnconfigure(0, weight=1)
tela.columnconfigure(1, weight=3)

# username
username_label = ttk.Label(tela, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(tela)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# password
password_label = ttk.Label(tela, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(tela,  show="*")
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# login button
login_button = ttk.Button(tela, text="Login")
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

tela.mainloop()