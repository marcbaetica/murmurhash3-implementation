def make_ascii_table():
    for i in range(0, 128):
        # print(f'{i}, {chr(i):>10}')   # '|| 65,          A'
        # print(f'{i}, {chr(i):^10}')   # '|| 65,     A     '
        # print(f'{i}, {chr(i):<12}')   # '|| 65, A           '
        # print(f'{i:<10}, {chr(i)}')     # '|| 65        , A' 
        # str() because a type object does not support string formatting.
        # <class 'str'> <class 'int'> <class 'str'> <class 'str'>
        print(f'{str(type(chr(i))):^5} {str(type(i)):^5} {str(type(hex(i))):>5} {str(type(bin(i))):>12}')
        print(f'{chr(i):^5} {i:^5} {hex(i):>5} {bin(i):>12}')   # '  A    65    0x41    0b1000001'


make_ascii_table()

