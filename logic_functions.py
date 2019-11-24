from all_data import Users, Shops, Cupons
import json

def get_global_coupons():
    scup = Cupons()
    urls =[]
    for cupon  in cup.cupons:
        urls.append({
            'id':cupon,
            'url':cup.cupons[cupon]['url'],
            'validate':cup.cupons[cupon]['validate']})

    return json.dumps(urls)

    
def get_all_cupons(user_id):
    """
    :return: json - list of urls and id
    """
    cup = Cupons()
    usr = Users()
    return json.dumps( cup.retrun_urls_with_validates(usr.users[user_id]['cupons']) )

def get_cupons_of_shop(user_id, shop):
    """
    :return: json - list of urls
    """
    usr = Users()
    cup = Cupons()
    urls =[]
    for cupon  in usr.users[user_id]['cupons']:
        if cup.cupons[cupon]['shop'] == shop:
            urls.append({
                'id':cupon,
                'url':cup.cupons[cupon]['url'],
                'validate':cup.cupons[cupon]['validate']})

    return json.dumps(urls)

def cupon_detail(cupon_id):
    """
    :param user_id (string): id of user
    :return: json of shop_name, date, condition
    """
    cup = Cupons()
    return json.dumps(cup.cupons[cupon_id])

def show_blacklist(user_id):
    """
    :param user_id (string): id of user
    :return: json of shop_name which were listed out from user
    """
    sh = Shops()
    usr = Users()
    return json.dumps(usr.users[user_id]['blacklist'])

def show_all_shops():
    """
    :return: json of shop_name
    """
    sp = Shops()
    data =[]
    for name, url in sp.shops:
        data.append({
            "name":name,
            'url':url
        })

    return json.dumps(data)

def add_shop_to_blacklist(user_id, shop_name):
    """
    :param shop_name: name of shop to be added
    """
    usr = Users()
    usr.users[user_id]['blacklist'].add(shop_name)
    usr.save()


def remove_shop_from_blacklist(user_id, shop_name):
    """
    :param shop_name: name of shop to be removed from blacklist
    """
    usr = Users()
    usr.users[user_id]['blacklist'].remove(shop_name)
    usr.save()

# for progress bar
def get_coupon_procent(user_id,coupon_id):
    user = Users()
    cp = Cupons()
    
    shop = cp.cupons[coupon_id]['shop']
    if shop in user.users[user_id]['expenses'].keys():
        current_expenses = user.users[user_id]['expenses'][shop]

        required = cp.cupons[coupon_id]['requrement']

        result = current_expenses/required
        result*=100
        result = int(result)
        if result>100:
            result=100
    else:
        result = 0

    return json.dumps(result)
## -------------------



def add_new_shop(user_id, shop_name):
    usr = Users()
    usr.users[user_id]['shops'].append(shop_name)
    usr.save()

def check_if_shop_in_db_add_if_yes(user_id, shop_name):
    usr = Users()
    if shop_name in usr.users[user_id]['shops']:
        add_new_shop(user_id, shop_name)
        # dodanie biedronki
        usr.users[user_id]['cupons'].append('id5')
        usr.users[user_id]['cupons'].append('id6')
        usr.users[user_id]['cupons'].append('id7')
        usr.save()
        # -----------------
        return True
    else:
        return False

def add_biedronka(user_id):
    usr = User()
 
    usr.save()


if __name__ =='__main__':
    print(get_all_cupons('user1'))
    print(cupon_detail('id2'))
    print(show_blacklist('user1'))
    print(show_all_shops())