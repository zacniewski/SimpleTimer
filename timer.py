from tkinter import *
from tkinter import ttk
import time
from datetime import datetime, date, timedelta
today=datetime.now()
def calculate(*args):
    try:
        today=datetime.now()
        year1=int(year.get())
        month1=int(month.get())
        day1=int(day.get())
        deadline=datetime(year1,month1,day1,8,0)  #deadline hour set to 8 AM
        cc=deadline-today
        ttk.Label(mainframe, text=(cc.days,"days")).grid(column=2, row=5, sticky=E)
        ttk.Label(mainframe, text=(int((cc.seconds)/3600),"h")).grid(column=2, row=6, sticky=E)
        ttk.Label(mainframe, text=(int(cc.seconds/60)-60*int(cc.seconds/3600),"m")).grid(column=2, row=7, sticky=E)
        
        ttk.Label(mainframe, text=("01 0")).grid(column=2, row=8, sticky=E)
        ttk.Label(mainframe, text=(cc.seconds-int((cc.seconds)/60)*60,"s")).grid(column=2, row=8, sticky=E)
        root.after(1000, calculate)
    except ValueError:
        pass
    
root = Tk()
root.title("Simple Timer")
mainframe = ttk.Frame(root, padding="3 3 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

year = StringVar()
month=StringVar()
day=StringVar()

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=4, row=3, sticky=W)
ttk.Label(mainframe, text="Current date:").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text=(today.year,"-",today.month,"-",today.day)).grid(column=3, row=1, sticky=E)
ttk.Label(mainframe, text="Enter you deadline:").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Year-").grid(column=2, row=2, sticky=E)
year_entry = ttk.Entry(mainframe, width=7, textvariable=year)
year_entry.grid(column=3, row=2, sticky=(W))
ttk.Label(mainframe, text="Month-").grid(column=2, row=3, sticky=E)
month_entry = ttk.Entry(mainframe, width=7, textvariable=month)
month_entry.grid(column=3, row=3, sticky=(W))
ttk.Label(mainframe, text="Day-").grid(column=2, row=4, sticky=E)
day_entry = ttk.Entry(mainframe, width=7, textvariable=day)
day_entry.grid(column=3, row=4, sticky=(W))
ttk.Label(mainframe, text="Left:").grid(column=1, row=5, sticky=E)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
year_entry.focus()
month_entry.focus()
day_entry.focus()
root.bind('<Return>', calculate)
root.mainloop()