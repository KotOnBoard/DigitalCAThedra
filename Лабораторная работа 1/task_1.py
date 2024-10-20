disc_space = 1.44 * 1024 * 1024
symb_weight = 4
symb_count = 25
string_count = 50
page_count = 100
book_count = int(disc_space // (symb_weight * symb_count * string_count * page_count))

print("Количество книг, помещающихся на дискету:", book_count)