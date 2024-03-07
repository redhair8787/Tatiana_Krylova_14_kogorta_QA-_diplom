import requests
import configuration
import data

#POST запрос на создание заказа
def create_new_order():
    return requests.post(url=configuration.URL_SERVER + configuration.CREATE_ORDER, json=data.body_create)
#print(create_new_order().status_code)

#GET запрос на поиск информации по заказа по его треку
def get_info_order_by_track(track):
    return requests.get(url=configuration.URL_SERVER + configuration.GET_INFO_BY_TRACK + str(track))