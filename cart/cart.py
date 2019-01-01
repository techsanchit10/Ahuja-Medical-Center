from decimal import Decimal
from django.conf import settings
from testapp.models import Test


class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        """
        Iterate over the items in the cart and get the tests from the database.
        """
        test_ids = self.cart.keys()
        # get the test objects and add them to the cart
        tests = Test.objects.filter(id__in=test_ids)
        for test in tests:
            self.cart[str(test.id)]['test'] = test

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def add(self, test, quantity=1, update_quantity=False):
        """
        Add a test to the cart or update its quantity.
        """
        test_id = str(test.id)
        if test_id not in self.cart:
            self.cart[test_id] = {'quantity': 0,
                                      'price': str(test.price)}
        if update_quantity:
            self.cart[test_id]['quantity'] = quantity
        else:
            self.cart[test_id]['quantity'] += quantity
        self.save()

    def remove(self, test):
        """
        Remove a test from the cart.
        """
        test_id = str(test.id)
        if test_id in self.cart:
            del self.cart[test_id]
            self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
