from tkinter import *
from tkinter.ttk import *
from decimal import *
getcontext().prec = 5
 
window = Tk()
window.title("Ideal Gas Accumulator Calcs")
window.geometry('800x600')
 
lbl0 = Label(window, text="Standard Conditions:")
lbl0.grid(column=0, row=0)
                
chk_state1 = BooleanVar()
chk_state1.set(True) #set check state 
def activatecheck1():
    if chk_state1.get() == True:          #whenever checked
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt1.insert(0, '14.7')
        txt2.insert(0, '60')
        txt1.config(state=DISABLED)
        txt2.config(state=DISABLED)
    elif chk_state1.get() == False:        #whenever unchecked
        txt1.config(state=NORMAL)
        txt2.config(state=NORMAL)
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt1.focus()
chk1 = Checkbutton(window, var=chk_state1, command = activatecheck1)
chk1.grid(column=1, row=0)

lbl00 = Label(window, text="Use default values:")
lbl00.grid(column=3, row=0)

chk_state2 = BooleanVar()
chk_state2.set(True) #set check state 
def activatecheck2():
    if chk_state2.get() == True:          #whenever checked
        txt3.delete(0, END)
        txt2_1.delete(0, END)
        txt6.delete(0, END)
        txt3.insert(0, '1000')
        txt2_1.insert(0, '3000')
        txt6.insert(0, '1200')
        txt3.config(state=DISABLED)
        txt2_1.config(state=DISABLED)
        txt6.config(state=DISABLED)
    elif chk_state2.get() == False:        #whenever unchecked
        txt3.config(state=NORMAL)
        txt2_1.config(state=NORMAL)
        txt6.config(state=NORMAL)
        txt3.delete(0, END)
        txt2_1.delete(0, END)
        txt6.delete(0, END)
        txt3.focus()
chk2 = Checkbutton(window, var=chk_state2, command = activatecheck2)
chk2.grid(column=4, row=0)
    

lbl1 = Label(window, text="stdpres")
lbl1.grid(column=0, row=1)
txt1 = Entry(window,width=10)
txt1.grid(column=1, row=1)
if chk_state1.get() == True:
    txt1.insert(0, '14.7')
    txt1.config(state=DISABLED)
    
lbl2 = Label(window, text="stdtemp")
lbl2.grid(column=0, row=2)
txt2 = Entry(window,width=10)
txt2.grid(column=1, row=2)
if chk_state1.get() == True:
    txt2.insert(0, '60')
    txt2.config(state=DISABLED)

lbl3 = Label(window, text="Precharge")
lbl3.grid(column=0, row=4)
txt3 = Entry(window,width=10)
txt3.grid(column=1, row=4)
if chk_state2.get() == True:
    txt3.insert(0, '1000')
    txt3.config(state=DISABLED)

lbl4 = Label(window, text="# Bottles")
lbl4.grid(column=0, row=5)
txt4 = Entry(window,width=10)
txt4.grid(column=1, row=5)

lbl5 = Label(window, text="Bottle Size")
lbl5.grid(column=0, row=6)
lbl5_1 = Label(window, text="11")
lbl5_1.grid(column=1, row=7)
lbl6_1 = Label(window, text="15")
lbl6_1.grid(column=2, row=7)
chk_state3 = BooleanVar()
chk_state3.set(False) #set check state 
def activatecheck3():
    if chk_state3.get() == True:          #whenever checked
        chk_state4.set(False)
        txt7.delete(0, END)
        txt7.insert(0, "9.9")
    elif chk_state3.get() == False:        #whenever unchecked
#     chk_state4.set(True)
        txt7.delete(0, END)
#        txt7.insert(0, "13.7")
chk3 = Checkbutton(window, var=chk_state3, command = activatecheck3)
chk3.grid(column=1, row=6)
chk_state4 = BooleanVar()
chk_state4.set(False) #set check state 
def activatecheck4():
    if chk_state4.get() == True:          #whenever checked
        chk_state3.set(False)
        txt7.delete(0, END)
        txt7.insert(0, "13.7")
    elif chk_state4.get() == False:        #whenever unchecked
#        chk_state3.set(True)
        txt7.delete(0, END)
#        txt7.insert(0, "9.9")
chk4 = Checkbutton(window, var=chk_state4, command = activatecheck4)
chk4.grid(column=2, row=6)
#txt5.grid(column=1, row=6)


lbl6 = Label(window, text="MOP")
lbl6.grid(column=3, row=4)
txt6 = Entry(window,width=10)
txt6.grid(column=4, row=4)
if chk_state2.get() == True:
    txt6.insert(0, '1200')
    txt6.config(state=DISABLED)

lbl2_1 = Label(window, text="Sys Pres")
lbl2_1.grid(column=3, row=5)
txt2_1 = Entry(window,width=10)
txt2_1.grid(column=4, row=5)
if chk_state2.get() == True:
    txt2_1.insert(0, '3000')
    txt2_1.config(state=DISABLED)
 
lbl7 = Label(window, text="Gas Vol")
lbl7.grid(column=3, row=6)
txt7 = Entry(window,width=10)
txt7.grid(column=4, row=6)

window.grid_rowconfigure(8, minsize=20)
window.grid_rowconfigure(9, minsize=20)


def clicked():
    if txt1.get() == "":
        psia = 0
    else:
        psia = txt1.get()
    if txt3.get() == "":
        precharge = 1000
    else:
        precharge = txt3.get()
    if txt2_1.get() == "":
        syspres = 3000
    else:
        syspres = txt2_1.get()
    if txt6.get() == "":
        MOP = float(precharge) + 200
    else:
        MOP = txt6.get()
    
    p0=float(precharge)+float(psia)
    p1=float(syspres)+float(psia)
    p2=float(MOP)+float(psia)

    
    updatevols(p0,p1,p2)  
        
    lbl9.configure(text = p0)
    lbl11.configure(text = p1)
    lbl13.configure(text = p2)

window.grid_rowconfigure(14, minsize=40)
btn = Button(window, text="Run Calcs", command=clicked)
btn.grid(column=2, row=15)
 
def updatevols(p0,p1,p2):

    e1 = p0/p1
    e2 = p0/p2
    
    if txt4.get() == "":
        numbot = 0
    else:
        numbot = txt4.get()
    if txt7.get() == "":
        botsize = 0
    else:
        botsize = txt7.get()
#        if chk_state3.get() == False and chk_state4.get() == False:
#           botsize = 0
#        else:
#           botsize = txt7.get()
        
    
    g0 = float(numbot) * float(botsize)
    g1 = g0*e1
    g2 = g0*e2
  
    
    g0=round(g0,2)
    g1=round(g1,2)
    g2=round(g2,2)

    l0=g0-g0
    l1=g0-g1
    l2=g0-g2
    
    l0=round(l0,2)
    l1=round(l1,2)
    l2=round(l2,2)
    
    
    lbl15.configure(text = g0)
    lbl16.configure(text = g1)
    lbl17.configure(text = g2)
                    
    lbl19.configure(text = l0)
    lbl20.configure(text = l1)
    lbl21.configure(text = l2)

    usablefluid = round(l1-l2,2)
    lbl24.configure(text = usablefluid)
    if txt22.get() == "":
        excess = 0
    else:
        excess = round(float(usablefluid) - float(txt22.get()),2)
    if excess > 0:
        result = "Pass"
    else:
        result = "Fail"
    lbl25.configure(text = excess)
    lbl26.configure (text = result)
           

lbl8 = Label(window, text="p0 (Precharged)")
lbl8.grid(column=0, row=11, sticky='e')
lbl9 = Label(window, text = "")
lbl9.grid(column=1, row=11)
lbl10 = Label(window, text="p1      (Charged)")
lbl10.grid(column=0, row=12, sticky='e')
lbl11 = Label(window, text="")
lbl11.grid(column=1, row=12)
lbl12 = Label(window, text="p2 (Discharged)")
lbl12.grid(column=0, row=13, sticky='e')
lbl13 = Label(window, text="")
lbl13.grid(column=1, row=13)

lbl14 = Label(window, text="Gas Vol")
lbl14.grid(column=3, row=10)
lbl15 = Label(window, text= "")
lbl15.grid(column=3, row=11)
lbl16 = Label(window, text= "")
lbl16.grid(column=3, row=12)
lbl17 = Label(window, text="")
lbl17.grid(column=3, row=13)

lbl18 = Label(window, text="Liq Vol")
lbl18.grid(column=4, row=10)
lbl19 = Label(window, text="")
lbl19.grid(column=4, row=11)
lbl20 = Label(window, text="")
lbl20.grid(column=4, row=12)
lbl21 = Label(window, text="")
lbl21.grid(column=4, row=13)

window.grid_rowconfigure(16, minsize=40)
lbl22 = Label(window, text="FVR")
lbl22.grid(column=1, row=17)
txt22 = Entry(window,width=10)
txt22.grid(column=2, row=17)
lbl23 = Label(window, text="Usable Fluid")
lbl23.grid(column=1, row=18)
lbl24 = Label(window, text="")
lbl24.grid(column=2, row=18)
lbl25 = Label(window, text="")
lbl25.grid(column=2, row=19)
lbl26 = Label(window, text="")
lbl26.grid(column=3, row=19)
lbl27 = Label(window, text="Excess")
lbl27.grid(column=1, row=19)

window.mainloop()