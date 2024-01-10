import pymysql.cursors

def get_conection():
    try:
        conection= pymysql.connect(host="mysql_db",user="emilio",password="pr@ct1c@",database="store")
        conection.cursor(pymysql.cursors.DictCursor)
        return conection
    except (Exception) as ex:
        raise Exception(ex)