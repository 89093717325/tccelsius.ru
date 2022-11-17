from app import app, db
from app.models import Car, Rent
from flask import render_template, request
from datetime import datetime
from collections import defaultdict


@app.route('/')
def index():
    
    Car_list = Car.query.all()

    context = {
        'Car_list': Car_list,
    }

    return render_template('index.html', **context)


@app.route('/create_auto', methods=['POST', 'GET'])
def create_auto():
    context = None

    if request.method == 'POST':
        
        auto_name = request.form['name']
        auto_price = request.form['price']
        auto_description = request.form['description']
        auto_transmission = request.form['transmission']
        auto_img = request.form['img']
        auto_img1 = request.form['img1']
        auto_img2 = request.form['img2']
        auto_img3 = request.form['img3']

        car_instance = Car()
        car_instance.name = auto_name
        car_instance.price = auto_price
        car_instance.description = auto_description
        car_instance.transmission = auto_transmission
        car_instance.img = auto_img
        car_instance.img1 = auto_img1
        car_instance.img2 = auto_img2
        car_instance.img3 = auto_img3
 
        db.session.add(car_instance)
        db.session.commit()

        context = {
            'method': 'POST',
            'name': auto_name,
            'description': auto_description,
            'price': auto_price,
            'transmission': auto_transmission,
            'img': auto_img,
        }
    
    elif request.method == 'GET':

        context = {
            'method': 'GET',
        }

    return render_template('create_auto.html', **context)

@app.route('/auto_detail/<int:car_id>', methods=['POST', 'GET'])
def auto_detail(car_id):
    
    car = Car.query.get(car_id)
    Rent_list = Rent.query.filter_by(car_id=car_id).all()

    context = {
        'car': car,
        'rent_list': Rent_list,
    }

    return render_template('auto_detail.html', **context)

@app.route('/del_auto/<int:car_id>', methods=['POST'])
def del_auto(car_id):
    
    car = Car.query.get(car_id)

    context = {
        'name': car.name,
        'price': car.price,
        'img': car.img,
    }
    
    db.session.delete(car)
    db.session.commit()

    return render_template('index.html', **context)

@app.route('/rent_auto/<int:car_id>', methods=['POST'])
def rent_auto(car_id):

    car = Car.query.get(car_id)
    start = None
    end = None

    if car.available:
        start = datetime.now()
        db.session.add(Rent(car_id = car_id, date_and_time_rent_start = start))
        car.available = False 
        db.session.commit()
    else:
        rent = Rent.query.filter_by(car_id=car_id).all()
        for i in rent:
            if i.date_and_time_rent_end == None:
                end = datetime.now()
                i.date_and_time_rent_end = end
                car.available = True
                db.session.commit() 

    Rent_list = Rent.query.filter_by(car_id=car_id).all()
    context = {
        'car': car,
        'rent_list': Rent_list,
    }

    return render_template('auto_detail.html', **context)


@app.route('/edit_auto/<int:car_id>', methods=['POST', 'GET'])
def edit_auto(car_id):
    
    car = Car.query.get(car_id)
    context = None

    if request.method == 'POST':
        new_name = request.form['new_name']
        new_description = request.form['new_description']
        new_price = request.form['new_price']
        new_transmission = request.form['new_transmission']
        new_img = request.form['new_img']
        new_img1 = request.form['new_img1']
        new_img2 = request.form['new_img2']
        new_img3 = request.form['new_img3']


        if new_name:
            car.name = request.form['new_name']
        
        if new_price:
            car.price = request.form['new_price']
        
        if new_transmission:
            car.transmission = request.form['new_transmission']

        if new_description:
            car.description = request.form['new_description']

        if new_img:
            car.img = request.form['new_img']

        if new_img1:
            car.img1 = request.form['new_img1']

        if new_img2:
            car.img2 = request.form['new_img2']

        if new_img3:
            car.img3 = request.form['new_img3']


    db.session.commit()

    context = {
        'car': car,
    }

    return render_template('edit_auto.html', **context)

@app.route('/rental_log', methods=['GET'])
def rental_log():

    counter_list = defaultdict(int)
    total_time_list = defaultdict(int) 
    total_cost = defaultdict(int) 
    Car_list = Car.query.all()
    Rent_list = Rent.query.all()
    
    for car in Car_list:
        for rent in Rent_list:
            if car.id == rent.car_id and rent.date_and_time_rent_end != None:
                counter_list[car.id] += 1
                total_time_list[car.id] += (rent.date_and_time_rent_end - rent.date_and_time_rent_start).seconds / 60
                total_cost[car.id] += ((rent.date_and_time_rent_end - rent.date_and_time_rent_start).seconds / 60)*car.price

    context = {
    'Car_list': Car_list,
    'Rent_list': Rent_list,
    'counter_list': counter_list,
    'total_time_list': total_time_list,
    'total_cost': total_cost,
    }

    return render_template('rental_log.html', **context)


@app.route('/about')
def about():

    context = {
    }

    return render_template('about.html', **context)

@app.route('/works')
def works():

    context = {
    }

    return render_template('works.html', **context)

@app.route('/contacts')
def contacts():

    context = {
    }

    return render_template('contacts.html', **context)

@app.route('/3d')
def DDD():

    context = {
    }

    return render_template('3D.html', **context)