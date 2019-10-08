# Machine Learning Class Week 4 Homework Answers

'''
0. Create a list containing five different sandwich ingredients, such as the following:
>>> ingredients = ['snails', 'leeches', 'gorilla belly-button lint', 'caterpillar eyebrows', 'centipede toes’]
Now create a loop that prints out the list (including the numbers):
>>> ingredients = ["ham","lettuce","tomatos","sauce","green pepper"]
Create the lists using the .append() method
'''
# --------------------------------Code between the lines!--------------------------------
ingredients = []
ingredients.append('snails')
ingredients.append('leeches')
ingredients.append('gorilla belly-button lint')
ingredients.append('caterpillar eyebrows')
ingredients.append('centipede toes')
print(ingredients)
ingredients2 = ["ham","lettuce","tomatos","sauce","green pepper"]

def print_ingredients(input_list):
    x = 1
    for i in ingredients:
        print('%s %s' % (x, i))
        x = x + 1

print_ingredients(ingredients)
print_ingredients(ingredients2)
# ---------------------------------------------------------------------------------------


'''
1. Your Weight on the Moon:
If you were standing on the moon right now, your weight would be
16.5 percent of what it is on Earth. You can calculate that by multiplying
your Earth weight by 0.165.
If you gained a kilo in weight every year for the next 15 years,
what would your weight be when you visited the moon each year
and at the end of the 15 years? 
Write a program using a for loop that prints your moon weight for each year.
'''
# --------------------------------Code between the lines!--------------------------------
earth_weight = 30
def weight_on_moon(weight):
    for year in range(1, 16):
        weight = weight + 1
        moon_weight = weight * 0.165
        print('Year %s is %s' % (year, moon_weight))

weight_on_moon(earth_weight)

# ---------------------------------------------------------------------------------------


'''
2. 
Instead of using math multiply op, please make use of range to do the multiplication. 
Hint: rang(start, end, step)  step is the increment to add. By default, it is 1.
Examples:
Input : n = 2, m = 3
Output :  6 
Input : n = 3, m = 4
Output :  12
'''
# --------------------------------Code between the lines!--------------------------------
def multiplication(n, m):
    result = 0
    for i in range(0, m):
        result = result + n
    print(result)
    return result
    
multiplication(2,3)
multiplication(3,4)
# ---------------------------------------------------------------------------------------
