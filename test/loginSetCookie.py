from app.services.cookie import set_cookies
def loginSetCookie(username, user_id, session_id, user_prefs):
    cookie_data = set_cookies(username, user_id, session_id, user_prefs)
    print(cookie_data)
    return cookie_data

loginSetCookie("username", "user_id", "session_id", "user_prefs")
