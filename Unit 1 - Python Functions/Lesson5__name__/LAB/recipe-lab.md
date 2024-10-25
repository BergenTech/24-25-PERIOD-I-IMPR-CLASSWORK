# Python Recipe Lab
## Practice with Recipes and Test Kitchens!

## Setup
1. Create a new folder called `my_kitchen`
2. Make two Python files:
   - `recipes.py` (your cookbook)
   - `make_dinner.py` (where you'll cook)

## Part 1: Basic Recipes
Open `recipes.py` and start with this code:

```python
# recipes.py
def make_sandwich(ingredient1, ingredient2):
    return f"A sandwich with {ingredient1} and {ingredient2}"

# Test Kitchen
if __name__ == '__main__':
    print("👩‍🍳 Testing sandwich recipe:")
    test_sandwich = make_sandwich("ham", "cheese")
    print(test_sandwich)
```

### 👉 Lab Task 1: Run Your Test Kitchen
1. Save and run `recipes.py`
2. You should see:
   ```
   👩‍🍳 Testing sandwich recipe:
   A sandwich with ham and cheese
   ```

### 👉 Lab Task 2: Add More Recipes
Add these recipes:
```python
def make_salad(veggie1, veggie2):
    return f"A fresh salad with {veggie1} and {veggie2}"

def make_juice(fruit):
    return f"Fresh {fruit} juice"
```

Add tests in your test kitchen:
```python
if __name__ == '__main__':
    # Your sandwich test...
    
    print("\n👩‍🍳 Testing salad recipe:")
    print(make_salad("tomato", "cucumber"))
    
    print("\n👩‍🍳 Testing juice recipe:")
    print(make_juice("orange"))
```

## Part 2: Cook Dinner
Create `make_dinner.py`:

```python
# make_dinner.py
import recipes

# Let's make dinner!
meal = recipes.make_sandwich("turkey", "lettuce")
side = recipes.make_salad("carrot", "spinach")
drink = recipes.make_juice("apple")

print("Tonight's dinner:")
print(meal)
print(side)
print(drink)
```

### 👉 Lab Task 3: Compare Running Both Files
Run each file and see what's different:
1. `recipes.py` - shows all your kitchen tests
2. `make_dinner.py` - only shows dinner

## Part 3: Create Your Own Recipes!

### 👉 Lab Task 4: Add These Recipes
```python
def make_soup(ingredient):
    # Make a soup recipe here!
    pass

def make_special(main, side, drink):
    # Create a special meal combination
    pass
```

Add tests:
```python
if __name__ == '__main__':
    # Your other tests...
    
    print("\n👩‍🍳 Testing soup recipe:")
    print(make_soup("chicken"))
    
    print("\n👩‍🍳 Testing special meal:")
    print(make_special("fish", "rice", "lemonade"))
```

## Bonus Challenges! 🌟

### Challenge 1: Make a Recipe Rating System
```python
def rate_recipe(recipe_name, stars):
    if stars > 4:
        return f"⭐⭐⭐⭐⭐ {recipe_name} was amazing!"
    else:
        return f"⭐⭐⭐ {recipe_name} was good!"
```

### Challenge 2: Create a Secret Recipe
Make your own special recipe with a fun twist!

## Debug Help 🔍
If something's not working:
1. Are both files in the same folder?
2. Did you save all changes?
3. Check your spelling and punctuation
4. Make sure indentation is correct

## Show Your Work! 🎉
Show your teacher:
1. Your test kitchen results
2. Your dinner menu
3. Any special recipes you created

## Extra Credit 🌟
Try to:
- Add emoji to your recipes
- Create breakfast and lunch menus
- Make a recipe that combines other recipes
