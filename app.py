import requests
import tkinter as tk
from datetime import datetime

from sklearn.semi_supervised import LabelPropagation

def trackBitcoin():
    url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR'
    response = requests.get(url).json()
    price = response['USD']
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text = str(price) + '$')
    labelTime.config(text = 'Updated at' +' '+time)

    root.after(1000, trackBitcoin)


root = tk.Tk()
root.title('Bitcoin Tracker')
root.geometry('400x500')

f1 =("poppins", 24, "bold")
f2 =("poppins", 22, "bold")
f3 =("poppins", 18, "normal")

label = tk.Label(root, text='Bitcoin Price', font=f1)
label.pack(pady=30) 

labelPrice = tk.Label(root, font=f2)
labelPrice.pack(pady=20)

labelTime = tk.Label(root, font=f3)
labelTime.pack(pady=20)

trackBitcoin()


root.mainloop()
