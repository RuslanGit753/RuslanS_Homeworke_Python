from smartphone import Smartphone

catalog = [
    Smartphone('Apple', 'iPhone 13 Pro', '+1 212-555-1234'),
    Smartphone('Samsung', 'Galaxy S21 Ultra', '+44 20 7946 0958'),
    Smartphone('Google', 'Pixel 6 Pro', '+1 415-555-5678'),
    Smartphone('OnePlus', 'OnePlus 9 Pro', '+91 98765 43210'),
    Smartphone('Xiaomi', 'Mi 11 Ultra', '+86 139 1234 5678')
]

for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model}. {smartphone.num}.')
