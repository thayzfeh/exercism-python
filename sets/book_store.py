
class Basket:
    def __init__(self,content):
        self.content = content
        self.base_price = 800

    def max_discount(self):
        discounts = []
        for limit in range(5,0,-1):
            books = self.content.copy()
            abs_discount = 0
            limit_holder = limit
            groups = []
            while len(books) != 0:
                possible_books = set(books)

                if len(possible_books) >= limit_holder:
                    possible_books = sorted(possible_books, key=lambda x: books.count(x), reverse=True)
                    for i in range(0,limit_holder):
                        books.remove(possible_books.pop(0))
                    groups.append(limit_holder)

                else:
                    limit_holder -= 1
                
                if limit_holder == 0:
                    raise ValueError("??????")
            
            while 5 in groups and 3 in groups:
                groups.remove(5)
                groups.remove(3)
                groups.extend([4,4])
            
            for g in groups:
                match g:
                    case 2: abs_discount += 5 * (g / len(self.content))
                    case 3: abs_discount += 10 * (g / len(self.content))
                    case 4: abs_discount += 20 * (g / len(self.content))
                    case 5: abs_discount += 25 * (g / len(self.content))

            discounts.append(abs_discount)
        return max(discounts)
    
    def total(self):
        return self.base_price * len(self.content) * (1 - (self.max_discount() / 100))


def total(basket):
    my_basket = Basket(basket)
    print(my_basket.max_discount())
    return my_basket.total()


print(total([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5]))
