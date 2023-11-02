import timeit
import matplotlib.pyplot as plt



# q1. part a

def power_iterative(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def power_divide_and_conquer(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        half_pow = power_divide_and_conquer(base, exponent // 2)
        return half_pow * half_pow
    else:
        half_pow = power_divide_and_conquer(base, (exponent - 1) // 2)
        return half_pow * half_pow * base
    
    
    
# q1. part b

# Naïve Iterative Approach:

# In the naïve iterative approach, 
# we have a loop that runs exponent times. 
# So, the time complexity is O(exponent), 
# which is linear in terms of the exponent.

# Divide-and-Conquer Approach:

# In the divide-and-conquer approach, 
# we are effectively halving the problem at each step. 
# So, the number of operations required to compute 
# the power of a number is logarithmic in terms of the exponent. 
# The time complexity is O(log exponent).



# q1. part c

exponents = [5, 10, 100, 200, 500, 1000]
iterative_times = []
divide_conquer_times = []

for exponent in exponents:
    # Measure the time for the iterative approach
    iterative_time = timeit.timeit("power_iterative(2, " + str(exponent) + ")", globals=globals(), number=1000)
    iterative_times.append(iterative_time)

    # Measure the time for the divide-and-conquer approach
    divide_conquer_time = timeit.timeit("power_divide_and_conquer(2, " + str(exponent) + ")", globals=globals(), number=1000)
    divide_conquer_times.append(divide_conquer_time)

# Plot the results
plt.plot(exponents, iterative_times, label="Iterative")
plt.plot(exponents, divide_conquer_times, label="Divide & Conquer")
plt.xlabel("Exponent")
plt.ylabel("Execution Time (s)")
plt.legend()
plt.show()

# q1. part d

# The divide-and-conquer approach is indeed more efficient for large exponents, 
# as it grows at a logarithmic rate compared to the linear growth of the iterative approach. 