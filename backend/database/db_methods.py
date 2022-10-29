from database.db_connector import DbConnector
from sqlalchemy import *
import sqlalchemy
class DbMethods():
    def __init__(self) -> None:
        self.db_connector = DbConnector()
        self.connection = self.db_connector.engine.connect()
        self.metadata = sqlalchemy.MetaData()
        self.locations = sqlalchemy.Table("locations",
        self.metadata,
        autoload=True,
        autoload_with=self.db_connector.engine,
        )
        self.routes = sqlalchemy.Table("routes",
        self.metadata,
        autoload=True,
        autoload_with=self.db_connector.engine,
        )
    def location_search_db(self,lat,log,keyword):
        lat_max = lat + 0.01
        lat_min = lat - 0.01
        log_max = log + 0.01
        log_min = log - 0.01

        stmt = select([self.locations]).where(and_(and_(between(self.locations.columns.latitude, lat_min, lat_max), between(self.locations.columns.longitude, log_min, log_max)), self.locations.columns.keyword == keyword))
        result = self.connection.execute(stmt)
        #print(result.fetchall())
        return result.fetchall()

    def location_insert_db(self,lat,log,keyword,filename):
        stmt = insert(self.locations).values(latitude=lat, longitude=log,keyword = keyword,filename = filename)
        result = self.connection.execute(stmt)

    def route_search_db(self,starting,destination):
        s_lat,s_log = starting
        d_lat, d_log = destination

        s_lat_min = s_lat - 0.01
        s_lat_max = s_lat + 0.01
        s_log_min = s_log - 0.01
        s_log_max = s_log + 0.01
        d_lat_min = d_lat - 0.01
        d_lat_max = d_lat + 0.01
        d_log_min = d_log - 0.01
        d_log_max = d_log + 0.01

        stmt = select([self.routes]).where(and_(and_(and_(between(self.routes.columns.s_lat, s_lat_min, s_lat_max), between(self.routes.columns.s_long, s_log_min, s_log_max)), between(self.routes.columns.d_lat, d_lat_min, d_lat_max)), between(self.routes.columns.d_long, d_log_min, d_log_max)))    
        result = self.connection.execute(stmt)
        # print(result.fetchall())
        return result.fetchall()
    
    def route_insert_db(self,source,destination,list):
        stmt = insert(self.routes).values(s_lat=source[0], s_long=source[1], d_lat = destination[0], d_long = destination[1], route = list)
        self.connection.execute(stmt)

    
        

if __name__ == "__main__":
    test = DbMethods()
    test.route_search_db((2.3,4.2),(1.2,3.5))
    # test.location_insert_db(2.47,35.32,"happy","arka.json")
    # test.location_search_db(2.421,35.32,"happy")
        