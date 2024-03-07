from stack import Stack

def base_convertor(dec_number,base):
    digits = '0123456789ABCDEF'
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base

    new_string = ''
    while not rem_stack.isEmpty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string

print(base_convertor(255,2))