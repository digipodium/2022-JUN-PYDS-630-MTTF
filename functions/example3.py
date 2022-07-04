def area_of_triangle():
    a = int(input("Enter the length of side a: "))
    b = int(input("Enter the length of side b: "))
    c = int(input("Enter the length of side c: "))
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("The area of the triangle is: ", area)

def area_of_circle():
    r = int(input("Enter the radius of the circle: "))
    area = 3.14 * r ** 2
    print("The area of the circle is: ", area)  

def area_of_rectangle():
    l = int(input("Enter the length of the rectangle: "))
    w = int(input("Enter the width of the rectangle: "))
    area = l * w
    print("The area of the rectangle is: ", area)

def menu():
    '''
    shows a menu to calculate the area of a shape
    that is selected by the user.
    '''
    print("1. Area of a triangle")
    print("2. Area of a circle")
    print("3. Area of a rectangle")
    print("4. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        area_of_triangle()
    elif choice == 2:
        area_of_circle()
    elif choice == 3:
        area_of_rectangle()
    elif choice == 4:
        print("Goodbye")
    else:
        print("Invalid choice")
        menu()

if __name__ == "__main__":
    menu()



