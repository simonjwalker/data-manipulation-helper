def multiply(multiplicand:int, multiplier:int) -> int:
    product = multiplicand * multiplier
    return product

def divide(dividend:int,divisor:int) -> float:
    if dividend == 0:
        raise ZeroDivisionError("Cannot divide dividend by 0")
    else:
        quotient = divisor / dividend
        return quotient
