input = 'input'

def main():
    sum_ = 0
    with open(input, 'rt') as input_file:
        for line in input_file.readlines():
            sum_ += int(line)//3 - 2
    print(sum_)

if __name__ == '__main__':
    main()
