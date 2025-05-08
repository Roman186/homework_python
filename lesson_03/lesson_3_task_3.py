from mailing import Mailing
from adress import Address

to_address = Address("628900", "Tyumen", "Lenina", "15", "155")
from_address = Address("628600", "Nizhnevartovsk", "Stroiteley", "16", "56")
mailing = Mailing(to_address, from_address, 6200, "155NV")

print(mailing)
