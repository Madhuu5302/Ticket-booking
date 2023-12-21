from tic_booking.util.DBPropertyUtil import DBPropUtil
import mysql.connector as sql


class DbConn():
    def __init__(self):
        self.conn = None
        self.stmt = None
        pass

    def open(self):
        try:
            l = DBPropUtil.get_property_string()
            self.conn = sql.connect(host=l[0], username=l[1], password=l[2], database=l[3])
            if self.conn:
                print("--Database Is Connected--")
            self.stmt = self.conn.cursor()
        except Exception as e:
            print(e)

    def close(self):
        self.conn.close()
