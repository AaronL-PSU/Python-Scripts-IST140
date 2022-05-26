import tkinter
from tkinter import messagebox
from tkinter import simpledialog
root = tkinter.Tk()
option = 0
customer =[]
barber=[]
work= 0
from datetime import datetime
now = datetime.now()
close = now.replace(hour=19, minute=45, second=0, microsecond=0)
messagebox.showinfo("Error","No customer check-ins after 7:45PM. See comments* to override for testing.")
messagebox.showinfo("Time","Current time: " + str(now))

while option !=5:
    option=simpledialog.askinteger("Number","""
1: To enter a customer into the queue
2: To remove a customer from the queue
3: Check-in a barber
4: Check-out a barber
5: Quit
""")
    if option==1:
        if now<close: #Comment out this line for testing after 7:45PM*
            customer.append(simpledialog.askstring("New Customer","What is the customer's name?: "))
            messagebox.showinfo("Customers","Current list of customers: " + str(customer))
            if len(barber) == 0:
                messagebox.showinfo("Error","There are no barbers yet")
            else:
                messagebox.showinfo("Queue","Current wait time: " + str(12/len(barber)*len(customer)-12) + " minutes.")
                queuelog = open("queue.txt","w")
                queuelog.write(str(now) + " " + str(len(customer)) + " " + str(len(barber)))
                queuelog.close()
                enterq = datetime.now()
        else:
            messagebox.showinfo("Closed","The barbershop is closed at 8PM, sorry.")#Comment out this line for testing after 7:45PM*
        

    elif option==2:
        customer.remove(str(simpledialog.askstring("Customer","What is the customer's name: ")))
        work+=12
        messagebox.showinfo("Customers","Current list of customers: " + str(customer))
        if len(barber) == 0:
            messagebox.showinfo("Error","There are no barbers yet")
        else:
            messagebox.showinfo("Queue","Current wait time: " + str(12/len(barber)*len(customer)-12) + " minutes.")
            leaveq = datetime.now()
            customerlog = open("customer.txt","w")
            customerlog.write(str(enterq) + " " + str(leaveq) + " " + str(leaveq - enterq))
            customerlog.close()
        

    elif option==3:
        barber.append(str(simpledialog.askstring("Barber","What is the barber's name?: ")))
        messagebox.showinfo("Barbers","Current list of barbers: " + str(barber))
        enterw = datetime.now()
        
    elif option==4:
        barber.remove(str(simpledialog.askstring("Barber","What is the barber's name: ")))
        messagebox.showinfo("Barbers","Current list of barbers: " + str(barber))
        messagebox.showinfo("Worked","Time worked: " + str(work) + " minutes.")
        leavew = datetime.now()
        barberlog = open("barber.txt","w")
        barberlog.write(str(enterw) + " " + str(leavew) + " " + str(leavew - enterw))
        barberlog.close()
