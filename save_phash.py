import pymysql

# Open database connection
db = pymysql.connect("ec2-3-120-31-216.eu-central-1.compute.amazonaws.com","zik","LTLoY7NKgiVwxSaF","game")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()