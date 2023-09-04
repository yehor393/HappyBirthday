from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    """
    Get a schedule of birthdays per week for a list of users.

    Args:
        users (list): A list of user dictionaries with "name" and "birthday" keys.

    Returns:
        dict: A dictionary where keys are weekdays and values are lists of names.
    """

    today = date.today()
    weekdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }
    birthday_schedule = {}

    def get_birthday_year(birthday):
        return birthday.replace(year=today.year + 1) if birthday.month == 1 else birthday.replace(year=today.year)

    def add_to_schedule(weekday, name):
        if weekday not in birthday_schedule:
            birthday_schedule[weekday] = []
        if name not in birthday_schedule[weekday]:
            birthday_schedule[weekday].append(name)

    next_week_start = today - timedelta(days=today.weekday()) + timedelta(days=6)
    next_week_start_1 = next_week_start + timedelta(days=1)
    end_for_next_week = today + timedelta(days=6)
    next_friday = today - timedelta(days=today.weekday()) + timedelta(days=11)
    start_current_week = today - timedelta(days=today.weekday())

    for user in users:
        if user["birthday"] is not None:
            birthday = get_birthday_year(user["birthday"])
            birth_weekday = weekdays.get(birthday.weekday())
            is_weekend = birth_weekday in ['Saturday', 'Sunday']

            if birthday >= start_current_week:
                if is_weekend and next_friday >= birthday >= start_current_week:
                    next_monday = weekdays.get(next_week_start_1.weekday())
                    add_to_schedule(next_monday, user['name'])
                elif next_friday >= birthday >= start_current_week:
                    add_to_schedule(birth_weekday, user['name'])

                if end_for_next_week > birthday > next_week_start:
                    add_to_schedule(birth_weekday, user['name'])

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
