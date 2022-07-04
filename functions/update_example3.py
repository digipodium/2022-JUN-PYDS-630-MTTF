def area_of_triangle(a,b,c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area



if __name__ == '__main__':
    print(area_of_triangle(3,4,5))