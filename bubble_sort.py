def bubble(array):
    for i in array:
        for j in (array - i):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff


def main():
    array = [{1, 5, 4 , 8, 123, 10}]
    bubble(array)
    print(array)

if __name__ == '__main__':
    main()