# powerball
Powerball Random Number Generator


The object of this project is to generate five random numbers that range from 1-69 and a powerball number that ranges from 1-26.
I found a library online that generates random numbers for powerball, but over time, I have found some commonalities across the numbers.

For example,  I noticed that in practically every drawing, at least three numbers are within the same twenty digits.  If the first number is a lower number (between 1 and 20) then the next two numbers are less than 30.  Also, in almost every drawing the first five numbers contain either two even and three odd numbers, or three even and two odd numbers. My objective is to impliment this sequence into the existing library I am using.
