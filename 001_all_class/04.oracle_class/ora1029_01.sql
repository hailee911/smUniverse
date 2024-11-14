--drop table member;

--drop table date_tab;

--drop table no_tab;

--drop table students;

-- create 테이블 생성, alter 테이블 수정, drop 테이블 삭제
create table member(
 no number(4),
 id varchar2(20),
 pw varchar2(20),
 name varchar2(20),
 phone varchar2(20),
 mdate date
);

-- insert 데이터 입력, select 데이터 검색, update 데이터 수정, delete 데이터 삭제
insert into member values(
 1,'aaa','1111','홍길동','010-1111-1111','2024-10-29'
);

select * from member;

-- f11 commit f12 rollback

insert into member values(
 2,'bbb','1111','유관순','010-2222-2222','2024-09-20'
);

-- delete 삭제
-- delete member where no = 2;
-- delete member

-- update 수정
update member set name = '홍길자' where no = 1;
update member set name = '김구';

select * from member;


-- create 테이블 생성
create table students(
 stuno number(4),
 name varchar2(20),
 kor number(3),
 eng number(3),
 total number(3),
 sdate date
);

insert into students values(
 1,'홍길동',100,100,100+100,sysdate
);

-- 특정 컬럼을 입력하면 그 컬럼만 검색
select name, sdate from students;

-- 특정컬럼만 입력하면 해당컬럼 입력
insert into students (stuno, name) values(2, '유관순');

select * from students;


------------
-- 테이블을 생성하면서 테이블 내용을 모두 복사
create table emp2 as select * from employees;
select * from emp2;
select count(*) from emp2;
-- count 데이터 개수
select count (*) from employees;
select * from employees;

-- 테이블 타입
desc employees; 

-- 테이블 구조만 복사
create table emp3 as select * from employees where 1=2;
select * from emp3;

-- 테이블이 존재 할 경우 데이터만 복사
create table member2 as select * from member where 1=2;
insert into member2 select * from member;


-- 테이블 컬럼 
-- 컬럼데이터 타입, 길이 변경

-- alter 변경 member 테이블 no 컬럼의 타입길이를 변경
desc member;
alter table member modify no number(10);

-- 타입 변경시 내용이 null이어야함
update member set no = null;
alter table member modify no varchar2(10);

-- alter 변경, 컬럼의 이름을 변경
alter table member rename column no to memberNo;

select memberno from member;

select * from member;

-- employees 테이블에서 사원번호, 사원이름, 입사일hire_date 출력
select employee_id, emp_name, hire_date from employees;

-- 연산자 : 산술연산자 + - * /
--drop table member;
--drop table member2;
--drop table emp2;

create table member (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);

select * from member;

--drop table students;

create table students (
	no number(4),
	name VARCHAR2(50),
	kor number(3),
	eng number(3),
	math number(3),
	total number(3),
	avg number,
	rank number(3),
	sdate DATE
);

select kor,eng,(kor+eng) from students;
select kor,eng,(kor+eng),abs(kor-eng) from students;

select * from students;

--select emp_name + email from employees;

-- concat 명령어, || 
select concat(employee_id,emp_name) from employees;
select employee_id||emp_name from employees;

-- 달러 환산 1384 
select salary from employees;
select salary*1384 from employees;
-- 문자로 변환, 천단위 표시
select to_char(salary*1384,'999,999,999') from employees;

select emp_name,salary,salary*1384 from employees;

create table stu(
no number(4),
name varchar2(20),
kor number(3)
);

insert into stu values(1,'홍길동',100);
insert into stu values(2,'유관순',99);

insert into stu values(3,'',0);
insert into stu values(4,null,null);

select * from stu;

-- null값 검색 is null 
select * from stu where name is null;

select * from employees;

-- nul이 아닌것 출력 : is not null
select commission_pct from employees where commission_pct is not null;

select salary from employees;
--연봉으로 계산 * 12
select salary, salary*12 from employees;
select salary, salary*12, salary*12*1384 from employees;

-- 커미션이 없는 사원은 null값이 있는데, null + - * / null값으로 변경
select salary, salary*12, salary*12+(salary*12)*(commission_pct*0.01) from employees;
-- 컬럼 별칭 사용 as , "있는 그대로 지정 가능" "특수문자, 사이공간까지 컬럼명으로 사용가능"
select salary, salary*12 as "연 봉", salary*12+(salary*12)*(nvl(commission_pct,0)*0.01) as "real salary" from employees;

-- nvl() 함수, nvl(kor,0) ; kor컬럼에 null값이 있으면 0으로 표시
select * from stu;
select no,name,kor,kor+100 from stu;
select no,name,kor,nvl(kor,0)+100 from stu;

--별칭 kor 국어 영어 수학 합계 평균 등수 입력일
select * from students;

select 
no as 번호,name as 이름,kor as 국어,eng as 영어, math as 수학, total as 합계, avg as 평균, rank as 등수, sdate as 입력일
from students; 

select * from employees;

select employee_id||emp_name||email from employees;
select concat(employee_id, emp_name) from employees;
select emp_name||' is a '||job_id from employees;

-- 중복제거 : distinct
select department_id from employees;
select distinct department_id from employees;
-- 정렬 order by 컬럼명 + asc(순차정렬 생략가능) + desc (역순정렬)
select distinct department_id from employees order by department_id desc;

-- job_id 중복제거 출력하시오.
select distinct job_id from employees;
select job_id from employees;

-- 문자열 자르기 substr(0,2) 0,1,2앞에까지 출력
select substr(job_id,4) from employees;

-- 4번째 컬럼데이터를 가져와서 중복을 제거함
select distinct substr(job_id,4) from employees;

-- where 절 : 조건비교연산자 > < >= <= = !=
select * from employees where manager_id = 124;
select * from employees where job_id = 'SH_CLERK';

select * from employees where employee_id > 100;

-- students 합계 250 이상
select * from students where total > 250 and kor>= 90;

select * from students where eng >= 70 and eng <= 90;

-- 월급이 5000 이상 8000이하
select * from employees where salary >= 5000 and salary <= 8000;

-- 월급이 5000이 아닌거
select * from employees where salary != 5000;

select count(*) from employees where department_id = 50;
select count(*) from employees where department_id != 50;

-- null값은 count() 포함되지 않음.
select count(*) from employees where department_id is null;

select count(employee_id) from employees; --107개
select count(department_id) from employees; --106개 , null값 포함 X

select * from employees;
select employee_id 사원번호,emp_name 사원명,salary 급여 from employees where salary <= 4000;

-- 숫자 비교연산자 가능, 날짜 비교연산자 가능
select emp_name, hire_date from employees;

select emp_name, hire_date from employees where hire_date <= '1999/12/31';

select emp_name, hire_date from employees where hire_date >= '2001-01-01' and hire_date <= '20041231';


-- 논리 연산자
-- 국어>90 또는 영어>90
select count(*) from students where kor>=90 or eng>=90;
select count(*) from students where kor>=90 and eng>=90;

select count(*) from students where not kor>=90;

-- 부서번호 department_id = 10
select * from employees where department_id = 80 and substr(job_id,4) = 'MAN';

select commission_pct from employees where commission_pct is not null;

select commission_pct from employees where commission_pct = 0.2 or commission_pct = 0.3 or commission_pct = 0.5;
-- 같은 방법
select commission_pct from employees where commission_pct in (0.2,0.3);

-- 사원번호 employee_id 107 110 120
select * from employees where employee_id in (107,110,120);
select * from employees where employee_id = 107 or employee_id = 110 or employee_id = 130;

between - and ; 포함이 되어있는경우만 해당
select * from employees where employee_id >= 150 and employee_id <= 170;
select * from employees where employee_id between 150 and 170;
--날짜 in
select hire_date from employees where hire_date in ('20040217','20020607');
--날짜 between
select hire_date from employees where hire_date between '20020617' and '20041231';

--job man 검색
select * from employees where substr(job_id,4) = 'MAN';
-- like 연산자 ; 포함되어있는 글자 검색 %끝나는단어 / 시작하는단어%
select * from employees where job_id like '%MAN';
select * from employees where job_id like 'ST%';

select * from employees where emp_name like '%a%';
-- _자리수
select * from employees where emp_name like '_t%';
select * from employees where emp_name like '___v%';

--뒤에서 2번째 자리에 l
select * from employees where emp_name like '%l__';

-- 첫번째 D

select * from employees where emp_name like '%a%';



