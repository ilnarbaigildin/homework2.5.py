immutable_var = 1, 'tomato', 3, 'apple'
print(immutable_var)
immutable_var[1] = 'orange'
print(immutable_var)
# Как и говорилось в лекции порядковое значение элементов нельзя изменить не смотря что я хочу поменять tomat на orange его я могу лишь добавить в конце кортежа

mutable_list = ['potato', 'tomato', 'bread', 'apple']
print(mutable_list[1])
mutable_list[1] = 'cake'
print(mutable_list)
