from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

try:
    password = quote_plus("Playdate@1208")
    engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/demo")

    with engine.connect() as conn:

        query = text("""
            with product_sales as (
                select p.ProductID,p.ProductName,p.Category,sum(s.Quantity * p.Price) as total_sales_amount,sum(s.Quantity) as total_units_sold
                from Sales s
                join Product p on s.ProductID = p.ProductID
                group by p.ProductID, p.ProductName, p.Category
            ),
            recent_customer as (
                select s.ProductID, c.CustomerName, c.Email, row_number() over(partition by s.ProductID order by s.SaleDate desc) as rn
                from Sales s
                join customers_1 c   -- changed here
                    on s.CustomerID = c.CustomerID
            )

            select ps.ProductName,ps.Category,ps.total_sales_amount,ps.total_units_sold,rc.CustomerName,rc.Email
            from product_sales ps
            join recent_customer rc
                ON ps.ProductID = rc.ProductID
            where rc.rn = 1
            order by ps.total_sales_amount desc, ps.total_units_sold desc
            limit 3
        """)

        result = conn.execute(query)

        for row in result:
            print(row.ProductName, row.Category,row.total_sales_amount,row.total_units_sold,row.CustomerName,row.Email)

except Exception as e:
    print("Error:", e)
