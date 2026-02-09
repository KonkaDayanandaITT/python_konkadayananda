from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

try:
    password = quote_plus("Playdate@1208")
    engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/demo")

    with engine.connect() as conn:

        try:
            check_customer = conn.execute(
                text("select count(*) from Customers where customer_id = 1")
            ).scalar()

            if check_customer == 0:
                raise Exception("Invalid Customerid, Please provide a valid Customerid.")

            insert_query = text("""
                insert into orders_1 (OrderID, CustomerID, OrderDate, TotalAmount)
                VALUES (4, 1, '2023-03-01', 200)
            """)
            conn.execute(insert_query)
            conn.commit()
            print("Order inserted successfully")

        except Exception as e:
            print("Error inserting order:", e)

        print("\nCustomers with Full Name:")
        full_name_query = text("""
            select customer_id,
                   concat(first_name,' ',last_name) as Full_Name,
                   age
            FROM Customers
        """)

        result = conn.execute(full_name_query)
        for row in result:
            print(row.customer_id, row.Full_Name, row.age)

        print("\nCustomers with last name Doe:")
        doe_query = text("""
            select *
            from Customers
            where last_name = 'Doe'
        """)

        result = conn.execute(doe_query)
        for row in result:
            print(row.customer_id, row.first_name, row.last_name, row.age)

except Exception as e:
    print("Database connection error:", e)
