import tkinter as tk
import math
from tkinter import *
import pyperclip

# create the main window
window = tk.Tk()

# set the window title
window.title("My GUI")

# set the minimum window size to 560x200
window.minsize(570, 270) #widthxheight

# create the input boxes
have1 = tk.Entry(window, width=20)
have2 = tk.Entry(window, width=20)
have3 = tk.Entry(window, width=20)
have4 = tk.Entry(window, width=20)
need1 = tk.Entry(window, width=20)
need2 = tk.Entry(window, width=20)
need3 = tk.Entry(window, width=20)
need4 = tk.Entry(window, width=20)

# set default values for the input boxes
# have1.insert(0, "0")
# have2.insert(0, "0")
# have3.insert(0, "0")
# have4.insert(0, "0")
# need1.insert(0, "0")
# need2.insert(0, "0")
# need3.insert(0, "0")
# need4.insert(0, "0")
have1.insert(0, "128")
have2.insert(0, "55")
have3.insert(0, "2")
have4.insert(0, "0")
need1.insert(0, "9")
need2.insert(0, "54")
need3.insert(0, "14")
need4.insert(0, "0")


# create the text boxes with borders
text1 = tk.Text(window, width=10, height=1, borderwidth=2, relief="groove")
text2 = tk.Text(window, width=10, height=1, borderwidth=2, relief="groove")
text3 = tk.Text(window, width=10, height=1, borderwidth=2, relief="groove")
text4 = tk.Text(window, width=10, height=1, borderwidth=2, relief="groove")

#define clipboard copy
def copy_to_clipboard():
    itemtocraft = "Items to Craft in order (Left to Right):\n" + text1.get('1.0', 'end').rstrip() + " | " + text2.get('1.0', 'end').rstrip() + " | " + text3.get('1.0', 'end').rstrip() + " | " + text4.get('1.0', 'end').rstrip() + "\n\n"
    
    itemhave = "Items Have:\n" + have1.get() + " | " + have2.get() + " | " + have3.get() + " | " + have4.get() + "\n"
    itemneed = "Items need:\n" + need1.get() + " | " + need2.get() + " | " + need3.get() + " | " + need4.get()
    pyperclip.copy(itemtocraft+itemhave+itemneed)

# create the button
button = tk.Button(window, text="Submit")
button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
copy_button = tk.Button(window, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=4, column=1, columnspan=3, padx=10, pady=10)


# create the label for the first row of input boxes
have_label = tk.Label(window, text="Items you Have")
have_label.grid(row=0, column=0, columnspan=4, padx=10)

# put the first 4 input boxes in one row
have3.grid(row=1, column=2, padx=10, pady=10)
have1.grid(row=1, column=0, padx=10, pady=10)
have4.grid(row=1, column=3, padx=10, pady=10)
have2.grid(row=1, column=1, padx=10, pady=10)

have_label = tk.Label(window, text="Items you Need")
have_label.grid(row=2, column=0, columnspan=4, padx=10)

need1.grid(row=3, column=0, padx=10, pady=10)
need2.grid(row=3, column=1, padx=10, pady=10)
need3.grid(row=3, column=2, padx=10, pady=10)
need4.grid(row=3, column=3, padx=10, pady=10)

tocraft_label = tk.Label(window, text="Items to Craft in order (Left to Right)")
tocraft_label.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

level1_label = tk.Label(window, text="Level 1 (Always 0)")
level1_label.grid(row=6, column=0, padx=10)

level2_label = tk.Label(window, text="Level 2")
level2_label.grid(row=6, column=1, padx=10)

level3_label = tk.Label(window, text="Level 3")
level3_label.grid(row=6, column=2, padx=10)

level4_label = tk.Label(window, text="Level 4")
level4_label.grid(row=6, column=3, padx=10)

text1.grid(row=7, column=0, padx=10, pady=10)
text2.grid(row=7, column=1, padx=10, pady=10)
text3.grid(row=7, column=2, padx=10, pady=10)
text4.grid(row=7, column=3, padx=10, pady=10)



def submit():
    # get the input values
    # hv1 = float(have1.get())
    # hv2 = float(have2.get())
    # hv3 = float(have3.get())
    # hv4 = float(have4.get())
    # nd1 = float(need1.get())
    # nd2 = float(need2.get())
    # nd3 = float(need3.get())
    # nd4 = float(need4.get())

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
    # text1.insert(tk.END, str(int(output1)))
    # text2.insert(tk.END, str(int(output2)))
    # text3.insert(tk.END, str(int(output3)))
    # text4.insert(tk.END, str(int(output4)))
    


# bind the submit function to the button click event
button.config(command=submit)

# run the main loop
window.mainloop()
