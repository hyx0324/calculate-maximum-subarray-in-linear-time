import numpy as np


def find_maximum_subarray(A, length):
    low = 0
    high = 0
    sub_low = 0
    sum = A[0]
    sub_sum = A[0]

    for i in range(1, length):
        if sub_sum < 0:
            sub_sum = 0
            sub_low = i

        if A[i] < 0:
            sub_sum += A[i]

        else:
            if A[i] + sub_sum >= sum:
                sum = A[i] + sub_sum
                low = sub_low
                high = i
                sub_sum += A[i]

    return low, high, sum


if __name__ == '__main__':
    A_size = 10
    A = list(np.random.randint(-100, 100, size=A_size))
    low, high, sum = find_maximum_subarray(A, len(A))

    print('The original list is:', A)
    print('\nThe maximum subarray is:', A[low: high + 1])
    print('\nThe sum is:', sum)