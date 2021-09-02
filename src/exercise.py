def main():
    #write your code below this line
    count = 0
    sum = 0
    while True:
        num = int(input("Give a number:"))
        if (num != 0):
            count += 1
            sum += num
        else:
            break
    print("Average of numbers: " + str(sum / count))

if __name__ == '__main__':
    main()
