# За да са здрави котките, храненето им трябва да следва определена диета.
# Напишете програма, която изчислява котешкото процентно разпределение на макроелементите в храната за един ден
# и пресмята колко средно калории дава един грам от тази храна. Макроелементите са: мазнини, протеини и въглехидрати.
# Разполагате с общия брой калории, които котката трябва да приеме за един ден.
# Известно е, че:
# •	1 грам мазнини = 9 калории
# •	1 грам протеини = 4 калории
# •	1 грам въглехидрати = 4 калории
# За да разберете колко калории дава един грам храна на котката, ще трябва да направите изчисления с реалното тегло
# а храната, тъй като тя съдържа вода. Трябва да се изчислят грамовете на мазнините, протеините и въглехидратите.
# Тяхната сума дава общото тегло на храната и от него трябва да извадим процентите вода.
# Вход:
# От конзолата се прочитат 5 реда:
# •	Процент на мазнините - цяло число в интервала [0…100]
# •	Процент на протеините - цяло число в интервала [0…100]
# •	Процент на въглехидратите - цяло число в интервала [0…100]
# •	Общ брой калории - цяло число в интервала [1000…15000]
# •	Процент на съдържанието на вода - цяло число в интервала [0…100]
# Пояснение: Когато правим подобни изчисления с проценти има голям шанс резултатът да не е цяло число!
# Изход:
# На конзолата се отпечатва 1 ред:
# •	"{calories}"
# Резултатът трябва да бъде форматиран до четвъртия знак след десетичната запетая.

percent_fat = int(input())
percent_protein = int(input())
percent_carbs = int(input())
total_calories = int(input())
percent_water = int(input())

grams_fat = percent_fat * total_calories / 100 / 9
grams_protein = percent_protein * total_calories / 100 / 4
grams_carbs = percent_carbs * total_calories / 100 / 4
grams_water = (100 - percent_water) / 100

calories_per_gram = total_calories / (grams_fat + grams_protein + grams_carbs)
real_calories = calories_per_gram * grams_water


print(f"{real_calories:.4f}")