import argparse

# other code. . .


def main(args):
    print(args.accumulate(args.integers))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some input data')
    parser.add_argument('integers',
                        metavar='N',
                        type=int,
                        nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum',
                        dest='accumulate',
                        action='store_const',
                        const=sum,
                        default=max,
                        help='sum the integers (default: find the max)')
    main(parser.parse_args())