import amino
email = input("Email/Почта: ")
password = input("Password/Пароль: ")
client=amino.Client()
client.login(email=email, password=password)
while True:
    link = input('ану быстра ввел че те нада узнать: ');
    linkInfo = client.get_from_code(link)
    info = info.json["extensions"]["linkInfo"];
    comid  = info["ndcId"];
    objectid = info["objectId"];
    print(f'ID сообщества: {comid} ID объекта: {objectid}')
