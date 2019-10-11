from decimal import Decimal
from django.conf import settings
from product.models import Pack


class Cart(object):

    def __init__(self, request):
        # initialization user cart
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # add to cart
    def add(self, pack, quantity=1, update_quantity=False):
        pack_id = str(pack.id)
        if pack_id not in self.cart:
            self.cart[pack_id] = {'quantity': 0, 'price': str(pack.price), 'uid': pack.uid}
        if update_quantity:
            self.cart[pack_id]['quantity'] = quantity
        else:
            self.cart[pack_id]['quantity'] += quantity
        self.save()

    # adjust in cart
    def adjust(self, pack, quantity):
        pack_id = str(pack.id)
        if self.cart[pack_id]['quantity'] == 1 and quantity == -1:
            quantity = 0
        self.cart[pack_id]['quantity'] += quantity
        self.save()

    # save cart to session
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # flag session modified
        self.session.modidied = True

    # remove from cart
    def remove(self, pack):
        pack_id = str(pack.id)
        if pack_id in self.cart:
            del self.cart[pack_id]
            self.save()

    def __iter__(self):
        pack_ids = self.cart.keys()
        packs = Pack.objects.filter(id__in=pack_ids)
        for pack in packs:
            self.cart[str(pack.id)]['pack'] = pack

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSIONS_ID]
        self.session.modified = True
