def reverse_no(n):
    reverse_no = 0
    while n > 0:
        digit = n % 10
        reverse_no = reverse_no * 10 + digit
        n = n // 10
    return reverse
  
num = 1234
print("Reversed:", reverse_number(num))
