import random

# Generate a random 9-digit number
random_digits = ''
for i in range(9):
    random_digits += str(random.randint(0, 9))

weight_1 = 10
checksum_1 = 0

# Calculate the first verification digit
for digit in random_digits:
    checksum_1 += int(digit) * weight_1
    weight_1 -= 1

digit_1 = (checksum_1 * 10) % 11
digit_1 = digit_1 if digit_1 <= 9 else 0

# Append the first verification digit to the original number
digits_with_1 = random_digits + str(digit_1)

weight_2 = 11
checksum_2 = 0

# Calculate the second verification digit
for digit in digits_with_1:
    checksum_2 += int(digit) * weight_2
    weight_2 -= 1

digit_2 = (checksum_2 * 10) % 11
digit_2 = digit_2 if digit_2 <= 9 else 0

# Concatenate the original number with both verification digits
cpf_generated = f'{random_digits}{digit_1}{digit_2}'

# Print the generated CPF
print(cpf_generated)
