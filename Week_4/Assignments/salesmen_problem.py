from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

try:
    password = quote_plus("Playdate@1208")
    engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/demo")

    with engine.connect() as conn:
        query = text("""
            select salesman_id, name, city, commission
            from salesman
            where name REGEXP '^[B-K]'
            
        """)

        result = conn.execute(query)

        for row in result:
            print(row.salesman_id, row.name, row.city, row.commission)
       

except Exception as e:
    print("Error executing query:", e)