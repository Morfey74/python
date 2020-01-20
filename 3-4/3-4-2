with open ('1.txt') as inf:
    s = inf.read().lower().strip().split(' ') # чтение из файла, уменьшаем все до нижнего регистра, убираем не нужны символы и разделяем пробелом
    c = {i: s.count(i) for i in s}# создаем словарь в соотвествии со словом и его повтороениями
m={key: value for key, value in c.items() if value==max(c.values())} # создаем новый словарь с максимальными значениями
m={k: v for k, v in m.items() if k==min(m)} # оставляем лексикографически первое знаечение
for k, v in m.items():
    g=str(k)+' '+str(v) # создаем строку с конечным значением
with open ('2.txt', 'w') as ouf: #записываем в файл
    ouf.write(g)
