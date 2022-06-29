Skip to content
Product 
Team
Enterprise
Explore 
Marketplace
Pricing 
Search
Sign in
Sign up
slytimer
/
pythonProject
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
pythonProject/main.py /
@slytimer
slytimer Add files via upload
Latest commit 675a250 on 16 Nov 2020
 History
 1 contributor
325 lines (255 sloc)  13.4 KB

import numpy as np
import pandas as pd
from scipy.stats import  binom
from scipy.stats import  poisson

def combinations(n, k):
    return (np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k)))

#===========================HomeWork - 3===============================================================================

#1. Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое,
# среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

sal = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
#считаем среднее арифметическое
sa=sal.sum()/sal.size
sa_=sal.mean()

#создаём массив квадратов разности
saq=(sal-sa)**2
#считаем СКО
std=(saq.sum()/sal.size)**.5
stdd=(saq.sum()/(sal.size-1))**.5

std_=sal.std()
stdd_=sal.std(ddof=1)

#считаем дисперсию смещенная оценка
var=saq.sum()/sal.size
var_=sal.var()

#считаем дисперсию несмещенная оценка
vard=saq.sum()/(sal.size-1)
vard_=sal.var(ddof=1)

print("1. Среднее арифметическое ",sa,sa_)
print("1. СКО ",std,std_)
print("1. дисперсия смещенная оценка ",var,var_)
print("1. дисперсия несмещенная оценка ",vard,vard_)




#2. В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?
#варианты: a) 2 из 2 белые и 1 из 4 белый, b) 1 из 2х белый и 2 из 4 белые, c)0 из 2х белые и 3 из 4 белые
t1=combinations(8, 2)
t2=combinations(12, 4)

#a)
a1=combinations(5, 2)
a2=combinations(5, 1)
b2=combinations(7, 3)
p1=a1/t1
p2=(a2*b2)/t2
pa=p1*p2
print("2. 2 из 2 белые и 1 из 4 белый",pa)

#b)
a1=combinations(5, 1)
b1=combinations(3, 1)
a2=combinations(5, 2)
b2=combinations(7, 2)
p1=(a1*b1)/t1
p2=(a2*b2)/t2
pb=p1*p2
print("2. 1 из 2х белый и 2 из 4 белые",pb)

#c)
a1=combinations(3, 2)
a2=combinations(5, 3)
b2=combinations(7, 1)
p1=a1/t1
p2=(a2*b2)/t2
pc=p1*p2
print("2. 0 из 2х белые и 3 из 4 белые",pc)

p=pa+pb+pc
print("2.вероятность того, что 3 мяча белые",p)

#3. На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень.
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6.
# Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом в). третьим спортсменом.
p1=0.9
p2=0.8
p3=0.6
q1=1-p1
q2=1-p2
q3=1-p3

#a)
p=p1*q2*q3
print("3.a первым спортсменом",p)
#b)
p=q1*p2*q3
print("3.b первым спортсменом",p)
#c)
p=q1*q2*p3
print("3.c первым спортсменом",p)


#4.В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило
# столько же, сколько на A и B вместе. Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. Студент сдал первую сессию.
# Какова вероятность, что он учится: a). на факультете A б). на факультете B в). на факультете C?

#вероятность того что случайный студент из факультета A
qa=0.25
#вероятность того что случайный студент из факультета B
qb=0.25
#вероятность того что случайный студент из факультета B
qc=0.5

pa=0.8
pb=0.7
pc=0.9

#доля сдавших студентов от общего количества поступивших
pt=qa*pa+qb*pb+qc*pc
print("4. доля сдавщих студентов от общего количества поступивших",pt)


#a)
p=qa*pa/pt
print("4.a из факультета A",p)

p=qb*pb/pt
print("4.b из факультета B",p)

p=qc*pc/pt
print("4.c из факультета C",p)


#5. Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1,
# для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя:
# а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?
p1=0.1
p2=0.2
p3=0.25
q1=1-p1
q2=1-p2
q3=1-p3

#a
p=p1*p2*p3
print("5.а Вероятность выхода из строя всех деталей",p)

#b
p12=p1*p2*q3
p13=p1*q2*p3
p23=q1*p2*p3
pt2=p12+p13+p23
print("5.б Вероятность выхода из строя 2х деталей",pt2)

#c
#ищем вероятность что не выйдет ни одна деталь
pn=q1*q2*q3
p=1-pn
print("5.в Вероятность выхода хотябы 1й детали",p)

#d
p1=p1*q2*q3
p2=q1*p2*q3
p3=q1*q2*p3
p=p1+p2+p3+pt2
print("5.г Вероятность выхода из строя 1-2х деталей",p)



#===========================HomeWork - 2===============================================================================
#1
#Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. Стрелок выстрелил 100 раз.
#Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
p = binom.pmf(85,100,.8)
print("1.The probability that the shooter will hit the target exactly 85 times is",p)

#2
#Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек. Какова вероятность,
# что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?
#2 way
#via binom
p1 = binom.pmf(0,5000,0.0004)
p2 = binom.pmf(2,5000,0.0004)

#via poisson
lam = 5000*0.0004
p3 = poisson.pmf(0,lam)
p4 = poisson.pmf(2,lam)
print('2.1.a The probability that none of them will burn out on the first day (binom)',p1)
print('2.1.a The probability that none of them will burn out on the first day (poisson)',p3)
print('2.1.b The probability that that exactly 2 will burn out (binom)',p2)
print('2.1.b The probability that that exactly 2 will burn out (poisson)',p4)


#3
#Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
p = binom.pmf(70,144,.5)
print('3 The probability that heads will come up exactly 70 times ',p)

#4
#В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые? Какова вероятность того, что хотя бы один мяч белый?

#overall combinations
t1 = combinations(10, 2)
t2 = combinations(11, 2)

#4.1 Какова вероятность того, что все мячи белые?
# кол-во вариантов белых среди белых
a1 = combinations(7, 2)
a2 = combinations(9, 2)

p1=a1/t1
p2=a2/t2
# оба события должны произойти
p=p1*p2
print('4.1 Вероятность того, что все мячи белые p=',p)

#4.2 Какова вероятность того, что ровно два мяча белые?
# 3 варианта: 2 белых + 0 белых, 1 белый + 1 белый, 0 белых + 2 белых
a1 = combinations(7, 2)
a2 = combinations(2, 2)
p1=a1/t1
p2=a2/t2
pa=p1*p2
print('2 белых + 0 белых pa=',pa)


a1 = combinations(2, 2)
a2 = combinations(9, 2)
p1=a1/t1
p2=a2/t2
pb=p1*p2
print('0 белых + 2 белых pb=',pb)

a1 = combinations(7, 1)
a2 = combinations(9, 1)
b1 = combinations(3, 1)
b2 = combinations(2, 1)
p1=(a1*b1)/t1
p2=(a2*b2)/t2
pc=p1*p2
print('1 белый + 1 белый pc=',pc)

p=pa+pb+pc
print('4.2 Вероятность того, что ровно два мяча белые p=',p)

#4.3 Какова вероятность того, что хотя бы один мяч белый?
#от обратного - найдём вероятность что ни один из мячей не белый
a1 = combinations(3, 2)
a2 = combinations(2, 2)
p1=a1/t1
p2=a2/t2
p=1-p1*p2
print('4.3 Вероятность того, что хотя бы один мяч белый p=',p)






#===========================HomeWork - 1===============================================================================


#Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести
a = combinations(13, 4)
t = combinations(52, 4) #overall combinations
p = round(a*100/t,2)
print('1.a The probability that all cards are cross ',p, '%')

#б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
#first solution
#find all combinations for aces
a1=combinations(4, 1)
a2=combinations(4, 2)
a3=combinations(4, 3)
a4=combinations(4, 4)

#find all combinations for the remainig cards
b1=combinations(48,3)
b2=combinations(48,2)
b3=combinations(48,1)

p=round((a1*b1+a2*b2+a3*b3+a4)*100/t,2)
print('1.b.1 The probability that among 4 cards there will be at least one ace ',p, '%')

#second solution
#find all combinations without aces
a=combinations(48,4)
p=round((1-a/t)*100,2)
print('1.b.2 The probability that among 4 cards there will be at least one ace ',p, '%')

#-------------------------------------------------------------------------------------------------
#На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
# Код содержит три цифры, которые нужно нажать одновременно.
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

t = combinations(10, 3) #overall combinations
#let's say only one code is correct
p = round(100/t,2)
print('2 The probability that a person who does not know the code will open the door on the first try ',p, '%')

#-------------------------------------------------------------------------------------------------
#В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?

t = combinations(15, 3) #overall combinations
a = combinations(9, 3) #all painted combinations
p = round(100*a/t,2)
print('3 The probability that all extracted parts are painted ',p, '%')

#-------------------------------------------------------------------------------------------------
#В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

t = combinations(100, 2) #overall combinations
p = round(1*100/t,4)
print('4 The probability that 2 purchased tickets will be winning ', p, '%')

a = combinations(2, 1)
b = combinations(2, 2)
print(a)
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
