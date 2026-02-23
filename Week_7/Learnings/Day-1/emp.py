emp_data = [{"Name": "Ravi", "Salary": "30000","Location": "Mumbai"},
     {"Name": "Santhosh", "Salary": "20000","Location": "Bangalore"},
     {"Name": "Anu", "Salary": "40000","Location": "Mumbai"},
     {"Name": "Raju", "Salary": "35000","Location": "Bangalore"},
     {"Name": "Sita", "Salary": "25000","Location": "Delhi"}]
 
# 1) No of employees in each location
# 2) Min, Max, Avg Salary of each location

location_count = {}

for emp in emp_data:
    loc = emp["Location"]
    
    if loc not in location_count:
        location_count[loc]= 1
        
    else:
        location_count[loc] += 1
        
print(location_count)


        

