from datetime import datetime
from time import sleep
from os import system

from mock_exam_tests import *


system('cls')

#Ismingizni tekshiradi va qayd qilib qo'yadi
name = input("Ismingizni kiriting! -> ")
def get_name():
    if len(name) >= 4:
        pass
    else:
        print('Yetarli emas!')
        get_name()
    with open('user.txt', 'a') as time:
        time.write(f"Foydalanuvchining ismi: '{name.capitalize()}', <-> '{datetime.now()}' da funksiyani ishga tushirdi! \n\n")

    return name

#Universitet sahifasiga kirish
def info(name = get_name()):
    sleep(1)
    print('Asalomu alekum. Bizning `Yap yangi Universitet`imizga hush keldinggiz!')
    sleep(1.1)
    print('Malumot olish uchun faqat kuting! ')
    sleep(1)
    st,nd,rd,fr = ' 1 <-- Universitet haqida malumot', " 2 <-- Universitetimizdagi yo'nalishlar", " 3 <-- Biz beradigan diplomlar", " 4 <-- Bizning ishonchli Skolarshiplarimiz!"
    print(st)
    sleep(1)
    print(nd)
    sleep(1)
    print(rd)
    sleep(1)
    print(fr)

    info_coledj = 'Bizning universitetimiz... vahokazo h.k\n'
    road_coledj = '"Matematika, Fizika", "Dasturlash", "Dangasalik mutahasisi"\n'


# Universitetning imkoniyatlarini tariflaydi
    def inner_woan(woan = 1):
        if woan != 1:
            return inner_woan(woan + 1)
        else:
            return  info_coledj

    def inner_tu(woan = 1):
        if woan != 2:
            return inner_tu(woan + 1)
        else:
            return road_coledj

    def inner_sri(woan = 1):
        if woan != 3:
            return inner_sri(woan + 1)
        else:
            return 'Bakalavr, Magistratura, Doctor|PhD\n'

    def inner_four(woan = 1):
        if woan != 4:
            return inner_four(woan + 1)
        else:
            return 'Bizda hach qanaqa "Grand-Prand" yo`q'

    w, t, s, f = inner_woan(), inner_tu(), inner_sri(), inner_four()
    def return_inner_func():
        system('cls')
        sleep(0.7)
        print(w)
        sleep(1)
        ask_road = input("Yo'nalishlarni ko'rmoqchimisiz! 'Y'dan boshqasi mumkin --> ")
        if ask_road.lower() != 'y':
            system('cls')
            sleep(0.5)
            print(t)
        sleep(1)
        ask_sri = input("Bizdagi mutaxasislik turlari! 'Y'dan boshqasi mumkin --> ")
        if ask_sri.lower() != 'y':
            system('cls')
            sleep(0.5)
            print(s)
        sleep(1)
        ask_skolar = input("Stipendiyalar bilan tanishmoqchimisiz! 'Y'dan boshqasi mumkin --> ")
        if ask_skolar.lower() != 'y':
            system('cls')
            sleep(0.5)
            print(f)

    return_inner_func()

# Mock  test oladi
zero = []
def exam_university(func = info()):
    sleep(1)
    exam_mock = input("O'zingizni sinab ko'rasizmi! 'H' yoki 'h' -> ")
    if exam_mock.lower() == 'h':
        mock_tests_five()
        def equal_both(ls=[18, 2, 2, 1, 3], lse = []):
            for i, v in enumerate(ls):
                for q, k in enumerate(mock_tests_ls):
                    if i == q and v == k:
                        lse.append(k)
            end = list(map(lambda x: zero.append(x), lse))
        return equal_both()
    else:
        print('Biz sizning ishtirokingizdan mamnunmiz! ')


exam_university()

# Mock exam ning foizini hisoblaydi
def percent_out():
    mock_percent = lambda x = sum(zero): x * 100 // 26
    if mock_percent() <= 100:
        system('cls')
        sleep(0.9)
        print(f"{name.capitalize()} Siz sinov intihonidan {mock_percent()}% to'pladingiz! ")
        sleep(0.5)

        with open('mock_exam.txt', 'a') as exam:
            exam.write(
                f"{name.capitalize()} sinov imtihonini '{datetime.now()}' o'tgan vaqtda topshirdi va {mock_percent()}% ball to'pladi!   \n\n")

    else:
        system('cls')
        sleep(0.5)
        print('Tizimda nosozlik!', exam_university())
        sleep(0.5)


percent_out()