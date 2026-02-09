from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

try:
    password = quote_plus("Playdate@1208")
    engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/demo")

    with engine.connect() as conn:
        query = text("""
        select h.hacker_id, h.name, sum(ms.max_score) as total_score
        from hackers h
        join(
            select hacker_id, challenge_id, max(score) as max_score
            from submissions
            group by hacker_id, challenge_id
        )ms
        on h.hacker_id = ms.hacker_id
        group by h.hacker_id, h.name
        having total_score > 0
        order by total_score desc, h.hacker_id asc
        """)

        result = conn.execute(query)

        for row in result:
            print(row.hacker_id, row.name, row.total_score)
       

except Exception as e:
    print("Error executing query:", e)