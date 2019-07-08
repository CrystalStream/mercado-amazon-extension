def get_ml_url_for(q):
    return 'https://listado.mercadolibre.com.mx/{q}#D[A:{q}]'.format(q=q)

def get_amazon_url_for(q):
    return 'https://www.amazon.com/s?k={}'.format(q)
