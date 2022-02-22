import pymysql
import config

def create_base_tables():
    try:
        connection = pymysql.connect(
            host = config.host,
            port = config.port,
            user = config.user,
            password = config.password,
            database = config.database,
            cursorclass = pymysql.cursors.DictCursor
        )
        print("Connection is successfully")

        try:
            with connection.cursor() as cursor:
                delete_command = "DROP TABLE resource"
                delete_second_command = "DROP TABLE items"
                cursor.execute(delete_command)
                cursor.execute(delete_second_command)

            with connection.cursor() as cursor:
                create_command = "CREATE TABLE `resource`(RESOURCE_ID int AUTO_INCREMENT,"\
                                " RESOURCE_NAME varchar(96), RESOURCE_URL varchar(2048),"\
                                " top_tag varchar(96), bottom_tag varchar(96), title_cut varchar(96), date_cut varchar(96), PRIMARY KEY (RESOURCE_ID));"
                cursor.execute(create_command)
                print("Table `Resource` is created")

                for element in config.resource_list:
                    insert_command = "INSERT INTO `resource`(RESOURCE_NAME, RESOURCE_URL, top_tag, bottom_tag, title_cut, date_cut) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(element["RESOURCE_NAME"], element["RESOURCE_URL"], element["top_tag"], element["bottom_tag"], element["title_cut"], element["date_cut"])

                    cursor.execute(insert_command)
                    connection.commit()

        except Exception as exc:
            print(exc)

        try:
            with connection.cursor() as cursor: 
                create_second_command = "CREATE TABLE `items`(id int AUTO_INCREMENT, res_id int, link varchar(2048), title varchar(2048), content varchar(2048), nd_date varchar(128), s_date varchar(128), not_date varchar(128), PRIMARY KEY (id));"
                cursor.execute(create_second_command)
                print("Table `Items` is created")
        except Exception as exc:
            print(exc)
        finally:
            connection.close()

    except Exception as exc:
        print(exc)