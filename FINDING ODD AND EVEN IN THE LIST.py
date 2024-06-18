# Pracrical 1
# FINDING EVEN AND ODD
print("""PRINTING ODD AND EVEN NUMBERS IN THE GIVEN LIST
list1 = [10,21,4,45,66,93,2]
""")
list1 = [10,21,4,45,66,93,2]
even, odd = 0,0
for num in list1:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print(">>>EVEN NUMBERS IN THE LIST")
print("---Even number in the list",even)
print("")#....sample
print(">>> ODD NUMBERS IN THE LIST")
print("---Odd numbers in the list",odd)
