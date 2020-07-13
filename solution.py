# Write a program determine whether the given number is Armstrong number or not.
# The program should return true or false

def checkArmstrong(num):
    # Your code goes here
    l = len(str(num))
    t = num
    for i in range(0, l):
        sum = 0
        a = t % 10
        sum = sum + (a ** l)
        t = t / 10
        if sum == num:
            return True
        else:
            return False
