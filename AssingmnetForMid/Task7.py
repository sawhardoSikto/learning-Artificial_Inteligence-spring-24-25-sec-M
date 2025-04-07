#task7
def modify_list(numbers):
    print("The original list:", numbers)
    
    unique_numbers = list(set(numbers))
    print("The unique numbers:", unique_numbers)
    
    unique_numbers.sort(reverse=True)
    print("The reverse sorted list:", unique_numbers)

    modified_list = []
    for num in unique_numbers:
        if num % 3 != 0:
            modified_list.append(num)
    
    print("Modified list:", modified_list)
    return modified_list  


numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))


modify_list(numbers)
