from tkinter import *
from tkinter import ttk

def create_window1():
    page3 = Toplevel(main)
    f3 = ttk.Button(page3, text = "Calculate", command = calculate_sell)
    f3.grid()
    return page3

def create_window2():
    page4 = Toplevel(main)
    f4 = ttk.Button(page4, text = "Calculate", command = calculate_rent)
    f4.grid(row = 11)
    return page4

def create_window3():
    page5 = Toplevel(main)
    f5 = ttk.Button(page5, text = "Calculate", command = calculate_combined)
    f5.grid(row = 6)
    return page5

def Income():
    Label(page1, text = "Enter your income:").grid(row = 2)
    income = Entry(page1)
    income.grid(row = 2, column = 1)
    return income

def change_income():
    Label(page1, text = "Enter your new income:").grid(row = 2)
    income = Entry(page1)
    income.grid(row = 2, column = 1)
    d.destroy()
    
def Rent(page4):
    Label(page4, text = "Price of the area in euro").grid(row = 0)
    purchasing_area = Entry(page4)
    purchasing_area.grid(row = 0, column = 1)
    Label(page4, text = "Price of the construction in euro:").grid(row = 1)
    construction_price = Entry(page4)
    construction_price.grid(row = 1, column = 1)
    Label(page4, text = "Enter the area in m*m:").grid(row = 2)
    area = Entry(page4)
    area.grid(row = 2, column = 1)
    Label(page4, text = "Enter the number of floors:").grid(row = 3)
    floors = Entry(page4)
    floors.grid(row = 3, column = 1)
    Label(page4, text = "Enter the rent price for 1 m*m per month:").grid(row = 4)
    rent = Entry(page4)
    rent.grid(row = 4, column = 1)
    Label(page4, text = "Profit months:").grid(row = 9)
    months = Entry(page4)
    months.grid(row = 9, column = 1)
    Label(page4, text = "Price of the construction maintenance for month in euro:").grid(row = 10)
    construction_maintenance = Entry(page4)
    construction_maintenance.grid(row = 10, column = 1)
    


def Sell(page3):
    Label(page3, text = "Price of the area in euro:").grid(row = 4)
    purchasing_area1 = Entry(page3)
    purchasing_area1.grid(row = 4, column = 1)
    Label(page3, text = "Price of the construction in euro:").grid(row = 5)
    construction_price1 = Entry(page3)
    construction_price1.grid(row = 5, column = 1)
    income_after_payments1 = income-construction_price1-purchasing_area1 
    Label(page3, text = "Price of the selling area:").grid(row = 6)
    selling_area = Entry(page3)
    selling_area.grid(row = 6, column = 1)
    


def Chance(page5):
    Label(page5, text = "The percentage of the sellings(The part of your possessions you want to sell.):").grid(row = 0)
    percentage_of_sellings = Entry(page5)
    percentage_of_sellings.grid(row = 0, column = 1)
    Label(page5, text = "The percentage of the rents(The part of things(for example: apartments)you want to rent.):").grid(row = 1)
    percentage_of_rents = Entry(page5)
    percentage_of_rents.grid(row = 1, column = 1)
    Label(page5, text = "Price of the construction in euro:").grid(row = 2)
    construction_price1 = Entry(page5)
    construction_price1.grid(row = 2, column = 1)
    Label(page5, text = "Price of the area in euro:").grid(row = 3)
    purchasing_area1 = Entry(page5)
    purchasing_area1.grid(row = 3, column = 1)
    Label(page5, text = "Price of the selling area:").grid(row = 4)
    selling_area = Entry(page5)
    selling_area.grid(row = 4, column = 1)
    residue_after_payments = income-construction_price1-purchasing_area1
    gains = selling_area-purchasing_area1-construction_price1
    Label(page5, text = "Enter the rent price for 1 m*m per month:").grid(row = 5)
    rent = Entry(page5)
    rent.grid(row = 5, column = 1)
    Label(page5, text = "Price of the construction maintenance for month in euro:").grid(row = 6)
    construction_maintenance = Entry(page5)
    construction_maintenance.grid(row = 6, column = 1)
    Label(page5, text = "Enter the area in m*m:").grid(row = 7)
    area = Entry(page5)
    area.grid(row = 7, column = 1)
    Label(page5, text = "Enter the number of floors:").grid(row = 8)
    floors = Entry(page5)
    floors.grid(row = 8, column = 1)
    construction_area = area*floors
    Label(page5, text = "Profit months:").grid(row = 9)
    months = Entry(page5)
    months.grid(row = 9, column = 1)
    


    
main = Tk()
main.title('Investment Calculator')
main.geometry('500x500')

a = Label(main, text = "INVESTMENTS CALCULATOR")
a.grid()

def two_functions1():
    page3 = create_window1()
    Sell(page3)

def two_functions2():
    page4 = create_window2()
    Rent(page4)

def two_functions3():
    page5 = create_window3()
    Chance(page5)

def calculate_rent(purchasing_area, construction_price, area, floors, rent, months, construction_maintenance, construction_area, residue_after_payments, income_for_month, x, j, p):
    construction_area = area*floors
    residue_after_payments = income-construction_price-purchasing_area
    income_for_month = (construction_area*rent)-construction_maintenance
    x = int((income-residue_after_payments)/income_for_month)
    j = months*(area*rent-construction_maintenance)
    p = j-x*(area*rent-construction_maintenance)
    if residue_after_payments >= 0:
        w = Label(page3, text = "There are")
        w.grid()
        w = Label(page3, text = residue_after_payments)
        w.grid()
        w = Label(page3, text = "euros left!")
        w.grid()
        w = Label(page3, text = "You will return your investments in")
        w.grid()
        w = Label(page4, text = x)
        w.grid()
        w = Label(page4, text = "months")
        w.grid()
        w = Label(page4, text = "Your income for")
        w.grid()
        w = Label(page4, text = months)
        w.grid()
        w = Label(page4, text = "months is")
        w.grid()
        w = Label(page4, text = p)
        w.grid()
	
    else:
        q = Label(page4, text = "You must pay")
        q.grid()
        q = Label(page4, text = 0-residue_after_payments)
        q.grid()
        q = Label(page4,text = "euros")
        q.grid()
        e = Label(page4, text = "You can make the payment after:")
        e.grid()
        e = Label(page4, int(x))
        e.grid()
        r = Label(page4, text = 'Income for month is')
        r.grid()
        r = Label(page4, text = income_for_month)
        r.grid()
        t = Label(page4, text = "The summarized area is")
        t.grid()
        t = Label(page4, text = construction_area)
        t.grid()    
    
    

def calculate_sell(purchasing_area1, construction_price1, residue_after_payments1, selling_area):
    gains = selling_area-purchasing_area1-construction_price1
    y = Label(page3, text = "Your gains are")
    y.grid()
    y = Label(page3, text = gains)
    y.grid()
    

def calculate_combined(percentage_of_sellings, percentage_of_rents, construction_price1, purchasing_area1, selling_area, residue_after_payments, gains, rent, construction_maintenance, area, floors, construction_area, months):
    income_for_month = (construction_area*rent)-construction_maintenance
    j = months*(area*rent-construction_maintenance)
    earnings = (percentage_of_rents/100)*j + (percentage_of_sellings/100)*gains
    y = int(((construction_price1 + purchasing_area1) - gains-construction_price1-purchasing_area1)/income_for_month)
    earnings_after_payments = int(earnings - y)
    if earnings > 0:
        u = Label(page5,text = "You will receive")
        u.grid()
        u = Label(page5, text = earnings)
        u.grid()
        o = Label(page5, text = "Do it if you want!")
        o.grid()
        o = Label(page5, text = "After")
        o.grid()
        o = Label(page5, text = y)
        o.grid()
        o = Label(page5, text = "months you will return your payments")
        o.grid()
        o = Label(page5, text = "Your resedue after payments is")
        o.grid()
        o = Label(page5, text = earnings_after_payments)
        o.grid()
        
    elif earnings == 0:
        p = Label(page5, text = earnings)
        p.grid()
        p = Label(page5, text = "You will not receive anything!")
        p.grid()
        a = Label(page5, text = "There is no point of doing this!")
        a.grid()
	
    else:
        s = Label(page5, text = "You must pay")
        s.grid()
        s = Label(page5, text = 0 - earnings)
        s.grid()
        s = Label(page5, text = "euro!")
        s.grid()
        d = Label(page5, text = "Do NOT do invest in this or take credit!")
        d.grid()
    

rows = 0
while rows < 50:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1
 
nb = ttk.Notebook(main)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
 
page1 = ttk.Frame(nb)
nb.add(page1, text='HOME')

d = ttk.Button(page1, text = "Add Income", command = Income)
d.grid()

e = ttk.Button(page1, text = "Change Income", command = change_income)
e.grid()

page2 = ttk.Frame(nb)
nb.add(page2, text='OPTIONS')

a = ttk.Button(page2, command = two_functions1, text = "Sell")
a.grid(row = 0)
b = ttk.Button(page2, command = two_functions2, text = "Rent")
b.grid(row = 1)
c = ttk.Button(page2, text = "Combined", command = two_functions3)
c.grid(row = 2)


main.mainloop()
