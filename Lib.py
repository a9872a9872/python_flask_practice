import hashlib
import json

def doHash(data):
    m = hashlib.md5()
    m.update(data.encode("utf-8"))
    return m.hexdigest()

def seed(Member, Post):
    testData = Member(name='admin', email='admin@gmail.com', password=doHash('admin'))
    testData.save()

    testData2 = Member(name='test', email='test@gmail.com', password=doHash('test'))
    testData2.save()

    with open('food.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        food = data['food']
        dessert = data['dessert']
        drink = data['drink']
        for data in food:
            testData = Post(
                name=data['name'],
                address=data['address'],
                time=data['time'],
                phone_number=data['phone_number'],
                website=data['url'],
                image=data['image'],
                type=0
            )
            testData.save()
        for data in dessert:
            testData = Post(
                name=data['name'],
                address=data['address'],
                time=data['time'],
                phone_number=data['phone_number'],
                website=data['url'],
                image=data['image'],
                type=1
            )
            testData.save()
        for data in drink:
            testData = Post(
                name=data['name'],
                address=data['address'],
                time=data['time'],
                phone_number=data['phone_number'],
                website=data['url'],
                image=data['image'],
                type=2
            )
            testData.save()