import re

def get_ml_products(html):
    items = []
    if html is None:
        return items
    
    product_list = html.find('ol', id="searchResults")
    if product_list:
        for item in product_list.find_all('li', class_="results-item"):
                items.append(parse_ml_item(item))
    return items

def get_amzn_products(html):
    items = []
    if html is None:
        return items
    
    product_list = html.find('div', class_="s-result-list")
    if product_list:
        for item in product_list.find_all('div', attrs={'data-asin': True}):
            items.append(str(item))
            
    return items

def gather_results(ml, amzn=None):
    return [get_ml_products(ml), get_amzn_products(amzn)]

def search(container, rules):
    rules = rules.split('.')
    while len(rules) > 1:
        rule = rules[0]
        attrs = re.findall('\[(.*?)\]', rule)
        if len(attrs):
            attr, value = attrs[0].split('=')
            rule = rules[0].replace('[{}]'.format(attrs[0]), '')
            parent = container.find(rule, **{attr: value.strip('\"')})
        else:
            parent = container.find(rules[0])

        return search(parent, '.'.join(rules[1:]))

    rule = rules[0]
    attrs = re.findall('\[(.*?)\]', rule)
    if len(attrs):
        attr, value = attrs[0].split('=')
        rule = rules[0].replace('[{}]'.format(attrs[0]), '')
        return container.find(rule, **{attr: value.strip('\"')})
    else:
        return container.find(rules[0])


def parse_ml_item(container):
    img = search(container, 'ul.li.img')
    price = search(container, 'div[class_="item__info"].div[class_="item__price"].span[class_="price__fraction"]')
    return {
        'name': img.get('title', img.get('alt', '')),
        'img': img.get('src', img.get('data-src', 'no-valid-img')),
        'price': '${}'.format(price.text)
    }

