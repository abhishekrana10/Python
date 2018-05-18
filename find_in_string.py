if __name__ == '__main__':
    s = input()
    alphanum = False
    for i in s:
        if i.isalnum():
            alphanum = True
            break
        else:
            pass
    print(alphanum)
    alpha = False
    for i in s:
        if i.isalpha():
            alpha = True
            break
        else:
            pass
    print(alpha)
    digit = False
    for i in s:
        if i.isdigit():
            digit = True
            break
        else:
            pass
    print(digit)
    lower = False
    for i in s:
        if i.islower():
            lower = True
            break
        else:
            pass
    print(lower)
    upper = False
    for i in s:
        if i.isupper():
            upper = True
            break
        else:
            pass
    print(upper)
