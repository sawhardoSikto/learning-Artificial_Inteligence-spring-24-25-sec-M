
#task9
def evencheck(number):
    even_number=[];
    for num in numbers:
        if (num%2==0):
            even_number.append(num);
    return even_number;
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("the even number is ",evencheck(numbers))


def get_grade(marks):
    if (90 <= marks <= 100):
        return "A"
    elif (80 <= marks <= 89):
        return "B"
    elif (70 <= marks <= 79):
        return "C"
    elif (60 <= marks <= 69):
        return "D"
    else:
        return "F"
    
marks = int(input("Enter your marks (0-100): "))
if (0 <= marks <= 100):
    grade = get_grade(marks)
    print(f"Your grade is: ",grade)
else:
    print("Invalid marks")
