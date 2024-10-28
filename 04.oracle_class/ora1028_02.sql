-- 테이블 생성
CREATE TABLE MEMBER(
ID VARCHAR2(20) PRIMARY KEY,
PW VARCHAR2(20),
NAME VARCHAR2(20),
PHONE VARCHAR2(20)
);

--- AAA 1111 홍길동 010-1111-1111
-- 입력
INSERT INTO MEMBER(ID,PW,NAME,PHONE) VALUES(
'AAA','1111','홍길동','010-1111-1111'
);

SELECT * FROM MEMBER;
COMMIT;

INSERT INTO MEMBER VALUES(
'BBB','1111','유관순','010-2222-2222'
);
COMMIT;

INSERT INTO MEMBER VALUES(
'CCC','이순신'
);

INSERT INTO MEMBER(ID,NAME) VALUES('CCC','이순신');
COMMIT;

-- 검색
SELECT * FROM MEMBER;

SELECT ID,PHONE FROM MEMBER;

SELECT NAME,PHONE FROM MEMBER;

SELECT NAME ID FROM MEMBER;

SELECT * FROM EMPLOYEES;

SELECT EMP_NAME, SALARY FROM EMPLOYEES;

SELECT * FROM MEMBER;

-- 수정
UPDATE MEMBER SET NAME = '홍길자' WHERE ID = 'AAA';
COMMIT;

SELECT * FROM MEMBER;

-- 삭제
DELETE MEMBER WHERE ID = 'CCC';
-- 데이터 확정 : COMMIT(저장), ROLLBACK(되돌리기)
COMMIT;
ROLLBACK -- COMMIT하면 롤백 불가
 
