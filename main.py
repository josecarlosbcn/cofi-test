from checkout import CheckOut


if __name__ == '__main__':
    c = CheckOut()
    products = ["VOUCHER", "TSHIRT", "MUG", "THSURT", "VOUCHER"]
    for p in products:
        c.scan(p)
    print(f"Cart: {c.cart}")
    print(f"Total : {c.total()}€")
