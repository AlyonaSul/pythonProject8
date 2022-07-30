tickets = int(input("Введите количество билетов: "))
sum: int = 0

for i in range(1, tickets+1):
    person_age = int(input("Введите возраст посетителя: "))
    if person_age < 18:
        print ("Вход бесплатный")
    elif 18 <= person_age <= 25:
            sum += 990
    elif person_age > 25:
            sum += 1390

if tickets > 3:
    sum = int(sum- (sum/100*10))
    print("Сумма к оплате со скидкой: " + str(sum) + "руб")
else:
    print ("Сумма к оплате:" + str(sum))