class Benchmark():
    def __init__(self, db_connection):
        self.__connection = db_connection
        

    def insert(self, lane_id, low, fair, high):
        '''
            INSERT A NEW BENCHMARK
        '''
        
        cursor = self.__connection.cursor()
        
        date = '06-17-2024'
        user = '989f91c0-557b-4da0-901c-e47f9c8ca27c'
        sql = '''
            INSERT INTO benchmark(id, lane_id, high, fair, low, active, created_at, updated_at, created_by, updated_by)
            VALUES(gen_random_uuid(), {lane_id}, {high}, {fair}, {low}, true, '{date}'::DATE, '{date}'::DATE, '{user}', '{user}')
        '''.format(lane_id=lane_id, high=high, fair=fair, low=low, date=date, user=user)
        
        cursor.execute(sql)

        
