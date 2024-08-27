from tkinter import *

root =Tk()
root.geometry("1000x500")
root.title("Shubhu Bill Management System ")
root.resizable(False,False)

def Reset():
  entry_pasta.delete(0,END) 
  entry_noodles.delete(0,END)
  entry_momos.delete(0,END)
  entry_golgappe.delete(0,END)
  entry_chaumin.delete(0,END) 
  entry_samosa.delete(0,END)
  entry_dosa.delete(0,END)
  Total_bill.delete(0,END)
  

def Total():
  try:a1=int(pasta.get())
  except: a1=0

  try:a2=int(noodles.get())
  except: a2=0

  try:a3=int(momos.get())
  except: a3=0

  try:a4=int(golgappe.get())
  except: a4=0

  try:a5=int(chaumin.get())
  except: a5=0

  try:a6=int(samosa.get())
  except:a6=0

  try:a7=int(dosa.get())
  except:a7=0

  #cost of items
  c1=70*a1
  c2=40*a2
  c3=60*a3
  c4=20*a4
  c5=30*a5
  c6=30*a6
  c7=60*a7

  lbl_total=Label(f2,font=('aria',20,'bold'),text='Total',width=18,fg='lightyellow',bg='black')
  lbl_total.place(x=0,y=50)

  entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg='white')
  entry_total.place(x=20,y=100)

  totalcost=c1+c2+c3+c4+c5+c6+c7
  String_bill='Rs.',str('%.2f' %totalcost)
  Total_bill.set(String_bill)



Label(text="Shubhu Bill Management System",bg="green",fg="black",font=("calibri",33,'bold'),width="300",height="2").pack()

#menu
f=Frame(root,bg="white",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="white").place(x=80,y=0)

Label(f,font=("Gentle Calligraphy",15, 'bold'),text="Pasta....Rs.70/Plate",fg="black",bg="white").place(x=10,y=80)
Label(f,font=("Gentle Calligraphy",15, 'bold'),text="Noodles....Rs.40/Plate",fg="black",bg="white").place(x=9,y=110)
Label(f,font=("Gentle Calligraphy",15, 'bold'),text="Momos....Rs.60/Plate",fg="black",bg="white").place(x=10,y=140)
Label(f,font=("Gentle Calligraphy",15, 'bold'),text="Golgappe....Rs.20/Plate",fg="black",bg="white").place(x=10,y=170)
Label(f,font=("Gentle Calligraphy",15, 'bold'),text="Chaumin....Rs.30/Plate",fg="black",bg="white").place(x=10,y=200)
Label(f,font=("Gentle Calligraphy",15, 'bold'),text="Samosa....Rs.30/Plate",fg="black",bg="white").place(x=10,y=230)
Label(f,font=("Gentle Calligraphy",15, 'bold'),text="Dosa....Rs.60/Plate",fg="black",bg="white").place(x=10,y=260)

#bill
f2=Frame(root,bg='white',highlightbackground='black',highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=('calibri',20,'bold'),bg='white')
Bill.place(x=120,y=10)


#Entry Work
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

pasta=StringVar()
noodles=StringVar()
momos=StringVar()
golgappe=StringVar()
samosa=StringVar()
chaumin=StringVar()
dosa=StringVar()
Total_bill=StringVar()

#Label
lbl_pasta=Label(f1,font=("aria",20,"bold"),text="Pasta",width=12,fg="black")
lbl_pasta.grid(row=1,column=0)

lbl_noodles=Label(f1,font=("aria",20,"bold"),text="Noodles",width=12,fg="black")
lbl_noodles.grid(row=2,column=0)

lbl_momos=Label(f1,font=("aria",20,"bold"),text="Momos",width=12,fg="black")
lbl_momos.grid(row=3,column=0)

lbl_golgappe=Label(f1,font=("aria",20,"bold"),text="Golgappe",width=12,fg="black")
lbl_golgappe.grid(row=4,column=0)

lbl_chaumin=Label(f1,font=("aria",20,"bold"),text="Chaumin",width=12,fg="black")
lbl_chaumin.grid(row=5,column=0)

lbl_samosa=Label(f1,font=("aria",20,"bold"),text="Samosa",width=12,fg="black")
lbl_samosa.grid(row=6,column=0)

lbl_dosa=Label(f1,font=("aria",20,"bold"),text="Dosa",width=12,fg="black")
lbl_dosa.grid(row=7,column=0)

#entry
entry_pasta=Entry(f1,font=("Mathematic Elegance",20,'bold'),textvariable=pasta,bd=6,width=8,bg="white")
entry_pasta.grid(row=1,column=1)

entry_noodles=Entry(f1,font=("Mathematic Elegance",20,'bold'),textvariable=noodles,bd=6,width=8,bg="white")
entry_noodles.grid(row=2,column=1)

entry_momos=Entry(f1,font=("Mathematic Elegance",20,'bold'),textvariable=momos,bd=6,width=8,bg="white")
entry_momos.grid(row=3,column=1)

entry_golgappe=Entry(f1,font=("Mathematic Elegance",20,'bold'),textvariable=golgappe,bd=6,width=8,bg="white")
entry_golgappe.grid(row=4,column=1)

entry_chaumin=Entry(f1,font=("Mathematic Elegance",20,'bold'),textvariable=chaumin,bd=6,width=8,bg="white")
entry_chaumin.grid(row=5,column=1)

entry_samosa=Entry(f1,font=("Mathematic Elegance",20,'bold'),textvariable=samosa,bd=6,width=8,bg="white")
entry_samosa.grid(row=6,column=1)

entry_dosa=Entry(f1,font=("Mathematic Elegance",20,'bold'),textvariable=dosa,bd=6,width=8,bg="white")
entry_dosa.grid(row=7,column=1)

#btn

btn_reset=Button(f1,bd=5,fg='black',bg='red',font=('aria',16,'bold'),width=10,text='Reset',command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg='black',bg='green',font=('ariel',16,'bold'),width=10,text='Total',command=Total)
btn_total.grid(row=8,column=1)


root.mainloop()
