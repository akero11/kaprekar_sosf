def get_extremes(number):
    sorted_ = sorted(number)

    asc = ''.join(sorted_[::-1])
    des = ''.join(sorted_)

    return(asc, des)


def fill(number, side = 'left'):
    digits = len(number)
    zeros = '0' * (4 - digits)

    full_number = (zeros + number) if side == 'left' else (number + zeros)

    return(full_number)


def kaprekar_routine(number):
    
    steps = 0

    if number != 6174:
        str_number = str(number)

        full_str_number = fill(str_number) if len(str_number) < 4 else str_number

        asc, desc = get_extremes(full_str_number)
        
        subtraction = ...

    return(steps)

def run():
    ...


if __name__ == '__main__':
    run()