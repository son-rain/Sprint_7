from scooter_api import CourierApi as courier_api


def login_and_delete(courier_data):
    courier_data.pop('firstName')
    login_response = courier_api.login(courier_data).json()
    del_response = courier_api.delete(login_response['id'])
    return del_response


def modify_courier_data(courier_data, key, value):
    body = courier_data.copy()
    body[key] = value

    return body


def delete_data_field(data, key):
    data.pop(key)
    return data
