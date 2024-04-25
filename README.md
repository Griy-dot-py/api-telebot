# Телеграм-бот для работы с API стороннего сайта
Python-телеграм бот, поддерживаемый версиями Python 3.9 и выше.

Модуль ``api/`` заменяем, вы можете использовать бота для работы с любым другим API. В качестве примера - бот для работы с погодными API.
___

## Погодный телеграм-бот 
**Бот умеет:**
 * Отслеживать текущюю погоду в вашем городе
 * Анализировать прогноз погоды и находить метеорологические данные, которые вам требуются
 * Возвращать краткую историю запросов

## Требования
 1. Установленная и/или веб-версия мессенжера Telegram.
 2. Бот-токен от [@BotFather](https://t.me/botfather)
 3. API-ключ. Погодный бот требует ключ от [Open Weather API](https://openweathermap.org/)
 4. Python версии 3.9+


## Установка
#### Установка необходимого ПО
Для начала нужно будет установить Python, если у вас его нет. Это можно сделать на оффициальном [сайте](https://www.python.org/).

Следующим шагом будет установка бота. Вы можете сделать это либо клонируя репозиторий:
```
$ git clone
```
либо скачав и распаковав zip-архив. Выбирайте то, что вам удобнее.

Далее, вам нужно будет создать для бота виртуальное окружение: находясь в корневой папке, поочередно выполните комманды:

на Windows:
```
> python -m venv .venv
```
```
> .\.venv\Scripts\activate
```
На Linux/Mac:
```
$ python3 -m venv .venv
```
```
$ source .venv/bin/activate
```
После этого у вас скорее всего появится надпись (.venv) в терминале, но если вы работаете в WindowsPowerShell, то этой надписи может и не быть.

В конце останется только установить необходимые Python пакеты:
```
(.venv) $ pip install -r requirements.txt
```
*(на Windows комманда та же)*

#### Получение данных для вашего бота
Далее следует получить токен у [@BotFather](https://t.me/botfather), следуя инструкции по созданию нового телеграм-бота.

Если вы планируете использование именно погодного бота, то вам будет нужен API-ключ. Пройдя регистрацию на [Open Weather API](https://openweathermap.org/), ваш беспланый ключ будет лежать в разделе My API keys.

#### Установка зависимостей
В корневой папке будет лежать файл ``.env.example``.Вам нужно будет здесь же создать здесь же файл ``.env``, в котором будут хранится переменные среды, т.е. персональные данные вашего бота. Скопируйте текст из первого файла во второй, заменяя строки "Токен от BotFather", "Ваш API ключ" на полученные выше данные(также в ковычках).

#### Запуск
После всего этого можете запускать скрипт ``main.py`` либо в среде разработки, либо, находясь в корне репозитория, выполнив одну из комманд:
```
> python main.py
```
```
$ python3 main.py
```
в зависимости от вашей ОС. На UNIX-подобных операционных системах у вас также есть возможность запуска в фоновом режиме, дописав `` &`` после комманды запуска.

## Комманды бота
#### Стандартные(независимо от API)
 * ``/start`` инициализация бота
 * ``/help`` показать список комманд
 * ``/hello_world`` написать "Привет, мир!"
 * ``/cancel`` отменить текущую операцию
 * ``/history`` показать краткую историю запросов

#### Погодные(настройка)
 * ``/change_city`` сменить город

#### Погодные
 * ``/current`` показать текущюю погоду в вашем городе
 * ``/low`` отсортировать по **возрастанию** погодные показатели прогноза на сегодня/завтра/ближайшие 5 дней.
 * ``/high`` то же самое, что и ``/low``, но сортировка идет по **убыванию**
 * ``/custom`` отфильтровать по-вашим запросам погодные показатели прогноза на сегодня/завтра/ближайшие 5 дней

## Переменные окружения
#### Обязательные
|Переменная |значения|описание|
|:---------:|:------:|--------|
|BOT_TOKEN| строка|Бот-токен, полученный от [@BotFather](https://t.me/botfather)|
|API_KEY|строка|Ваш API-ключ. Погодный бот требует ключ от [Open Weather API](https://openweathermap.org/).|

#### Кастомизация
|Переменная |значения|описание|значение по умолчанию|
|:---------:|:------:|--------|---|
|PATH_TO_DB|строка|путь до базы данных SQLite3.|*"telebot.db"*|
|LOG_ERRORS|true/false|вкл/откл логирование всех ошибок в файл logs/errors.log|*false*|
|DEBUG_TO_FILE|true/false|вкл/откл запись **всех** логов в logs/debug.log|*false*|
