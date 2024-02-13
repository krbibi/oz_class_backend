from flask import Flask, render_template
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '0000',
    db='kream',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)
cur = conn.cursor()

@app.route('/', methods = ['GET'],)
def index():
    category = '상의'
    sql = "select * from kream_data "
    cur.execute(sql)
    kream_data = cur.fetchall()

    kream_data_len = len(kream_data)
    return render_template('index.html',kream_data = kream_data,kream_data_len = kream_data_len)

if __name__ == '__main__':
	app.run(debug=True)

