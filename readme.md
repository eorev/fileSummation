##  File summation program for CISC320

This program is a summation program that takes in a file and sums up the numbers in the file. The program will then output the sum of the numbers in the file.

My program works by first accepting a file name in the main.  
Then the main program will read the file and make a array of the lines.
The answer function then accepts the lines from main and will check the lines for specific cases.
The first case is to check if it is the first in the list and assigns the length variable to the first value.
Then if it is not the first value it will check if it is -999 our break case. 
If not the value is then added to the sum variable.
The answer function then returns the sum.

The runtime of the answer function would be O(n).  
The reason for this is that the answer function will go through the entire list of lines and check each line for the cases.
Since the function runs over the entire list and checks it would be duration of n.