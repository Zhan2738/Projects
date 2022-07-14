import pymysql

conn = pymysql.connect(
    host='database-nlp-results.cllvuulvkujq.us-east-2.rds.amazonaws.com',
    port=3306,
    user='nlp_2022_spring',
    password='nlp_2022_spring',
    db='result_2021_fall'
)


def get_details(search_item):
    cur = conn.cursor()
    selectstatement = "SELECT * FROM data_output A WHERE A.ANALYTE LIKE '%{}%'".format(
        search_item)
    cur.execute(selectstatement)
    details = cur.fetchall()
    return details


def get_one_record(content):
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM data_output A WHERE A.title = '{}'".format(content))
    result = cur.fetchall()
    return result
