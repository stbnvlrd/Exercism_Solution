def smallest_product(min_factor, max_factor):
    for a in range(min_factor, max_factor + 1):
        for b in range(min_factor, max_factor + 1):
            mult = a * b
            if str(mult) == str(mult)[::-1]:
                return mult
    
def largest_product(min_factor, max_factor):
    for a in range(max_factor + 1, min_factor, -1):
        for b in range(max_factor + 1, min_factor, -1):
            mult = a * b
            if str(mult) == str(mult)[::-1]:
                return mult
    if mult == 0:
        return []
        
def largest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    else:
        products = []
        max_product = largest_product(min_factor, max_factor)
        print(max_product)
        if max_product is None:
            products = []
        else:
            for a in range(min_factor, max_factor + 1):
                values = []
                if (max_product/a) in range(min_factor, max_factor + 1):
                    values.append(a)
                    values.append(int(max_product/a))
                    products.append(values)
        print(products)
    return max_product, products

    
def smallest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    else:
        products = []
        min_product = smallest_product(min_factor, max_factor)
        if min_product is None:
            products = []
        else:
            for a in range(min_factor, max_factor + 1):
                values = []
                if (min_product/a) in range(min_factor, max_factor + 1):
                    values.append(a)
                    values.append(int(min_product/a))
                    products.append(values)
        print(products)
    return min_product, products
print(largest(1000, 9999))
print(smallest(1000, 9999))

print(largest(15, 15))
print(smallest(15, 15))