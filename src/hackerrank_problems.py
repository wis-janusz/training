import timeit
#Matrix flipping game

example = [[1,2,3,4],[10,10,10,10],[15,14,13,12],[5,6,7,8]]
big_example = [list(range(1000))]*1000
def flip_matrix(arr):

    max_quad = []
    for i in range(len(arr)//2):
        for j in range(len(arr)//2):
            max_quad.append(max([arr[i][j], arr[i][-j-1], arr[-i-1][j], arr[-i-1][-j-1]]))
    
    return sum(max_quad)

def flip_matrix_with_flatten(arr):

    n = len(arr)//2

    ul_quad = [row[:n] for row in arr[:n]]
    ur_quad = [row[n:] for row in arr[:n]]
    ll_quad = [row[:n] for row in arr[n:]]
    lr_quad = [row[n:] for row in arr[n:]]

    ur_quad = [list(reversed(row)) for row in ur_quad]
    ll_quad = reversed(ll_quad)
    lr_quad = [list(reversed(row)) for row in list(reversed(lr_quad))]

    ul_quad = [number for row in ul_quad for number in row]
    ur_quad = [number for row in ur_quad for number in row]
    ll_quad = [number for row in ll_quad for number in row]
    lr_quad = [number for row in lr_quad for number in row]

    return sum(map(max, zip(ul_quad, ur_quad, ll_quad, lr_quad)))

print(timeit.timeit('[func(big_example) for func in (flip_matrix,)]', globals=globals(), number=100))
print(timeit.timeit('[func(big_example) for func in (flip_matrix_with_flatten,)]', globals=globals(), number=100))
