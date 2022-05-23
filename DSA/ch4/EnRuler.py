# Recursice English ruler

def er(n, cn=0):
    two = cn % 0.5 == 0 
    four = cn % 0.25 == 0
    eight = cn % 0.125 == 0  

    a = two and four and eight

    if int(cn) == cn:
        print(f'---- {cn}')
    elif two:
        print('---')
    elif four:
        print('--')
    elif eight:
        print('-')

    if cn != n:
            er(n, cn + 0.125)
er(5)