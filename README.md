# Задание 2: "API-тесты" курс ЯндексПрактикум | Diplom_2
Для тестирования был выбран сервис [Stella Burgers](https://stellarburgers.nomoreparties.site/) | [API Stella Burgers](API_documentation/API_Stella_Burger.pdf)

В связи с грядущим релизом, был покрыт автотестами следующий набор тестов: 

[Создание пользователя](tests/test_create_user.py)
- Создание уникального пользователя
- Создание пользователя, который уже зарегистрирован
- Создание пользователя с незаполненными одним из обязательных полей

[Логин пользователя](tests/test_login_user.py)
- Логин под существующим пользователем
- Логин с неверным логином и паролем

[Изменение данных пользователя](tests/test_changing_user_data.py)
- C авторизацией / Без авторизации

[Создание заказа](tests/test_create_order.py)
- C авторизацией / Без авторизации
- С ингредиентами / Без ингредиентов 
- С неверным хешем ингредиентов

[Получение заказов конкретного пользователя](tests/test_get_order_for_user.py)
- Авторизованный пользователь / Неавторизованный пользователь

---
### Перед работой с репозиторием требуется установить зависимости 
``` shell
pip3 install -r requirements.txt
```
### Запустить все тесты из директории tests
```shell
pytest tests --alluredir=allure_results
```
### Посмотреть отчет в веб версии пройденного прогона
```shell
allure serve allure_results
```
