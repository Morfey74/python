with open ('1.txt')as inf: # Чтение из файла и построчное разбиение
    s = inf.read().split('\n')
m=[s[i].split(';') for i in range(len(s))] # Разбиваем список на список списков(двумерная матрица)
with open ('2.txt', 'w')as ouf: # Запись в файл
    for i in range(len(m)):
        for j in range(len(m[i])):
            a=(str(round(((int(m[i][1]) + int(m[i][2]) + int(m[i][3])) / 3), 9))) # вычисление средней оценки ученика по всем предметам
        k=[round((sum(int(i1) for n,i1,i2,i3 in m) /len(m)), 9),round((sum(int(i2) for n,i1,i2,i3 in m) /len(m)), 9),round((sum(int(i3) for n,i1,i2,i3 in m) /len(m)), 9)] # вычисление среднего балла всех учеников по предмету
        ouf.write(a+'\n') # запись средней оценки ученика по всем предметам
    ouf.write(str(k[0])+' '+str(k[1])+' '+str(k[2])) # запись среднего балла всех учеников по предмету
