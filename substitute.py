# Любимият отбор на Пепи е на финал, но започва да губи мача.
# Треньорът на отбора не знае какви смени да направи, за да обърне резултата.
# Напишете програма, с която ще разберете кой са първите 6 валидни смени, които могат да се направят.
# Знаем, че всяка цифра от двата номера е в даден интервал:
# •	Първата цифра на първото число е в интервала от цифрата K до 8, включително.
# •	Втората цифра на първото число е в интервала от 9 до L, включително.
# •	Първата цифра на второто число е в интервала от цифрата M до 8, включително.
# •	Втората цифра на второто число е в интервала от 9 до N, включително.
# За да бъде възможна една смяна, първата цифра на всеки от номерата трябва да бъде четна, а втората -  нечетна.
# За да бъде валидна една смяна, то номерата НЕ трябва да съвпадат.
# Вход:
# От конзолата се четат 4 реда:
# •	K – цяло число в интервала [0..8]
# •	L – цяло число в интервала [0..9]
# •	M– цяло число в интервала [0..8]
# •	N – цяло число в интервала [0..9]
# Изход:
# На конзолата да се отпечатат първите 6 валидни смени по следния начин:
# •	Ако смяната е възможна и номерата НЕ съвпадат, тя Е валидна и трябва да се отпечата: "{K}{L} - {M}{N}"
# •	Ако смяната е възможна, но номерата съвпадат, тя НЕ е валидна и трябва да се отпечата: "Cannot change the same player."

K = int(input())
L = int(input())
M = int(input())
N = int(input())
counter = 0

for i in range(K, 9):
    for j in range(9, L-1, -1):
        for k in range(M, 9):
            for l in range(9, N-1, -1):
                if counter == 6:
                    break
                if i % 2 == 0 and j % 2 != 0 and k % 2 == 0 and l % 2 != 0 and (i != k or j != l):
                    counter += 1
                    print(f"{i}{j} - {k}{l}")
                if i % 2 == 0 and j % 2 != 0 and k % 2 == 0 and l % 2 != 0 and (i == k and j == l):
                    print("Cannot change the same player.")







