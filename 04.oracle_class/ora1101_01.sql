-- 입사일의 마지막 날짜 출력
select hire_date, last_day(hire_date) from employees;
-- 1년 후 날짜 출력
select sdate, add_months(sdate,12) from students;
select sdate, add_months(sdate,-6) from students;
-- 현재일 기준으로 가입일이 6개월이내의 회원만 출력
select sdate from students where sdate >= add_months(sysdate,-6) order by sdate;
-- 월별로 가입인원을 출력하시오.
select substr(mdate,4,2) from member group by substr(mdate,4,2);
select substr(mdate,0,5),count(*) from member group by substr(mdate,0,5);
-- employees - department_id 인원 출력 
select department_id, count(*) from employees group by department_id;



