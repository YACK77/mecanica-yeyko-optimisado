import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("DATABASE_URL")

conn = psycopg2.connect(url)
cur = conn.cursor()

tables = [
    "products",
    "users",
    "sales",
    "sale_items",
    "purchases",
    "purchase_items",
    "inventory_movements"
]

for table in tables:
    # 1. Deshabilitar RLS para que el Table Editor y cualquier usuario puedan ver y editar datos sin bloqueos
    cur.execute(f"ALTER TABLE {table} DISABLE ROW LEVEL SECURITY;")
    # 2. Conceder permisos explícitos
    cur.execute(f"GRANT ALL ON TABLE {table} TO postgres, anon, authenticated, service_role;")

conn.commit()
print("RLS deshabilitado y permisos otorgados a todas las tablas con exito.")

cur.close()
conn.close()
