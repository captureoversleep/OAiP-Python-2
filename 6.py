fb_gen = input('Напишите ваши общие впечатления: ')
fb_plus = input('Напишите что вам понравилось: ')
fb_minus = input('Напишите что вам не понравилось: ')

lenght = len(fb_gen) + len(fb_plus) + len(fb_minus)
discount = lenght * 0.10
print('Ваша скидка за отзыв:', discount)
print('Спасибо что помогаете нам стать лучше!')
#print('check:', lenght, len(fb_gen), len(fb_plus,), len(fb_minus))