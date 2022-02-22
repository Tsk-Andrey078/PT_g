import pymysql
import config
import createTables
import dateparser
import time
import parseMethods

def no_bottom(row, connection, cursor):
    print(row)
    
    top_tag_parse = parseMethods.parse_link(row)
    print(len(top_tag_parse))

    title_cut_parse = parseMethods.parse_title(row)
    print(len(title_cut_parse))

    date_cut_parse = parseMethods.parse_date(row)    
    print(len(date_cut_parse))

    i = 1
    while i != len(top_tag_parse):
        news_id = row["RESOURCE_ID"]
        print(top_tag_parse[i])
        link = top_tag_parse[i].get("href")
        
        if link.find("http") == -1:
            url_begin = row["RESOURCE_URL"]
            index_start = url_begin.index('/', 9)
            url_begin = url_begin[0:index_start]
            link = url_begin + link
            
        title_text = title_cut_parse[i].text
        print(title_text)
        content_text = ''
        date = date_cut_parse[i].text
        date_object = dateparser.parse(date)
        date = date_object.date()
        date_unix = date_object.timestamp()
        insert_time = time.time()

        insert_command = "INSERT INTO `items` (res_id, link, title, content, nd_date, s_date, not_date) VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}')".format(news_id, link, title_text, content_text, date_unix, insert_time, date)

        cursor.execute(insert_command)
        connection.commit()

        i += 1

def have_bottom(row, connection, cursor):
    print(row)
    
    top_tag_parse = parseMethods.parse_link(row)
    print(len(top_tag_parse))

    title_cut_parse = parseMethods.parse_title(row)
    print(len(title_cut_parse))

    bottom_tag_parse = parseMethods.parse_bottom(row)
    print(len(bottom_tag_parse))

    date_cut_parse = parseMethods.parse_date(row)    
    print(len(date_cut_parse))

    i = 1
    while i != len(top_tag_parse):
        news_id = row["RESOURCE_ID"]
        print(top_tag_parse[i])
        link = top_tag_parse[i].get("href")
        
        if link.find("http") == -1:
            url_begin = row["RESOURCE_URL"]
            index_start = url_begin.index('/', 9)
            url_begin = url_begin[0:index_start]
            link = url_begin + link
            
        title_text = title_cut_parse[i].text
        print(title_text)
        content_text = bottom_tag_parse[i].text
        date = date_cut_parse[i].text
        date_object = dateparser.parse(date)
        date = date_object.date()
        date_unix = date_object.timestamp()
        insert_time = time.time()

        insert_command = "INSERT INTO `items` (res_id, link, title, content, nd_date, s_date, not_date) VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}')".format(news_id, link, title_text, content_text, date_unix, insert_time, date)

        cursor.execute(insert_command)
        connection.commit()

        i += 1

try:
    createTables.create_base_tables()

    connection = pymysql.connect(
        host = config.host,
        port = config.port,
        user = config.user,
        password = config.password,
        database = config.database,
        cursorclass = pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor: 
            output_command = "SELECT * FROM `resource`"
            cursor.execute(output_command)
            rows = cursor.fetchall()
            for row in rows:
                if len(row["bottom_tag"]) < 3:
                    no_bottom(row, connection, cursor)

                if len(row["bottom_tag"]) > 3:
                    have_bottom(row, connection, cursor)

    except Exception as exc:
        print("Error! 2: " + exc)
    finally:
        connection.close()

except Exception as exc:
    print("Error! 1: " + exc)