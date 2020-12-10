from constants import URL
from constants import BCOLORS
from constants import DISCOUNT_ACTIVE
import json
import os


class CheckOut:
    def __init__(self):
        self.list_products, self.__catalog = CheckOut.__read_products()
        self.cart = {}

    def __del__(self):
        del self.list_products
        del self.__catalog
        del self.cart

    """Methods"""
    @staticmethod
    def __read_products():
        """
        :return: Return a list of name of products and a list with all the information of each product
        """
        list_products = []
        try:
            with open(URL.JSON_PRODUCTS) as f:
                data = json.load(f)
                for item in data:
                    list_products.append(item["Code"])
        except FileNotFoundError:
            print(BCOLORS.FAIL + f"CheckOut::__read_products:: No se encuentra el archivo {URL.JSON_PRODUCTS}" + BCOLORS.ENDC)
            os._exit(3)
        return list_products, data

    def scan(self, product):
        """
        :param product: Product buyed
        :return: Update the cart with the quantity of the products buyed by the custome after the last scan
        """
        if product in self.list_products:
            self.cart[product] =  self.cart[product] + 1 if product in self.cart else 1
        else:
            print(BCOLORS.FAIL + f"El producto {product} NO SE ENCUENTRA en el catálogo" + BCOLORS.ENDC)

    def __search_item_in_catalog(self, product):
        """
        :param product: Name of the product
        :return: Return all the info of the product
        """
        for item in self.__catalog:
            if item["Code"] == product:
                return item

    def __total_voucher(self, quantity):
        """
        :param quantity: Total units buyed by the customer
        :return: The total ammount of voucher buyed after aplying discounts if these apply
        """
        price = self.__search_item_in_catalog("VOUCHER")["Price"]
        if DISCOUNT_ACTIVE.VOUCHER:
            total = int(quantity/2) * price
            total += quantity % 2 * price
        else:
            total = quantity * price
        return total

    def __total_tshirt(self, quantity):
        """
        :param quantity: Total units buyed by the customer
        :return: The total ammount of tshirt buyed after aplying discounts if these apply
        """
        if DISCOUNT_ACTIVE.TSHIRT:
            price = self.__search_item_in_catalog("TSHIRT")["Price"] if quantity < 3 else self.__search_item_in_catalog("TSHIRT")["Bulk-price"]
            total = quantity * price
        else:
            total = quantity * self.__search_item_in_catalog("TSHIRT")["Price"]
        return total

    def __total_mug(self, quantity):
        """
        :param quantity: Total units buyed by the customer
        :return: The total ammount of mugs buyed after aplying discounts if these apply
        """
        price = self.__search_item_in_catalog("MUG")["Price"]
        return quantity * price

    def total(self):
        """
        :return: The total value of the cart after applying discounts. After make the calculus of the total ammount the cart is emptied.
        """
        total = 0
        for item in self.cart.keys():
            function = "_CheckOut__total_%s" % item.lower()
            total += getattr(self, function)(self.cart[item])
        self.cart = {}
        return total
