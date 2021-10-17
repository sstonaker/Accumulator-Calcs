from tkinter import *
from tkinter.ttk import *
from decimal import *
getcontext().prec = 5

window = Tk()
window.title("Ideal Gas Accumulator Calcs")
window.geometry('800x600')

lbl_std_cond = Label(window, text="Standard Conditions:")
lbl_std_cond.grid(column=0, row=0)

chk_std_cond_state = BooleanVar()
chk_std_cond_state.set(True)  # set check state


def activatecheck1():
    if chk_std_cond_state.get() == True:  # whenever checked
        txt_std_pres.delete(0, END)
        txt_std_temp.delete(0, END)
        txt_std_pres.insert(0, '14.7')
        txt_std_temp.insert(0, '60')
        txt_std_pres.config(state=DISABLED)
        txt_std_temp.config(state=DISABLED)
    elif chk_std_cond_state.get() == False:  # whenever unchecked
        txt_std_pres.config(state=NORMAL)
        txt_std_temp.config(state=NORMAL)
        txt_std_pres.delete(0, END)
        txt_std_temp.delete(0, END)
        txt_std_pres.focus()


chk_std_cond = Checkbutton(
    window, var=chk_std_cond_state, command=activatecheck1)
chk_std_cond.grid(column=1, row=0)

lbl_default_vals = Label(window, text="Use default values:")
lbl_default_vals.grid(column=3, row=0)

chk_default_vals_state = BooleanVar()
chk_default_vals_state.set(True)  # set check state


def activatecheck2():
    if chk_default_vals_state.get() == True:  # whenever checked
        txt_precharge.delete(0, END)
        txt_sys_pres.delete(0, END)
        txt_min_op_pres.delete(0, END)
        txt_precharge.insert(0, '1000')
        txt_sys_pres.insert(0, '3000')
        txt_min_op_pres.insert(0, '1200')
        txt_precharge.config(state=DISABLED)
        txt_sys_pres.config(state=DISABLED)
        txt_min_op_pres.config(state=DISABLED)
    elif chk_default_vals_state.get() == False:  # whenever unchecked
        txt_precharge.config(state=NORMAL)
        txt_sys_pres.config(state=NORMAL)
        txt_min_op_pres.config(state=NORMAL)
        txt_precharge.delete(0, END)
        txt_sys_pres.delete(0, END)
        txt_min_op_pres.delete(0, END)
        txt_precharge.focus()


chk_default_vals = Checkbutton(
    window, var=chk_default_vals_state, command=activatecheck2)
chk_default_vals.grid(column=4, row=0)


lbl_std_pres = Label(window, text="stdpres")
lbl_std_pres.grid(column=0, row=1)
txt_std_pres = Entry(window, width=10)
txt_std_pres.grid(column=1, row=1)
if chk_std_cond_state.get() == True:
    txt_std_pres.insert(0, '14.7')
    txt_std_pres.config(state=DISABLED)

lbl_std_temp = Label(window, text="stdtemp")
lbl_std_temp.grid(column=0, row=2)
txt_std_temp = Entry(window, width=10)
txt_std_temp.grid(column=1, row=2)
if chk_std_cond_state.get() == True:
    txt_std_temp.insert(0, '60')
    txt_std_temp.config(state=DISABLED)

lbl_precharge = Label(window, text="Precharge")
lbl_precharge.grid(column=0, row=4)
txt_precharge = Entry(window, width=10)
txt_precharge.grid(column=1, row=4)
if chk_default_vals_state.get() == True:
    txt_precharge.insert(0, '1000')
    txt_precharge.config(state=DISABLED)

lbl_num_bottles = Label(window, text="# Bottles")
lbl_num_bottles.grid(column=0, row=5)
txt_num_bottles = Entry(window, width=10)
txt_num_bottles.grid(column=1, row=5)

lbl_bottle_size = Label(window, text="Bottle Size")
lbl_bottle_size.grid(column=0, row=6)
lbl_11_gal = Label(window, text="11")
lbl_11_gal.grid(column=1, row=7)
lbl_15_gal = Label(window, text="15")
lbl_15_gal.grid(column=2, row=7)
chk_11_gal_state = BooleanVar()
chk_11_gal_state.set(False)  # set check state


def activatecheck3():
    if chk_11_gal_state.get() == True:  # whenever checked
        chk_15_gal_state.set(False)
        txt_gas_vol.delete(0, END)
        txt_gas_vol.insert(0, "9.9")
    elif chk_11_gal_state.get() == False:  # whenever unchecked
        #     chk_15_gal_state.set(True)
        txt_gas_vol.delete(0, END)


#        txt_gas_vol.insert(0, "13.7")
chk_11_gal = Checkbutton(window, var=chk_11_gal_state, command=activatecheck3)
chk_11_gal.grid(column=1, row=6)
chk_15_gal_state = BooleanVar()
chk_15_gal_state.set(False)  # set check state


def activatecheck4():
    if chk_15_gal_state.get() == True:  # whenever checked
        chk_11_gal_state.set(False)
        txt_gas_vol.delete(0, END)
        txt_gas_vol.insert(0, "13.7")
    elif chk_15_gal_state.get() == False:  # whenever unchecked
        #        chk_11_gal_state.set(True)
        txt_gas_vol.delete(0, END)


#        txt_gas_vol.insert(0, "9.9")
chk_15_gal = Checkbutton(window, var=chk_15_gal_state, command=activatecheck4)
chk_15_gal.grid(column=2, row=6)
#txt5.grid(column=1, row=6)


lbl_min_op_pres = Label(window, text="MOP")
lbl_min_op_pres.grid(column=3, row=4)
txt_min_op_pres = Entry(window, width=10)
txt_min_op_pres.grid(column=4, row=4)
if chk_default_vals_state.get() == True:
    txt_min_op_pres.insert(0, '1200')
    txt_min_op_pres.config(state=DISABLED)

lbl_sys_pres = Label(window, text="Sys Pres")
lbl_sys_pres.grid(column=3, row=5)
txt_sys_pres = Entry(window, width=10)
txt_sys_pres.grid(column=4, row=5)
if chk_default_vals_state.get() == True:
    txt_sys_pres.insert(0, '3000')
    txt_sys_pres.config(state=DISABLED)

lbl_gas_vol = Label(window, text="Gas Vol")
lbl_gas_vol.grid(column=3, row=6)
txt_gas_vol = Entry(window, width=10)
txt_gas_vol.grid(column=4, row=6)

window.grid_rowconfigure(8, minsize=20)
window.grid_rowconfigure(9, minsize=20)


def clicked():
    if txt_std_pres.get() == "":
        psia = 0
    else:
        psia = txt_std_pres.get()
    if txt_precharge.get() == "":
        precharge = 1000
    else:
        precharge = txt_precharge.get()
    if txt_sys_pres.get() == "":
        syspres = 3000
    else:
        syspres = txt_sys_pres.get()
    if txt_min_op_pres.get() == "":
        MOP = float(precharge) + 200
    else:
        MOP = txt_min_op_pres.get()

    p0 = float(precharge)+float(psia)
    p1 = float(syspres)+float(psia)
    p2 = float(MOP)+float(psia)

    updatevols(p0, p1, p2)

    lbl_p0.configure(text=p0)
    lbl_p1.configure(text=p1)
    lbl_p2.configure(text=p2)


window.grid_rowconfigure(14, minsize=40)
btn = Button(window, text="Run Calcs", command=clicked)
btn.grid(column=2, row=15)


def updatevols(p0, p1, p2):

    e1 = p0/p1
    e2 = p0/p2

    if txt_num_bottles.get() == "":
        numbot = 0
    else:
        numbot = txt_num_bottles.get()
    if txt_gas_vol.get() == "":
        botsize = 0
    else:
        botsize = txt_gas_vol.get()
#        if chk_11_gal_state.get() == False and chk_15_gal_state.get() == False:
#           botsize = 0
#        else:
#           botsize = txt_gas_vol.get()

    g0 = float(numbot) * float(botsize)
    g1 = g0*e1
    g2 = g0*e2

    g0 = round(g0, 2)
    g1 = round(g1, 2)
    g2 = round(g2, 2)

    l0 = g0-g0
    l1 = g0-g1
    l2 = g0-g2

    l0 = round(l0, 2)
    l1 = round(l1, 2)
    l2 = round(l2, 2)

    lbl_g0.configure(text=g0)
    lbl_g1.configure(text=g1)
    lbl_g2.configure(text=g2)

    lbl_l0.configure(text=l0)
    lbl_l1.configure(text=l1)
    lbl_l2.configure(text=l2)

    usablefluid = round(l1-l2, 2)
    lbl_usable_fluid_calc.configure(text=usablefluid)
    if txt_fvr.get() == "":
        excess = 0
    else:
        excess = round(float(usablefluid) - float(txt_fvr.get()), 2)
    if excess > 0:
        result = "Pass"
    else:
        result = "Fail"
    lbl_excess_calc.configure(text=excess)
    lbl_result.configure(text=result)


lbl_p0_precharged = Label(window, text="p0 (Precharged)")
lbl_p0_precharged.grid(column=0, row=11, sticky='e')
lbl_p0 = Label(window, text="")
lbl_p0.grid(column=1, row=11)
lbl_p1_charged = Label(window, text="p1      (Charged)")
lbl_p1_charged.grid(column=0, row=12, sticky='e')
lbl_p1 = Label(window, text="")
lbl_p1.grid(column=1, row=12)
lbl_p2_discharged = Label(window, text="p2 (Discharged)")
lbl_p2_discharged.grid(column=0, row=13, sticky='e')
lbl_p2 = Label(window, text="")
lbl_p2.grid(column=1, row=13)

lbl_calcs_gas_vol = Label(window, text="Gas Vol")
lbl_calcs_gas_vol.grid(column=3, row=10)
lbl_g0 = Label(window, text="")
lbl_g0.grid(column=3, row=11)
lbl_g1 = Label(window, text="")
lbl_g1.grid(column=3, row=12)
lbl_g2 = Label(window, text="")
lbl_g2.grid(column=3, row=13)

lbl_liq_vol = Label(window, text="Liq Vol")
lbl_liq_vol.grid(column=4, row=10)
lbl_l0 = Label(window, text="")
lbl_l0.grid(column=4, row=11)
lbl_l1 = Label(window, text="")
lbl_l1.grid(column=4, row=12)
lbl_l2 = Label(window, text="")
lbl_l2.grid(column=4, row=13)

window.grid_rowconfigure(16, minsize=40)
lbl_fvr = Label(window, text="FVR")
lbl_fvr.grid(column=1, row=17)
txt_fvr = Entry(window, width=10)
txt_fvr.grid(column=2, row=17)
lbl_usable_fluid = Label(window, text="Usable Fluid")
lbl_usable_fluid.grid(column=1, row=18)
lbl_usable_fluid_calc = Label(window, text="")
lbl_usable_fluid_calc.grid(column=2, row=18)
lbl_excess_calc = Label(window, text="")
lbl_excess_calc.grid(column=2, row=19)
lbl_result = Label(window, text="")
lbl_result.grid(column=3, row=19)
lbl_excess = Label(window, text="Excess")
lbl_excess.grid(column=1, row=19)

window.mainloop()
