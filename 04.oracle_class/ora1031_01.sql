select * from member;
update member set pw='1111' where id = 'Towell';

select hire_date,round(hire_date) from employees;

select hire_date, trunc(hire_date,'month') from employees;

select add_months(trunc(sysdate,'month'),1) from dual;

-- vip 요금제로 변경을 하면 다음달부터 1일부터 혜택

select sysdate,add_months(trunc(sysdate,'month'),1) from dual;

-- 입사일 기준 다음달부터 1일부터 혜택을 주겠다고 함.
-- 입사일 다음달 1일 출력하시오.
select * from employees;

select emp_name, add_months(trunc(hire_date,'month'),1) from employees;

-- 입사일 기준 1년 후 날짜를 출력
select sysdate,add_months(sysdate,12) from dual;
select sysdate, sysdate+365 from dual;

-- 그 달 마지막 날짜
select hire_date,last_day(hire_date) from employees;

--입사일 기준 1년 후 날짜와, 1년 후 마지막 그달의 날짜를 출력
select hire_date ,add_months(hire_date,12), last_day(add_months(hire_date,12)) from employees;


-- extract 함수: 특정 년 월 일 시 분 초 만 분리해서 가져오는 함수

select extract(month/day from sdate) from students;
-- 입력일 기준 1년 후 마지막 날짜가 8/31 9/30, 10/31인 학생들을 모두 출력하시오.
select sdate, last_day(sdate+365) from students where last_day(sdate+365) in ('25/08/31','25/09/30','25/10/31');

select sysdate from dual;

select extract(year from sysdate) from dual;
select extract(month from sysdate) from dual;
select extract(day from sysdate) from dual;

-- systimestamp 년월일시분초
select systimestamp from dual;
select extract(hour from systimestamp) from dual;
select extract(minute from systimestamp) from dual;
select extract(second from systimestamp) from dual;

select sdate, extract(month from last_day(sdate+365)) from students where extract(month from sdate) in (8,11,12);

-- substr함수 : 문자에서 (시작위치, 가져올 개수)
select sysdate,substr(sysdate,4) from dual;
select sdate, last_day(sdate+365) sdate2 from students
where substr(last_day(sdate+365),4,2)in (8,10,12) order by sdate2;


-- 날짜 -> 문자 to_char
-- 문자 -> 날짜 to_date
-- 문자 -> 숫자 to_number
-- 날짜 형변환해서 날짜 포맷을 변경
-- date 타입 -> char 타입으로 변경해서 포맷
select sysdate from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd') from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd hh24:mi:ss') from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd am hh24:mi:day') from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd hh24:mi:dy') from dual;
select sysdate,to_char(sysdate,'yy-mon-dd hh24:mi:ss') from dual;

select hire_date, to_char(hire_date,'yyyy-mm-dd am hh:mi:ss')from employees;

-- students테이블 sdate 2024/01/01 형태로 출력하시오.
select sdate, to_char(sdate,'yyyy/mm/dd') from students;

select kor from students where kor = 70;

-- 숫자타입 -> 문자타입 변경해서 포맷 천단위 표시
select salary*1382.86*12 from employees;
-- 자리수 채우기 9 : 빈공백으로 채움 0: 0으로 채움
-- L : 국가통화기호표시, $:$표시가 됨
select to_char(salary*1382.86*12,'L 999,999,999') from employees;


select to_char(12,'0000') from dual;
select 12 from dual;

select to_char(123456,'000000000'),to_char(123456,'999,999,999') from dual;

create table chart2(
no number(4),
kor number(10),
kor_char number(10),
kor_mark number(10)
);

-- 숫자형 타입은 숫자앞에 0이 있어도 표시가 되지 않음. : 문자형 타입만 가능
-- 천단위 표시는 숫자형타입에 입력이 안됨 : 문자형 타입에만 가능
-- 문자형 타입에는 숫자형타입 가능
insert into chart2 values(
5,5000000,05000000,05000000
);

select * from chart;

-- 숫자형 타입, 문자형(숫자)타입은 사칙연산 가능
-- 숫자형타입과 문자 천단위 표시 숫자타입은 사칙연산 불가능, 천단위표시는 문자형 타입
-- 숫자형타입 + 문자(숫자형) 타입 = 두타입 결과값 출력
select kor, kor+kor_char from chart;
select kor, kor+kor_mark from chart;

desc chart; -- number,varchar2

desc chart2; -- 모든타입 number

insert into chart values(
1,10000,to_char(10000,'00000000'),to_char(10000,'0,000,000')
);

insert into chart values(
1,10000,10000,10000
);

select * from chart;
select * from chart2;

select to_date('20241031') from dual;

-- number형 타입 -> 날짜형 타입
select sysdate - to_date(20231101) from dual;
-- 문자형 타입 -> 날짜형 타입
select sysdate - to_date('20231101') from dual;

--문자형 타입 -> 숫자형 타입
-- 천단위 문자형 타입 -> 천단위 제외 숫자형 타입
select to_number('20,000','999,999') from dual;

select * from chart;

select kor,to_number(kor_mark,'999,999,999') from chart;

insert into chart values(3,30000,'0030000','3,000,000');

-- 날짜 -> 문자 to_char     ## 날짜포맷
-- 문자 -> 날짜 to_date     ## 날짜 사칙연산
-- 숫자 -> 문자 to_char     ## 천단위, 숫자앞에 0 을표시, 통화표시
-- 문자 -> 숫자 to_number ## 천단위 표시 , 천단위 삭제해서 사칙연산

select department_id from employees;
select department_id from employees where department_id is null;

select commission_pct from employees where commission_pct is not null;

-- 월급 * 커미션을 계산하시오.
select salary+salary*nvl(commission_pct,0) from employees;

-- null 경우 0 표시
-- null 경우 CEO 표시
select department_id is null ;

select nvl(to_char(department_id), 'CEO') from employees where department_id is null;

-- group 함수
-- sum avg count min max
select salary from employees;
select to_char(sum(salary),'L999,999') from employees;

select avg(salary) from employees;
--소수점 2자리 반올림
select round(avg(salary),4) from employees;
select trunc(avg(salary),4) from employees;
-- 최대값,최소값
select max(salary) from employees;
select min(salary) from employees;

--- 평균값보다 월급이 높은 사원을 출력하시오
select emp_name,salary from employees where salary > 6461.83;

-- 평균값을 select 해서 입력함
select count(salary) from employees where salary >= (select avg(salary) from employees);

-- emp_name ; 단일함수, avg ; 그룹함수 ; 같이쓰면 에러
select emp_name, avg(salary) from employees;
select department_id, max(salary) from employees;

-- students 모든 학생의 kor 점수 합계 평균 최대값 최소값을 구하시오.
select kor from students;
select sum(kor),avg(kor),max(kor),min(kor), median(kor) from students;

-- 부서번호가 50 사원들의 월급의 합 평균 최대값 최소값 출력
select sum(salary), avg(salary), max(salary), min(salary) from employees where department_id = 50;

-- 부서번호가 30
select sum(salary), avg(salary), max(salary), min(salary) from employees where department_id = 20;

-- group by ; 단일함수를 출력하고 싶을 때 단일함수를 입력하면 됨.
select department_id, max(salary) from employees group by department_id;

select max(salary) from employees where department_id = 50;

select emp_name,salary from employees;
select avg(salary) from employees;

-- 단일함수와 그룹함수 함계 사용ㅇ하려면 group by 지정
select department_id,avg(salary) from employees group by department_id order by department_id;

select emp_name ,max(salary) from employees group by emp_name; -- 그룹핑 할걸 그룹핑 

-- 평균월급보다 높은 사람 수를 출력하시오.
select count(salary), min(salary),max(salary) from employees where salary > (select avg(salary)from employees);

-- 수학함수 : abs(절대값) ceil(올림) floor(버림) round(반올림) trunc(자름) mod(나머지) power(제곱) sqrt(제곱근)
select power(3,2),3*3, sqrt(4) from dual;

select sysdate,to_number(sysdate) from dual; -- 에러 날짜형 타입 숫자형 변경 불가
select 20240110,to_date(20240110) from dual;

select '20240101', to_number('20240101') from dual;
select to_date('20240101') from dual;

-- 날짜형 -> 문자형 변환
select sysdate,to_number(to_char(sysdate,'yyyymmdd')) from dual;

-- 날짜형타입을 문자형타입으로 변경시, 년 월 일 한글 입력방법
select sysdate, to_char(sysdate,'yyyy"년"mm"월"dd"일" day') from dual;
select sysdate, to_char(sysdate,'yyyy mm dd day') from dual;

---- 문자형 함수
select emp_name, email from employees;
-- 문자형 타입을 합쳐서 +기호를 사용해서 합치려고 하면 에러
-- concat / || 
select concat(emp_name,email) from employees;
select emp_name||email from employees;

-- lower; 소문자 취환, upper; 대문자 취환, initcap; 첫글자만 대문자
select * from member where lower(name) = 'bryan';

select 'joJn',initcap('john'),lower('john'),upper('john') from dual;

--lpad ; 왼쪽 자리수 채우기
select 'john',lpad('john',10,'#')from dual;

--rpad ; 오른쪽 자리수 채우기
select 'john',rpad('john',10,'#') from dual;

-- trim 앞 뒤 빈공백없애기 ltrim(왼) rtrim(오) 중간 빈공백 못없앰
select '    aaa',trim('    aaa   '),ltrim('    aaa'),rtrim('aaa    ') from dual;
-- replace ; 취환
select '   a bc ', trim('   a bc ') from dual;
select '   a bc ', trim('   a bc '),replace('   a bc ',' ','') from dual;

-- substr ;특정위치 자르기 (시작위치, 개수)
select 'abcdefu',substr('abcedfu',6,2) from dual;

-- 입사일이 3월인 사원 출력
select to_char(hire_date,'yyyy-mm-dd') from employees where substr(hire_date,4,2) > 7;

-- translate 치환
-- 한글자 한글자에 해당되는 단어를 각각 단어로 치환
-- 순서에 없는 변환글자는 삭제처리
select 'axyzxxy',translate('axyzxxy','xy','ab') from dual;


