def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    pow = 0
    sum = 0
    for digit in digits[::-1]:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base") 
        sum += digit * (input_base ** pow)
        pow += 1
    digits = []
    if sum == 0: return [0]
    quotient = sum
    while quotient > 0:
        quotient = sum // output_base
        digit = sum % output_base
        digits.append(digit)
        sum = quotient
    return digits[::-1]
