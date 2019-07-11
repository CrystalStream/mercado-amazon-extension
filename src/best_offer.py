import re

def get_ml_products(html):
    product_list = html.find('ol', id="searchResults")
    if product_list is None:
        return []

    return [parse_item(item) for item in product_list.find_all('li', class_="results-item")]

    # items = []
    
    # product_list = html.find('ol', id="searchResults")
    # if product_list:
    #     for item in product_list.find_all('li', class_="results-item"):
    #             items.append(parse_ml_item(item))
    # return items

def get_amzn_products(html):
    product_list = html.find('div', class_="s-result-list")
    if product_list is None:
        return []

    return [parse_item(item, 'amzn') for item in product_list.find_all('div', attrs={'data-asin': True})]

    # items = []

    # product_list = html.find('div', class_="s-result-list")
    # if product_list:
    #     for item in product_list.find_all('div', attrs={'data-asin': True}):
    #         items.append(parse_amzn_item(item))
            
    # return items

def gather_results(ml, amzn):
    ml_products = get_ml_products(ml) if ml is not None else []
    amzn_products = get_amzn_products(amzn) if amzn is not None else []

    return [ml_products, amzn_products]

def search(container, rules):
    rules = rules.split('.')

    if container is None:
        return None
    
    while len(rules) > 1:
        search_criteria = get_search_criteria(rules[0])
        if 'criteria' in search_criteria:
            parent = container.find(search_criteria['rule'], **search_criteria['criteria'])
        else:
            parent = container.find(search_criteria['rule'])

        # rule = rules[0]
        # attrs = re.findall('\[(.*?)\]', rule)
        # if len(attrs):
        #     attr, value = attrs[0].split('=')
        #     rule = rules[0].replace('[{}]'.format(attrs[0]), '')
        #     parent = container.find(rule, **{attr: value.strip('\"')})
        # else:
        #     parent = container.find(rules[0])

        return search(parent, '.'.join(rules[1:]))


    search_criteria = get_search_criteria(rules[0])
    if 'criteria' in search_criteria:
        return container.find(search_criteria['rule'], **search_criteria['criteria'])
    else:
        return container.find(search_criteria['rule'])

    # rule = rules[0]
    # attrs = re.findall('\[(.*?)\]', rule)
    # if len(attrs):
    #     attr, value = attrs[0].split('=')
    #     rule = rules[0].replace('[{}]'.format(attrs[0]), '')
    #     return container.find(rule, **{attr: value.strip('\"')})
    # else:
    #     return container.find(rules[0])

def get_search_criteria(rule):
    attrs = re.findall('\[(.*?)\]', rule)
    if len(attrs):
        attr, value = attrs[0].split('=')
        rule = rule.replace('[{}]'.format(attrs[0]), '')
        return {
            'rule': rule,
            'criteria': { attr: value.strip('\"') }
        }

    return {
        'rule': rule
    }

def parse_item(container, store='ml'):
    img_selector = 'ul.li.img'
    price_selector = 'div[class_="item__info"].div[class_="item__price"].span[class_="price__fraction"]'

    if store == 'amzn':
        img_selector = 'div[class_="s-image-tall-aspect"].img'
        price_selector = 'span[class_="a-price"].span'

    img = search(container, img_selector)
    price = search(container, price_selector)

    return {
        'name': img.get('title', img.get('alt', '')),
        'img': img.get('src', img.get('data-src', 'no-valid-img')),
        'price': '${}'.format(price.text if price else 'N/A')
    }


# def parse_ml_item(container):
#     img = search(container, 'ul.li.img')
#     price = search(container, 'div[class_="item__info"].div[class_="item__price"].span[class_="price__fraction"]')
#     return {
#         'name': img.get('title', img.get('alt', '')),
#         'img': img.get('src', img.get('data-src', 'no-valid-img')),
#         'price': '${}'.format(price.text)
#     }

# def parse_amzn_item(container):
#     img = search(container, 'div[class_="s-image-tall-aspect"].img')
#     price = search(container, 'span[class_="a-price"].span')
#     return {
#         'name': img.get('alt', ''),
#         'img': img.get('src', ''),
#         'price': price.text if price else  'N/A'
#     }

