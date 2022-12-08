Learning project to better understand different widgets for Tkinter framework in python And to better understand how git and github works in general

files include a main.py which is all you need to download and run

This simulates a calculator application similar to an app you might find on any IOS device in its horizontal state.

NOTE: I only tested this on two different screens and they look as intended on them. This may not be the case for alternative screen sizes

The window is also set the be the size it is opened in to prevent more hassle with sizing

The maximum number of digits you can input and display at once is 9 However, you can bypass the amount displayed by performing operations that exceed the limit

This is very simple to resolve as I can change the display to ressemble "{:2e}".format(temp) Then to keep track of the actual value, I can

have a variable that tracks the actual value and perform the operations that hopefully do not exceed the limit
or do something similar to "{:.8f}".format(float(temp)) then add the commas again to better visualize the number for the user However, I did not implement this as the main purpose was to better my understanding of the Tkinter framework that is provided in the python library
As stated above, since this project served to develop my understanding of Tkinter, the objects, functions, and variables are all over the place and are messy at times Since the numerical buttons are all similar, only differing by value and appearance, it is feasible to create them in a for_loop and assign their respective action to declutter the program. In addition, that would allow easy changes in each button to be made across all of them. However, since the application functions as intended and I do not plan on changing them anymore, it is not necessary to apply this change.

My process for designing this:

Drew what I intended the application to look like
Listed any functions, objects, and variables that I might need
Implemented each feature and tested along the way
Implement more features and test new and old to make sure it didn't break
Debugged anything that is needed
Hope you enjoy!
