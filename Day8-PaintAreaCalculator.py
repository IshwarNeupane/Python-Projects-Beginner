import math
def paint_area(height, width, coverage):
    total_paint = math.ceil ((height * width) / coverage)
    print(f"You will need {total_paint} cans of paint.")
    
test_h= int(input("Height of wall: "))
test_w= int(input("Width of wall: "))
test_c= int(input("Coverage of paint: "))
# Calling the function.
paint_area(height= test_h,width= test_w,coverage= test_c)