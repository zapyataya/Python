text = 'asdxfghyxyx'
new_text = ''
for i in text:
    if i == 'x':
        new_text += 'y'
    else:
        new_text += i
print(new_text)