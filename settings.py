#mysql settings
class MySQLConfig(object):

	DEBUGE = True
	SECRET_KEY = "fkbmbhjkkjgjlklnmbvbnvjhgiu"
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{ipaddress}:{port}/{database}".format(
		username="root",password="zxcvbnm12321",ipaddress="localhost",port="3306",database="mall")
		# username="root",password="123456",ipaddress="localhost",port="3306",database="mall")
	SQLALCHEMY_TRACK_MODIFICATIONS = True#动态追踪修改设置
	SQLALCHEMY_ECHO = True 

WHITE_NAME_LIST = ["/api/login","/api/regist","/api/goods/type","/api/by/tag/goods"]