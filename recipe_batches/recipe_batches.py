#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients, batch_count=0):
    batch_count = batch_count
    if len(recipe) > len(ingredients):
        return batch_count

    # keys is name of ingredients
    for key in ingredients.keys():
        if ingredients[key] < recipe[key]:
            return batch_count
    else:
        ingredients[key] = ingredients[key] - recipe[key]
        batch_count += 1
        newIngr = ingredients

    return recipe_batches(recipe, newIngr, batch_count)


print('recipe made: ')
print(recipe_batches({'milk': 100, 'butter': 50, 'cheese': 10},
                     {'milk': 198, 'butter': 52, 'cheese': 10}))


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
