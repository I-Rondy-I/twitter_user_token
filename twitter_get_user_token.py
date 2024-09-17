from flask import Flask, redirect, request, session, url_for
from requests_oauthlib import OAuth1Session
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Klucz do sesji Flask (zmień na coś bardziej tajnego)

# Twoje klucze aplikacji Twitter
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'

@app.route('/')
def index():
    # Utwórz sesję OAuth1
    oauth = OAuth1Session(API_KEY, API_SECRET_KEY)
    # Uzyskaj token wstępny
    fetch_response = oauth.fetch_request_token(REQUEST_TOKEN_URL)
    # Zapisz token wstępny w sesji
    session['oauth_token'] = fetch_response.get('oauth_token')
    session['oauth_token_secret'] = fetch_response.get('oauth_token_secret')
    # Przekieruj użytkownika do strony autoryzacji Twittera
    authorization_url = oauth.authorization_url(AUTHORIZATION_URL)
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    # Pobierz token i sekret z sesji
    oauth_token = session.get('oauth_token')
    oauth_token_secret = session.get('oauth_token_secret')

    # Utwórz sesję OAuth1 z tokenami
    oauth = OAuth1Session(API_KEY, API_SECRET_KEY, oauth_token, oauth_token_secret)
    # Uzyskaj tokeny dostępu
    oauth_response = oauth.fetch_access_token(ACCESS_TOKEN_URL)
    
    # Zapisz tokeny do pliku
    with open('token.txt', 'w') as file:
        file.write(f"Access Token: {oauth_response.get('oauth_token')}\n")
        file.write(f"Access Token Secret: {oauth_response.get('oauth_token_secret')}\n")
    
    return 'Tokeny zostały zapisane do pliku token.txt'

if __name__ == '__main__':
    app.run(debug=True)
