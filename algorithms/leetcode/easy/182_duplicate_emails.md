```text
Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.

编写一个 SQL 查询，查找 Person 表中所有重复的电子邮箱。
```

```sql
-- 方法一
select Email from Person group by Email having count(Email) > 1;

-- 方法二
select distinct a.Email from Person a, Person b where a.Email = b.Email and a.Id != b.Id;
```
