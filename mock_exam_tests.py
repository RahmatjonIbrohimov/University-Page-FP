from time import sleep
from os import system


mock_tests_ls = []
def mock_tests_five():
    # 1 - savol
    sleep(0.5)
    print("3dan 9gacha bo'lgan juft sonlarni kiriting!")
    sleep(0.7)
    ques_ls = []
    question_first = int(input('Faqat bitta sonni kiriting! --> '))
    ques_ls.append(question_first)
    question_first_1 = int(input('Faqat bitta sonni kiriting! --> '))
    ques_ls.append(question_first_1)
    question_first_2 = int(input('Faqat bitta sonni kiriting! --> '))
    ques_ls.append(question_first_2)

    ques_lamb = list(filter(lambda i: i % 2 == 0, ques_ls))
    mock_tests_ls.append(sum(ques_lamb))



    # 2 - savol
    system('cls')
    sleep(0.5)
    print("1000 sonining natural bo’luvchilari soni nechta? \n      1)24   2)16   3)28   4)32")
    sleep(0.7)
    question_seccond = int(input('Variantni kiriting! --> '))
    mock_tests_ls.append(question_seccond)

    # 3 - savol
    system('cls')
    sleep(0.5)
    print("1 dan 100 gacha bo’lgan sonlar ichida 2ga ham 3ga ham bo’linmaydiganlari nechta?\n       1)34        2)33     3)30      4)35")
    sleep(0.7)
    question_third = int(input('Variantni kiriting! --> '))
    mock_tests_ls.append(question_third)

    # 4 - savol
    system('cls')
    sleep(0.5)
    print(
        "Shar radiusi 6  ga teng. Radius uchidan u bilan 30º burchak tashkil qiluvchi tekislik o`tkazilgan. Shra bilan tekislik hosil qilgan kesimning yuzini toping?  1) 27π 2) 8π 3) 64π 4) 25π?")
    sleep(0.7)
    question_third = int(input('Variantni kiriting! --> '))
    mock_tests_ls.append(question_third)

    # 5 - savol
    system('cls')
    sleep(0.5)
    print('''Radiusi 15va20 ga teng bo`lgan 2 shar markazlari orasidagi masofa 25 ga teng. Shar sirtlari kesishishidan hosil bo`lgan aylana uzunligini toping?
           1) 27π     2) 8π    3) 24π    4) 25π''')
    sleep(0.7)
    question_third = int(input('Variantni kiriting! --> '))
    mock_tests_ls.append(question_third)

    # return  mock_tests_ls
