import tkinter as tk
import tkinter.font as font
import pyautogui
from functools import partial



width, height= pyautogui.size()
# print(width, height )

# creates the gui
window = tk.Tk()

# sets the gui window size, using data from the users screen rez so its kinda consistent
window.geometry(str(width // 5) + "x" + str(height//2))
# -2 create white space at bottom for me

# making so i don't have to deal with window size changes by making the window constant size
window.minsize(width // 5, height//2)
window.maxsize(width // 5, height//2)

# formatting is harder to account for each device and the size
# since can't place based on pixels <- some are chars 
# establish a grid 
# idk if all this is rly necessary ngl since the code im looking at doesn't have it but when i take it out, my thing doesnt work 
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)



# print(height//2)
window.title("Calculator")

# so it is width/ height in characters not pixels, in that case, i think the width is fine as is, then I can have height be like 3 or 5
# then the the numbers that will appear will be there
# label will be the actual text portion of the calculator

# can fit 000000000000 - 12 char basically
# idk why this doesn't really break the box size tho

curr_display = "0"

label = tk.Label(window, text=curr_display,  
    fg="white",
    bg="black", 
    width = width // 4, 
    height= 7, anchor="se")
label.grid(row = 0, rowspan=1, columnspan= 4, sticky="NESW")
label['font'] = font.Font(size=30)

# this will save the first and last calculator values so when we do =, it will be easy to call    
# remember to set to None since I will do check for 
first = None
signage = None
prev = 0
# event for numerical number presses

def add_to_display(value):
    global first
    global curr_display
    global signage
    global prev

    if value == "del":
        curr_display = "0"
        label.config(text = curr_display)
        prev = 0
        first = None
        signage = None
        return
    curr_display = curr_display.replace(",", "")
    if signage == ".":
        # here we want to add to behind of decimal
        # but how to continue formatting?
        
        # so max char is 3 sets of 3 so 9
        # that is 2 commas
        # therefore as long as it is less than 12, we should still be able to add decimal
        # 12,123,123.
        # actually i want to keep it consistent of 9 numbers total so remove 2
        if ( len(curr_display) < 10):
            curr_display = curr_display + str(value)
            # know max is 1 decimal
            # find pos, format until then
            # then add the rest of it since behidn decimal doesnt need commans
            curr_display = '{:,}'.format(int(curr_display[0:curr_display.find(".")]) ) + curr_display[curr_display.find("."):]
            label.config(text = curr_display)
        return
        
        
    # huh rly would make things easier if my entire thing was just append to end
    curr_display = curr_display.replace(",", "")
    # print(curr_display)
    if ( abs(float(curr_display)) <= 99999999):
        # curr_display = str(int(curr_display)*10 + value)
        curr_display = curr_display + str(value)
        curr_display = '{:,}'.format(int(curr_display) )
        label.config(text = curr_display)
        

def sign_change():
    global curr_display
    curr_display = curr_display.replace(",", "")
    # not sure why the format thing gets removed here but ig ill just put in in to keep it consistent

    # curr_display = str( -1 * int(curr_display)) idk why that breaks it but lets do smth else
    if curr_display.startswith("-"):
        curr_display = curr_display[1:]


    else:
        # print(curr_display)
        curr_display = "-" + curr_display
        # print(curr_display)
    curr_display = '{:,}'.format(int(curr_display) )
    label.config(text = curr_display)

def perform_action(action):
    global curr_display
    global first
    global signage
    global prev
    if action == "+":
        # basically i want to have the button appear different than it was before when clicked
        # but save that for next time
        # set curr_display to 0
        first = curr_display.replace(",", "")
        curr_display = "0"
        signage = "+"
        # print(first)

    elif action == "-":
        first = curr_display.replace(",", "")
        curr_display = "0"
        signage = "-"

    elif action == "x":
        first = curr_display.replace(",", "")
        curr_display = "0"
        signage = "x"
    elif action == "/":
        first = curr_display.replace(",", "")
        curr_display = "0"
        signage = "/"

    elif action == "%":
        # this is a one time thing so no need to keep track of those
        curr_display = curr_display.replace(",", "")
        curr_display = int(curr_display) / 100
        curr_display = '{:,}'.format(int(curr_display) )
        label.config(text = curr_display)
        
    elif action == ".":
        if signage == ".":
            return
        curr_display = curr_display + "."
        label.config(text = curr_display)
        signage = "."
    else:
        
        # action here is =
        temp = curr_display.replace(",", "")
        # print(first)
        if first == None:
            # so this is the place where ppl spam = after like x so we see signage and store smth as the value we perform
            # order doesn't matter for + and * but remember that it does for - and /
            
            if signage == "+":
                # print("here2")
                curr_display = str(int(temp) + int(prev)) 
            elif signage == "-":
                curr_display = str(int(prev) - int(temp)) 

            elif signage == "x":
                curr_display = str(int(temp) * int(prev))
            elif signage == "/":
                curr_display = str(int(prev) / int(temp))

        else:
            prev = temp
            if signage == "+":
                # print("here")
                curr_display = str(int(temp) + int(first))
            elif signage == "-":
                curr_display = str(int(first) - int(temp))
            elif signage == "x":
                curr_display = str(int(temp) * int(first))
            elif signage == "/":
                curr_display = str(int(first) / int(temp))
            
            first = None    
            
        curr_display = '{:,}'.format(int(curr_display) )
        label.config(text = curr_display)

# ok now we need 5 rows and 4 columns of buttons -> 5x4
# nvm making it > 10 rubs the boxes in the wrong way
myFont = font.Font(size=15)

button_ac = tk.Button(window,
    text="Clear",
    width=11,
    height=3,
    bg="#8f8d8b",
    fg="white", command = partial(add_to_display, "del")
)
button_ac.grid(row = 2, column=0, sticky= 'NSEW')
# button_ac['font'] = myFont

# currently i have a char is ~21 pixels
# idk if this method will transfer to others

# button_ac.place(x=0, y = 106)

button_7 = tk.Button(window,
    text="7",
    width=11,
    height=3,
    bg="blue",
    fg="white", command=partial(add_to_display, 7)
)
button_7.grid(row = 3, column= 0, sticky= 'NSEW')
# button_7['font'] = myFont

# button_7.place(x=0, y = 190)

button_4 = tk.Button(window,
    text="4",
    width=11,
    height=3,
    bg="blue",
    fg="white", command=partial(add_to_display, 4)
)
button_4.grid(row = 4, column= 0, sticky= 'W')
# button_4['font'] = myFont


button_1 = tk.Button(window,
    text="1",
    width=11,
    height=3,
    bg="blue",
    fg="white", command=partial(add_to_display, 1)
)
button_1.grid(row = 5, column= 0, sticky= 'NSEW')
# button_1['font'] = myFont



button_0 = tk.Button(window,
    text="0",
    width=11,
    height=3,
    bg="blue",
    fg="white", command=partial(add_to_display, 0)
)
button_0.grid(row = 6, column= 0, columnspan=2, sticky= 'NSEW')
# button_0['font'] = myFont

# smth cool i noticed is that u can leaving the last , in python and it won't give any errors
# but imma remove them just in case it isn't the same throughout other versions
button_sign = tk.Button(window,
    text="+/-",
    width=11,
    height=3,
    bg="#8f8d8b",
    fg="white", command = sign_change
)
button_sign.grid(row = 2, column= 1, sticky= 'NSEW')
# button_sign['font'] = myFont

button_percent = tk.Button(window,
    text="%",
    width=11,
    height=3,
    bg="#8f8d8b",
    fg="white",
).grid(row = 2, column= 2, sticky= 'NSEW')

button_divide = tk.Button(window,
    text="÷",
    width=11,
    height=3,
    bg="#f5a316",
    fg="yellow", command=partial(perform_action, "/")
)
button_divide.grid(row = 2, column= 3, sticky= 'NSEW')
# button_divide['font'] = myFont

button_8 = tk.Button(window,
    text="8",
    width=11,
    height=3,
    bg="blue",
    fg="yellow", command=partial(add_to_display, 8)
).grid(row = 3, column= 1, sticky= 'NSEW')

button_9 = tk.Button(window,
    text="9",
    width=11,
    height=3,
    bg="blue",
    fg="white", command=partial(add_to_display, 9)
).grid(row = 3, column= 2, sticky= 'NSEW')

button_x = tk.Button(window,
    text="x",
    width=11,
    height=3,
    bg="#f5a316",
    fg="white", command=partial(perform_action, "x")
).grid(row = 3, column= 3, sticky= 'NSEW')

button_5 = tk.Button(window,
    text="5",
    width=11,
    height=3,
    bg="blue",
    fg="white", command=partial(add_to_display, 5)
).grid(row = 4, column= 1, sticky= 'NSEW')

button_6 = tk.Button(window,
    text="6",
    width=11,
    height=3,
    bg="blue",
    fg="white", command=partial(add_to_display, 6)
).grid(row = 4, column= 2, sticky= 'NSEW')

button_minus = tk.Button(window,
    text="-",
    width=11,
    height=3,
    bg="#f5a316",
    fg="white", command=partial(perform_action, "-")
).grid(row = 4, column= 3, sticky= 'NSEW')

button_2 = tk.Button(window,
    text="2",
    width=11,
    height=3,
    bg="blue",
    fg="white", command=partial(add_to_display, 2)
).grid(row = 5, column= 1, sticky= 'NSEW')

button_3 = tk.Button(window,
    text="3",
    width=10,
    height=3,
    bg="blue",
    fg="white", command=partial(add_to_display, 3)
).grid(row = 5, column= 2, sticky= 'NSEW')

button_plus = tk.Button(window,
    text="+",
    width=10,
    height=3,
    bg="#f5a316",
    fg="white", command=partial(perform_action, "+")
).grid(row = 5, column= 3, sticky= 'NSEW')

button_period = tk.Button(window,
    text=".",
    width=10,
    height=3,
    bg="blue",
    fg="white", command=partial(perform_action, ".")
).grid(row = 6, column= 2, sticky= 'NSEW')

button_equal = tk.Button(window,
    text="=",
    width=10,
    height=3,
    bg="#f5a316",
    fg="white", command=partial(perform_action, "=")
).grid(row = 6, column= 3, sticky= 'NSEW')

window.mainloop()

