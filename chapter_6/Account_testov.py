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
        >>> transaction_usd.amount, transaction_usd.currency, transaction_usd.date,
            transaction_usd.usd_conversion_rate, transaction_usd.description, transaction_usd.usd
        (10 USD 10.10.2010 1 None 10)    
        >>> transaction_rub = Transaction(20, "20.02.2020", "RUB", 0.013, "Transaction #123")
        >>> transaction_rub.amount, transaction_rub.currency, transaction_rub.date,
            transaction_rub.usd_conversion_rate, transaction_rub.description, transaction_rub.usd
        (20 RUB 20.02.2020 0.013 Transaction #123 0.26)
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



"""
Реализуйте класс Account, который хранил бы номер счета, назва>
ние счета и список транзакций (объектов класса Transaction). Номер
счета должен быть реализован в виде свойства, доступного только
для чтения. Название счета должно быть реализовано в виде свой>
ства, доступного для чтения и для записи с проверкой длины назва>
ния, которое должно содержать не менее четырех символов. Класс
должен поддерживать встроенную функцию len() (возвращая чис>
ло транзакций) и содержать два вычисляемых свойства, доступных
только для чтения: balance, возвращающее баланс счета в долларах
США, и all_usd, возвращающее True, если все транзакции выполня>
лись в долларах США, или False – в противном случае. Добавьте
три дополнительных метода: apply() для добавления транзакции,
save() и load(). Методы save() и load() должны сохранять и загру>
жать объекты в двоичном формате, в файле, имя которого совпада>
ет с номером счета и с расширением .acc. Они должны сохранять
и загружать номер счета, название счета и все транзакции. Реали>
зацию класса можно уместить в девяносто строк программного ко>
да вместе с несколькими простейшими доктестами, включающими
проверку операций сохранения и загрузки с помощью такого про>
граммного кода, как name = os.path.join(tempfile.gettempdir(), ac!
count_name), который позволяет получить подходящее имя времен>
ного файла. Требуется удалить временные файлы по завершении
доктестов.
"""
class LoadError(Exception):
    pass

class SaveError(Exception):
    pass


import pickle

class Account:
    def __init__(self, number, name):
        """Contains information about the account(number, name, list of transactions).
        >>> import os
        >>> import tempfile
        >>> import Account_testov
        >>> name = os.path.join(tempfile.gettempdir(), "0001")
        >>> account = Account_testov.Account(name, "My organization")
        >>> account.name, account.balance, account.all_usd, len(account)
        (My organization 0 True 0)
        >>> account.apply(Account_testov.Transaction(138, "01-10-2010"))
        >>> account.apply(Account_testov.Transaction(257, "21-10-2010", "USD"))
        >>> account.apply(Account_testov.Transaction(-13, "15-11-2010"))
        >>> account.name, account.balance, account.all_usd, len(account)
        (My organization 382 True 3)
        >>> account.apply(Account_testov.Transaction(570, "01-10-2010", "RUB", 0.013))
        >>> account.name, account.balance, account.all_usd, len(account)
        (My organization 389.41 False 4)
        >>> account.save() 
        >>> duplicate_account = Account_testov.Account(name, "My organization")
        >>> duplicate_account.name, duplicate_account.balance, duplicate_account.all_usd, len(duplicate_account)
        (My organization 0 True 0)
        >>> duplicate_account.load()
        >>> duplicate_account.name, duplicate_account.balance, duplicate_account.all_usd, len(duplicate_account)
        (My organization 389.41 False 4)
        >>> try:
        ...     os.remove(name + ".acc")
        ... except EnvironmentError:
        ...     pass
        """
        self.__number = number
        self.__name = name
        self.__list_of_transactions = []

    @property
    def number(self):
        """Account number. Read only."""
        return self.__number

    @property
    def name(self):
        """Account title. For reading and writing. It must be at least 4 characters long."""  
        return self.__name

    @name.setter
    def name(self):
        assert len(self.__name) >= 4, "The account name must contain at least four characters."
        return self.__name

    def __len__(self):
        """Returns the number of transactions"""
        return len(self.__list_of_transactions)

    @property
    def balance(self):
        """Returns the account balance in US dollars."""
        account_balance = 0
        for transaction in self.__list_of_transactions:
            account_balance += transaction.usd
        return account_balance

    @property
    def all_usd(self):
        """Returns True if all transactions were made in US dollars, False otherwise"""
        for transaction in self.__list_of_transactions:
            if transaction.currency != "USD":
                return False
        return True

    def apply(self, new_transaction):
        """Adds transactions to the list."""
        assert "Transaction" in str(type(new_transaction)),  "You can only add objects of the 'Transactions' class"
        return self.__list_of_transactions.append(new_transaction)

    
    def save(self):
        """Saves the object in binary format with the extension ". acc"
        """
        filename = self.__name + ".acc"
        fh = None
        try:
            data = [self.__number, self.__name, self.__list_of_transactions]
            fh = open(filename, "wb")
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()

    def load(self):
        """Loads object data from a file
        """
        filename = self.__name + ".acc"
        fh = None
        try:
            fh = open(filename, "rb")
            data = pickle.load(fh)
            (self.__number, self.__name, self.__list_of_transactions) = data
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()
