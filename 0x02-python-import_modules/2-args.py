#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_args = len(argv) - 1

    if num_args == 0:
        print("0 arguments.")
    else:
        plural_s = 's' if num_args > 1 else ''
        print("{} argument{}:".format(num_args, plural_s))

        for i in range(1, num_args + 1):
            print("{}: {}".format(i, argv[i]))

