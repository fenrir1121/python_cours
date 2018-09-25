import sys

if len(sys.argv) > 1:
	digit_string = sys.argv[1]
else:
	digit_string = "872"

def sum_digit_in_string(s):
    result = 0
    for digit in s:
        result += int(digit)
    return (result)

print(sum_digit_in_string(digit_string))
