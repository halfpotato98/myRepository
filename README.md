# Reflection
Reflection for Grocery Frequencies

In this project I was tasked with creating a program that uses C++ (Source.cpp) and Python (PythonCode.py) to help grocery store owners quantify products sold.  The user has four options: print a list of product frequencies, display a particular frequency, display a histogram of the data, or quit.  

I started option 1 by taking a look at the input file; just a text file of individual products in the order they were purchased.  I built a Python function to read each line and add each line to a list.  I then utilized the "Counter" function to create a dictionary of how many of each product were purchased.  I then ordered this dictionary in descending order by value using the "sorted" function.  I then printed each key and value of the dictionary.

For option 2, I asked the user for an input in C++ and passed that to Python a separate Python function.  While in this python function I again created a list and a counted dictionary.  I then returned the value for the specific key input.  If the input did not match a key, capitalization notwithstanding, the function simply returns 0.  C++ then prints the input and the number returned.

For the third option, I printed a histogram of the data.  This was accomplished by printing each food type and an "=" for the quantity purchased.  This was accomplished with a simple "for" loop.  As part of this function I also output a text file of product frequencies (outputFrequencies.txt) and read the data for the histogram from this text file.

The fourth option is a simple quit process.  This was accomplished with a "while" loop.

The thing I did best was keeping the code to a minimum.  I used a few Python functions such as "Counter" and "sorted" that made the code much more concise and easy to read.  I could enhance my code by only including the code to create the list and dictionary once, and by checking the memory to see if the list has already been created, and if so, use it.  This could be done perhaps by having the Python functions call another function.  This would save memory and time.  The piece of code I found most difficult to write was the portion that linked C++ and Python.  This portion was written for us but required some understanding, edits, and seemed to have a folder problem.  This might have been related to the folder location of the different files.  They need to all be in the same folder to be able tofind each other. I was able to get the program to run by restarting the virtual machine.  Dialogue with other students and the professor was important towards figuring out this problem.  Skills improved while writing this program include organization, communication, and experience with Python's vast library of functions. I made this program maintable by including in-line comments.  I made it readable by keeping the code concise and using industry standard variable names.  I made the program adaptable by separating each function based on user choice.





