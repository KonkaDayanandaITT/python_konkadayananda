from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

try:
    password = quote_plus("Playdate@1208")
    engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/demo")

    with engine.connect() as conn:
        query = text("""
        select t.customer_id, t.purch_amt as max_purchase_amount,
               date_add(t.ord_date, interval 7 day) as shipment_date,
               now() as ins_date,
               datediff(now(), date_add(t.ord_date, interval 7 day)) as data_Latency
        from tableA t
        join(
            select customer_id, max(purch_amt) as max_amt
            from tableA
            where customer_id between 3002 and 3007
            group BY customer_id
            having max(purch_amt) > 1000
        )m
        on t.customer_id = m.customer_id
        and t.purch_amt = m.max_amt
        """)

        result = conn.execute(query)

        for row in result:
            print(row[0], row[1], row[2], row[3], row[4])



except Exception as e:
    print("Error executing query:", e)
