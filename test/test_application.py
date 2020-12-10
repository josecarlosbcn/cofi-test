# -*- coding: latin-1 -*-
import unittest
import os
from checkout import CheckOut
from constants import DISCOUNT_ACTIVE


class MyTestCase(unittest.TestCase):
    def setUp(self):
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    def test_json_load(self):
        c = CheckOut()
        self.assertIn("VOUCHER", c.list_products, "ERROR::test_json_load:: El producto VOUCHER NO EXISTE en nuestro catálogo")
        self.assertIn("TSHIRT", c.list_products, "ERROR::test_json_load:: El producto TSHIRT NO EXISTE en nuestro catálogo")
        self.assertIn("MUG", c.list_products, "ERROR::test_json_load:: El producto MUG NO EXISTE en nuestro catálogo")

    def test_scan_products(self):
        products = ["VOUCHER", "VOUCHER", "VOUCHER", "MUG", "TSHIRT", "TSHIRT", "MUG", "MUG", "TSHIRT", "VOUCHER", "TSHIRT", "MUG",
                    "TSHIRT", "TSHIRT", "TSHIRT", "TSHIRT", "VOUCHER"]
        c = CheckOut()
        for p in products:
            c.scan(p)
        self.assertEqual(5, c.cart["VOUCHER"], "ERROR::test_scan_products:: El número de productos VOUCHER NO ES EL CORRECTO")
        self.assertEqual(8, c.cart["TSHIRT"], "ERROR::test_scan_products:: El número de productos TSHIRT NO ES EL CORRECTO")
        self.assertEqual(4, c.cart["MUG"], "ERROR::test_scan_products:: El número de productos MUG NO ES EL CORRECTO")

    def test_total_voucher(self):
        products = ["VOUCHER", "VOUCHER", "VOUCHER", "VOUCHER", "VOUCHER"]
        c = CheckOut()
        for p in products:
            c.scan(p)
        if DISCOUNT_ACTIVE.VOUCHER:
            self.assertEqual(15.00, c.total(), "ERROR::test_total_voucher:: El total del producto VOUCHER con oferta aplicable NO ES CORRECTO")
        else:
            self.assertEqual(25.00, c.total(), "ERROR::test_total_voucher:: El total del producto VOUCHER sin oferta aplicable NO ES CORRECTO")

    def test_total_tshirt(self):
        products = ["TSHIRT", "TSHIRT", "TSHIRT", "TSHIRT", "TSHIRT"]
        c = CheckOut()
        for p in products:
            c.scan(p)
        if DISCOUNT_ACTIVE.VOUCHER:
            self.assertEqual(95.00, c.total(), "ERROR::test_total_tshirt:: El total del producto TSHIRT con oferta aplicable NO ES CORRECTO")
        else:
            self.assertEqual(100.00, c.total(), "ERROR::test_total_tshirt:: El total del producto TSHIRT sin oferta aplicable NO ES CORRECTO")

    def test_total_mug(self):
        products = ["MUG", "MUG", "MUG"]
        c = CheckOut()
        for p in products:
            c.scan(p)
        self.assertEqual(22.50, c.total(), "ERROR::test_total_mug:: El total del producto MUG NO ES CORRECTO")

    def test_total(self):
        products = ["VOUCHER", "VOUCHER", "VOUCHER", "MUG", "TSHIRT", "TSHIRT", "MUG", "MUG", "TSHIRT", "VOUCHER", "TSHIRT", "MUG",
                    "TSHIRT", "TSHIRT", "TSHIRT", "TSHIRT", "VOUCHER"]
        c = CheckOut()
        for p in products:
            c.scan(p)
        if DISCOUNT_ACTIVE.VOUCHER and DISCOUNT_ACTIVE.TSHIRT:
            self.assertEqual(197.00, c.total(), "ERROR::test_total:: El total de los productos con promociones en VOUCHER y TSHIRT NO ES CORRECTO")
        if DISCOUNT_ACTIVE.VOUCHER and not DISCOUNT_ACTIVE.TSHIRT:
            self.assertEqual(205.00, c.total(), "ERROR::test_total:: El total de los productos con promociones en VOUCHER NO ES CORRECTO")
        if not DISCOUNT_ACTIVE.VOUCHER and DISCOUNT_ACTIVE.TSHIRT:
            self.assertEqual(207.00, c.total(), "ERROR::test_total:: El total de los productos con promociones en VOUCHER NO ES CORRECTO")
        if not DISCOUNT_ACTIVE.VOUCHER and not DISCOUNT_ACTIVE.TSHIRT:
            self.assertEqual(215.00, c.total(), "ERROR::test_total:: El total de los productos SIN promociones NO ES CORRECTO")
        products = ["VOUCHER", "VOUCHER", "MUG", "MUG", "MUG", "TSHIRT", "VOUCHER", "TSHIRT", "MUG", "TSHIRT", "TSHIRT", "TSHIRT", "VOUCHER"]
        for p in products:
            c.scan(p)
        if DISCOUNT_ACTIVE.VOUCHER and DISCOUNT_ACTIVE.TSHIRT:
            self.assertEqual(135.00, c.total(), "ERROR::test_total:: El total de los productos con promociones en VOUCHER y TSHIRT NO ES CORRECTO")
        if DISCOUNT_ACTIVE.VOUCHER and not DISCOUNT_ACTIVE.TSHIRT:
            self.assertEqual(140.00, c.total(), "ERROR::test_total:: El total de los productos con promociones en VOUCHER NO ES CORRECTO")
        if not DISCOUNT_ACTIVE.VOUCHER and DISCOUNT_ACTIVE.TSHIRT:
            self.assertEqual(145.00, c.total(), "ERROR::test_total:: El total de los productos con promociones en VOUCHER NO ES CORRECTO")
        if not DISCOUNT_ACTIVE.VOUCHER and not DISCOUNT_ACTIVE.TSHIRT:
            self.assertEqual(150.00, c.total(), "ERROR::test_total:: El total de los productos SIN promociones NO ES CORRECTO")
        products = ["VOUCHER", "VOUCHER", "VOUCHER", "MUG", "TSHIRT", "VOUCHER", "TSHIRT", "VOUCHER"]
        for p in products:
            c.scan(p)
        if DISCOUNT_ACTIVE.VOUCHER and DISCOUNT_ACTIVE.TSHIRT:
            self.assertEqual(62.50, c.total(), "ERROR::test_total:: El total de los productos con promociones en VOUCHER y TSHIRT NO ES CORRECTO")
        if DISCOUNT_ACTIVE.VOUCHER and not DISCOUNT_ACTIVE.TSHIRT:
            self.assertEqual(62.50, c.total(), "ERROR::test_total:: El total de los productos con promociones en VOUCHER NO ES CORRECTO")
        if not DISCOUNT_ACTIVE.VOUCHER and DISCOUNT_ACTIVE.TSHIRT:
            self.assertEqual(62.50, c.total(), "ERROR::test_total:: El total de los productos con promociones en VOUCHER NO ES CORRECTO")
        if not DISCOUNT_ACTIVE.VOUCHER and not DISCOUNT_ACTIVE.TSHIRT:
            self.assertEqual(72.50, c.total(), "ERROR::test_total:: El total de los productos SIN promociones NO ES CORRECTO")


if __name__ == '__main__':
    unittest.main()
