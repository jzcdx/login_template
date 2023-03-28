from sqlalchemy import create_engine, URL, text, Table, MetaData, Column, Integer, String, Double, select, delete, update, insert
import os

class DBH: #database helper
    def __init__(self):
        url_object = URL.create(
            "postgresql+psycopg2",
            username="postgres",
            password=os.environ['pg_pw_local'],  # DO NOT ESCAPE THIS PASSWORD 
            host="localhost",
            database="login_placeholder"
        )   
        self.engine = create_engine(url_object)

        metadata_obj = MetaData()
        self.user_account = Table(
            "user_account",
            metadata_obj,
            Column("id", Integer),
            Column("email", String(100)),
            Column("password", String(100)),
        )

    def test(self): #to see if the connections work
        with self.engine.connect() as conn:
            stmt = select(self.user_account);
            res = conn.execute(stmt);
            rows = res.mappings().all()
            print(rows);
            return rows;

    def get_password(self, email): #userId
        with self.engine.connect() as conn:
            stmt = select(self.user_account).where(self.user_account.c.email == email);
            res = conn.execute(stmt);
            rows = res.mappings().all();
            if rows:
                return rows[0] #returns a single dict if the email exists in your database
            return None 
    
    """
    def create_account():
        with self.engine.connect() as conn:
            stmt = 
    """
dbh = DBH()

res = dbh.get_password("asdff@gmail.com");


