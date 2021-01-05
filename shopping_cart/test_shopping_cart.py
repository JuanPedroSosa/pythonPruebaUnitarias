import unittest
from shopping_cart import Item, ShoppingCart, NoExistsItemError

API_REST = 10

class TestShoppingCart(unittest.TestCase):

	# se ejecuta antes de la prueba
	def setUp(self):
		self.pan = Item("pan", 50)
		self.jugo = Item("jugo", 15)
		self.shopping_cart = ShoppingCart()
		self.shopping_cart.add_item(self.pan)

	# se ejecuta después de la prueba
	def tearDown(self):
		pass

	def test_cinco(self):
		assert 5 + 5 == 10

	def test_nombre_producto(self):
		item = Item("manzana", 12.0)
		self.assertEqual(item.name, "manzana")

	def test_nombre_producto_pan(self):
		self.assertEqual(self.pan.name, "pan")

	def test_nombre_producto_jugo(self):
		self.assertNotEqual(self.jugo.name, "pan")

	def test_contiene_productos(self):
		self.assertTrue(self.shopping_cart.contains_item())

	def test_no_contiene_productos(self):
		self.shopping_cart.remove_item(self.pan)
		self.assertFalse(self.shopping_cart.contains_item())

	# assertIs compara objetos
	def test_obtener_producto_pan(self):
		item = self.shopping_cart.get_item(self.pan)
		self.assertIs(item, self.pan)

	def test_exception_obtener_jugo(self):
		with self.assertRaises(NoExistsItemError):
			self.shopping_cart.get_item(self.jugo)

	def test_total_con_un_producto(self):
		total = self.shopping_cart.total()
		self.assertGreater(total, 0)
		self.assertLess(total, self.pan.price + 1.0)
		self.assertEqual(total, self.pan.price)

	def test_codigo_pan(self):
		self.assertRegex(self.pan.code(), self.pan.name)

	# validación manual que reemplazan a los assert
	def test_fail(self):
		if 2 > 3:
			self.fail("dos no es mayor a 3")

	# en el caso que deseamos saltar una prueba usamos skip
	@unittest.skip("Salto la prueba")
	def test_prueba_skip(self):
		pass

	@unittest.skipIf( True, "Salto la prueba")
	def test_prueba_skip1(self):
		pass

	@unittest.skipUnless( False, "Salto la prueba")
	def test_prueba_skip2(self):
		pass

	@unittest.skipUnless( API_REST > 18, "Salto la prueba")
	def test_prueba_skip3(self):
		pass

if __name__ == "__main__":
	unittest.main()
