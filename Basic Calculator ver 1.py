def operations(*number):
    def add(*number):
        result = 0
        for i in number:
            result = result + i
        return result
    def sub(*number):
        result1 = number[0]
        for i in number[1:]:
            result1 = result1 + (-i)
        return result1

    def mul(*number):
        result2 = 1
        for i in number:
            result2 = result2 * i
        return result2

    def div(*number):
        result3 = number[0]
        number = number[1:]
        for i in number:
            result3 = result3 / i
        return result3
    add=add(*number)
    sub=sub(*number)
    mul=mul(*number)
    div=div(*number)
    Cal=[add,sub,mul,div]
    return Cal
Calname=["Addition","Subtraction","Multiplication","Division"]
ans=operations(24,8,3)
print(ans)