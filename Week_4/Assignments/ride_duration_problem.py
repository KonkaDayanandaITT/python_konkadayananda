from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

try:
    password = quote_plus("Playdate@1208")
    engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/demo")

    with engine.connect() as conn:
        query = text("""
            select ride_id,start_terminal,end_terminal,ride_duration,
               row_number() over(
                   partition by end_terminal
                   order by ride_duration desc
               ) as row_num,

               sum(ride_duration) over(
                   partition by end_terminal
                   order by ride_duration desc
               ) as running_total_duration

            from Ride_table
            order by end_terminal, ride_duration desc
        """)

        result = conn.execute(query)

        for row in result:
            print(row[0], row[1], row[2], row[3], row[4], row[5])

except Exception as e:
    print("Error executing query:", e)
