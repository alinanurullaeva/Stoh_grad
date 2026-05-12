def application_data():
    with open('Application_data/age', 'r', encoding='utf-8') as f:
        age = f.read().split('\n')

    with open('Application_data/air_flag', 'r', encoding='utf-8') as f:
        air_flag = f.read().split('\n')

    with open('Application_data/appl_rej', 'r', encoding='utf-8') as f:
        appl_rej = f.read().split('\n')

    with open('Application_data/car_own', 'r', encoding='utf-8') as f:
        car_own = f.read().split('\n')

    with open('Application_data/default', 'r', encoding='utf-8') as f:
        default = f.read().split('\n')

    with open('Application_data/gender', 'r', encoding='utf-8') as f:
        gender = f.read().split('\n')

    with open('Application_data/good_work', 'r', encoding='utf-8') as f:
        good_work = f.read().split('\n')

    with open('Application_data/income', 'r', encoding='utf-8') as f:
        income = f.read().split('\n')

    with open('Application_data/region_rating', 'r', encoding='utf-8') as f:
        region_rating = f.read().split('\n')

    with open('Application_data/req_count', 'r', encoding='utf-8') as f:
        req_count = f.read().split('\n')

    with open('Application_data/score', 'r', encoding='utf-8') as f:
        score = f.read().split('\n')

    age = [int(el) for el in age]
    air_flag = [int(el) for el in air_flag]
    appl_rej = [int(el) for el in appl_rej]
    car_own = [int(el) for el in car_own]
    default = [int(el) for el in default]
    gender = [int(el) for el in gender]
    good_work = [int(el) for el in good_work]
    income = [int(el) for el in income]
    region_rating = [int(el) for el in region_rating]
    req_count = [int(el) for el in req_count]
    c = [1 for i in range(len(default))]
    score = [float('.'.join(el.split(','))) for el in score]
    return [default[:180000], age[:180000], air_flag[:180000], appl_rej[:180000], car_own[:180000],
            gender[:180000], good_work[:180000], income[:180000], region_rating[:180000], req_count[:180000],
            score[:180000], c[:180000]]