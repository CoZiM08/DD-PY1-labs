# TODO Найдите количество книг, которое можно разместить на дискете


disceta = 1.44
Mb_in_b = 1024 ** 2
discetainb = disceta * Mb_in_b

pages = 100
stroki= 50
symbols = 25
onesymb = 4
allstroki = stroki * pages
allsymbols = symbols * allstroki
safe = allsymbols * onesymb

count = discetainb / safe
count = round(count)





print("Количество книг, помещающихся на дискету:", count)
