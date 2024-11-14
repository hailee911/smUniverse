--view
--상담원 : 사원들 전화를 가지고 사원들에게 마케팅을 하려고 함
--100명에게 사원 테이블 오픈 제공해달라고 요청 : 마케팅
--직원가 100만원 90% 10만원 아이폰 16

create or replace view employees_view
as
select employee_id,emp_name,email,phone_number,hire_date
from employees;

--employees_view
select * from employees_view;



--사원버노 사원명 이메일 폰버노 입사일 부서버노 부서명 출력
create or replace view emp_view
as
select employee_id,emp_name,email,phone_number,a.department_id,department_name
from employees a, departments b where a.department_id = b.department_id;

select * from emp_view;

drop view emp_view;

--view 컬럼 추가
comment on column employees_view.employee_id is '사원번호에 해당됩니다.';
--컬럼 커멘트 주석확인
select * from user_col_comments;
--테이블 커멘트 주석확인
select * from user_tab_comments;
--
select * from employees;
select * from employees_view;

drop table emp02;
--
create table emp02(
employee_id number(6),
emp_name varchar2(80),
hire_date date,
salary number(8,2),
department_id number(6)
);

desc emp02;
insert into emp02(employee_id,emp_name,hire_date,salary,department_id)
select employee_id,emp_name,hire_date,salary,department_id from employees;

select * from emp02;
--view 생성
--with read only : 읽기전용 (select만 가능)
create or replace view emp02_view as select employee_id,emp_name,hire_date from emp02
with read only
;

drop view emp02_view;

-view select
select * from emp02_view order by employee_id;
--단순 view : 1개 테이블로 구성된 것
--insert,update,delete 가능 not null 제약조건이 되어있으면 insert 불가할수도 있음.
--복합 view : 2개 이상 테이블 조인, 함수사용, group by 같은 경우는 insert,update,delete 불가능

--100번 이름 홍길동
update emp02_view set emp_name = '유관순' where employee_id = 101;

insert into emp02_view values(
207,'유관순',sysdate
);
select * from emp02 order by employee_id;
delete emp02 where employee_id = 207;

alter table emp02 modify salary not null;

select * from students;
--no :seq
-- 입력데이터 : name,kor,eng,math
--total, avg, rank : 오라클에서 입력
--sdate : sysdate 오라클에서 입력

insert into students values(students_seq.nextval,name,kor,eng,math,
kor+eng+math,(kor+eng+math)/3,sysdate);

-- avg 소수점 2자리까지만 출력하시오
select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy/mm/dd') from students;

select total, rank() over(order by total desc) from students;

update students a set rank = 
(select ranks from
(select no,rank()over(order by avg desc)ranks from students)b
where a.no = b.no);

select * from students order by rank;


