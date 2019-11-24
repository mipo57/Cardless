import json
from flask import Flask, request, render_template
import logic_functions
from Calls import Authorize, Token

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/account")
def account():
    return render_template('account.html')

@app.route("/index")
def index2():
    return render_template('index.html')

@app.route("/products/<typ>")
def products(typ):
    if (typ == "shops"):
        return render_template('products.html', fc="get_all_cuopns")
    elif (typ == "all"):
        return render_template('products.html', fc="get_global_coupons")

    return render_template('products.html', fc="get_premium_coupons")


@app.route("/product/<product>")
def product(product):
    return render_template('product.html', product=product)


new_payment = None # get name of shop of new payments


@app.route('/get_global_coupons')
def get_global_coupons():
    return logic_functions.get_global_coupons()

@app.route('/get_all_cuopns')
def get_all_cupons():
    user_id = request.args.get('user_id')
    return logic_functions.get_all_cupons(user_id)

@app.route('/get_premium_coupons')
def get_premium_coupons():
    PREMIUM = "Zabka"
    user_id = request.args.get('user_id')
    return logic_functions.get_cupons_of_shop(user_id, PREMIUM)


@app.route('/cupon_detail')
def cupon_detail():
    cupon_id = request.args.get('cupon_id')
    return logic_functions.cupon_detail(cupon_id)


@app.route('/show_blacklist')
def show_blacklist():
    user_id = request.args.get('user_id')
    return logic_functions.show_blacklist(user_id)


@app.route('/show_all_shops')
def show_all_shops():
    return logic_functions.show_all_shops()


@app.route('/get_percent')
def get_procent():
    user_id = request.args.get('user_id')
    cupon_id = request.args.get('cupon_id')
    return logic_functions.get_coupon_procent(user_id, cupon_id)


@app.route('/add_shop_to_blacklist')
def add_shop_to_blacklist():
    user_id = request.args.get('user_id')
    shop_name = request.args.get('shop_name')
    return logic_functions.add_shop_to_blacklist(user_id,shop_name)


@app.route('/remove_shop_from_blacklist')
def remove_shop_from_blacklist():
    user_id = request.args.get('user_id')
    shop_name = request.args.get('shop_name')
    return logic_functions.remove_shop_from_blacklist(user_id,shop_name)

@app.route('/new_payment')
def check_new_payment():
    global new_payment
    user_id = request.args.get('user_id')
    if new_payment:
        if not logic_functions.check_if_shop_in_db_add_if_yes(user_id, new_payment):
            # if new payment from new shop
            name = new_payment
            new_payment = None
            return name
    return 'no'

# TODO check every second if new paymnet
@app.route('/fake_payment')
def make_fake_payment():
    global new_payment
    new_payment = "Biedronka"
    return ''

# authorisation wrapper
@app.route('/authorisation')
def authorisation():
    callbackLink = request.args.get('link')
    print(callbackLink)
    return Authorize(callbackLink)


if __name__ == "__main__":
    app.run("0.0.0.0", port=80)