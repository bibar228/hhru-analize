import time
import pymysql





def sql_add(title: str, count_skill: int):
    try:
        values = (title, count_skill)
        try:
            connection = pymysql.connect(host='127.0.0.1', port=3306, user='hh_user', password='warlight123',
                                             database='hh',
                                             cursorclass=pymysql.cursors.DictCursor)
            try:
                with connection.cursor() as cursor:
                    insert_query = "INSERT INTO `vision_skills` (title, count_skill) " \
                                   "VALUES (%s, %s)"
                    cursor.execute(insert_query, (values))
                    connection.commit()
            finally:
                connection.close()

        except Exception as e:
           print(e)

    except Exception as e:
        print(e)


#sql_req("LUNCUSDT", 7.21, 1.87, 2.65, 0.92, -0.05, 16078)
def sql_del():
    try:
        connection = pymysql.connect(host='127.0.0.1', port=3306, user='hh_user', password='warlight123',
                                     database='hh',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                insert_query = "DELETE FROM `vision_skills`"
                cursor.execute(insert_query)
                connection.commit()
        finally:
            connection.close()

    except Exception as e:
        print(e)