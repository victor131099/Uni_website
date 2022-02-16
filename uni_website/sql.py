import sqlite3
import os
from sqlite3.dbapi2 import Date
import bcrypt
import time
# This class is a simple handler for all of our SQL database actions
# Practicing a good separation of concerns, we should only ever call
# These functions from our models

# If you notice anything out of place here, consider it to your advantage and don't spoil the surprise


class SQLDatabase():
    '''
        Our SQL Database

    '''

    # Get the database running
    def __init__(self, database_arg="user.db"):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "user.db")
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
        self.database_setup()
    # SQLite 3 does not natively support multiple commands in a single statement
    # Using this handler restores this functionality
    # This only returns the output of the last command

    def execute(self, sql_string):
        out = None
        for string in sql_string.split(";"):
            try:
                out = self.cur.execute(string)
            except:
                pass
        return out

    # Commit changes to the database
    def commit(self):
        self.conn.commit()

    # -----------------------------------------------------------------------------

    # Sets up the database
    # Default admin password
    def database_setup(self, admin_password='kTLc$9Bs777'):

        # Create the the database
        self.execute("drop table if exists user")
        self.execute("CREATE TABLE user (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,username char(100) NOT NULL, password char(100) NOT NULL, admin INTEGER, isMuted char(3) NOT NULL, attempts INTEGER DEFAULT 0, last_attempt INTEGER DEFAULT 0)")
        salt = bcrypt.gensalt()
        tom_pwd = bcrypt.hashpw("kTLc$9Bs_tom".encode(), salt).decode()
        sql_query = """
            INSERT INTO user (id,username, password, admin, isMuted) VALUES (1, 'Tom', '{tom_pwd}', 1, 'no')"""
        sql_query = sql_query.format(tom_pwd=tom_pwd)
        self.execute(sql_query)
        salt = bcrypt.gensalt()
        victor_pwd = bcrypt.hashpw("kTLc$9Bs_victor".encode(), salt).decode()
        sql_query = """
            INSERT INTO user (id,username, password, admin, isMuted) VALUES (2, 'Victor', '{victor_pwd}', 1, 'no')"""
        sql_query = sql_query.format(victor_pwd=victor_pwd)
        self.execute(sql_query)
        salt = bcrypt.gensalt()
        dylan_pwd = bcrypt.hashpw("kTLc$9Bs_dylan".encode(), salt).decode()
        sql_query = """
            INSERT INTO user (id,username, password, admin, isMuted) VALUES (3, 'Dylan', '{dylan_pwd}', 1, 'no')"""
        sql_query = sql_query.format(dylan_pwd=dylan_pwd)
        self.execute(sql_query)
        self.execute("drop table if exists question")
        self.execute(
            "CREATE TABLE question (qid INTEGER PRIMARY KEY,id NOT NULL, qdate TIMESTAMP,description char(1000) , title char(1000), nresponse INTEGER)")
        self.execute("drop table if exists comment")
        self.execute(
            "CREATE TABLE comment (cid INTEGER PRIMARY KEY,qid INTEGER NOT NULL,id INTEGER NOT NULL,  cdate TIMESTAMP,description char(1000))")
        self.execute("INSERT INTO question (qid,id, qdate, description, title, nresponse ) VALUES (1, 3, CURRENT_TIMESTAMP, 'In html, what does the <p> tag do?' , 'what does the <p> tag do?' , 3 )")
        self.execute("INSERT INTO question (qid,id, qdate, description, title, nresponse ) VALUES (2, 1, CURRENT_TIMESTAMP, 'I dont understand the concept of tags. Can someone help please?' , 'What is a HTML tag?' ,0 )")
        self.execute("INSERT INTO question (qid,id, qdate, description, title, nresponse ) VALUES (3, 2, CURRENT_TIMESTAMP, 'I thought tags were just in HTML, what do they do in CSS?' , 'What is a CSS tag? ',0 )")
        self.execute(
            "INSERT INTO comment (cid ,qid ,id,  cdate,description ) VALUES  (1, 1,1, CURRENT_TIMESTAMP, 'The <p> tag creates a paragraph of text.')")
        self.execute(
            "INSERT INTO comment (cid ,qid ,id ,  cdate,description ) VALUES  (2, 1,1, CURRENT_TIMESTAMP, 'It allows you to display characters on the webpage.')")
        self.execute(
            "INSERT INTO comment (cid,qid , id, cdate,description ) VALUES  (3, 1,1, CURRENT_TIMESTAMP, 'Hopefully that answers your question!')")
        self.commit()
        # Add our admin user
        self.add_user('admin', admin_password, admin=1)

    # -----------------------------------------------------------------------------
    # User handling
    # -----------------------------------------------------------------------------

    # Add a user to the database
    def add_user(self, username, password, admin=0):
        encoded = password.encode()
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(encoded, salt).decode()
        sql_cmd = """
                INSERT INTO user
                (username, password, admin, isMuted)
                VALUES('{username}', '{hashed}', {admin}, '{isMuted}')
            """
        sql_cmd = sql_cmd.format(
            username=username, hashed=hashed, admin=admin, isMuted='no')

        self.execute(sql_cmd)
        self.commit()
        return True

    # -----------------------------------------------------------------------------
    # Add a user to the database
    def display_questions(self):

        self.cur.execute(
            "SELECT * FROM question INNER JOIN user on question.id = user.id")

        result = self.cur.fetchall()

        return result

    def create_post(self,  title, description, id, nresponse=0):
        if self.check_user_muted(id):
            return

        self.cur.execute("SELECT count(*) FROM question")
        count = int(self.cur.fetchone()[0])
        qid = count+1
        sql_cmd = """ INSERT INTO question VALUES({qid}, {id}, CURRENT_TIMESTAMP, '{description}', '{title}', {nresponse})"""
        sql_cmd = sql_cmd.format(
            qid=qid, id=id, description=description, title=title, nresponse=nresponse)
        self.execute(sql_cmd)
        self.commit()
        return True

    def display_post(self,  qid):
        sql_query = """SELECT * FROM question q join user u on u.id =q.id  where qid ={qid}"""
        sql_query = sql_query.format(qid=qid)
        self.cur.execute(sql_query)
        result = self.cur.fetchone()
        print(result)
        return result

    def comment_post(self, description,  qid, id):
        if self.check_user_muted(id):
            return

        self.cur.execute("SELECT count(*) FROM comment")
        count = int(self.cur.fetchone()[0])
        cid = count+1

        sql_query = """ INSERT INTO comment VALUES({cid}, {qid},{id}, CURRENT_TIMESTAMP, '{description}')"""
        sql_query = sql_query.format(
            cid=cid, qid=qid, id=id,  description=description)
        self.cur.execute(sql_query)
        self.commit()
        sql_query = """SELECT q.qid FROM comment c join question q on c.qid =q.qid  where q.qid ={qid}"""
        sql_query = sql_query.format(qid=qid)
        self.cur.execute(sql_query)
        result = int(self.cur.fetchone()[0])
        print(result)
        sql_query = """ update question set nresponse = nresponse+1 where qid = {result}"""
        sql_query = sql_query.format(result=result)
        self.cur.execute(sql_query)
        self.commit()
        return result
    # Check login credentials

    def search_question(self, word):
        sql_query = """SELECT * FROM question  where title like '%{word}%'"""
        sql_query = sql_query.format(word=word)
        self.cur.execute(sql_query)
        result = self.cur.fetchall()
        print(result)
        return result

    def display_comment(self, qid):
        sql_query = "SELECT * FROM comment c inner join user u on u.id = c.id where c.qid ={qid}"
        sql_query = sql_query.format(qid=qid)
        self.cur.execute(sql_query)
        result = self.cur.fetchall()
        print(result)
        return result

    def check_credentials(self, username, password):
        sql_query = """
                SELECT password FROM user WHERE username = '{username}'
        """
        sql_query = sql_query.format(username=username)
        self.cur.execute(sql_query)
        result = self.cur.fetchone()
        hashed_pass = ""
        if result is not None:
            hashed_pass = result[0]
        try:
            if bcrypt.checkpw(password.encode(), hashed_pass.encode()):
                return True
            return False
        except ValueError:
            return False

    # check if a user exists
    def user_exists(self, username):
        sql_query = """
            SELECT username FROM user WHERE username = '{username}'
        """
        sql_query = sql_query.format(username=username)
        self.cur.execute(sql_query)
        result = self.cur.fetchall()

        if len(result) >= 1:
            return True
        else:
            return False

    # Get all users in table
    def get_all_users(self):
        sql_query = "SELECT username FROM user"
        self.cur.execute(sql_query)
        result = self.cur.fetchall()
        return result

    # Get all users muted or unmuted value
    def get_all_users_muted(self):
        sql_query = "SELECT username, isMuted FROM user"
        self.cur.execute(sql_query)
        result = self.cur.fetchall()
        return result

    # Check if user is muted or not
    def check_user_muted(self, id):
        sql_query = """
            SELECT isMuted FROM user WHERE id = {id}
        """
        sql_query = sql_query.format(id=id)
        self.cur.execute(sql_query)
        result = self.cur.fetchone()

        if result is not None:
            mute_status = result[0]
        else:
            return False

        if mute_status == "yes":
            return True
        return False

    # Delete user from table
    def delete_user(self, username):
        sql_query = """
            DELETE FROM user WHERE username = '{username}'
        """
        sql_query = sql_query.format(username=username)
        self.cur.execute(sql_query)
        self.commit()

    # Mute or unmute user from table
    def mute_user(self, username, isMuted):
        sql_query = """
            UPDATE user SET isMuted = '{isMuted}' WHERE username = '{username}'
        """
        if(isMuted == "yes"):
            sql_query = sql_query.format(isMuted="no", username=username)
        else:
            sql_query = sql_query.format(isMuted="yes", username=username)

        self.cur.execute(sql_query)
        self.commit()

    # Check if current user is an admin
    def is_admin(self, id):
        sql_query = """
            SELECT admin FROM user WHERE id = {id}
        """
        sql_query = sql_query.format(id=id)
        self.cur.execute(sql_query)
        result = self.cur.fetchone()

        if result is not None:
            admin_status = result[0]
        else:
            return False

        if admin_status:
            return True
        return False

    def get_userid(self, username):
        sql_query = """
            SELECT id FROM user WHERE username = '{username}'
        """
        sql_query = sql_query.format(username=username)
        self.cur.execute(sql_query)
        result = self.cur.fetchone()

        if result is not None:
            return result[0]
        else:
            return False

    def get_all_ids(self):
        sql_query = """
            SELECT id FROM user
        """
        self.cur.execute(sql_query)
        result = self.cur.fetchall()
        return result

    def check_id_username(self, id, username):
        sql_query = """
            SELECT id FROM user WHERE username = '{username}' AND id = '{id}'
        """
        sql_query = sql_query.format(username=username, id=id)
        self.cur.execute(sql_query)
        result = self.cur.fetchone()

        if result is not None:
            return result[0]
        return False

    # add a login attempt to the database based on the user id, and whether it was successful or not (True or False)
    def add_login_attempt(self, id, successful):
        if not successful:
            sql_query = """ update user set attempts = attempts+1, last_attempt = {time} where id = {id}"""
        else:
            sql_query = """ update user set attempts = 0, last_attempt = {time} where id = {id}"""
        sql_cmd = sql_query.format(
            id=id, time=time.time())
        self.execute(sql_cmd)
        self.commit()
        return

    # return whether the user can login, based on their login attempts and last login
    def login_allowed(self, uid):
        sql_query = """
            SELECT last_attempt, attempts FROM user WHERE id = '{id}'
        """
        sql_query = sql_query.format(id=uid)
        self.cur.execute(sql_query)
        result = self.cur.fetchone()
        if result == None:
            return False
        if(result[0] == None or result[1] == None):
            return False
        if result[1] < 3 or result[0]+(60*5) < time.time():
            return True
        return False
