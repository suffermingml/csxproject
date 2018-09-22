#!/usr/bin/python3
from math import *
from scipy.optimize import fsolve, root
from tkinter import *

fields = 'D1', 'D2', 'C1', 'C2','t1', 't2', 't3'


def makeform(root1, fields):
   entries = []
   for field in fields:
      row = Frame(root1)
      lab = Label(row, width=6, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

def fetch(entries,fu):
   ent2.delete(1.0,END)
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text)) 
   d1=float(entries[0][1].get())
   d2=float(entries[1][1].get())
   c1=float(entries[2][1].get())
   c2=float(entries[3][1].get())
   t1=float(entries[4][1].get())
   t2=float(entries[5][1].get())
   t3=float(entries[6][1].get())
   
   def func(i):
      x=i[0]
      return c1*exp(-x*t2)+(d2*c1/(d1*exp(-x*t1)))*exp(-x*t3)-c2

   def f(ii):
      q=float(ii)
      return c1*exp(-ii*t2)+(d2*c1/(d1*exp(-ii*t1)))*exp(-ii*t3)-c2
   # def f(i):
   # #    ii=i.tolist()
   #    return c1*exp(-ii*t2)+(d2*c1/(d1*exp(-ii*t1)))*exp(-ii*t3)-c2
   fu=fsolve(func,[1])
   Vd=d1*exp(-fu*t1)/c1
   print('Ans:  k: "%f",Vd:"%f",(error:"%f")' % (fu,Vd,f(fu)))
   ent2.insert(END, 'Ans:  k: "%f",Vd:"%f",(error:"%f")' % (fu,Vd,f(fu)))

if __name__ == '__main__':
   root1 = Tk()
   root1.title('1276-biogroup')
   root1.geometry('520x350')
   ents = makeform(root1, fields)
   d1=ents[0][1].get()
   d2=ents[1][1].get()
   c1=ents[2][1].get()
   c2=ents[3][1].get()
   t1=ents[4][1].get()
   t2=ents[5][1].get()
   t3=ents[6][1].get()
   fu=[]


   quote='Ans:'
   ent2 = Text(root1,height=1)
   ans=[]
   ent2.insert(END, quote)
   root1.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root1, text='Show',
          command=(lambda e=ents: fetch(e,fu)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root1, text='Quit', command=root1.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   ent2.pack(side=RIGHT, expand=YES, fill=X)
   l = Label(root1, 
    text='created by sufferming',    
    font=('Arial', 12),    
    width=17, height=2  
    ).place(x=370, y=320, anchor='nw')
   root1.mainloop()