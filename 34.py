# 34

poem = list(input("Введите стихотворение: ").split())
glas = 'аеёиоуыэюя'

slogset = set()
for el in poem:
    slog_qty = 0
    for i in el:
        if i in glas:
            slog_qty += 1
    slogset.add(slog_qty)

check = len(slogset) == 1
if check:
    print("Парам пам-пам")
else:
    print("Пам парам")

