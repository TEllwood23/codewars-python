def rgb(r, g, b):
        return convert_to_hex(r) + convert_to_hex(g) + convert_to_hex(b)

def convert_to_hex(num):
    hex_dict = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    if num < 1:
        final_hex = '00'
    elif num > 255:
        final_hex = 'FF'
    else:
        quotient = num//16
        remain = num % 16
        final_hex = hex_dict[quotient] + hex_dict[remain]

    return final_hex

print(rgb(0, 0, 0))
print(rgb(255, 255, 255))
print(rgb(-20, 275, 125))
