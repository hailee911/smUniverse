drop table emp02;
drop table mem2;
select * from mem;

create table emp02(
empno number(4) primary key,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);
INSERT INTO emp02 VALUES (
,'홍길동','clerk',2
);

INSERT INTO emp02 VALUES (
,'유관순',null,null
);

drop table emp02;

create table emp02(
empno number(4) unique,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);

INSERT INTO emp02 VALUES (
1,'홍길동','clerk',2
);
INSERT INTO emp02 VALUES (
2,'유관순',null,null
);
INSERT INTO emp02 VALUES (
null,'이순신',null,null
);
INSERT INTO emp02 VALUES (
null,'강감찬',null,null
);
-- unique 무결성 제약조건 위배
INSERT INTO emp02 VALUES (
2,'김구',null,null
);

select * from emp02;

delete emp02 where empno is null;
alter table emp02 modify empno not null;
alter table emp02 modify empno;

-- not null pk_emp02_empno 별칭
alter table emp02 add constraint pk_emp02_empno primary key(empno);

drop table mem;
create table mem(
id varchar2(30) primary key,
pw varchar2(30)not null,
name varchar2(100)default '무명',
deptno number(2)
);
insert into mem values(
'aaa','1111','홍길동','Male'
);
insert into mem values(
'bbb','1111','유관순','Female'
);

commit;

create table board2(
bno number(4) primary key,
btitle varchar2(1000) not null,
id varchar2(30),
constraint fk_board2_id foreign key(id) references mem(id)
);
select * from mem;
insert into board2 values(
,'제목4','bbb'
);

--외래키 삭제
alter table board2 drop constraint fk_board2_id;

----부모키 삭제시 외래키로 등록된 값들을 모두 삭제
alter table board2
add constraint fk_board2_id foreign key(id)
references mem(id) on delete cascade; -- on delete set null
-- default : on delete retricted : 부모키 삭제시, 외래키에 등록된 값이 있으면, 삭제가 되지 않음.
-- on delete set null : 부모키 삭제시, 외래키로 등록된 값을 삭제는 하지 않고, 해당되는 컬럼값만 null 처리

select * from board2;
select * from mem;
drop table mem;
--부모테이블의 aaa삭제시 자식테이블의 aaa글이 모두 삭제
delete mem where id = 'aaa';

insert into mem values(
'ccc','1111','이순신',30
);

select * from mem;

decode(deptno,
10,'총무부',
20,'인사부',
0,'마케팅'
)
from mem;

select job_id from employees;
--clerk:5%,rep-10% man-15%
--1.clerk rep man 사람을 출력하시오.
--1번째에서 3개를 가져오기
select substr(job_id,4)as job from employees where  substr(job_id,4) in('CLERK','REP','MAN');

select  substr(job_id,4),salary, 
select substr(job_id,4) job , salary,
decode (substr(job_id,4),
'CLERK',salary*1.05,
'REP', salary*1.1,
'MAN',salary*1.15
) sal
from employees
where substr(job,4) in ('CLERK','REP','MAN')
;


create table lavel_data (
	id VARCHAR2(50) primary key,
	lavel number(1) not null
);
insert into lavel_data (id, lavel) values ('Arlen', 4);
insert into lavel_data (id, lavel) values ('Catie', 4);
insert into lavel_data (id, lavel) values ('Adoree', 5);
insert into lavel_data (id, lavel) values ('Cher', 4);
insert into lavel_data (id, lavel) values ('Dorita', 5);
insert into lavel_data (id, lavel) values ('Zulema', 1);
insert into lavel_data (id, lavel) values ('Richy', 4);
insert into lavel_data (id, lavel) values ('James', 5);
insert into lavel_data (id, lavel) values ('Aeriel', 5);
insert into lavel_data (id, lavel) values ('Reinald', 3);
insert into lavel_data (id, lavel) values ('Bernardina', 1);
insert into lavel_data (id, lavel) values ('Tiertza', 2);
insert into lavel_data (id, lavel) values ('Carolyne', 5);
insert into lavel_data (id, lavel) values ('Jonis', 1);
insert into lavel_data (id, lavel) values ('Abigael', 5);
insert into lavel_data (id, lavel) values ('Pauli', 4);
insert into lavel_data (id, lavel) values ('Sheffie', 2);
insert into lavel_data (id, lavel) values ('Tully', 2);
insert into lavel_data (id, lavel) values ('Ricard', 5);
insert into lavel_data (id, lavel) values ('Jameson', 3);
insert into lavel_data (id, lavel) values ('Thorstein', 1);
insert into lavel_data (id, lavel) values ('Arlyne', 5);
insert into lavel_data (id, lavel) values ('Mela', 5);
insert into lavel_data (id, lavel) values ('Yetta', 3);
insert into lavel_data (id, lavel) values ('Corilla', 4);
insert into lavel_data (id, lavel) values ('Adoree', 1);
insert into lavel_data (id, lavel) values ('Sabine', 3);
insert into lavel_data (id, lavel) values ('Nelson', 3);
insert into lavel_data (id, lavel) values ('Isahella', 5);
insert into lavel_data (id, lavel) values ('Mandel', 5);
insert into lavel_data (id, lavel) values ('Sasha', 4);
insert into lavel_data (id, lavel) values ('Deanne', 1);
insert into lavel_data (id, lavel) values ('Thorny', 1);
insert into lavel_data (id, lavel) values ('Jacki', 3);
insert into lavel_data (id, lavel) values ('Sibby', 2);
insert into lavel_data (id, lavel) values ('Jack', 2);
insert into lavel_data (id, lavel) values ('Chandra', 2);
insert into lavel_data (id, lavel) values ('Cecilla', 5);
insert into lavel_data (id, lavel) values ('Saunder', 1);
insert into lavel_data (id, lavel) values ('Way', 4);
insert into lavel_data (id, lavel) values ('Velma', 3);
insert into lavel_data (id, lavel) values ('Keelia', 1);
insert into lavel_data (id, lavel) values ('Clay', 4);
insert into lavel_data (id, lavel) values ('Grace', 2);
insert into lavel_data (id, lavel) values ('Maura', 5);
insert into lavel_data (id, lavel) values ('Karolina', 4);
insert into lavel_data (id, lavel) values ('Mal', 5);
insert into lavel_data (id, lavel) values ('Annette', 4);
insert into lavel_data (id, lavel) values ('Issy', 2);
insert into lavel_data (id, lavel) values ('Reid', 2);
insert into lavel_data (id, lavel) values ('Dall', 4);
insert into lavel_data (id, lavel) values ('Sukey', 2);
insert into lavel_data (id, lavel) values ('Etty', 5);
insert into lavel_data (id, lavel) values ('Kendall', 5);
insert into lavel_data (id, lavel) values ('Gibby', 4);
insert into lavel_data (id, lavel) values ('Kylila', 2);
insert into lavel_data (id, lavel) values ('Orelia', 2);
insert into lavel_data (id, lavel) values ('Alexei', 4);
insert into lavel_data (id, lavel) values ('Iorgo', 1);
insert into lavel_data (id, lavel) values ('Clive', 1);
insert into lavel_data (id, lavel) values ('Roger', 1);
insert into lavel_data (id, lavel) values ('Halette', 3);
insert into lavel_data (id, lavel) values ('Clyve', 3);
insert into lavel_data (id, lavel) values ('Peadar', 1);
insert into lavel_data (id, lavel) values ('Mose', 4);
insert into lavel_data (id, lavel) values ('Raimundo', 3);
insert into lavel_data (id, lavel) values ('Glori', 1);
insert into lavel_data (id, lavel) values ('Merrel', 2);
insert into lavel_data (id, lavel) values ('Ulberto', 2);
insert into lavel_data (id, lavel) values ('Bren', 4);
insert into lavel_data (id, lavel) values ('Ker', 2);
insert into lavel_data (id, lavel) values ('Rosalinda', 1);
insert into lavel_data (id, lavel) values ('Delphinia', 5);
insert into lavel_data (id, lavel) values ('Johnette', 3);
insert into lavel_data (id, lavel) values ('Marilyn', 3);
insert into lavel_data (id, lavel) values ('Paddy', 2);
insert into lavel_data (id, lavel) values ('Antony', 3);
insert into lavel_data (id, lavel) values ('Kinna', 5);
insert into lavel_data (id, lavel) values ('Rogers', 5);
insert into lavel_data (id, lavel) values ('Zolly', 5);
insert into lavel_data (id, lavel) values ('Lance', 1);
insert into lavel_data (id, lavel) values ('Carroll', 2);
insert into lavel_data (id, lavel) values ('Geralda', 2);
insert into lavel_data (id, lavel) values ('Riobard', 2);
insert into lavel_data (id, lavel) values ('Sunshine', 4);
insert into lavel_data (id, lavel) values ('Betteanne', 2);
insert into lavel_data (id, lavel) values ('Andrea', 1);
insert into lavel_data (id, lavel) values ('Theresina', 3);
insert into lavel_data (id, lavel) values ('Koenraad', 4);
insert into lavel_data (id, lavel) values ('Eydie', 1);
insert into lavel_data (id, lavel) values ('Karolina', 2);
insert into lavel_data (id, lavel) values ('Sutton', 5);
insert into lavel_data (id, lavel) values ('Ikey', 5);
insert into lavel_data (id, lavel) values ('Ugo', 1);
insert into lavel_data (id, lavel) values ('Mallory', 4);
insert into lavel_data (id, lavel) values ('Mariska', 2);
insert into lavel_data (id, lavel) values ('Edmund', 3);
insert into lavel_data (id, lavel) values ('Twyla', 5);
insert into lavel_data (id, lavel) values ('Laney', 5);
insert into lavel_data (id, lavel) values ('Onida', 4);

select * from lavel_data;
-- 1 2 3:5000 4 5:20000 포인트--
-- decode는 일치하는 경우만 사용가능
-- case decode와 같은 기능이지만,비교연산자를 사용할수있음
select id,lavel, decode(lavel,1,5000,2,5000,3,5000,4,20000,5,20000)as point from lavel_data;

select id,lavel,
case 
when lavel >= 1 and lavel <= 3 then 5000 
when lavel >=4 and lavel <=5 then 20000
end point
from lavel_data;

select * from students;

-- avg:90이상 A 80이상 B 70이상 C 60 D 그외 F
select avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
when avg < 60 then 'F'
end grade
from students;
-- 테이블 전체복사
create table stu as select * from students;
select * from stu;
alter table stu add result varchar2(2);

--result 컬럼에 추가하시오.
update stu set result = 
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
when avg < 60 then 'F'
end;

select * from stu;

select id,pw,name,deptno,
case when deptno=10 then '총무부' when deptno=20 then '인사부' when deptno=30 then '마케팅' end as deptName
from mem;

-- rank() over 등수 매기기 가능
select no, name, total,
rank()over(order by total desc)
from stu order by no;
-- rank()over() 중복순위 개수만큼 다음순값을 증가시킴 3위 두명이면 다음순위 5등
-- dense_rank()over() 중복순위여도 다음 순위 순차증가 3위 두명이어도 다음 순위 4등
select no, name, total,
dense_rank()over(order by total desc)
from stu;

-- 순위를 rank컬럼에 추가하시오.
select ranks from (select dense_rank()over(order by total desc) ranks
from stu b);

update stu a set rank = (
select ranks from (select no,rank() over(order by total desc) as ranks from stu
)b
where b.no = a.no);

select * from stu;

select no,rank from stu;

--case
--salary 5000 이하 월급 15%인상 5000~8000 10%인상 8000이상 5%인상을 해서 출력하시오.
select salary, case 
when salary <= 5000 then salary*1.15
when salary > 5000 and salary <= 8000 then salary*1.1
when salary >= 8000 then salary*1.05
end 인상금
from employees;

-- emp_name 대문자 D 포함시 10% 인상 M이 포함시 5% 그외 0%
select emp_name, salary, case
when emp_name like '%D%' then salary*1.1
when emp_name like '%M%' then salary*1.05
else salary
end Nsalary
from employees;

-- 커미션이 있는 사원수를 출력하시오.
select count(*) from employees where commission_pct is not null;
-- 부서별 사원수를 출력하시오.
select count(*),department_id from employees group by department_id;

-- 부서별 평균월급을 출력
select department_id,avg(salary) from employees group by department_id;


--그룹함수 조건을 사용하려면, 비교연산 having절을 사용함
--부서별 평균월급이 7000보다 높은 사람의 인원
select count(*),department_id,avg(salary) from employees group by department_id
having avg(salary) >= 7000;

select * from employees;
--부서별 평균월급보다 적게받는 사원수를 출력하시오.
select avg(salary from employees;

select department_id,count(*) from employees
where (select avg(salary) from employees) >= salary
group by department_id
;

--그룹별 평균월급
select avg(salary) from employees group by department_id;
--부서별 평균 월급보다 적게받는 사원수


-- 부서별 평균 월급이 6000이하인 부서별 인원수를 출력
-- 그룹함수는 having절에 조건문을 사용해야함 where 절에서는 사용불가
select department_id, avg(salary),count(salary) from employees
group by department_id
having avg(salary)<6000;

--부서별 평균월급보다 적게받는 사원수 출력 ???
select department_id,count(*) from employees a
where salary <
(
select salarys from(
select department_id,avg(salary) salarys from employees 
group by department_id
) b
where a.department_id = b.department_id
)
group by a.department_id
order by department_id
;

-- 30번 부서 총 사원 수 6명, 평균월급 - 4150 보다 낮은 사원 수 5명
select department_id,emp_name,salary from employees
where department_id = 30;
select department_id,avg(salary) from employees where department_id = 30 group by department_id;

-- 부서의 최대값과 최소값 출력하되 최대급여가 5000 이상인 부서만 출력하시오.
select department_id, max(salary),min(salary) from employees group by department_id having max(salary)>=5000
order by department_id desc;

-- 학번 이름 전화번호 주소 성별 학년 학기 국어 영어 수학 합계 평균 등수
-- 1001 홍길동 010 서울 남자 1학년 1학기 100 100 100 300 100 1
-- 1001 홍길동 010 서울 남자 1학년 2학기 90 90 90 270 90 8
-- 1001 홍길동 010 서울 남자 1학년 3학기 95 95 95 285 15
-- 1001 홍길동 010 서울 남자 1학년 4학기 100 100 99 299 2
-- 1001 홍길동 010 서울 남자 2학년 1학기 100 100 100 300 100 1
-- 1001 홍길동 010 서울 남자 2학년 2학기 90 90 90 270 90 8
-- 1001 홍길동 010 서울 남자 2학년 3학기 95 95 95 285 15
-- 1001 홍길동 010 서울 남자 2학년 4학기 100 100 99 299 2 ...

-- 부서명 departments
select * from departments;
select * from employees;
-- donald OConnell 의 부서명
select emp_name, department_id from employees where emp_name = 'Donald OConnell';

select department_id,department_name from departments
where department_id = 50;

-- join을 사용해야 두개의 쿼리를 1개의 쿼리로 구성이 가능해짐
select emp_name, department_id, department_name from emp_name ,departments
where emp_name = 'Donald OConnell' and department_id = 50;

-- join
-- 1. cross join ( equi join non-equi join)
-- 2. inner join
-- 3. outer join
-- 4. self join

-- cross join : 특별한 키워드 없이 두개의 테이블을 검색하는 것
select * from employees; -- 107
select * from departments; -- 27
select count(*) from employees, departments; -- 27 * 107 = 2889
select * from employees,departments;

--inner join: equi join : 같은 컬럼을 가지고 비교해서 두개의 테이블을 검색 

select emp_name,e.department_id,department_name from employees e,departments d
where e.department_id = d.department_id -- (+) outer join
; -- 106 (null 제외) 
-- 두 테이블 속 동일한 컬럼은 꼭 명시

select email,phone from member;
select bno,btitle,bcontent,id from board;

select bno,btitle,bcontent,a.id,email,phone, bgroup,bstep,bindent,bhit,bdate,bfile from member a,board b
where a.id=b.id;

select * from jobs;

-- inner join (equi) ; 사원번호, 사원명, job_id job_title 출력
select * from employees;

select employee_id, emp_name, a.department_id,department_name, a.job_id, job_title from employees a, jobs b, departments c
where a.job_id = b.job_id and a.department_id = c.department_id;

-- member 닉네임
-- board 게시글

select * from member;
select * from board;

select bno, btitle, name, bgroup, bstep , bindent, bhit, bdate, bfile from board a, member b
where a.id = b.id;

-- 사원번호, 사원명, 월급, 부서번호, 부서명
-- 월급 평균 월급보다 적은 사원을 출력하시오.
select employee_id, emp_name, salary, a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id and salary <= (select avg(salary)from employees);

-- 부서별 평균 월급보다 작은 사원을 출력하시오.????????
select employee_id, emp_name, salary, a.department_id,(select avg(salary) from employees group by a.department_id), 
department_name
from employees a, departments b
where a.department_id = b.department_id 
and salary < (
select salarys from (select department_id,avg(salary) salarys from employees
group by department_id)c 
where a.department_id = c.department_id
);


select department_id, avg(salary) from employees group by department_id;

-- job_id clerk 인 사원의
-- 사원명 사원번호 부서명 부서번호 직급번호 직급명 출력
select employee_id, emp_name, department_name, a.department_id, a.job_id, job_title
from employees a, departments b, jobs c
where a.department_id = b.department_id and a.job_id = c.job_id 
and substr(c.job_id,4) in ('CLERK','MAN');

select salary from employees order by salary;
-- 2000~4000 E, 4000~6000 D 6000~8000 C 8000~10000 B 10000~100000 A등급

create table salgrade(
grade varchar2(10),
losal number(6),
hisal number(6)
);

insert into salgrade values(
'E등급',2000,4000
);
insert into salgrade values(
'D등급',4001,6000
);
insert into salgrade values(
'C등급',6001,8000
);
insert into salgrade values(
'B등급',8001,10000
);
insert into salgrade values(
'A등급',10001,100000
);
select * from salgrade;

-- salary 등급을 넣으려고 함
-- 등급은 salgrade에 있음
-- salgrade employees 같은 컬럼이 없음
-- non-equi join을 사용해서 테이블을 join 하려고 함
select salary from employees;
select * from salgrade;

--non-equi join : 두 테이블간 같은 컬럼이 없으면서 두 테이블의 값을 비교해서 출력
select emp_name, salary, grade from employees,salgrade
where salary between losal and hisal
; -- 그냥 합치게 되면 ; 107*5 = 535개

-- non-equi join 활용해서 students total ABCDF 등급을 출력하시오
-- 100-90 89-80 79-70 69-60 60미만
create table stu_grade(
grade varchar2(10),
lototal number(6),
hitotal number(6,2)
);

select * from stu_grade;
select * from students;

select name, avg, grade from stu_grade, students
where avg between loavg and hiavg;

select total from students;

select * from stu;

update stu set result = ''; -- 다 널값으로 변경

alter table stu modify result varchar2(10); -- A등급 (최소 7바이트)

--result의 결과값을 non-equi join을 사용해서 입력하시오.
update stu a set result = (
select results from (
select no, grade as results from stu,stu_grade
where avg between loavg and hiavg) b
where a.no = b.no
);
-- 와 진짜 하나도 모르곘다;

-- self join
select employee_id,emp_name,manager_id from employees;
--케빈 모구모구
select employee_id,emp_name from employees where employee_id = 124;


-- self join : 자신의 테이블 2개를 join 결과값을 출력
select a.employee_id, a.emp_name,a.manager_id,b.emp_name 
from employees a, employees b
where a.manager_id = b.employee_id and a.manager_id = 124;




