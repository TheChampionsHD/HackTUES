from tkinter import *

root = Tk()

def Decision(decision):
    if decision == "Rent":
        w = Label(root, Rent(decision))
        w.pack()
    elif decision == "Sell":
        w = Label(root, Sell(decision))
        w.pack()
    elif decision == "Combined":
        w = Label(root, Combined(decision))
        w.pack()


def Rent(decision):
    purchasing_area = float(input("Price of the area in euro:"))
    construction_price = float(input("Price of the construction in euro:"))
    area = float(input("Enter the area in m*m:"))
    floors = int(input("Enter the number of floors:"))
    construction_area = area*floors
    rent = float(input("Enter the rent price for 1 m*m per month:"))
    months = int(input("Profit months:"))
    construction_maintenance = float(input("Price of the construction maintenance for month in euro:"))
    residue_after_payments = user.income-construction_price-purchasing_area
    income_for_month = (construction_area*rent)-construction_maintenance
    x = int((user.income-residue_after_payments)/income_for_month)
    j = months*(area*rent-construction_maintenance)
    p = j-x*(area*rent-construction_maintenance)
    if residue_after_payments >= 0:
        w = Label(root, text = "There are")
        w.pack()
        w = Label(root, text = residue_after_payments)
        w.pack()
        w = Label(root, text = "euros left!")
        w.pack()
        w = Label(root, text = "You will return your investments in")
        w.pack()
        w = Label(root, text = x)
        w.pack()
        w = Label(root, text = "months")
        w.pack()
        w = Label(root, text = "Your income for")
        w.pack()
        w = Label(root, text = months)
        w.pack()
        w = Label(root, text = "months is")
        w.pack()
        w = Label(root, text = p)
        w.pack()
	
    else:
        q = Label(root, text = "You must pay")
        q.pack()
        q = Label(root, text = 0-residue_after_payments)
        q.pack()
        q = Label(root,text = "euros")
        q.pack()
        e = Label(root, text = "You can make the payment after:")
        e.pack()
        e = Label(root, int(x))
        e.pack()
        r = Label(root,text = 'Income for month is')
        r.pack()
        r = Label(root,text = income_for_month)
        t = Label(root, text = "The summarized area is")
        t.pack()
        t = Label(root, text = construction_area)
        t.pack()

def Sell(decision):
    purchasing_area1 = float(input("Price of the area in euro:"))
    construction_price1 = float(input("Price of the construction in euro:"))
    income_after_payments1 = user.income-construction_price1-purchasing_area1
    selling_area = float(input("Price of the selling area:"))
    gains = selling_area-purchasing_area1-construction_price1
    y = Label(root, text = "Your gains are")
    y.pack()
    y = Label(root, text = gains)
    y.pack()
    
def Combined(decision):
    percentage_of_sellings = float(input("The percentage of the sellings(The part of your possessions you want to sell.):"))
    percentage_of_rents = float(input("The percentage of the rents(The part of things(for example: apartments)you want to rent.):"))
    construction_price1 = float(input("Price of the construction in euro:"))
    purchasing_area1 = float(input("Price of the area in euro:"))
    selling_area = float(input("Price of the selling area:"))
    residue_after_payments = user.income-construction_price1-purchasing_area1
    gains = selling_area-purchasing_area1-construction_price1
    rent = float(input("Enter the rent price for 1 m*m per month:"))
    construction_maintenance = float(input("Price of the construction maintenance for month in euro:"))
    area = float(input("Enter the area in m*m:"))
    floors = int(input("Enter the number of floors:"))
    construction_area = area*floors
    months = int(input("Profit months:"))
    income_for_month = (construction_area*rent)-construction_maintenance
    j = months*(area*rent-construction_maintenance)
    earnings = (percentage_of_rents/100)*j + (percentage_of_sellings/100)*gains
    y = int(((construction_price1 + purchasing_area1) - gains-construction_price1-purchasing_area1)/income_for_month)
    earnings_after_payments = int(earnings - y)
    
    
    if earnings > 0:
        u = Label(root,text = "You will receive")
        u.pack()
        u = Label(root, text = earnings)
        u.pack()
        o = Label(root, text = "Do it if you want!")
        o.pack()
        o = Label(root, text = "After")
        o.pack()
        o = Label(root, text = y)
        o.pack()
        o = Label(root, text = "months you will return your payments")
        o.pack()
        o = Label(root, text = "Your resedue after payments is")
        o.pack()
        o = Label(root, text = earnings_after_payments)
        o.pack()
        
    elif earnings == 0:
        p = Label(root, text = earnings)
        p.pack()
        p = Label(root, text = "You will not receive anything!")
        p.pack()
        a = Label(root, text = "There is no point of doing this!")
        a.pack()
	
    else:
        s = Label(root, text = "You must pay")
        s.pack()
        s = Label(root, text = 0 - earnings)
        s.pack()
        s = Label(root, text = "euro!")
        s.pack()
        d = Label(root, text = "Do NOT do invest in this or take credit!")
        d.pack()

    

class User:
    def __init__(self, income):
        self.income = income

user = User(float(input("Your income:")))
decision = input("What do you want to do?(Sell/Rent/Combined)")
a = Label(root, Decision(decision))
a.pack()


