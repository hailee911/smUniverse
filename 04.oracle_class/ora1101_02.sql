-- 11/01
CREATE TABLE EMP3 AS SELECT * FROM EMPLOYEES; -- TABLE COPY
CREATE TABLE EMP4 AS SELECT * FROM EMPLOYEES WHERE 1=2; -- TABLE COPY NO CONTENTS
SELECT * FROM EMP3;
SELECT * FROM EMP4;
-- 테이블 구조가 있는 상태에서 모든 데이터를 입력하는 방법
INSERT INTO EMP4 SELECT * FROM EMPLOYEES;
-- INSERT UPDATE DELETE -- COMMIT/ROLLBACK
-- 제약조건이 NULL 이 들어가면 안되는 것을 확인
INSERT INTO EMP4(EMPLOYEE_ID,EMP_NAME,HIRE_DATE,SALARY) SELECT EMPLOYEE_ID,EMP_NAME,HIRE_DATE,SALARY FROM EMPLOYEES;

------ 테이블
-- CREATE ALTER DROP
SELECT * FROM EMP4;
-- ALTER ADD ; 테이블에 컬럼 추가
ALTER TABLE EMP4 ADD(HIRE_DATE2 DATE);
DESC EMP4;
-- 컬럼변경 ; 컬럼안에 데이터가 있다면 제약조건, 65 길이의 문자가 있을 경우 50으로 변경 불가
ALTER TABLE EMP4 MODIFY(EMAIL VARCHAR2(70));
ALTER TABLE EMP4 MODIFY(EMAIL VARCHAR2(50));

SELECT EMP_NAME FROM EMP4;
SELECT MAX(LENGTH(EMP_NAME)) FROM EMP4;
SELECT LENGTH(EMP_NAME) FROM EMP4 ORDER BY LENGTH(EMP_NAME)DESC;

-- 다른 타입인 경우 데이터를 NULL 로 변경 후 타입을 변경
DESC EMP4;

-- 이메일에 EMPLOYEE_ID 값 복사
UPDATE EMP4 SET EMAIL = EMPLOYEE_ID;
-- EMPLOYEE_ID PHONE_NUMBER 입력 -- PHONE_NUMBER 문자형타입 EMPLOYEE_ID 숫자형 타입
UPDATE EMP4 SET PHONE_NUMBER = EMPLOYEE_ID;

-- 문자형타입을 숫자형 타입에 복사
-- 안에 있는 데이터가 모두 숫자형이기에 가능
-- 문자가 포함되어 있으면 안됨
UPDATE EMP4 SET MANAGER_ID = PHONE_NUMBER;
UPDATE EMP4 SET PHONE_NUMBER = '198A' WHERE EMPLOYEE_ID = 198;

-- 컬럼 이름 변경
ALTER TABLE EMP4 RENAME COLUMN PHONE_NUMBER TO P_NUMBER;

-- 속성 변경
ALTER TABLE EMP4 MODIFY HIRE_DATE DATE NULL;
ALTER TABLE EMP4 MODIFY HIRE_DATE DATE NOT NULL;

-- 컬럼 삭제
ALTER TABLE EMP4 DROP COLUMN HIRE_DATE2;
-- 테이블 삭제
DROP TABLE EMP2;
DROP TABLE EMP3;
-- 테이블 이름 변경
RENAME EMP44 TO EMP4;

----
DROP TABLE BOARD;

DROP TABLE BMEMBER;

-- CHECK - MALE,FEMALE 2가지 형태 외에는 입력 안되게
-- NOT NULL - 빈공백은 가능함
SELECT * FROM BMEMBER;

-- PRIMARY KEY ; 중복불가 NULL 불가

CREATE TABLE EMP3(
EMPNO NUMBER(4) UNIQUE,
ENAME VARCHAR2(30) NOT NULL,
JOB VARCHAR2(9),
DEPTNO NUMBER(2)
);

INSERT INTO EMP3 VALUES(
1,'홍','01','01'
);
INSERT INTO EMP3 VALUES(
2,'유','02','02'
);
-- UNIQUE NULL 값은 혀용
INSERT INTO EMP3 (ENAME,JOB,DEPTNO) VALUES(
'이','03','03'
);
-- UNIQUE 중복은 불가
INSERT INTO EMP3 VALUES(
2,'강','04','04'
);
SELECT * FROM EMP3;

-- primary key 등록시 null 값이 존재하면 안됨 중복도 존재하면 안됨
-- primary key 추가, 수정
-- constraint id_pk 이름 설정
ALTER TABLE MEMBER ADD CONSTRAINT ID_PK PRIMARY KEY(ID);
SELECT * FROM MEMBER;
INSERT INTO MEMBER VALUES('fff','1111','홍길자','aaa@aaa.COM','123-456-789','Female','golf',sysdate);

alter table member drop constraint id_pk;

create table board(
bno number(4)primary key,
btitle varchar2(100) not null,
bcontent clob,
id varchar2(30),
bgroup number(4),
bstep number(4),
bindent number(4),
bhit number(4),
bdate date,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval,'제목1','내용1','aaa',board_seq.currval,0,0,0,sysdate,''
);
insert into board values(
board_seq.nextval,'제목2','내용2','bbb',board_seq.currval,0,0,0,sysdate,''
);
insert into board values(
board_seq.nextval,'제목5','내용5','ddd',board_seq.currval,0,0,0,sysdate,''
);

select * from board;

----------------
create table mem2 (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('aaa', '1111', '홍길동', 'rsherville0@tinyurl.com', '324-226-8544', 'Male', 'golf', '2024-03-06');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('bbb', '1111', '유관순', 'mrubinlicht1@fotki.com', '475-964-8193', 'Female', 'book', '2024-08-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('ccc', '1111', '이순신', 'bchstney2@walmart.com', '541-891-0085', 'Female', 'run', '2024-08-16');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('ddd', '1111', '강감찬', 'cstubbes3@chron.com', '900-194-4605', 'Female', 'game', '2024-02-10');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('eee', '1111', '김구', 'tnacey4@list-manage.com', '727-883-1542', 'Female', 'golf', '2024-09-10');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Trineman', '6216', 'Riobard', 'rtrineman5@prweb.com', '140-720-7698', 'Male', 'book', '2024-09-03');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Towell', '5201', 'Bryan', 'btowell6@stumbleupon.com', '365-214-7874', 'Male', 'run', '2024-03-16');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Neagle', '4903', 'Horacio', 'hneagle7@nifty.com', '114-384-4352', 'Male', 'run', '2024-02-01');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Gresham', '4089', 'Valentine', 'vgresham8@quantcast.com', '547-694-3516', 'Female', 'swim', '2024-10-11');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('O''Dare', '6041', 'Doroteya', 'dodare9@dyndns.org', '102-500-7735', 'Female', 'game', '2024-07-29');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Doumic', '1343', 'Stepha', 'sdoumica@com.com', '745-998-5005', 'Female', 'game', '2024-08-08');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Allmann', '9173', 'Husein', 'hallmannb@imageshack.us', '122-775-3647', 'Male', 'book', '2024-01-01');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Tommis', '6716', 'Roderic', 'rtommisc@sourceforge.net', '673-244-8303', 'Male', 'book', '2024-07-09');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Bleaden', '4168', 'Drud', 'dbleadend@123-reg.co.uk', '838-544-2408', 'Male', 'golf', '2024-06-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('D''Aguanno', '7476', 'Wini', 'wdaguannoe@cyberchimps.com', '237-714-1340', 'Female', 'run', '2024-06-27');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Gegay', '8185', 'Bernette', 'bgegayf@yahoo.com', '982-358-5670', 'Female', 'golf', '2024-07-05');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Flea', '6937', 'Fidelity', 'ffleag@reverbnation.com', '602-708-0462', 'Female', 'run', '2024-01-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Shory', '1240', 'Robb', 'rshoryh@intel.com', '621-231-3542', 'Male', 'run', '2024-09-13');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Harm', '1438', 'Flinn', 'fharmi@yelp.com', '328-792-9216', 'Male', 'golf', '2023-12-05');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Poschel', '9693', 'Sterling', 'sposchelj@usnews.com', '499-462-1400', 'Male', 'swim', '2024-05-27');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Medford', '5717', 'Jacquenette', 'jmedfordk@epa.gov', '634-270-7550', 'Female', 'book', '2024-02-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Gianelli', '5559', 'Katherina', 'kgianellil@wikipedia.org', '967-878-2128', 'Female', 'game', '2024-05-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Kolodziejski', '5522', 'Danella', 'dkolodziejskim@jugem.jp', '110-354-1019', 'Female', 'golf', '2024-03-25');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Mildmott', '9678', 'Jule', 'jmildmottn@wix.com', '286-208-5611', 'Male', 'run', '2024-07-23');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Pietrowski', '6843', 'Ediva', 'epietrowskio@photobucket.com', '571-362-5389', 'Female', 'golf', '2023-12-30');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Chasemoore', '9290', 'Dunc', 'dchasemoorep@geocities.jp', '390-444-9215', 'Male', 'golf', '2024-03-27');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Overnell', '6410', 'Barth', 'bovernellq@cdbaby.com', '825-465-2790', 'Male', 'run', '2024-06-12');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Benford', '8906', 'Margette', 'mbenfordr@twitter.com', '210-839-4892', 'Female', 'swim', '2024-06-20');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Portman', '6013', 'Orson', 'oportmans@reverbnation.com', '258-285-2186', 'Male', 'golf', '2024-06-09');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Elflain', '7065', 'Trish', 'telflaint@intel.com', '319-787-3297', 'Female', 'golf', '2024-04-30');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Ockland', '7153', 'Deirdre', 'docklandu@sfgate.com', '895-501-5958', 'Female', 'run', '2023-12-03');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Le Floch', '5518', 'Linea', 'lleflochv@hp.com', '734-888-6261', 'Female', 'swim', '2024-01-24');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('McGaugan', '5439', 'Conny', 'cmcgauganw@imageshack.us', '376-451-4038', 'Male', 'game', '2023-11-08');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Lilburn', '6148', 'Shepherd', 'slilburnx@sina.com.cn', '250-173-1654', 'Male', 'swim', '2024-07-03');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Frew', '7401', 'Meaghan', 'mfrewy@unc.edu', '276-431-6409', 'Female', 'swim', '2023-12-04');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Myner', '1917', 'Lorrie', 'lmynerz@wikimedia.org', '550-264-0011', 'Male', 'book', '2024-10-06');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Knightsbridge', '2295', 'Elias', 'eknightsbridge10@dedecms.com', '906-789-7346', 'Male', 'swim', '2023-12-30');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Merwood', '6745', 'Georgy', 'gmerwood11@comcast.net', '904-984-7938', 'Male', 'golf', '2024-01-14');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Dewsbury', '1477', 'Bond', 'bdewsbury12@amazon.co.jp', '106-232-5734', 'Male', 'swim', '2024-02-02');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Kliche', '5468', 'Nevins', 'nkliche13@admin.ch', '608-113-7174', 'Male', 'game', '2024-06-22');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Fick', '7675', 'Panchito', 'pfick14@senate.gov', '430-438-4575', 'Male', 'book', '2024-03-12');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Danielczyk', '5661', 'Reinaldos', 'rdanielczyk15@irs.gov', '359-176-0405', 'Male', 'book', '2024-05-27');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Blazey', '8853', 'Lou', 'lblazey16@about.com', '729-460-3951', 'Male', 'run', '2024-04-12');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Godly', '6603', 'Pail', 'pgodly17@plala.or.jp', '190-426-8746', 'Male', 'run', '2024-06-02');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Attwoull', '3472', 'Cliff', 'cattwoull18@slideshare.net', '570-758-4710', 'Male', 'golf', '2024-08-10');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Chason', '5763', 'Terrie', 'tchason19@symantec.com', '650-189-0579', 'Female', 'run', '2024-03-11');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Noni', '2224', 'Jannel', 'jnoni1a@bloglovin.com', '871-506-4522', 'Female', 'book', '2024-01-04');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Graham', '3477', 'Mendy', 'mgraham1b@trellian.com', '887-280-4803', 'Male', 'swim', '2024-09-01');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Griffey', '8521', 'Raff', 'rgriffey1c@51.la', '947-561-4983', 'Male', 'swim', '2024-04-12');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Wretham', '3484', 'Laure', 'lwretham1d@ted.com', '183-800-2897', 'Female', 'book', '2023-11-07');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Sewart', '5890', 'Lodovico', 'lsewart1e@shareasale.com', '962-952-9409', 'Male', 'swim', '2024-05-25');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Leber', '3162', 'Cory', 'cleber1f@foxnews.com', '773-506-6136', 'Female', 'run', '2024-05-03');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Germain', '2786', 'Teodoor', 'tgermain1g@usda.gov', '287-887-6296', 'Male', 'book', '2024-09-25');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('O''Dooghaine', '4249', 'Jeni', 'jodooghaine1h@washingtonpost.com', '656-654-8738', 'Female', 'book', '2024-02-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Ralestone', '2620', 'Lenard', 'lralestone1i@w3.org', '692-797-1702', 'Male', 'book', '2024-09-07');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Yong', '8340', 'Kasey', 'kyong1j@seattletimes.com', '820-634-7148', 'Female', 'run', '2023-12-04');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Yukhov', '6010', 'Gallard', 'gyukhov1k@weather.com', '602-990-8790', 'Male', 'run', '2023-12-22');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Digman', '1555', 'Britt', 'bdigman1l@google.com', '997-747-6638', 'Female', 'game', '2023-11-04');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Rocks', '1647', 'Dane', 'drocks1m@latimes.com', '455-553-6937', 'Male', 'book', '2023-12-07');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Lewisham', '8757', 'Danni', 'dlewisham1n@addtoany.com', '597-704-9376', 'Female', 'swim', '2024-02-09');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('O''Spillane', '4868', 'Hamlen', 'hospillane1o@indiegogo.com', '584-856-0076', 'Male', 'golf', '2024-02-19');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Keoghane', '8511', 'Garrott', 'gkeoghane1p@accuweather.com', '655-285-1122', 'Male', 'game', '2024-01-23');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Gransden', '3139', 'Maire', 'mgransden1q@bloglines.com', '517-233-8716', 'Female', 'book', '2024-02-24');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Kobiera', '5689', 'Jaime', 'jkobiera1r@flickr.com', '325-635-7089', 'Female', 'run', '2023-11-16');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Craske', '6088', 'Isa', 'icraske1s@delicious.com', '903-771-5929', 'Male', 'golf', '2024-06-26');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Island', '9324', 'Terrance', 'tisland1t@cmu.edu', '569-238-3939', 'Male', 'golf', '2024-03-16');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Hazeldine', '9138', 'Glenn', 'ghazeldine1u@foxnews.com', '118-455-4847', 'Male', 'game', '2024-08-10');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Gutch', '8827', 'Davin', 'dgutch1v@jiathis.com', '602-127-7922', 'Male', 'book', '2024-07-06');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Pavlenkov', '8269', 'Elane', 'epavlenkov1w@cyberchimps.com', '172-572-0209', 'Female', 'game', '2023-12-27');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Kasman', '3887', 'Davita', 'dkasman1x@de.vu', '140-813-6914', 'Female', 'book', '2024-09-15');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Andraud', '6948', 'Gunter', 'gandraud1y@rambler.ru', '999-479-2224', 'Male', 'swim', '2024-03-10');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Mandrey', '9531', 'My', 'mmandrey1z@whitehouse.gov', '809-354-8112', 'Male', 'golf', '2024-04-17');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Teers', '1997', 'Lynda', 'lteers20@bigcartel.com', '831-197-8592', 'Female', 'golf', '2024-07-28');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('MacBey', '8775', 'Farand', 'fmacbey21@seesaa.net', '319-735-6030', 'Female', 'swim', '2024-06-05');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Bontoft', '2628', 'Blanca', 'bbontoft22@webnode.com', '818-469-6633', 'Female', 'run', '2024-09-25');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Gercken', '3185', 'Heinrik', 'hgercken23@webmd.com', '604-301-2929', 'Male', 'game', '2024-03-28');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Huzzay', '5857', 'Alf', 'ahuzzay24@sogou.com', '570-223-4310', 'Male', 'book', '2024-08-16');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Tredger', '7675', 'Sherwood', 'stredger25@bbc.co.uk', '527-871-8185', 'Male', 'run', '2024-06-01');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Canadine', '8566', 'Nicolis', 'ncanadine26@devhub.com', '800-674-8410', 'Male', 'golf', '2024-08-03');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Paireman', '7080', 'Nichol', 'npaireman27@msn.com', '668-411-8679', 'Female', 'run', '2024-01-01');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Powis', '6242', 'Mehetabel', 'mpowis28@surveymonkey.com', '271-883-5391', 'Female', 'book', '2024-09-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Walsh', '7311', 'Luther', 'lwalsh29@gmpg.org', '523-360-3018', 'Male', 'golf', '2024-09-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Pont', '4975', 'Edd', 'epont2a@nbcnews.com', '551-629-4794', 'Male', 'golf', '2024-02-22');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Osborne', '7007', 'Gauthier', 'gosborne2b@naver.com', '711-842-1931', 'Male', 'run', '2024-05-31');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Tinker', '8402', 'Andree', 'atinker2c@wp.com', '731-985-8198', 'Female', 'swim', '2023-12-23');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Persence', '7577', 'Obediah', 'opersence2d@elegantthemes.com', '549-594-4369', 'Male', 'run', '2024-05-28');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Boatwright', '1204', 'Ernie', 'eboatwright2e@printfriendly.com', '833-853-7804', 'Male', 'swim', '2024-01-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Kirkhouse', '6330', 'Pernell', 'pkirkhouse2f@soup.io', '412-173-6891', 'Male', 'book', '2024-06-12');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Ghidetti', '9376', 'Den', 'dghidetti2g@seattletimes.com', '165-768-1973', 'Male', 'run', '2024-10-21');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Keppel', '1397', 'Yolanthe', 'ykeppel2h@harvard.edu', '928-660-5279', 'Female', 'run', '2024-09-09');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Matteini', '7664', 'Zola', 'zmatteini2i@jalbum.net', '672-317-8567', 'Female', 'swim', '2024-05-28');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Malmar', '9156', 'Andriana', 'amalmar2j@ed.gov', '588-732-4548', 'Female', 'run', '2024-01-25');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Waplington', '7863', 'Tobiah', 'twaplington2k@dell.com', '996-187-6594', 'Male', 'game', '2024-07-11');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Cosyns', '2387', 'Lauri', 'lcosyns2l@edublogs.org', '943-340-9913', 'Female', 'game', '2024-04-05');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Atto', '5832', 'Had', 'hatto2m@mozilla.com', '624-750-8503', 'Male', 'game', '2024-06-07');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Bushell', '8202', 'Franz', 'fbushell2n@indiegogo.com', '274-938-6045', 'Male', 'game', '2024-03-06');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Glassford', '3189', 'Virgil', 'vglassford2o@usatoday.com', '361-318-5270', 'Male', 'run', '2024-05-23');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Aron', '3277', 'Freeland', 'faron2p@timesonline.co.uk', '724-482-5099', 'Male', 'game', '2024-08-25');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Tavner', '8684', 'Brig', 'btavner2q@webeden.co.uk', '366-125-0586', 'Male', 'run', '2024-05-14');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Shiliton', '5557', 'Sandi', 'sshiliton2r@abc.net.au', '407-488-9852', 'Female', 'book', '2024-01-11');

update mem2 set id='abc',pw='1111',name='이다영',email ='idy0911@naver.com' where id= 'Trineman';

select * from member;
delete member;
select * from mem2;
insert into member select * from mem2;
select * from member;

select * from bmember;
select * from board;

-- 테이블 합치기
select BNO,BTITLE,BCONTENT,NICNAME,AGE,GENDER,PW,EMAIL,BGROUP,BSTEP,BINDENT,BHIT,BFILE from board,bmember
WHERE BOARD.ID = BMEMBER.ID; -- MEMBER.ID ; PRIMARY KEY BOARD.ID ; FOREIGN KEY

SELECT EMPLOYEE_ID, EMP_NAME, EMAIL,SALARY, EMPLOYEES.DEPARTMENT_ID,DEPARTMENT_NAME FROM EMPLOYEES,DEPARTMENTS
WHERE EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID
;

SELECT DEPARTMENT_ID, DEPARTMENT_NAME FROM DEPARTMENTS WHERE DEPARTMENT_ID = 10;

DESC BOARD;
-- FOREIGN KEY 추가, 변경
-- 닉네임 ; ID_FK , FOREIGN KEY ; ID , BMEMBER테이블의 PRIMARY KEY ; ID 등록
ALTER TABLE BOARD ADD CONSTRAINT id_fk FOREIGN KEY (ID) REFERENCES BMEMBER(ID);

SELECT * FROM BOARD;
SELECT * FROM BMEMBER;
-- ABC 글을 등록하면 등록이 안됨


