from math import sqrt
def prime(arg):
    try:
        arg = int(arg)
    except ValueError:
        return False
    if isinstance(arg,int) and 0 < arg < 10000000:
        sqrt_arg = int(sqrt(arg))
        for i in range(2, sqrt_arg+1):
            if arg % i == 0:
                return False
            else:
                pass
        return True
    else:
        return False 