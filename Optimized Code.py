import tkinter as tk
import math
import datetime
from tkinter import ttk
from tkcalendar import DateEntry
import pyperclip

from tktimepicker import SpinTimePickerOld
"""
This program requires to manipulate tktimepicker because its limitations
can't make the program work well.
You can install tktimepicker normally with pip and just replace the code
in timepicker.py with the timepicker.py here:
https://github.com/plopop0/GenshinHelpertkTimePicker/blob/d8dbe648f14c5c24ef4176c158c92754b195213b/build/lib/tktimepicker/timepicker.py

to view what changed go here:
https://github.com/plopop0/GenshinHelpertkTimePicker/commit/d8dbe648f14c5c24ef4176c158c92754b195213b

I'm just starting out so I don't really know how to repackage a pre-built package on my own repo so forgive me. s
"""

# create the main window
window = tk.Tk()

# set the window title
window.title("Genshin Helper")

# set the minimum window size to 560x200
window.minsize(570, 270) #widthxheight

# create a tab control
tab_control = ttk.Notebook(window)

# create tabs
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

# add tabs to tab control

tab1_txt, tab2_txt, tab3_txt = " Ascension Materials ", "     Resin     ", "   Artifacts   "
tab_control.add(tab1, text=tab1_txt)
tab_control.add(tab2, text=tab2_txt)
tab_control.add(tab3, text=tab3_txt)

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
# op_box = tk.Label(tab2, text="Condensed Resin: 0\nFragile Resin: 0") #previous ver
op_box = tk.Text(tab2, width=20, height=8)

#for timepicker use only
nowdt = datetime.datetime.now()
nowdt += datetime.timedelta(minutes=320)

# Create the widgets for tab 2
resin_have = tk.Entry(tab2, width=10)
date_picker = DateEntry(tab2, width=12, background='darkblue', foreground='white', borderwidth=2)

#backwards
time_picker = SpinTimePickerOld(tab2,h_width=5,m_width=5,p_width=4,
                                i_hr=int(nowdt.strftime('%I')),i_min=nowdt.minute,i_p=nowdt.strftime('%p'))
time_picker.addAll(0,1)
#change spinTimePickerOld with my own so that i have more control

# h_var = tk.StringVar(value='5')
# m_var = tk.StringVar(value='5')

# h_TP = tk.Spinbox(window, width=5, increment=1, from_=1, to=12,
#                                           validate="all")
# m_TP = tk.Spinbox(window, width=5, increment=1, from_=1, to=59,
#                                           validate="all")
# p-TP =

#/backwards

text_box1 = tk.Text(tab2, width=22, height=1)
text_box2 = tk.Text(tab2, width=10, height=1)
personal_dtformat = "%m/%d/%Y %I:%M %p"

# Place the widgets in tab 2
resin_have_label.grid(row=0, column=0, padx=0, pady=0)
full_resin_label.grid(row=0, column=1, padx=0, pady=0)
resin_have.grid(row=1, column=0, padx=10, pady=10)
text_box1.grid(row=1, column=1, padx=10, pady=10)

calcdtres_label.grid(row=2, column=0, padx=0, pady=0)
calcdtres_output_label.grid(row=2, column=1, padx=10, pady=10)
date_picker.grid(row=3,column=0,sticky="w",padx=10)
text_box2.grid(row=3, column=1, padx=10, pady=10)

op_box.grid(row=0, rowspan=4, column=2, sticky="w", padx=10, pady=10)

#backwards
resin_back_button = tk.Button(tab2, text="Resin Calculate",
                            #   command=printshit,
                               width=15, height=1)
resin_back_button.grid(row=4, column=1, padx=10)

time_picker.grid(row=4, column=0,sticky="w",padx=10, pady=10)


#default values
resin_have.insert(0, "0")

def res_copy():
    res_copy_clip = op_box.get("1.0", tk.END)
    pyperclip.copy(res_copy_clip)
    
resin_copy = tk.Button(tab2, text="Copy", command=res_copy)
resin_copy.grid(row=4, column=2, columnspan=3, padx=10, pady=10)

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
    
    #calculate resin
    resin_output = math.floor(total_minutes/8+float(reshav))

    #output num
    text_box2.delete("1.0", tk.END)
    text_box2.insert(tk.END, resin_output)

    #detailed output
    op_box_val = text_box2.get("1.0", tk.END)
    op_box_val = op_box_val.replace('\n','')
    wantdatetime = datetime.datetime(int(resin_year),
                                    int(resin_month),
                                    int(resin_day),
                                    int(resin_hour),
                                    int(resin_minute))
    wantdatetime_str = wantdatetime.strftime(personal_dtformat)
    nowdatetime_str = nowdatetime.strftime(personal_dtformat)

    op_box.delete("1.0", tk.END)
    op_box.insert(tk.END, ""
        +f"{reshav}->{op_box_val} Resin\n"
        +"from\n"
        +f"{nowdatetime_str}\n"
        +"to\n"
        +f"{wantdatetime_str}\n"
        +f"Condensed Resin: {math.floor(resin_output/40)}\nFragile Resin: {math.floor(resin_output%40/20)}"
        )
    # op_box.config(text=f"Condensed Resin: {math.floor(resin_output/40)}\nFragile Resin: {math.floor(resin_output%40/20)}")
    
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
    

resin_button = tk.Button(tab2, text="Submit", command=printshit, width=55, height=2)
resin_button.grid(row=5, column=0,columnspan=4, pady=10)


#endregion

#region Artifacts Calculator codes Tab 3

#Labels
arti_hv_label = tk.Label(tab3, text="Number of Artifacts You have")
arti_op_label = tk.Label(tab3, text="Output")
# arti_op = tk.Label(tab3, text="temp text")
arti_op = tk.Text(tab3, width=10, height=1)

#widgets
arti_hv = tk.Entry(tab3, width=10)

#place widgets
arti_hv_label.grid(row=0,column=0,padx=20)
arti_op_label.grid(row=0,column=1,padx=20)

arti_hv.grid(row=1,column=0,padx=10,pady=10)
arti_op.grid(row=1,column=1,padx=10,pady=10)

#default values
arti_hv.insert(0, "1400")

def arti_calc():
    #calculations
    cr_runs = math.ceil((1500-float(arti_hv.get()))/15)

    arti_op.delete("1.0", tk.END)
    arti_op.insert(tk.END, str(cr_runs))

#button
a_submit = tk.Button(tab3, text="Calculate",
                              command=arti_calc,
                               width=15, height=1)
a_submit.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

#endregion

def on_tab_keypress(event):
    current_tab = tab_control.tab(tab_control.select(), "text")
    if current_tab == tab1_txt:
        button.invoke()
    elif current_tab == tab2_txt:
        resin_button.invoke()
    elif current_tab == tab3_txt:
        a_submit.invoke()

window.bind("<Return>", on_tab_keypress)

# run the main loop
window.mainloop()
