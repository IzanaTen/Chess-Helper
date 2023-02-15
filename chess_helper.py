import tkinter as tk
import requests
from bs4 import BeautifulSoup
import os
import time
import threading

root = tk.Tk()
root["bg"] = "gray"
root.geometry("500x550")
root.attributes("-topmost", True)
root.resizable(False, False)

chessboard = tk.Frame(root, bg="green", width=800, height=800)
chessboard.pack(side="top")

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            color = "white"
        else:
            color = "black"
        square = tk.Frame(chessboard, bg=color, width=63, height=63)
        square.grid(row=i, column=j)
        square.square_name = letters[j] + str(8 - i)

text_input = tk.Text(root, height=20, width=20)
text_input.pack(side="left", pady=6)

def fetch_data():
    link = text_input.get("1.0", "end").strip()
    while True:
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        pieces = soup.find_all("div", class_="piece")
        for piece in pieces:
            print(piece["class"], piece["style"])
        time.sleep(5)  # opóźnienie w sekundach

def on_submit():
    thread = threading.Thread(target=fetch_data)
    thread.start()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(side="left", padx=20)

root.mainloop()
