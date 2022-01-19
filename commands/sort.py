sort_type = input("Which variant of sort do you want to use('1' or '2')?: ")

class sort1:
    def sort():
        """Sorting using inbuilt packages"""
        
        numbers = input('Please enter the numbers: ')
        type = input("Ascending or Descending order: ")
        list = numbers.split(',')

        for number in range(0 , len(list)):
            list[number] = int(list[number])
        list.sort()

        if type == 'ascending':
            pass
        elif type == 'descending':
            list.reverse()

        def convert(list_of_numbers):
            integer = [str(i) for i in list_of_numbers]

            result = ", ".join(integer)
            return result

        print('Here is the sorted list of numbers: ' + convert(list))
        print('The highest number: ' + str(max(list)))
        print('The lowest number: ' + str(min(list)))


class sort2:
    def sort():
        """Sorting using algorithms"""

        def BubbleSort(inputList):
            for _ in range(len(inputList)):
                for index in range(len(inputList)):

                    if index < (len(inputList) - 1):
                        if int(inputList[index]) > int(inputList[index + 1]):
                            inputList[index], inputList[index + 1] = inputList[index + 1], inputList[index]

                    if index > 0:
                        if int(inputList[index]) < int(inputList[index - 1]):
                            inputList[index], inputList[index - 1] = inputList[index - 1], inputList[index]

            return inputList

        if __name__ == "__main__":
            intList = input('Please enter the numbers: ').split(",")
            type = input("Ascending or Descending order: ").lower()
            intList = BubbleSort(intList)
            if type == "descending": intList.reverse()
            print(",".join(intList))


if sort_type == "1":
    sort = sort1
    sort.sort()
elif sort_type == "2":
    sort = sort2
    sort.sort()
