from faker import Faker


class User:

    @staticmethod
    def create_data_user():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return reg_data

    data_correct = {
        "email": 'tets_2503@yandex.ru',
        "password": "password"}

    data_negative = {
        "email": 'tets_2503123@yandex.ru',
        "password": "password"}

    data_double = {
        "email": 'tets_2503@yandex.ru',
        "password": "password",
        "name": "Username"}

    data_without_email = {
        "email": '',
        "password": "password",
        "name": "Username"}

    data_without_password = {
        "email": 'tets_2503@yandex.ru',
        "password": "",
        "name": "Username"}

    data_without_name = {
        "email": 'tets_2503@yandex.ru',
        "password": "password",
        "name": ""}

    data_updated = {
        "email": 'tets_2503@yandex.ru',
        "password": "password",
        "name": "Test"}
