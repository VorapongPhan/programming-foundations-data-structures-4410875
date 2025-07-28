user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    items = {}

    for key in user_pref.keys():
        if user_pref[key] != None:
            items[key] = user_pref[key]

    return items


print(update_preferences(user_preferences))
