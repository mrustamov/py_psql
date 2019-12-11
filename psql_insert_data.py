#!/usr/bin/python

import psycopg2
from config import config


def insert_common(common_name):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO common(common_name)
             VALUES(%s) RETURNING common_id;"""
    conn = None
    vendor_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (common_name,))
        # get the generated id back
        common_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return common_id

if __name__ == '__main__':
    # insert one vendor
    insert_common("IO DEV.")