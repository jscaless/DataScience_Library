import pandas as pd

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame(data=[[30,21]],columns=['Apples','Bananas'])
fruit_sales = pd.DataFrame(data=[[35,21],[41,34]],index=['2017 Sales','2018 Sales'],columns=['Apples','Bananas'])
ingredients = pd.Series(data=['4 cups','1 cup','2 large','1 can'],index=['Flour','Milk','Eggs','Spam'],name='Dinner')
# Check your answer
# q1.check()
print(fruits)
print('-'*40)
print(fruit_sales)
print('-'*40)
print(ingredients)