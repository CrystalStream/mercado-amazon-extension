def get_products(html, page):
    items = []
    if html is None:
        return items

    if page == 'ml':
        product_list = html.find('ol', id="searchResults")
        if product_list:
            for item in product_list.find_all('li', class_="results-item"):
                items.append(str(item))
    if page == 'amzn':
        product_list = html.find('div', class_="s-result-list")
        if product_list:
            for item in product_list.find_all('div', attrs={'data-asin': True}):
                items.append(str(item))
    return items

def gather_results(ml, amzn=None):
    return [get_products(ml, 'ml'), get_products(amzn, 'amzn')]
