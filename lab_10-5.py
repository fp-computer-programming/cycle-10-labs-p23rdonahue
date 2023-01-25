#author: RED 1/25/23

def add_foods(foods):
    sixth_letter=[]
    not_foods=[]
    short_foods=[]
    for food in foods:
        try:
        
            sixth_letter.append(food[5])
        
        except TypeError:
            not_foods.append(food)
        
        except IndexError:
            short_foods.append(food)
    print(f'sixth_letter: {sixth_letter}')
    print(f'not_foods: {not_foods}')
    print(f'short_foods: {short_foods}')    

add_foods(['potatoes','salsa','cherries','banana','apple'])
add_foods(['naan','celery','buckwheat',7,'clementine'])
add_foods(['cheeseburger',True, 'chicken','rice','radish'])
