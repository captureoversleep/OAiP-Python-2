staff1 = 'анна'
staff2 = 'александр'
feedback = input('Напишите свой отзыв: ')
feedback = feedback.lower()
pos1 = feedback.find(staff1)
pos2 = feedback.find(staff2)
s1 = feedback[pos1 : pos1 + 4]
s2 = feedback[pos2 : pos2 + 9]
print('на премию:', s1 + ', ' + s2)
