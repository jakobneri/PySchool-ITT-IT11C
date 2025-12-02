target = int(input("Enter a number to count to: "))
stepSize = float(input("Enter the step size: ")) 
counter = 0


if target < 0:
    while counter >= target:
        print(counter)
        counter -= stepSize

else:
    while counter <= target:
        print(counter)
        counter += stepSize