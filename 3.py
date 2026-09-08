feedback = 'В отеле "Либерти" мне больше всего понравился заботливый персонал'
feedback = feedback.lower()
target_lenght = len('заботливый персонал')
pos = feedback.find('заботливый')

fb_out = feedback[pos:pos + target_lenght]
print(fb_out)
