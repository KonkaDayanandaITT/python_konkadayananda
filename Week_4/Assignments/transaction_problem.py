from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

try:
    password = quote_plus("Playdate@1208")
    engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/demo")

    with engine.connect() as conn:
        query = text("""
            select t1.transaction_date,t1.product_name,t1.revenue,
                (
                    select t2.revenue
                    from Transaction t2
                    where t2.transaction_date < t1.transaction_date
                    order by t2.transaction_date desc
                    limit 1
                ) as previous_revenue,
                (
                    select t3.revenue
                    from Transaction t3
                    where t3.transaction_date > t1.transaction_date
                    order by t3.transaction_date asc
                    limit 1
                ) as next_revenue

            from Transaction t1
            order by t1.transaction_date
        """)

        result = conn.execute(query)

        for row in result:
            print(row.transaction_date, row.product_name, row.revenue, row.previous_revenue, row.next_revenue)

except Exception as e:
    print("Error executing query:", e)
