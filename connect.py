import snowflake.connector

conn = snowflake.connector.connect(
    user = 'Kushal7999',
    password = 'Novdec_2022#',
    account = 'uk00763.ap-southeast-1',
    database = 'EMPLOYEE'    
)

cur = conn.cursor()
try:
    cur.execute("Select * from EMPLOYEE.PUBLIC.EMPLOYEEDETAILS")
    one_row = cur.fetchone()
    all_row = cur.fetchall()
    print(one_row)
    print(all_row)
finally:
    cur.close()
conn.close()        