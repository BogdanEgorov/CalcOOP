from main import CashCalculator
from main import Record

cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
# и к этой записи тоже дата должна добавиться автоматически

cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))

# а тут пользователь указал дату, сохраняем её

cash_calculator.add_record(Record(amount=3000,comment='бар в Танин др', date='08.11.2019'))

print(cash_calculator.get_today_cash_remained('rub'))