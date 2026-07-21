import os
from flask import Flask, render_template

app = Flask(__name__)

# Route cho trang chủ
@app.route('/')
def home():
    return render_template('index.html')

# Nếu bạn có các trang khác như shop, cart, checkout... bạn có thể khai báo thêm như thế này:
@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
