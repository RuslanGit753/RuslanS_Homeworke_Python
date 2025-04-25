from address import Address
from mailing import Mailing

to_address = Address(
    "123456", "Москва", "Ленинградский проспект", "10", "5"
)
from_address = Address(
    "654321", "Санкт-Петербург", "Невский проспект", "20", "10"
)

mailing = Mailing(to_address, from_address, 1500, "TRACK123456789")

print(mailing)
