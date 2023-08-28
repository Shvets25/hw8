from datetime import date, timedelta

def get_birthdays_per_week(users):
    today = date.today()
    current_weekday = today.weekday()  # 0 - Monday, 6 - Sunday
    days_in_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    birthdays_per_week = {}

    for day in days_in_week:
        days_ahead = (days_in_week.index(day) - current_weekday) % 7
        target_date = today + timedelta(days=days_ahead)
        birthdays_per_week[day] = []

        for user in users:
            birthday = user["birthday"]
            if (birthday - target_date).days < 7:
                birthdays_per_week[day].append(user["name"])

    return birthdays_per_week

# Тестові дані
users = [
    {"name": "Bill", "birthday": date(2023, 8, 28)},
    {"name": "Jan", "birthday": date(2023, 8, 30)},
    {"name": "Kim", "birthday": date(2023, 8, 31)}
]

# Виведення результатів
birthdays_this_week = get_birthdays_per_week(users)
for day, names in birthdays_this_week.items():
    print(f"{day}: {names}")
