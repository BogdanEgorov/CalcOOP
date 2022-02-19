import datetime as dt

class Record:
    def __init__(self, amount, date, comment):
        self.amount = amount
        self.date = dt.datetime.today()
        self.comment = comment

class Calculator:
    def __init__(self, limit):
        self.records = []
        self.limit = limit

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.datetime.now()
        today_stats = sum(record.amount for record in self.records)
        return today_stats

    def get_week_stats(self):
        today = dt.datetime.now()
        week = today - dt.timedelta(7)
        week_stats = sum(record.amount for record in self.records)
        return week_stats

class CaloriesCalculator:
    def get_calories_remained(limit):

        calories_remained = limit - Calculator.get_today_stats()
        if calories_remained <= 0:
            return "Хватит есть!"
        else:
            return ("Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более" + {calories_remained} + "кКал")

class CashCalculator:

        USD_RATE = 78.0
        EURO_RATE = 88.0
        RUB_RATE = 1.0

        def get_today_cash_remained(self, currency):
            cash_remained = self.remained()
            if cash_remained == 0:
                return 'Денег нет, держись'
            currencies = {
                'eur': ('Euro', self.EURO_RATE),
                'usd': ('USD', self.USD_RATE),
                'rub': ('руб', self.RUB_RATE),
            }
            if cash_remained > 0:
                return f'На сегодня осталось {cash_remained} '
            if cash_remained < 0:
                return f'Денег нет, держись: твой долг - {cash_remained}'


