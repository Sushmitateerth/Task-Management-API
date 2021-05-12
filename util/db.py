import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

config = {
    'user': os.getenv("USER"),
    'host': os.getenv("HOST"),
    'port': os.getenv("PORT"),
    'dbname': os.getenv("DBNAME"),
    'password': os.getenv("PASSWORD"),
}


def clear_db(clear_user=True):
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM public."Board"')
            if clear_user:
                cur.execute('DELETE FROM public."User"')
