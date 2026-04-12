# fraction to recurring decimal
def fraction_to_decimal(numerator, denominator):
    if numerator == 0:
        return "0"
    
    result = []
    
    # handle sign
    if (numerator < 0) ^ (denominator < 0):
        result.append("-")
    
    numerator = abs(numerator)
    denominator = abs(denominator)
    
    # integer part
    result.append(str(numerator // denominator))
    remainder = numerator % denominator
    
    if remainder == 0:
        return ''.join(result)
    
    result.append(".")
    
    # fractional part
    remainder_map = {}
    while remainder and remainder not in remainder_map:
        remainder_map[remainder] = len(result)
        remainder *= 10
        result.append(str(remainder // denominator))
        remainder %= denominator
    
    if remainder:
        result.insert(remainder_map[remainder], "(")
        result.append(")")
    
    return ''.join(result)

print("1/2 =", fraction_to_decimal(1, 2))
print("2/3 =", fraction_to_decimal(2, 3))
print("4/333 =", fraction_to_decimal(4, 333))


# integer to english words
def number_to_words(num):
    if num == 0:
        return "Zero"
    
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", 
             "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", 
            "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]
    
    def helper(n):
        if n == 0:
            return ""
        elif n < 10:
            return ones[n] + " "
        elif n < 20:
            return teens[n-10] + " "
        elif n < 100:
            return tens[n//10] + " " + helper(n%10)
        else:
            return ones[n//100] + " Hundred " + helper(n%100)
    
    result = ""
    i = 0
    
    while num > 0:
        if num % 1000 != 0:
            result = helper(num % 1000) + thousands[i] + " " + result
        num //= 1000
        i += 1
    
    return result.strip()

print("123 ->", number_to_words(123))
print("12345 ->", number_to_words(12345))
print("1234567 ->", number_to_words(1234567))
