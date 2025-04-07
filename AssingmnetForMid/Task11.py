def getSecondLargest(arr):
    unique_number=list(set(arr))
    unique_number.sort(reverse=True)
    if(len(unique_number)<2):
        return none;
    return unique_number[1];
number=list(map(int,input("ener the list of numbers separated by space ").split()))
print("The second largest number: ",getSecondLargest(number))