starting_cows = 2
target_time = 90

def count_cows(starting_n, t):
    cow_dict = {0:0, 1:0, 2:0, 3:0, 4:starting_n}
    steps = 1+t//5
    
    for _ in range(steps):
        cow_dict[4] = cow_dict[4]+cow_dict[3]
        cow_dict[3] = cow_dict[2]
        cow_dict[2] = cow_dict[1]
        cow_dict[1] = cow_dict[0]
        cow_dict[0] = cow_dict[4]//2

    return cow_dict[4]

adult_cows = count_cows(starting_cows, target_time)

print(f'After {target_time} minutes, starting with {starting_cows}, there will be {adult_cows} adult cows.')
   
