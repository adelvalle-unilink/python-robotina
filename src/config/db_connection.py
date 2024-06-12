# RETURN CONNECTION TO POSTGRESQL DB
import psycopg2

def connect(config):
    try:
        with psycopg2.connect(**config) as conn:
            return conn
    except (psycopg2.DatabaseError, Exception) as err:
        print("DATABASE ERROR:", err)
