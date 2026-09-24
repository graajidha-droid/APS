# Write your MySQL query statement below
SELECT e.name,b.bonus from Employee e
left Join Bonus b on
b.empId=e.empId
where bonus<1000 or b.bonus IS NULL;