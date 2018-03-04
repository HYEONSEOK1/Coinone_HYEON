import balance
import buy
import sell
import hashlib
from tkinter import *
from random import random

class Cont1:
	def __init__(self,win):
		self.buttonframe=Frame(win)
		self.buttonframe.pack(fill=X,anchor=N)
		self.button=Button(self.buttonframe,text="Balance",command=Balance)
		self.button.pack(side=LEFT,padx=10,pady=10)
		
class Cont2:
	def __init__(self,win):
		self.buttonframe=Frame(win)
		self.buttonframe.pack(fill=X,anchor=N)
		self.solin=Entry(self.buttonframe)
		self.solin.pack(side=LEFT,padx=10)
		self.solin1=Entry(self.buttonframe)
		self.solin1.pack(side=LEFT,padx=10)
		self.solin2=Entry(self.buttonframe)
		self.solin2.pack(side=LEFT,padx=10)
		
class Cont3:
	def __init__(self,win):
		self.buttonframe=Frame(win)
		self.buttonframe.pack(fill=X,anchor=N)
		self.button=Button(self.buttonframe,text="Buy",command=Buy)
		self.button.pack(side=LEFT,padx=10,pady=5)
		self.button1=Button(self.buttonframe,text="Sell",command=Sell)
		self.button1.pack(side=LEFT)
class Cont4:
	def __init__(self,win):
		self.win=win
		self.v=StringVar()
		self.buttonframe=Frame(self.win)
		self.buttonframe.pack(fill=X,anchor=N,pady=5)
		self.label=Label(self.buttonframe,bg="yellow",textvariable=self.v,width=70)
		self.label.pack(side=LEFT,padx=5)
		self.v.set("")
	def main_message(self,msg):
		self.v.set(msg)
class Cont5:
	def __init__(self,win):
		self.win=win
		self.buttonframe=Frame(self.win)
		self.buttonframe.pack(side=LEFT,fill=X,anchor=N)
		self.scrollbar=Scrollbar(self.buttonframe)
		self.scrollbar.pack(side=RIGHT,fill=Y)
		self.listbox=Listbox(self.buttonframe,yscrollcommand=self.scrollbar.set,bg="white",width=65,height=20)
		self.listbox.pack(side=LEFT)
		self.scrollbar.config(command=self.listbox.yview)
	def message_dis(self,msg):
		self.listbox.insert(END,msg)

def Balance():
	ace=balance.data		
	for i in ace.keys():
		container5.message_dis(i)
		container5.message_dis(ace[i])
		
def Buy():
	payload=buy.payload
	payload.update({
    'price': container2.solin1.get(),
    'qty': container2.solin2.get(),
    'currency': container2.solin.get()})
	data = buy.get_response('v2/order/limit_buy/', payload)
	container4.main_message(data)		
	
def Sell():
	data=sell.data
	data = sell.get_response('v2/order/limit_sell/', sell.create_payload({
		'price': container2.solin1.get(),
		'qty': container2.solin2.get(),
		'currency': container2.solin.get(),}))
	container4.main_message(data)	
win=Tk()
win.title("trade_coinone")
win.geometry("500x500")
win.resizable(1,1)
label=Label(win,font=3,height=2,text="coinone trade")
label.config(fg='blue',anchor=S)
label.pack()

container1=Cont1(win)
container2=Cont2(win)
container3=Cont3(win)
container4=Cont4(win)
container5=Cont5(win)

win.mainloop()
