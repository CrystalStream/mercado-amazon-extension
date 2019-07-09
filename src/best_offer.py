def get_ml_products(html):
    items = []
    if html is None:
        return items
    
    product_list = html.find('ol', id="searchResults")
    if product_list:
        for item in product_list.find_all('li', class_="results-item"):
                items.append(str(item))
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
