import app
from models import Admin, db
from utils import md5, getNowDataTime

if __name__ == '__main__':
    with app.app.app_context():
        account = "admin"
        admin = Admin.query.filter_by(account=account).first()
        if admin:
            print("The user already exists")
        else:
            data = {
                "name": "admin",
                "account": "admin",
                "password": md5("123456"),
                "createTime": getNowDataTime(),
                "level": 0
            }
            admin = Admin(**data)
            db.session.add(admin)
            db.session.commit()
            print("Create Success")
