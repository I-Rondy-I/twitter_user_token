from requests_oauthlib import OAuth1Session

# Ваши ключи приложения
API_KEY = 'ваш_API_Key'
API_SECRET_KEY = 'ваш_API_Secret_Key'

# Токены пользователя
ACCESS_TOKEN = 'ваш_Access_Token'
ACCESS_TOKEN_SECRET = 'ваш_Access_Token_Secret'

# Создание OAuth1Session с ключами и токенами
oauth = OAuth1Session(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# URL для отправки твита
tweet_url = 'https://api.twitter.com/1.1/statuses/update.json'

# Данные твита
tweet_data = {'status': 'Привет, Twitter!'}

# Отправка POST запроса
response = oauth.post(tweet_url, params=tweet_data)

# Проверка ответа
if response.status_code == 200:
    print('Твит отправлен успешно!')
else:
    print('Ошибка:', response.status_code, response.text)
