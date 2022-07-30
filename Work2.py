tickets = input('Введите количество билетов:')
sum = 0

for i in range(1, tickets+1):
    person_age = input(int("Введите возраст посетителя"))
    if person_age < 18:
        print ("Вход бесплатный")
    else:
        if 18 <= person_age <= 25:
            sum += 990
        elif person_age > 25:
            sum += 1390

print ("Сумма к оплате:" + str(sum))

if tickets > 3:
    sum = sum/100*10

print("Сумма к оплате со скидкой:")