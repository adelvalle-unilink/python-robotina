class Lane():
    def __init__(self, db_connection):
        self.connection = db_connection
        
        
    def get_all(self, ids):
        cursor = self.connection.cursor()
        
        sql = '''
            SELECT 
                l.id, 
                l.origin_zipcode, 
                l.destination_zipcode,
                e.name AS equipment_name,
                e.id AS equipment_id,
                c1.name AS origin_city_name,
                c2.name AS destination_city_name,
                s1.name AS origin_state_name,
                s2.name AS destination_state_name,
                l.miles
            FROM lane AS l
            JOIN equipment AS e ON e.id = l.equipment_id
            JOIN city AS c1 ON  c1.id = l.origin_city_id
            JOIN city AS c2 ON c2.id = l.destination_city_id
            JOIN state AS s1 ON s1.id = c1.state_id
            JOIN state AS s2 ON s2.id = c2.state_id
        '''
        
        # ADDING WHERE CONDITION TO SQL QUERY.
        if len(ids) == 1: 
                sql += " WHERE l.id = {id}".format(id = ids[0])
        else:
            tup = tuple(ids)
            sql += " WHERE l.id IN {tup}".format(tup=tup)
                
        cursor.execute(sql)
        return cursor.fetchall()
    