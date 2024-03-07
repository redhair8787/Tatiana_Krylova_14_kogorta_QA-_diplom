import sender_stand_request
#Крылова Татьяна, 14-я когорта, Инженер по тестированию плюс - Дипломный проект

#Тест. По треку заказа можно получить данные о заказе.
def test_get_info_by_track_positive_assert():
    new_order_response = sender_stand_request.create_new_order()  #в переменную записываем ответ при создании нового заказа
    track = new_order_response.json()["track"] #записываем полученный трек в переменную
    order_info = sender_stand_request.get_info_order_by_track(track)  #записываем в перменную результат запроса на получение информации заказа по треку
    assert order_info.status_code == 200 #проверяем что код ответа равен 200

