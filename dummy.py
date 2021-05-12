import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

with psycopg2.connect(dbname=os.getenv("DBNAME"),
                      user=os.getenv("USER"),
                      password=os.getenv("PASSWORD"),
                      host=os.getenv("HOST"),
                      port=os.getenv("PORT")) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM public."User"')
        print(cur.fetchone())
