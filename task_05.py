from datetime import datetime, timedelta


def date_in_future(number_of_days):
    today = datetime.now()
    if type(number_of_days) is not int:
        return today.strftime("%d-%m-%Y %H:%M:%S")
    date_in_the_future = today + timedelta(number_of_days)
    return date_in_the_future.strftime("%d-%m-%Y %H:%M:%S")


# print(date_in_future([]))
