cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ]
]

def list_to_buy(list1, persons):
    if persons <= 0:
        print("Введенно неверное количество людей ")
        return 0
    else:
        for dish in cook_book:
            print(dish[0].capitalize() + ";")
            for ingredient in dish[1]:
                print("{name}, {amount}{weight}".format(name=ingredient[0].capitalize(),amount=ingredient[1]*persons,weight=ingredient[2]))
            print()

person = int(input("Введите количество людей, на которых необходимо приготовить блюда "))
list_to_buy(cook_book,person)