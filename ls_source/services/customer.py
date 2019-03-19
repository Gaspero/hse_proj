# -*- coding: utf-8 -*-

from playhouse.shortcuts import model_to_dict
from flask_restful import Resource, reqparse

from application import DB
from models.customer import Customer

class GetCustomer(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('customer_id', type=int, required=True,
                                   help='Incorrect customer_id', location='json')
        super(GetCustomer, self).__init__()

    def get(self, customer_id):
        result = Customer.get_or_none(Customer.customer_id == customer_id)
        if result:
            customer = model_to_dict(result, exclude=[Customer.create_time, Customer.birth_day])
            customer['create_time'] = result.create_time.strftime('%Y-%m-%d %H:%M:%S')
            customer['birth_day'] = result.birth_day.strftime('%Y-%m-%d %H:%M:%S')
            return {'result': customer}

class GetCustomers(Resource):

    def get(self):
        customers = []
        result = Customer.select()
        for customer in result:
            row = model_to_dict(customer, exclude=[Customer.create_time, Customer.birth_day])
            row['create_time'] = customer.create_time.strftime('%Y-%m-%d %H:%M:%S')
            row['birth_day'] = customer.birth_day.strftime('%Y-%m-%d %H:%M:%S')
            customers.append(row)
        return {'result': customers}


class AddCustomer(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('first_name', type=str, required=True,
                                   help='Incorrect first_name', location='headers')
        self.reqparse.add_argument('last_name', type=str, required=True,
                                   help='Incorrect last_name', location='json')
        self.reqparse.add_argument('email', type=str, required=True,
                                   help='Incorrect email', location='json')
        self.reqparse.add_argument('phone', type=str, required=True,
                                   help='Incorrect phone', location='json')
        self.reqparse.add_argument('birth_day', required=True,
                                   help='Incorrect birth_day', location='json')
        self.reqparse.add_argument('district', type=str, required=True,
                                   help='Incorrect district', location='json')
        self.reqparse.add_argument('address', type=str, required=True,
                                   help='Incorrect address', location='json')
        self.reqparse.add_argument('linked_card', type=int, required=True,
                                   help='Incorrect linked_card', location='json')
        super(AddCustomer, self).__init__()

    def get(self):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        #  with DB.atomic():
        customer = Customer.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            birth_day=birth_day,
            district=district,
            address=address,
            linked_card=linked_card)
        return {'isSuccess': True, 'customer_id': customer.customer_id}
    # TODO: исправить, не работает


class DeleteCustomer(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('customer_id', type=int, required=True,
                                   help='Incorrect customer_id', location='json')
        super(DeleteCustomer, self).__init__()

    def get(self, customer_id):
        query = Customer.delete().where(Customer.customer_id == customer_id)
        num = query.execute()
        return {'isSuccess': True, 'rowsUpdated': str(num)}


class UpdateCustomer(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('customer_id', type=int, required=True,
                                   help='Incorrect customer_id', location='json')
        super(UpdateCustomer, self).__init__()

    def get(self, customer_id):
        query = Product.update(price=10).where(Product.product_id == product_id)
        num = query.execute()
        return {'isSuccess': True, 'rowsUpdated': str(num)}
    # TODO: починить

