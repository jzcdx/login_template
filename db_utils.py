from sqlalchemy import create_engine, URL, text, Table, MetaData, Column, Integer, String, Double, select, delete, update, insert
import os
import bcrypt

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
            print("dbh test function invoked")
            stmt = select(self.user_account);
            res = conn.execute(stmt);
            rows = res.mappings().all()
            conn.close()
            print(rows);
            return rows;

    def read_password(self, email): #userId
        with self.engine.connect() as conn:
            stmt = select(self.user_account).where(self.user_account.c.email == email);
            res = conn.execute(stmt);
            rows = res.mappings().all();
            conn.close()
            if rows:
                return rows[0]["password"] #returns a single dict if the email exists in your database
            return None 
    
    
    def create_account(self, new_email, new_password):
        with self.engine.connect() as conn:
            #we're gonna check if the email exists in our system first
            stmt = select(self.user_account).where(self.user_account.c.email == new_email);
            res = conn.execute(stmt);
            rows = res.mappings().all();

            if rows: #so the email is taken
                return False #this is whether or not the account creation succeeded
            
            #don't forget to hash those passwords
            salt = bcrypt.gensalt() 
            hashed = bcrypt.hashpw(new_password.encode('utf8'), salt)
            hashed = hashed.decode()

            stmt = insert(self.user_account).values(
                email = new_email,
                password = hashed
            ).returning(self.user_account.c.id)

            new_id = conn.execute(stmt)
            print("created account, new id: " , new_id.mappings().all())
            conn.commit();
            return True #acc creation succeeded

dbh = DBH()

#print("Creating account, Success: " , dbh.create_account("bearsley@gmail.com", "iambearsley"))

res = dbh.read_password("bearsley@gmail.com");
res = dbh.read_password("asdf@gmail.com")
#print(res)
pw_input = "iambearsley"
pw_input = "testpassword7"
#print("checking pw: " , bcrypt.checkpw(pw_input.encode('utf8'), res.encode('utf8')))

