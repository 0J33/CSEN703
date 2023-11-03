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

# q1. part c

# exponents = [1, 10, 100, 1000, 10000, 1000000] # can't run 10^6 because it takes a long time
exponents = [1, 10, 100, 1000, 10000]
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