
import pytest
import requests

from data.handlers import Urls, Handlers
from data.user_data import User


@pytest.fixture(scope="function")
def create_user():
    payload = User.create_data_user()
    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_USER}", data=payload)
    token = response.json()["accessToken"]
    yield response, payload, login_data, token
    requests.delete(f"{Urls.MAIN_URL}{Handlers.DELETE_USER}", headers={'Authorization': f'{token}'})
