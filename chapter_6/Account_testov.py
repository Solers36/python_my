"""
Создайте класс Transaction, который хранит сумму, дату, валюту
(по умолчанию «USD» – доллар США), курс валюты по отношению
к доллару (по умолчанию 1) и описание (по умолчанию None). Все ат>
рибуты данных должны быть частными. Реализуйте следующие
свойства, доступные только для чтения: amount, date, currency,
usd_conversion_rate, description и usd (вычисляется, как amount *
usd_conversion_rate). Реализацию класса можно уместить в шестьде>
сят строк программного кода, включая несколько простейших доктестов.
"""


class Transaction:
    def __init__(self, amount, date, currency="USD", usd_conversion_rate=1, description=None):
        """
        >>> transaction_usd = Transaction(10, 10.10.2010)
        >>> print(transaction_usd.amount, transaction_usd.currency, transaction_usd.date,
                    transaction_usd.usd_conversion_rate, transaction_usd.description, transaction_usd.usd)
        10 USD 10.10.2010 1 None 10    
        >>> transaction_rub = Transaction(20, "20.02.2020", "RUB", 0.013, "Transaction #123")
        >>> print(transaction_rub.amount, transaction_rub.currency, transaction_rub.date,
                    transaction_rub.usd_conversion_rate, transaction_rub.description, transaction_rub.usd)
        20 RUB 20.02.2020 0.013 Transaction #123 0.26
        """
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__usd_conversion_rate = usd_conversion_rate
        self.__description = description

    @property
    def amount(self):
        return self.__amount

    @property
    def date(self):
        return self.__date

    @property
    def currency(self):
        return self.__currency

    @property
    def usd_conversion_rate(self):
        return self.__usd_conversion_rate

    @property
    def description(self):
        return self.__description

    @property
    def usd(self):
        return self.__amount * self.__usd_conversion_rate
