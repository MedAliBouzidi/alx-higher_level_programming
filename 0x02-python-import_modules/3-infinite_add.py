#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    total = 0
    count = len(sys.argv) - 1
    for index in range(count):
        total += int(sys.argv[index + 1])
    print("{}".format(total))
