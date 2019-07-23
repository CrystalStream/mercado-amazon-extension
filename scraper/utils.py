import urllib.parse

def get_ml_url_for(q):
    return 'https://listado.mercadolibre.com.mx/{q}#D[A:{q}]'.format(q=urllib.parse.quote(q))

def get_amazon_url_for(q):
    return 'https://www.amazon.com.mx/s?k={}'.format(urllib.parse.quote(q))
