import tkinter as tk
from tkinter import *
import tkinter.messagebox

structure = Tk()
structure.attributes("-fullscreen",True)
structure.title("Currency converter")

Tops = Frame(structure, bg = '#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)

headlabel =Label(font=('Verdana ', 60, 'bold','italic'), text='Currency converter',bg='#e6e5e5', fg='black')
headlabel.place(x=200,y=20)

variable1 = StringVar(structure)
variable2 = StringVar(structure)

variable1.set("currency")
variable2.set("currency")

def RealTimeCurrencyConversion():
	from forex_python.converter import CurrencyRates
	c = CurrencyRates()

	from_currency = variable1.get()
	to_currency = variable2.get()

	if (Amount1_field.get() ==''):
		tk.messagebox.showinfo("Error !", "Amount Not Entered.\n Please a valid amount.")

	elif (from_currency == "currency" or to_currency == "currency"):
		tk.messagebox.showinfo("Error !","Currency Not Selected.\n Please select FROM and TO Currency form menu.")

	else:
		new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
		new_amount = float("{:.4f}".format(new_amt))
		Amount2_field.insert(0, str(new_amount))

def clear_all():
	Amount1_field.delete(0, tk.END)
	Amount2_field.delete(0, tk.END)

CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "EUR"]

structure.configure(background='#e6e5e5')
structure.geometry("700x400")

label1 =Label(structure, font=('lato black', 15, 'bold'), text="\t Amount : ", bg="#e6e5e5", fg="black")
label1.place(x=80,y=200)

label2 =Label(structure, font=('lato black', 15, 'bold'), text="\t From Currency : ", bg="#e6e5e5", fg="black")
label2.place(x=80,y=300)

label3 = Label(structure, font=('lato black', 15, 'bold'), text="\t To Currency : ", bg="#e6e5e5", fg="black")
label3.place(x=80,y=400)

label4 =Label(structure, font=('lato black', 15, 'bold'), text="\t Converted Amount : ", bg="#e6e5e5", fg="black")
label4.place(x=80,y=550)

FromCurrency_option = tk.OptionMenu(structure, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(structure, variable2, *CurrenyCode_list)

FromCurrency_option.place(x=450,y=300)
ToCurrency_option.place(x=450,y=400)

Amount1_field =Entry(structure)
Amount1_field.place(x=400,y=200)

Amount2_field =Entry(structure)
Amount2_field.place(x=500,y=550)

Label_9 = Button(structure, font=('arial', 15, 'bold'), text=" Convert ", padx=2, pady=2, bg="teal", fg="white",command=RealTimeCurrencyConversion)
Label_9.place(x=550,y=450)

Label_9 = Button(structure, font=('arial', 15, 'bold'), text=" Clear All ", padx=2, pady=2, bg="teal", fg="white",command=clear_all)
Label_9.place(x=550,y=600)

Label_10=Button(structure,height=2,width=5,text="EXIT",bg="dark green",fg="yellow",font=("ComicSans",20,"bold"),command=structure.destroy)
Label_10.place(x=830,y=800)

structure.mainloop()