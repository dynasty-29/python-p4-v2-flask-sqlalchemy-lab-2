#!/usr/bin/env python3

from app import app
from models import db, Customer, Review, Item

with app.app_context():

    Customer.query.delete()
    Review.query.delete()
    Item.query.delete()
    # Ensure customers and items are inserted before reviews
    customer1 = Customer(name="Alice")
    customer2 = Customer(name="Bob")
    db.session.add_all([customer1, customer2])
    db.session.commit()  # Commit to assign IDs

    item1 = Item(name="Laptop", price=999.99)
    item2 = Item(name="Headphones", price=199.99)
    db.session.add_all([item1, item2])
    db.session.commit()  # Commit to assign IDs

    # Now, insert reviews referencing the created customers and items
    review1 = Review(comment="Great product!", customer_id=customer1.id, item_id=item1.id)
    review2 = Review(comment="Not bad.", customer_id=customer2.id, item_id=item2.id)
    db.session.add_all([review1, review2])
    db.session.commit()  # Commit reviews


    # customer1 = Customer(name='Tal Yuri')
    # customer2 = Customer(name='Raha Rosario')
    # customer3 = Customer(name='Luca Mahan')
    # db.session.add_all([customer1, customer2, customer3])
    # db.session.commit()

    # item1 = Item(name='Laptop Backpack', price=49.99)
    # item2 = Item(name='Insulated Coffee Mug', price=9.99)
    # item3 = Item(name='6 Foot HDMI Cable', price=12.99)
    # db.session.add_all([item1, item2, item3])
    # db.session.commit()

    # db.session.add(Review(comment="zipper broke the first week",
    #                customer=customer1, item=item1))
    # db.session.add(Review(comment="love this backpack!",
    #                customer=customer2, item=item1))
    # db.session.add(Review(comment="coffee stays hot for hours!",
    #                customer=customer1, item=item2))
    # db.session.add(Review(comment="best coffee mug ever!",
    #                customer=customer3, item=item2))
    # db.session.add(Review(comment="cable too short",
    #                customer=customer3, item=item3))
    # db.session.commit()
