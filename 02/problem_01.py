input = 'input'

def main():
    ops = []
    with open(input, 'rt') as inputfile:
        ops = map(int, inputfile.read().split(','))
    i = 0
    ops[1] = 12
    ops[2] = 2
    while i < len(ops):
        if ops[i] == 1:
            ops[ops[i+3]] = ops[ops[i+1]] + ops[ops[i+2]]
            i += 4
        elif ops[i] == 2:
            ops[ops[i+3]] = ops[ops[i+1]] * ops[ops[i+2]]
            i += 4
        elif ops[i] == 99:
            break
        else:
            raise Exception('Unexpected opcode')
    print(ops[0])

if __name__ == '__main__':
    main()
