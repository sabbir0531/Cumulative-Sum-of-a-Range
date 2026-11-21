print("Current number and previous number sum in a range(10)")
previous_number = 0

# loop from 0 to 9
for i in range(10):
    x_sum = i + previous_number
    print(f"Current number {i} Previous number {previous_number} and Sum: {x_sum} ")

    #update the previous number next iteration
    previous_number = i