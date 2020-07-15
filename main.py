from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from urllib import request, response
import json


try:
    html = request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js')
    data = html.read()
    JSON_object = json.loads(data)
except:
    messagebox.showerror('Error', 'Bad or no interner conncection.')


# Convert function
def convert():
    enrt_azn.delete(0, END)
    enrt_eur.delete(0, END)
    enrt_usd.delete(0, END)
    enrt_gbp.delete(0, END)
    try:
        RUB = float(entry_RUB.get())
        enrt_azn.insert(
            0, round(RUB / float(JSON_object['Valute']['AZN']['Value']), 2))
        enrt_eur.insert(
            0, round(RUB / float(JSON_object['Valute']['EUR']['Value']), 2))
        enrt_usd.insert(
            0, round(RUB / float(JSON_object['Valute']['USD']['Value']), 2))
        enrt_gbp.insert(
            0, round(RUB / float(JSON_object['Valute']['GBP']['Value']), 2))
    except:
        messagebox.showwarning(
            'Error', 'Shouldn\'t be string!\nUse dot for float numbers!')


# Starting amount
START_AMOUNT = 1000

root = Tk()
root.title('Currency Converter')
root.iconbitmap('logo.ico')
root.geometry('370x320+600+200')
root.resizable(0, 0)

# Header Frame
header_frame = Frame(root)
header_frame.pack(fill=X)
header_frame.grid_columnconfigure(0, weigh=1)
header_frame.grid_columnconfigure(1, weigh=1)

# Header style
head_currency = Label(header_frame, text='Currency',
                      bg='#ccc', font='Arial 12 bold')
head_currency.grid(row=0, column=0, sticky=EW)
head_buy = Label(header_frame, text='RUB', bg='#ccc', font='Arial 12 bold')
head_buy.grid(row=0, column=1, sticky=EW)

# AZN Currency
azn_currency = Label(header_frame, text='AZN', font='Arial 10')
azn_currency.grid(row=1, column=0, sticky=EW)
azn_buy = Label(header_frame, text=JSON_object['Valute'][
                'AZN']['Value'], font='Arial 10')
azn_buy.grid(row=1, column=1, sticky=EW)

# USD Currency
usd_currency = Label(header_frame, bg='#ccc', text='USD', font='Arial 10')
usd_currency.grid(row=2, column=0, sticky=EW)
usd_buy = Label(header_frame, bg='#ccc', text=JSON_object[
                'Valute']['USD']['Value'], font='Arial 10')
usd_buy.grid(row=2, column=1, sticky=EW)

# EUR Currency
euro_currency = Label(header_frame, text='EUR', font='Arial 10')
euro_currency.grid(row=3, column=0, sticky=EW)
euro_buy = Label(header_frame, text=JSON_object['Valute'][
                 'EUR']['Value'], font='Arial 10')
euro_buy.grid(row=3, column=1, sticky=EW)

# GBP Currency
gbp_currency = Label(header_frame, bg='#ccc', text='GBP', font='Arial 10')
gbp_currency.grid(row=4, column=0, sticky=EW)
gbp_buy = Label(header_frame, bg='#ccc', text=JSON_object[
                'Valute']['GBP']['Value'], font='Arial 10')
gbp_buy.grid(row=4, column=1, sticky=EW)

# Convert Frame
conv_frame = Frame(root)
conv_frame.pack(fill=BOTH, expand=1)
conv_frame.grid_columnconfigure(1, weight=1)

# RUB
lab_RUB = Label(conv_frame, text='RUB', bg='#fff', font='Arial 10 bold')
lab_RUB.grid(row=0, column=0, padx=10, pady=10)
entry_RUB = ttk.Entry(conv_frame, justify=CENTER, font='Arial 10 bold')
entry_RUB.grid(row=0, column=1, columnspan=2, pady=10, padx=10, sticky=EW)
entry_RUB.insert(0, START_AMOUNT)

# Exchange button
conv_button = ttk.Button(conv_frame, text='Convert', command=convert)
conv_button.grid(row=1, column=1, columnspan=2, padx=10, sticky=EW)

# Result Frame
result_frame = Frame(root)
result_frame.pack(expand=1, fill=BOTH, pady=5)
result_frame.grid_columnconfigure(1, weight=1)

# AZN
res_azn = Label(result_frame, text='AZN:', font='Arial 10')
res_azn.grid(row=2, column=0, padx=9)
enrt_azn = ttk.Entry(result_frame, justify=CENTER, font='Arial 10')
enrt_azn.grid(row=2, column=1, columnspan=2, padx=10, pady=3, sticky=EW)
enrt_azn.insert(
    0, round(START_AMOUNT / float(JSON_object['Valute']['AZN']['Value']), 2))

# USD
res_usd = Label(result_frame, text='USD:', font='Arial 10')
res_usd.grid(row=3, column=0)
enrt_usd = ttk.Entry(result_frame, justify=CENTER, font='Arial 10')
enrt_usd.grid(row=3, column=1, columnspan=2, padx=10, pady=3, sticky=EW)
enrt_usd.insert(
    0, round(START_AMOUNT / float(JSON_object['Valute']['USD']['Value']), 2))

# EUR
res_eur = Label(result_frame, text='EUR:', font='Arial 10')
res_eur.grid(row=4, column=0)
enrt_eur = ttk.Entry(result_frame, justify=CENTER, font='Arial 10')
enrt_eur.grid(row=4, column=1, columnspan=2, padx=10, pady=3, sticky=EW)
enrt_eur.insert(
    0, round(START_AMOUNT / float(JSON_object['Valute']['EUR']['Value']), 2))

# GBR
res_gbp = Label(result_frame, text='GBR:', font='Arial 10')
res_gbp.grid(row=5, column=0)
enrt_gbp = ttk.Entry(result_frame, justify=CENTER, font='Arial 10')
enrt_gbp.grid(row=5, column=1, columnspan=2, padx=10, pady=3, sticky=EW)
enrt_gbp.insert(
    0, round(START_AMOUNT / float(JSON_object['Valute']['GBP']['Value']), 2))

root.mainloop()
