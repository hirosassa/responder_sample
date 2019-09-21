import os
import responder
import pymysql

api = responder.API()


@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"


@api.route("/hello/{who}")
def hello_to(req, resp, *, who):
    resp.text = f"hello, {who}"


@api.route("/hello/{who}/json")
def hello_to_json(req, resp, *, who):
    resp.media = {"hello": who}


# show status code
# curl -LI localhost:5042/416 -o /dev/null -w '%{http_code}\n' -s
@api.route("/416")
def teapot(req, resp):
    resp.status_code = api.status_codes.HTTP_416


# connect to DB
@api.route("/hello_db/{who}")
def hello_db(req, resp, *, who):
    conn = pymysql.connect(host=os.environ.get("DB_HOST"),
                           user=os.environ.get("DB_USER"),
                           password=os.environ.get("DB_PASSWORD"),
                           db=os.environ.get("DB_DATABASE"),
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql = f'select name, specialty from test_user where name = "{who}"'
            print(sql)
            cursor.execute(sql)
            who = cursor.fetchone()
            if who is None:
                resp.media = {"hello": "nobody"}
            else:
                resp.media = {"hello": who}
    finally:
        conn.close()


if __name__ == '__main__':
    api.run(address='0.0.0.0', port=80)
