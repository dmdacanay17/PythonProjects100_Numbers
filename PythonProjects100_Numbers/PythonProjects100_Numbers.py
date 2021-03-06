import math

#Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.
def piToNthDigit(n):
    return False
#Find e to the Nth Digit - Just like the previous problem, but with e instead of PI. Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.
def eToNthDigit(n):
    return math.e

#Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
def fibonacci(n):
    fib = [0,1]
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    for i in range(2,n+1):
        fib.append(fib[i-2]+fib[i-1])
    return fib

#Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
def primeFact(n):
    factors = []
    k = 2
    while n > 1:
        if n % k == 0:
            factors.append(k)
            n = n/k
            k = 2
        else:
            k = k + 1
    return factors

#Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
def primeNumber():
    goOn = "y"
    cur = 1
    while goOn == "y":
        cur = cur + 1
        if goOn == "y":
            while( not isPrime(cur)):
                cur = cur + 1
        print(cur)
        goOn = input(str("Find Next Prime? (y)"))

def isPrime(n):
    for i in range(2,n):
        if n%i == 0 and i < n/2+1:
            return False
    return True

#Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.
def tileCost(w,h,cost):
    return w*h*cost

#Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
def mortgageCalc(mortgage, terms, interest, interval):
    return False

#Change Return Program - The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
def changeBack(cost, given):
    change ={
        "quarters":0,
        "dimes":0,
        "nickles":0,
        "pennies":0
        }
    dif = given - cost
    while dif > 0.0:
        if dif >= 0.25:
            change["quarters"]+=1
            dif -= 0.25
        elif dif >= 0.10:
            change["dimes"]+=1
            dif -= 0.10
        elif dif >= 0.05:
            change["nickles"]+=1
            dif -= 0.05
        else:
            change["pennies"]+= 1
            dif -= 0.01
    return change

#Binary to Decimal and Back Converter - Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
def binConverter(key, num):
    num = int(num)
    if num == 0:
        return 0
    if key == "dec":
        bin = ""
        while num > 0:
            bin += str(num%2)
            num = int(num/2)
        return bin[::-1]
    elif key == "bin":
        bin = str(num)
        bin = bin[::-1]
        dec = 0
        for i in range(0, len(bin)):
            dec += int(bin[i])* (2**i)
        return dec

#Calculator - A simple calculator to do basic operators. Make it a scientific calculator for added complexity.
def calculator(equation):
    try:
        equation = equation.replace(" ","")
        if(equation.count("(") != equation.count(")")):
            return "Error"
        while "(" in equation:
            open = []
            clo = []
            open.append(equation.find("("))
            i = open[0]+1
            while len(open) != len(clo):
                if str(equation[i]) == "(":
                    open.append(i)
                elif str(equation[i]) == ")":
                    clo.append(i)
                i += 1
            equation = equation[0:open[0]] + calculator(equation[open[0]+1:clo[len(clo)-1]]) + equation[clo[len(clo)-1]+1::]
        ops = []
        for i in range(0, len(equation)-1):
            if i > len(equation)-1:
                break
            c = str(equation[i])
            if c == "*" or c == "/" or c == "+" or c == "-" or c == "%":
                if str(equation[i+1]) =="*":
                    ops.append("**")
                    equation = equation.replace("**", " ", 1)
                else:
                    ops.append(c)
                    equation = equation.replace(c, " ", 1)
        nums = equation.split(' ')
        while "**" in ops:
            i = ops.index("**")
            nums[i] = str(float(nums[i]) ** float(nums[i+1]))
            ops.pop(i);
            nums.pop(i+1)
        while "/" in ops or "*" in ops or "%" in ops:
            indexes = []
            if "/" in ops:
                indexes.append(ops.index("/"))
            if "*" in ops:
                indexes.append(ops.index("/"))
            if "%" in ops:
                indexes.append(ops.index("%"))
            indexes.sort()
            i = indexes[0]
            if ops[i] == "/":
                nums[i] = str(float(nums[i]) / float(nums[i+1]))
                ops.pop(i);
                nums.pop(i+1)
            elif ops[i] == "*":
                nums[i] = str(float(nums[i]) * float(nums[i+1]))
                ops.pop(i);
                nums.pop(i+1)
            else:
                nums[i] = str(float(nums[i]) % float(nums[i+1]))
                ops.pop(i);
                nums.pop(i+1)


        while "+" in ops or "-" in ops:
            indexes = []
            if "+" in ops:
                indexes.append(ops.index("+"))
            if "-" in ops:
                indexes.append(ops.index("-"))
            indexes.sort()
            i = indexes[0]
            if ops[i] == "+":
                nums[i] = str(float(nums[i]) + float(nums[i+1]))
                ops.pop(i);
                nums.pop(i+1)
            else:
                nums[i] = str(float(nums[i]) - float(nums[i+1]))
                ops.pop(i);
                nums.pop(i+1)
        return nums[0]
    except:
        return "Error: wrong format"

#Unit Converter (temp, currency, volume, mass and more) - Converts various units between one another. The user enters the type of unit being entered, the type of unit they want to convert to and then the value. The program will then make the conversion.
#Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
#Distance Between Two Cities - Calculates the distance between two cities and allows the user to specify a unit of distance. This program may require finding coordinates for the cities like latitude and longitude.
#Credit Card Validator - Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number (look into how credit cards use a checksum).
#Tax Calculator - Asks the user to enter a cost and either a country or state tax. It then returns the tax plus the total cost with tax.
#Factorial Finder - The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. Solve this using both loops and recursion.
def factorialLoop(n):
    if n == 0:
        return 0
    fact = 1;
    for i in range(1, n+1):
        fact *= i;
    return fact;

def factorialRecursion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return n * factorialRecursion(n-1);

#Complex Number Algebra - Show addition, multiplication, negation, and inversion of complex numbers in separate functions. (Subtraction and division operations can be made with pairs of these operations.) Print the results for each operation tested.
#Happy Numbers - A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.
#Number Names - Show how to spell out a number in English. You can use a preexisting implementation or roll your own, but you should support inputs up to at least one million (or the maximum value of your language's default bounded integer type, if that's less). Optional: Support for inputs other than positive integers (like zero, negative integers, and floating-point numbers).
#Coin Flip Simulation - Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.
#Limit Calculator - Ask the user to enter f(x) and the limit value, then return the value of the limit statement Optional: Make the calculator capable of supporting infinite limits.
#Fast Exponentiation - Ask the user to enter 2 integers a and b and output a^b (i.e. pow(a,b)) in O(lg n) time complexity.