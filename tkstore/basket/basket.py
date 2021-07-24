class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('seshkey')
        if 'seshkey' not in request.session:
            basket = self.session['sehkey'] = {}
        self.basket = basket
