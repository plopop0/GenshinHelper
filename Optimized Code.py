import tkinter as tk
import math
import datetime
from tkinter import ttk
from tkcalendar import DateEntry
from tktimepicker import SpinTimePickerOld
import pyperclip

# create the main window
window = tk.Tk()

# set the window title
window.title("My GUI")

# set the minimum window size to 560x200
window.minsize(570, 270) #widthxheight

# create a tab control
tab_control = ttk.Notebook(window)

# create tabs
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

# add tabs to tab control
tab_control.add(tab1, text="Tab 1")
tab_control.add(tab2, text="Tab 2")

# pack the tab control to the main window
tab_control.grid(column=0, row=0, sticky="nsew")

#region Crafting Calculator codes Tab 1

# create the input boxes
have1 = tk.Entry(tab1, width=20)
have2 = tk.Entry(tab1, width=20)
have3 = tk.Entry(tab1, width=20)
have4 = tk.Entry(tab1, width=20)
need1 = tk.Entry(tab1, width=20)
need2 = tk.Entry(tab1, width=20)
need3 = tk.Entry(tab1, width=20)
need4 = tk.Entry(tab1, width=20)

# set default values for the input boxes
have1.insert(0, "128")
have2.insert(0, "55")
have3.insert(0, "2")
have4.insert(0, "0")
need1.insert(0, "9")
need2.insert(0, "54")
need3.insert(0, "14")
need4.insert(0, "0")

# create the text boxes with borders
text1 = tk.Text(tab1, width=10, height=1, borderwidth=2, relief="flat")
text2 = tk.Text(tab1, width=10, height=1, borderwidth=2, relief="flat")
text3 = tk.Text(tab1, width=10, height=1, borderwidth=2, relief="flat")
text4 = tk.Text(tab1, width=10, height=1, borderwidth=2, relief="flat")

text1.grid(row=7, column=0, padx=10, pady=10)
text2.grid(row=7, column=1, padx=10, pady=10)
text3.grid(row=7, column=2, padx=10, pady=10)
text4.grid(row=7, column=3, padx=10, pady=10)

#define clipboard copy
def copy_to_clipboard():
    itemtocraft = "Items to Craft in order (Left to Right):\n" + text1.get('1.0', 'end').rstrip() + " | " + text2.get('1.0', 'end').rstrip() + " | " + text3.get('1.0', 'end').rstrip() + " | " + text4.get('1.0', 'end').rstrip() + "\n\n"
    
    itemhave = "Items Have:\n" + have1.get() + " | " + have2.get() + " | " + have3.get() + " | " + have4.get() + "\n"
    itemneed = "Items need:\n" + need1.get() + " | " + need2.get() + " | " + need3.get() + " | " + need4.get()
    pyperclip.copy(itemtocraft+itemhave+itemneed)

# create the button
button = tk.Button(tab1, text="Submit")
copy_button = tk.Button(tab1, text="Copy", command=copy_to_clipboard)

button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
copy_button.grid(row=4, column=1, columnspan=3, padx=10, pady=10)


# create the label for the first row of input boxes
have_label = tk.Label(tab1, text="Items you Have")
have_label.grid(row=0, column=0, columnspan=4, padx=10)

# put the first 4 input boxes in one row
have3.grid(row=1, column=2, padx=10, pady=10)
have1.grid(row=1, column=0, padx=10, pady=10)
have4.grid(row=1, column=3, padx=10, pady=10)
have2.grid(row=1, column=1, padx=10, pady=10)

have_label = tk.Label(tab1, text="Items you Need")
have_label.grid(row=2, column=0, columnspan=4, padx=10)

need1.grid(row=3, column=0, padx=10, pady=10)
need2.grid(row=3, column=1, padx=10, pady=10)
need3.grid(row=3, column=2, padx=10, pady=10)
need4.grid(row=3, column=3, padx=10, pady=10)

# Grouping the labels being made
tocraft_label = tk.Label(tab1, text="Items to Craft in order (Left to Right)")
level1_label = tk.Label(tab1, text="Level 1 (Always 0)")
level2_label = tk.Label(tab1, text="Level 2")
level3_label = tk.Label(tab1, text="Level 3")
level4_label = tk.Label(tab1, text="Level 4")

# Placing the labels on the grid
tocraft_label.grid(row=5, column=0, columnspan=4, padx=10, pady=10)
level1_label.grid(row=6, column=0, padx=10)
level2_label.grid(row=6, column=1, padx=10)
level3_label.grid(row=6, column=2, padx=10)
level4_label.grid(row=6, column=3, padx=10)




def submit():
    # get the input values
    hv = [float(have1.get()), float(have2.get()), float(have3.get()), float(have4.get())]
    nd = [float(need1.get()), float(need2.get()), float(need3.get()), float(need4.get())]

    # this part was useless lmao
    # max1 = float(hv1)
    # max2 = math.floor(max1/3.0) + float(hv2)
    # max3 = math.floor(max2/3.0) + float(hv3)
    # max4 = math.floor(max3/3.0) + float(hv4)

    excess = [hv[0]-nd[0], 0.0, 0.0, 0.0]
    for i in range(1, 4):
        excess[i] = math.floor(excess[i-1]/3) + hv[i] - nd[i]

    output = [0, 0, 0, 0]
    tc = [0,0,0,0,0]
    if (excess[3] >= 0):
        for i in range(3, -1, -1):
            tc[i] = (nd[i] - (hv[i] - tc[i+1])) * 3
            output[i] = 0 if tc[i] < 0 else tc[i] / 3
            [text.delete("1.0", tk.END) for text in [text1, text2, text3, text4]]
            [text1.insert(tk.END, str(int(output[i]))) for i, text1 in enumerate([text1, text2, text3, text4])]
    else:
        [text.delete("1.0", tk.END) for text in [text1, text2, text3, text4]]
        text1.insert(tk.END, "Not")
        text2.insert(tk.END, "Enough")
        text3.insert(tk.END, "Materials")
        text4.insert(tk.END, "!")

# bind the submit function to the button click event
button.config(command=submit)



#endregion

#region Resin Calculator codes Tab 2

#Labels
resin_have_label = tk.Label(tab2, text="Resin you have")
full_resin_label = tk.Label(tab2, text="Date and Time to full")
calcdtres_label = tk.Label(tab2, text="Calculate Resin at this Date and Time")
calcdtres_output_label = tk.Label(tab2, text="Output")
shit_label = tk.Label(tab2, text="Condensed Resin: 0\nFragile Resin: 0")

#for timepicker use only
nowdt = datetime.datetime.now()

# Create the widgets for tab 2
resin_have = tk.Entry(tab2, width=10)
date_picker = DateEntry(tab2, width=12, background='darkblue', foreground='white', borderwidth=2)
time_picker = SpinTimePickerOld(tab2,h_width=5,m_width=5,p_width=4,i_hr=int(nowdt.strftime('%I')),i_min=nowdt.minute,i_p=nowdt.strftime('%p'))
time_picker.addAll(0,1)

text_box1 = tk.Text(tab2, width=22, height=1)
text_box2 = tk.Text(tab2, width=10, height=1)
personal_dtformat = "%m/%d/%Y %I:%M %p"

#default values
resin_have.insert(0, "0")

def printshit():
    nowdatetime = datetime.datetime.now()
    # nowdatetime_formatted = nowdatetime.strftime('%m/%d/%Y %I:%M %p')

    #calculate date and time until resin cap
    reshav = resin_have.get()
    delta = datetime.timedelta(hours=math.floor((160.0 - float(reshav))*8/60), minutes=((160-float(reshav))*8)%60)
    fullrestime = nowdatetime + delta
    text_box1.delete("1.0", tk.END)
    text_box1.insert(tk.END, fullrestime.strftime(personal_dtformat))
    
    #calculate amount resin, from resin amount now, on a certain datetime
    date = date_picker.get_date()
    resin_month = date.month
    resin_day = date.day
    resin_year = date.year
    resin_hour = float(time_picker.hours())
    nowhr = nowdatetime.hour
    resin_minute = float(time_picker.minutes())
    nowmin = nowdatetime.minute

    #converts hours from 12h to 24h
    if(time_picker.period()=="a.m" and time_picker.hours()==12):resin_hour = 0
    elif(time_picker.period()=="p.m" and time_picker.hours()<12):resin_hour += 12

    #goback to this, it needs to be dependent on the day
    # if(nowdatetime.strftime("%p")=="PM" and time_picker.period()=="a.m"):resin_hour +=

    # hrdifftomin = (resin_hour-nowhr)*60
    # mindiff = 0
    # if(hrdifftomin==0):mindiff = resin_minute-nowmin
    # elif(hrdifftomin>=60):mindiff = (resin_minute)+(60-nowhr)
    # elif(hrdifftomin<0):mindiff = 0

    # convert the input values to minutes
    start_time = nowhr * 60 + nowmin
    end_time = resin_hour * 60 + resin_minute

    start_date = nowdatetime.year * 365 + (nowdatetime.month - 1) * 30 + nowdatetime.day
    end_date = resin_year * 365 + (resin_month - 1) * 30 + resin_day

    # calculate the difference in minutes
    total_minutes = (end_date - start_date) * 24 * 60 + (end_time - start_time)
    
    resin_output = math.floor(total_minutes/8+float(reshav))

    text_box2.delete("1.0", tk.END)
    text_box2.insert(tk.END, resin_output)
    
    shit_label.config(text=f"Condensed Resin: {math.floor(resin_output/40)}\nFragile Resin: {math.floor(resin_output%40/20)}")
    # wantdatetime = datetime.datetime(int(resin_year),int(resin_month),int(resin_day),int(resin_hour),int(resin_minute))
    # print(nowdatetime.strftime("%Y-%m-%d %H:%M"))
    # print(wantdatetime.strftime("%Y-%m-%d %H:%M"))


    # for variable in [resin_year, resin_month, resin_day, resin_hour, resin_minute]:
    #     print(variable," ")

    # print(nowdatetime.strftime("%Y-%m-%d %H:%M"))
    # print(wantdatetime.strftime("%Y-%m-%d %H:%M"))
    # print(divmod(int((wantdatetime-nowdatetime).total_seconds()),60))

    # resin_hour += resin_minute/60
    # resin_dtoutput = (resin_hour*60/8)+float(reshav)
    # print(resin_dtoutput)

    # print(resin_hour, " ", time_picker.minutes(), " ", time_picker.period())

    # print(math.floor((160.0 - float(reshav))*8/60))
    # print(((160-float(reshav))*8)%60)
    

resin_button = tk.Button(tab2, text="Submit", command=printshit, width=30, height=2)

# Place the widgets in tab 2
resin_have_label.grid(row=0, column=0, padx=0, pady=0)
full_resin_label.grid(row=0, column=1, padx=0, pady=0)
resin_have.grid(row=1, column=0, padx=10, pady=10)
text_box1.grid(row=1, column=1, padx=10, pady=10)

calcdtres_label.grid(row=2, column=0, padx=0, pady=0)
calcdtres_output_label.grid(row=2, column=1, padx=10, pady=10)
date_picker.grid(row=3,column=0,sticky="w",padx=10)
text_box2.grid(row=3, rowspan=2, column=1, padx=10, pady=10)


shit_label.grid(row=3, rowspan=2, column=2, padx=10, pady=10)

time_picker.grid(row=4, column=0,sticky="w",padx=10, pady=10)

resin_button.grid(row=5, column=0,columnspan=3 , pady=10)


#endregion


# run the main loop
window.mainloop()
