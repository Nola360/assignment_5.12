#Akinola Daramola Jr
#Programming Exercise 5.12
#Due Date: 07/20/2022

"""    
Maximum of Two Values
Write a function named max that accepts two integer values as arguments and returns the value that is the greater of the two.
For example, if 7 and 12 are passed as arguments to the function, the function should return 12.
Use the function in a program that prompts the user to enter two integer values.
The program should display the value that is the greater of the two

"""


#Defining main function
def main():

    int1 = int(input("Enter a number: "))
    int2 = int(input("Enter another number: "))



    #Storing max function in variable 
    greater_number = max(int1, int2)

    #Displaying result of return statement 
    print(f"Greater Number: {greater_number:,}")


#Defining function with two paramenters (int1 & int2) to determine which integer is greatest
def max(int1, int2):
    #If statment to compare the integers
    if int1 > int2:
        return int1 #returns int1 if larger
    else:
        return int2 #returns int2 if larger
   
    
        


#Calling main function to invoke return statement function
main()



