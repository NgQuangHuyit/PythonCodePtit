def count_digit_frequency(A, B):
    digit_frequency = [0] * 10

    for digit in range(10):
        power_of_10 = 1
        while B // power_of_10 > 0:
            divisor = power_of_10 * 10
            quotient = B // divisor
            remainder = B % divisor
            count = quotient * power_of_10

            if remainder >= power_of_10:
                count += min(max(0, remainder - power_of_10 * digit + 1), power_of_10)

            if A > 0:
                quotient = (A - 1) // divisor
                remainder = (A - 1) % divisor
                count -= quotient * power_of_10

                if remainder >= power_of_10:
                    count -= min(max(0, remainder - power_of_10 * digit + 1), power_of_10)

            digit_frequency[digit] += count
            power_of_10 *= 10

    return digit_frequency


for t in range(int(input())):
    A, B = map(int, input().split())
    print(*count_digit_frequency(A, B))
