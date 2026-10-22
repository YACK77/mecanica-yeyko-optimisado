import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("DATABASE_URL")
print(f"URL: {url}")

try:
    conn = psycopg2.connect(url)
    cur = conn.cursor()

    cur.execute("SELECT current_database(), current_schema(), current_user;")
    db, schema, user = cur.fetchone()
    print(f"Database: {db}, Current Schema: {schema}, User: {user}")

    cur.execute("""
        SELECT table_schema, table_name 
        FROM information_schema.tables 
        WHERE table_schema NOT IN ('information_schema', 'pg_catalog')
        ORDER BY table_schema, table_name;
    """)
    tables = cur.fetchall()
    print(f"Total tablas encontradas: {len(tables)}")
    for s, t in tables:
        print(f" - Schema: {s} | Tabla: {t}")

    # Check products row count
    try:
        cur.execute("SELECT count(*) FROM products;")
        print(f"Filas en products: {cur.fetchone()[0]}")
    except Exception as e:
        print(f"Error consultando products: {e}")

    cur.close()
    conn.close()
except Exception as e:
    print(f"Error de conexion: {e}")
