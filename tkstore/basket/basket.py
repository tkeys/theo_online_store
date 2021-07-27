class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('seshkey')
        if 'seshkey' not in request.session:
            basket = self.session['sehkey'] = {'number':23424242342}
        self.basket = basket(request)
