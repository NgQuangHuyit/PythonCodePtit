def is_palindrome(num_str):
    return num_str == num_str[::-1]


def count_palindromes_in_all_bases(a, b, M):
    count = 0
    for num in range(a, b + 1):
        is_palindrome_in_all_bases = True
        for base in range(2, M + 1):
            num_str_base = ''
            while num > 0:
                num, remainder = divmod(num, base)
                num_str_base += str(remainder)

            if not is_palindrome(num_str_base):
                is_palindrome_in_all_bases = False
                break

        if is_palindrome_in_all_bases:
            count += 1

    return count


# Nhập input
a, b, M = map(int, input().split())

# Đếm số thuận nghịch trong tất cả các cơ số từ 2 đến M
result = count_palindromes_in_all_bases(a, b, M)
print(result)