from sqlalchemy import create_engine, Table, Column, String, Date, MetaData, text, orm
import logging
import sqlalchemy
import os
import json
THIS_FILE = os.path.dirname(os.path.abspath(__file__))
PROJ_FILE = os.path.abspath(os.path.join(THIS_FILE,"../"))

class DbConnector:
    def __init__(self):
        self.db_config = self.read_db()
        self._init_db_engine()
        self.create_session()

    def _init_db_engine(self):
        self.engine = create_engine(f'mysql+pymysql://{self.db_config["user"]}:{self.db_config["password"]}@{self.db_config["host"]}/{self.db_config["database"]}')

        logging.info(f"Connected to database {self.db_config['database']}")
        #print(f"Connected to database {self.db_config['database']}")

    def create_session(self):
        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=self.engine)
        self.Session = Session()

    def read_db(self):
        path = f"{PROJ_FILE}/database/config.json"
        with open(path,"rb") as f:
            return json.load(f)
db_connector = DbConnector()
connection = db_connector.engine.connect()
metadata = sqlalchemy.MetaData()
print(connection,metadata)
