import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()


conn = psycopg2.connect(host="db.edxuyjtckpuddspvemkr.supabase.co", database="postgres", user="postgres", password=os.environ.get("SUPABASE_PASSWORD"))
cur = conn.cursor()
conn.commit()
cur.close()
conn.close()