"""
Разработайте класс с "полной инкапсуляцией", доступ к атрибутам которого и изменение данных 
реализуются через вызовы методов. В объектно-ориентированном программировании принято имена методов 
для извлечения данных начинать со слова get (взять), а имена методов, в которых свойствам 
присваиваются значения, – со слова set (установить). Например, getField, setField.
"""


class Encapsulation:
    
    def __init__(self, field):
        self.__field = field

    def getField(self):
        return self.__field

    def setField(self, new_field):
        self.__field = new_field

    def __setattr__(self, attr, value):
        if attr == '_Encapsulation__field':
            self.__dict__[attr] = value
        else:
            raise AttributeError

a = Encapsulation("Field")
print(a.getField())
a.setField("No!!")
print(a.getField())

# a.__field = "Oops!"