from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

try:
    password = quote_plus("Playdate@1208")
    engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/demo")

    with engine.connect() as conn:
        query = text("""
            select o.customer_id, count(*) as total_orders,
            group_concat(o.order_date) as order_dates
            from orders o
            group by o.customer_id
            order by total_orders desc, o.customer_id asc
            limit 1;
        """)

        result = conn.execute(query)

        for row in result:
            print("Customer:", row.customer_id)
            print("Total Orders:", row.total_orders)
            print("Order Dates:", row.order_dates)

except Exception as e:
    print("Error executing query:", e)
