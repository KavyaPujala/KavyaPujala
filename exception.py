def divide(a, b):
    try:
        r=a/b
        return r
    except ZeroDivisionError as e:
        print("error")
        return None
numerator=10
denominator=0
result=divide(numerator,denominator)
if result is not None:
    print("result",result)