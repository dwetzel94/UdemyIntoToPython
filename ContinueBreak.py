# shoppingList = ("beans", "tomatoes", "cookies", "rice", "broccoli", "berries") #list of strings
# for item in shoppingList:
#     if item == "rice":
#         #continue #excludes the condition and moves on through the loop
#         break
#
#     print("Buy " + item)

# meal = ["meatballs", "rice", "olives", "weetabix", "broccoli"]
# legendary_food_item = ' ' #initializing variable
#
# for item in meal:
#     if item == "weetabix":
#         legendary_food_item = item
#         break  #exits loop
#     else:
#         print("I'll have the rest of that")
#
# if legendary_food_item:
#         print("gimme da BIIIXXXX")

# for i in range(0, 100, 7):
#     print(i)
#     if i > 0 and i % 11 == 0:
#         break

for i in range(0, 20):
    if i == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    print(i)