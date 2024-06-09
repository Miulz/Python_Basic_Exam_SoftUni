# Деси има фризьорски салон в София. Тя всеки ден си поставя за цел да постигне определена печалба.
# Напишете програма, която изчислява дали е успяла да постигне целта за деня, като знаете следното:
# Деси ще приема клиенти докато не приключи работния ден. Ако постигне желания приход обаче, тя ще затвори салона.
# Когато клиент влезе ще може да си избере една от следните услуги:
# •	Подстригване (haircut):
# o	Мъжко (mens) - 15лв.
# o	Дамско (ladies) – 20лв.
# o	Детско (kids) – 10лв.
# •	Боядисване (color):
# o	Поддръжка (touch up) – 20лв.
# o	Пълно боядисване (full color) – 30лв.
# Вход:
# От конзолата първоначално се чете 1 ред:
# •	цел за деня – цяло число в интервала [1 … 5000]
# След това се четат поредица от редове до получаване на команда "closed" или докато Деси не постигне целта за деня
# – услугата, която иска клиентът – текст с възможности "haircut" и "color".
# При команда "haircut" ще се очаква да се въведе видът на подстригването – "mens", "ladies" или "kids".
# При команда "color" ще се очаква видът на боядисването – "touch up" или "full color".
# Изход:
# На конзолата се отпечатват 2 реда:
# •	На първия ред:
# o	Ако Деси е успяла да постигне целта за деня:
# "You have reached your target for the day!"
# o	Ако Деси не е успяла да постигне целта за деня:
# "Target not reached! You need {колко пари не и достигат, за да стигне целта}lv. more."
# •	На втория ред:
# 	"Earned money: {парите, които е спечелила за деня}lv."

target = int(input())
command = input()
total_money = 0

while command != "closed":
    if command == "haircut":
        haircut_type = input()
        if haircut_type == "mens":
            total_money += 15
        elif haircut_type == "ladies":
            total_money += 20
        elif haircut_type == "kids":
            total_money += 10
    elif command == "color":
        color_type = input()
        if color_type == "touch up":
            total_money += 20
        elif color_type == "full color":
            total_money += 30

    if total_money >= target:
        print("You have reached your target for the day!")
        print(f"Earned money: {total_money}lv.")
        break

    command = input()

if command == "closed":
    money_needed = target - total_money
    print(f"Target not reached! You need {money_needed}lv. more.")
    print(f"Earned money: {total_money}lv.")
