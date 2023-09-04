from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):

    today = date.today()
    birthday_schedule = {}

    for user in users:
        # Check if the user has a valid birthday and if the month of the birthday is January
        if user["birthday"] is not None and user["birthday"].month == 1:
            birthday = user["birthday"].replace(year=today.year + 1)
            birth_weekday = birthday.strftime('%A')
        else:
            # Replace the year of the user's birthday with the current year
            birthday = user["birthday"].replace(year=today.year)
            birth_weekday = birthday.strftime('%A')

        # Check if the user's birthday is today or in the future
        if birthday >= today:
            # Check if the birthday falls on a weekend (Saturday or Sunday)
            if birth_weekday in ['Saturday', 'Sunday']:
                next_monday = (today + timedelta(days=(7 - today.weekday()))).strftime('%A')
                birthday_schedule.setdefault(next_monday, []).append(user['name'])
            else:
                birthday_schedule.setdefault(birth_weekday, []).append(user['name'])

    return birthday_schedule

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
