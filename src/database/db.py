import pymysql.cursors

def get_conection():
    try:
        #conection= pymysql.connect(host="192.168.64.3",user="emilio",password="Hol@2023",database="store")
        conection= pymysql.connect(host="emi_db",user="emilio",password="Hol@2023",database="store")
        conection.cursor(pymysql.cursors.DictCursor)
        return conection
    except (Exception) as ex:
        raise Exception(ex)