input = 'input'

def main():
    sum_ = 0
    with open(input, 'rt') as input_file:
        for line in input_file.readlines():
            initial_fuel = int(line)//3 - 2
            more_fuel = initial_fuel//3 - 2
            while(more_fuel > 0):
                initial_fuel += more_fuel
                more_fuel = more_fuel//3 - 2
            sum_ += initial_fuel
    print(sum_)

if __name__ == '__main__':
    main()
