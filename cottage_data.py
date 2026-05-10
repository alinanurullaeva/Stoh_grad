def cottage_data():
    with open('Cottage_data/price', 'r', encoding='utf-8') as f:
        price = f.read().split('\n')

    with open('Cottage_data/living_area', 'r', encoding='utf-8') as f:
        living_area = f.read().split('\n')

    with open('Cottage_data/total_area', 'r', encoding='utf-8') as f:
        total_area = f.read().split('\n')

    with open('Cottage_data/land', 'r', encoding='utf-8') as f:
        land = f.read().split('\n')

    with open('Cottage_data/dist', 'r', encoding='utf-8') as f:
        dist = f.read().split('\n')

    with open('Cottage_data/lake', 'r', encoding='utf-8') as f:
        lake = f.read().split('\n')
    return [price, living_area, total_area, land, dist, lake]

def cottage_data_ln():
    with open('Cottage_data/price', 'r', encoding='utf-8') as f:
        price = f.read().split('\n')

    with open('Cottage_data_ln/living_area_ln', 'r', encoding='utf-8') as f:
        living_area_ln = f.read().split('\n')

    with open('Cottage_data_ln/total_area_ln', 'r', encoding='utf-8') as f:
        total_area_ln = f.read().split('\n')

    with open('Cottage_data_ln/land_ln', 'r', encoding='utf-8') as f:
        land_ln = f.read().split('\n')

    with open('Cottage_data_ln/dist_ln', 'r', encoding='utf-8') as f:
        dist_ln = f.read().split('\n')

    with open('Cottage_data_ln/lake', 'r', encoding='utf-8') as f:
        lake = f.read().split('\n')
    return [price, living_area_ln, total_area_ln, land_ln, dist_ln, lake]


def get_data(if_ln):
    if if_ln:
        data = cottage_data_ln()
    else:
        data = cottage_data()
    price, living_area, total_area, land, dist, lake = data
    price = [float('.'.join(el.split(','))) for el in price]
    living_area = [float('.'.join(el.split(','))) for el in living_area]
    total_area = [float('.'.join(el.split(','))) for el in total_area]
    land = [float('.'.join(el.split(','))) for el in land]
    dist = [float('.'.join(el.split(','))) for el in dist]
    lake = [int(lake[i]) for i in range(len(lake))]
    c = [1 for i in range(len(price))]
    return [price, living_area, total_area, land, dist, lake, c]
