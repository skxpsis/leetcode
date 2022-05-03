# function for determining if a number is a happy number
def happy(num):
    # list to control when to stop iterating
    stop = [1]
    # square the number and input the number into the stop list
    while num not in stop:
        stop.append(num)
        num = sum(int(x)**2 for x in str(num))
    # return 1 if the number is a happy number, 0 if otherwise
    if num == 1:
        is_happy = 1
    else:
        is_happy = 0
    return is_happy
    
# call the happy() function and return the value
for line in sys.stdin:
    line = int(line)
    happy_value = happy(line)
    print(happy_value, end="")
