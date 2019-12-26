```text
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+


编写一个 SQL 查询，获取 Employee 表中第二高的薪水（Salary） 。
```

```sql
-- 思想就是不是最大数的最大数
select max(Salary) SecondHighestSalary from Employee where salary < (select max(Salary) from Employee);
```
