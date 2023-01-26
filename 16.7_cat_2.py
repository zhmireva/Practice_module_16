from cat import Cat

cat_1 = Cat('Барон', 'мальчик', 2)
cat_2 = Cat('Семен', 'мальчик', 2)

print('Все коты на сайте: \n')
print(cat_1.getName(), cat_1.getGender(), cat_1.getAge())
print(cat_2.getName(), cat_2.getGender(), cat_2.getAge())
