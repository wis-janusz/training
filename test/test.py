from sklearn.ensemble import BaggingRegressor
import beginner_problems
import statistics
#beginner_problems.number_guessing(20)

my_odd_list = [4,1,6,1,73,6,45,4,2,8,6,2,4,5,9,71,3]
my_even_list = my_odd_list[:-1]
one_mode_list = [0,1,2,3,4,4,5]
two_mode_list = [0,1,2,3,3,4,4,5]
no_mode_list = [0,1,2,3,4,5]

#print(beginner_problems.calc_mean(my_odd_list))
#print(statistics.mean(my_odd_list))

#print(beginner_problems.calc_median(my_odd_list))
#print(beginner_problems.calc_median(my_even_list))
#print(statistics.median(my_odd_list))
#print(statistics.median(my_even_list))

print(beginner_problems.calc_mode(one_mode_list))
print(statistics.multimode(one_mode_list))
print(beginner_problems.calc_mode(two_mode_list))
print(statistics.multimode(two_mode_list))
print(beginner_problems.calc_mode(no_mode_list))
print(statistics.multimode(no_mode_list))