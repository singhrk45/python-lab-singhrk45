try:
    n=int(input())
    b=int(input())
    a=input()
    c=n+b
    l=a+b
    n.append(3)
except ValueError:
    raise ValueError('value error occurred')
except TypeError:
    raise TypeError('Type error occurred')
except:
    raise AttributeError(' Attribute error occurred ')