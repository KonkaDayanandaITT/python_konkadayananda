from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

try:
    password = quote_plus("Playdate@1208")
    engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/demo")

    with engine.connect() as conn:
        query = text("""
        select distinct so.salesman_id,c.customer_id
        from sample_orders so
        join sample_customer c
            on so.customer_id = c.customer_id
        """)

        result = conn.execute(query)

        for row in result:
            print(row[0], row[1])

except Exception as e:
    print("Error executing query:", e)
