from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

try:
    password = quote_plus("Playdate@1208")
    engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/demo")

    with engine.connect() as conn:
        query = text("""
            select e.employee_name, d.department_name, s.salary_amount
            from employees e
            join salaries s 
                on e.employee_id = s.employee_id
            join departments d
                on e.department_id = d.department_id
            join(
                select e.department_id, max(s.salary_amount) as max_salary
                from employees e
                join salaries s
                    on e.employee_id = s.employee_id
                group by e.department_id
            )m
            on e.department_id = m.department_id
            and s.salary_amount = m.max_salary
            
        """)

        result = conn.execute(query)

        for row in result:
            print(row.employee_name, row.department_name, row.salary_amount)
       

except Exception as e:
    print("Error executing query:", e)