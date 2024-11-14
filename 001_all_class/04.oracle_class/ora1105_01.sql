--join
--inner join - equi join / non-equi-join / self join / outer join

-- employees 사원번호 - employees 사원명 부서번호 부서명 departments 을 출력하시오.
select employee_id,emp_name,a.department_id,department_name from employees a, departments b
where a.department_id = b.department_id
;

select * from stu_grade;

-- 두 테이블간 동일한 컬럼없이 데이터를 가져오는 방법 : non-equi join
-- avg값을 가지고 다른 컬럼을 다른 테이블에서 가져와 출력
select name,avg,grade from students,stu_grade
where avg between loavg and hiavg
;

--self join 자신의 테이블을 2번 호출
--
select a.employee_id,a.emp_name,a.manager_id,b.emp_name from employees a, employees b
where a.manager_id = b.employee_id
;

select * from students;
select * from stu;

alter table stu drop column result; -- 컬럼삭제
alter table stu add result varchar2(10); -- 컬럼추가

--avg의 컬럼을 가지고, st_grade 활용해서 이 값을 result 컬럼에 모두 입력하시오.
--no,avg,result 출력
select no,avg,result from stu;

select no,avg,result,grade
from stu,stu_grade
where avg between loavg and hiavg;

-- non-equi join update 구문
update stu set result = (
select grade
from stu_grade
where stu.avg between loavg and hiavg
);

select * from stu;

--non-equi join update 구문
update stu a set result = (
select grades from (
select no,grade as grades
from stu,stu_grade
where avg between loavg and hiavg)b
where a.no = b.no
);
--...?
select grades from (
select no,grade as grades
from stu,stu_grade
where avg between loavg and hiavg);
-- 다른 방법인데 참고만 하자..

-- rank() 등수함수
select * from stu;
update stu set rank = '';
select no,name,avg,rank,rank()over(order by avg desc) as ranks from stu;
-- rank()의 결과값을 rank 컬럼에 모두 입력하시오.


update stu a set rank = (
select ranks from (
select no, rank()over(order by avg desc) as ranks from stu) b
where a.no = b.no
);
select * from stu order by avg desc;

-- null값을 포함한 개수 107개
-- null값을 제외한 개수 106개
-- null값에 0출력 ceo
select nvl(manager_id,0) from employees;
select nvl(to_char(manager_id),'ceo') manager_id from employees;
--self join manager_id, 매니저의 이름을 출력하시오.
select a.employee_id,a.emp_name,a.manager_id,b.emp_name from employees a, employees b
where a.manager_id = b.manager_id;

select a.employee_id, a.emp_name, a.manager_id, b.emp_name,a.salary
from employees a, employees b
where a.manager_id = b.employee_id(+);
-- outer join

--사원번호 사원명 부서번호 부서명 출력 -- euqi-join employees에 없는 부서도 출력하시오.
-- 부서번호 null값도 출력하시오.
select employee_id,emp_name,a.department_id,department_name
from employees a, departments b
where a.department_id(+) = b.department_id;

-- ansi cross join
select * from employees cross join departments;
-- cross join
select * from employees,departments;

-- ansi inner join
select a.department_id,department_name
from employees a inner join departments b
on a.department_id = b.department_id;

-- ansi join : using
select department_id,department_name from employees
inner join departments using(department_id);

-- ansi join : natural join - 두개의 공통부분의 컬럼이 있으면 자동으로 인식해서 검색
select department_id,department_name
from employees natural join departments;

select * from employees a natural join departments b;

--equi join
select a.department_id,department_name
from employees a, departments b
where a.department_id = b.department_id;

-- outer join (left right full)->(+)
select a.department_id,department_name
from employees a full outer join departments b
on a.department_id = b.department_id;

-- 오라클 outer-join : 두개의 컬럼의 (+)는 에러
select employee_id, emp_name,a.department_id,department_name
from employees a, departments b
where a.department_id = b.department_id(+);

-- union : 중복은 제외 49개 24+35 59개
-- union all: 중복 허용
select * from students
where total >= 250
union
select * from students
where name like '%a%';

select * from students
where total>=250 or name like '%a%';

-- union : 같은 테이블 다른 테이블 모두 사용이 가능하고 컬럼의 타입만 맞으면 모두 출력
select employee_id, emp_name from employees
union
select no, name from students;

-- 자유게시판, 공지사항, 이벤트, 종합게시판
-- 통합적으로 검색해서 출력하고 싶을 때 union

-- union :같은테이블 다른테이블 모두 사용이 가능하고 컬럼의 타입만 맞으면 모두출력
-- 조건 : 1. 위쪽 쿼리문과 아래쪽 쿼리문 개수가 동일
-- 조겅 : 2. 타입 무조건 일치
select employee_id no,emp_name, manager_id name from employees
union
select no, name,kor from students;

-- employees department_id가 50인 사원 검색 -> 부서번호 부서이름
-- employees에 salary 5000 and 8000 작은 사원의 부서번호 부서이름
-- 두개를 union하시오.
select department_id, department_name emp_name from departments
where department_id = 50
union
select department_id, emp_name from employees where salary between 5000 and 8000;

-- 중복제거 distinct
select distinct(department_id) from employees;


-- employees에 없는 departments의 부서 검색 -> 부서번호 부서이름
select department_id, department_name emp_name from departments a
where not exists
(
select 1 from employees b where a.department_id = b.department_id
);

desc member; -- name, mdate
desc students; -- name sdate

select name, mdate from member
union
select name, sdate from students;

select * from board;

create table board2 (
	bno number(4),
	btitle VARCHAR2(50),
	bcontent VARCHAR2(50),
	id VARCHAR2(50),
	bgroup number(4),
	bstep number(4),
	bindent number(4),
	bhit number(4),
	bfile VARCHAR2(50)
);


select * from board2;

delete board2 where bno = 21;

select * from board2
where bno between 1 and 20;

-- rownum : 번호를 새롭게 부여
select rownum,bno,btitle from (
select bno, btitle from board2
order by btitle);

drop table board2;

