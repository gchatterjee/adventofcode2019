input = 'input'

def compute(noun, verb):
    ops = []
    with open(input, 'rt') as inputfile:
        ops = map(int, inputfile.read().split(','))
    i = 0
    ops[1] = noun
    ops[2] = verb
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
    return ops[0]

def main():
    for noun in range(100):
        for verb in range(100):
            if compute(noun, verb) == 19690720:
                print(100*noun + verb)
                return

if __name__ == '__main__':
    main()
