def solution(numbers):
    size = len(numbers)
    arr = []
    for i in range(size-2):
        if numbers[i+2]:
            # a < b
            if (numbers[i] < numbers[i+1]):
                # b > c
                if (numbers[i+1] > numbers[i+2]):
                    arr.append(1)
                else:
                    arr.append(0)
            # a > b
            elif (numbers[i] > numbers[i+1]):
                # b < c
                if (numbers[i+1] < numbers[i+2]):
                    arr.append(1)
                else:
                    arr.append(0)
            else:
                arr.append(0)
                break
        else:
            break
    return arr
  
