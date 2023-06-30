# WHERE
- FROM 뒤에 쓰면서 필터링해주는 기능
<!--
SELECT *
FROM users
WHERE first_name = 'Michael';
-->

# 비교연산자
- = : 같음
- < : 미만
- > : 초과
- >= : 이상
- <= : 이하
- != : 같지 않음
- <> : 같지 않음


# 논리연산자
- and : 교집합
<!-- 
select * from users
where id < 10000
and first_name = 'David'
-->

- or : 합집합
<!-- 
select * from users
where age < 20
or age > 60

select * from users
where first_name = 'David'
and (age < 20 or age > 60)
-->

- NOT : 반대로
<!-- 
select * from users
where NOT(country = 'United States')
-->


# BETWEEN 연산
- BETWEEN A AND B : A와 B를 포함한 사이의 값
<!-- 
select * 
from users
where age between 20 and 30
-->

- 1월 가입한 유저를 조회하고 싶은 경우
<!-- 
select *
from users
where created_at between '2020-01-01' and '2020-02-01'
-->

- 2020-01-01 00:00:00 부터 2020-01-31 00:00:00 사이를 조회하기 때문에 2020-01-31일의 값은 조회할 수 없습니다.
<!-- 
select *
from users
where created_at between '2020-01-01' and '2020-01-31'
-->


# IN 연산
- IN A : A안에 값과 일치하는 값을 조회
<!-- 
select * 
from products
where brand in ('Onia', 'Hurley', 'Matix');
-->

<!-- 
select * 
from users
where id in (1978,4834,37153,49725,61293,63470,74653,80628,84078,41307,44567,45095,60864,97606,9432,20729,21930,33675);
-->


# LIKE 연산
- 비교 문자와 형태가 일치(%(모든 문자), _(한 글자) 사용)
- 대소문자를 안가림
- `%`는 와일드카드

- product의 name안에 Young이 포함된 레코드를 조회
<!--
select * 
from products
where name like '%Young%';
-->

- product의 name이 Hurley로 시작되는 레코드를 조회
<!-- 
select * 
from products
where name like 'Hurley%';
-->

- 언더바는 한개의 글자를 포함 (언더바의 갯수가 3개이므로 Da로 시작하면서 뒤에 3글자가 붙는 총 5글자인 레코드를 조회)
<!-- 
select distinct first_name
from users
where first_name like 'Da___';
-->


# IS NULL
- NULL 값을 갖는 값(0은 값이 있는 것입니다.)

-비어있는 값 조회
<!-- 
select * 
from order_items
where shipped_at IS NULL;
-->

- 비어있지 않는 값 조회
<!-- 
select * 
from order_items
where shipped_at IS NOT NULL;
-->

-------------------------------------------------------


# 연습문제

1. 상품정보(products) 테이블에서 카테고리(category)가 ‘Swim’ 인 레코드의 모든 항목를 조회하세요.
<!-- 
select *
from products
where category = 'Swim';
-->

2. 상품정보(products) 테이블에서 브랜드(brand)가 ‘2EROS’인 레코드의 id, 비용(cost), 브랜드(brand)를 조회하세요.
<!-- 
select id, cost, brand
from products
where brand = '2EROS';
-->

3. 상품정보(products) 테이블에서 비용(cost)이 30이하이고 상품대상, 구분, 분야(department)이 ‘Men’인 모든 레코드를 10개를 조회하세요.
<!-- 
select *
from products
where cost <= 30 and department  = 'Men' limit 10;
-->

4. 상품정보(products) 테이블에서 판매가격(retail_price)이 40이상인 레코드들의 카테고리(category) 속성값을 중복제거(distinct)하여 조회하세요.
<!-- 
select
	distinct category
from products
where retail_price >= 40;
-->

5. 상품정보(products) 테이블에서 비용(cost)이 50이상이고 70이하인 모든 레코드들 조회하세요.
<!-- 
select
	*
from products
where cost between 50 and 70;
-->

<!-- 
select
	*
from products
where cost >= 50 and cost <= 70;
-->

6. 상품정보(products) 테이블에서 상품명(name)에 ‘Men’과 ‘Sport’ 두 단어가 들어간 모든 레코드들 조회하세요.
<!-- 
select
	*
from products
where name like '%Men%' and name like '%Sport%';
-->

7. 상품정보(products) 테이블에서 브랜드(brand)가 ‘TYR’이 아니고 이름(name)에 ‘Suit’가 포함되고 할인율이 50이상인 모든 레코드와 할인율을 조회합니다. 할인율 : (비용/판매비용)*100  할인율의 컬럼 이름은 sale_price로 표현합니다.
<!-- 
select
	*,
	(cost / retail_price) * 100 as sale_price
from products
where not (brand = 'TYR') and name like '%Suit%';
-->

-------------------------------------------------------


# 집계함수
- 단일 컬럼으로 집계만 해줌


# COUNT
- 해당 항목 레코드의 개수를 반환하는 함수
- COUNT(별표)와 COUNT(컬럼명) 차이
COUNT(별표) : NULL값 포함 O
COUNT(컬럼명) : NULL값 포함 X


# SUM
- 해당 항목 레코드의 합계를 반환하는 함수


# GROUP BY
- 특정 항목을 기준으로 그룹화하여 조회할 수 있습니다. 데이터를 그룹화 하여 조회할 때, 그룹화 하려는 항목이 select 에 들어가야 합니다.
- 집계함수가 포함되어야 하고 그룹핑한 항목들만 select에 쓸수 있음.
<!-- 
select country, count(id) 
from users
group by country;
-->

<!-- 오류
select country, city count(id) 
from users
group by country;
-->

<!-- 오류 고침
select country, city count(id) 
from users
group by country, city;
-->

-------------------------------------------------------

# 연습문제
1. 회원(users) 테이블에서 전체 유저의 평균연령을 조회하세요.
<!--
select avg(age)
from users;
-->

2. 회원(users) 테이블에서 여성 유저의 평균연령을 조회하세요.
<!--
select avg(age)
from users
where gender = 'F';
-->

3. 회원(users) 테이블에서 국가별 가입자수를 조회하세요.
<!-- 
select
	country,
	count(id) as country_user_count
from users
group by country;
-->

4. 회원(users) 테이블에서 남성 유저의 국가별 가입자 수를 조회하세요.
<!-- 
select
	country,
	count(id) as country_user_count
from users
where gender = 'M'
group by country;
-->

5. 회원(users) 테이블에서 가입기간(created_at)이 2020년도 1월인 유저의 국가별 가입자 수 (country_user_count)를 조회하세요.
<!-- 
select
	country,
	count(id) as country_user_count
from users
where created_at between '2020-01-01 00:00:00' and '2020-02-01'
group by country;
-->
<!-- 
select 
    country,
    count(id) as country_user_count
from users
where created_at >= '2020-01-01'
and created_at < '2020-02-01'
group by country
-->

# 질문
<!-- 3, 4, 5번 문제에서 count()의 괄호 안에 id를 넣었을 때와 country를 넣었을 때 결과값은 똑같이 받았는데 눈에 보이지 않는 차이가 있을까요?? -->

# 답변
<!-- 말그대로 id컬럼데이터의 갯수를 세느냐 아니면 country컬럼의 갯수를 세느냐의 차이예요.
만약 country값이 null인 유저가 있다면 
count(country) 요렇게 세었을때는 해당 유저는 카운트되지 않을거예요.
count(id)로 해준 이유는 id는 모든 유저가 가지고 있는 데이터라서 입니다. -->

6. ★★★회원(users) 테이블에서 가입기간(created_at)이 2020년도 1월인 유저의 국가별 성별 가입자 수(country_gender_user_count)를 조회하세요.
<!-- 
select 
    country,
    gender,
    count(id) as country_gender_user_count
from users
where created_at >= '2020-01-01'
and created_at < '2020-02-01'
group by country, gender;
-->

7. ★★★ 주문정보(orders) 테이블에서 주문생성일이 2022년도인 주문중에서 주문 상태가 환불(Returned)상태인 주문을 기준으로 유저 아이디(user_id)별 총 주문 아이템(num_of_item)의 합계를 조회하세요.
<!-- 
select 
    user_id,
    sum(num_of_item)
from orders
where (created_at >= '2022-01-01'
and created_at < '2023-01-01') and status = 'Returned'
group by user_id;
-->

-------------------------------------------------------

# HAVING
- 그룹화된 데이터에 조건을 부여합니다. 그룹화된 데이터에 조건을 부여하므로 GROUP BY와 함께 사용합니다.


# OREDER BY
- 오름차순 : ASC(기본, 작은 수에서 큰 수로, Ascending)
- 내림차순 : DESC(큰 수에서 작은 수로, Descending)


# 작성 순서
1. from
2. where
3. group by
4. having
5. select
6. order by
7. limit

- 국가별 20세 이하 유저수가 500명 이상인 유저수 국가 TOP 5를 조회하는 과정
<!-- 
select 
	country,
	count(id) as user_count
from users
where age <= 20
group by country
having count(id) >= 500
order by user_count desc
limit 5;
-->

-------------------------------------------------------

# 연습문제
1. 회원 테이블(users)에서 국가별 유저수를 조회하세요. 
- 조회 항목 : 국가명(country), 국가별 유저수(user_count)
- 조건 : 국가의 유저수가 3000명 이상인 국가
- 정렬 : 국가별 유저수 많은순으로 정렬

<!-- 
select 
	country,
	count(id) as user_count
from users
group by country
having count(id) >= 3000
order by count(id) desc;
-->

2. 상품정보(products) 테이블에서 여성 스웨터중 판매가격이 제일 저렴한 5개를 조회하세요.

- 조건
    - category : Sweaters
    - department : Women
    - 정렬 : 판매가격(retail_price)이 낮은 순
    - 갯수제한 : 5개

<!-- 
select 
	*
from products
where category = 'Sweaters' and department = 'Women'
order by retail_price asc
limit 5;
-->

3. 상품정보(products) 테이블에서 여성 스웨터의 브랜드별 평균 판매가격이 100이하인 브랜드의 브랜드 이름과 여성스웨터 평균판매가격을  조회하세요.

- 조건
    - category : Sweaters
    - department : Women
    - 그룹조건 : 평균 판매가격이 100 이하
    - 정렬순서 : 평균 판매가격이 낮은 순

<!-- 
select 
	brand,
	avg(retail_price) as retail_price_avg
from products
where category = 'Sweaters' and department = 'Women'
group by brand
having avg(retail_price) <= 100
order by avg(retail_price) asc;
-->

4. 상품정보(products) 테이블에서 각 제품의 id, 이름, 카테고리, 브랜드, 비용(cost), 판매가(retail_price), 이익금액(profit), 이익율(profit_rate)을 조회하세요.

- 이익금액(profit) : 판매가(retail_price) - 비용(cost)
- 이익율(profit_rate) : (판매가(retail_price) - 비용(cost)) / 판매가(retail_price) * 100

<!-- 
select 
	id,
	name,
	category,
	brand,
	cost,
	retail_price,
	(retail_price - cost) as profit,
	(retail_price - cost) / retail_price * 100 as profit_rate
from products;
-->

5. 상품정보(products) 테이블에서 수영카테고리 제품의 각 브랜드별 최소이익율, 최대 이익율, 평균 이익율을 조회하세요.

- 조건
    - category : Swim
    - 이익율(profit_rate) : (판매가(retail_price) - 비용(cost)) / 판매가(retail_price) * 100

<!-- 
select
	brand,
	min((retail_price - cost) / retail_price * 100)as min_profit_rate,
	max((retail_price - cost) / retail_price * 100)as max_profit_rate,
	avg((retail_price - cost) / retail_price * 100)as avg_profit_rate
from products
where category = 'Swim'
group by brand;
-->

6. 연습문제 5-5 데이터에서 평균이익율이 높은 TOP 5 브랜드와 평균이익율을 조회하세요.

<!-- 
select
	brand,
	avg((retail_price - cost) / retail_price * 100)as avg_profit_rate
from products
where category = 'Swim'
group by brand
order by avg_profit_rate desc
limit 5;
-->

-------------------------------------------------------

# 숫자 함수

# ROUND
- 해당 항목 레코드의 숫자를 반올림하여 출력하는 함수
- select round(반올림할 숫자, 자릿수)
<!-- 
select round(100.56789,3)
-->


# TRUNC
- 해당 항목 레코드의 숫자를 내림(절삭)하여 출력하는 함수
- select trunc(숫자, 자릿수)
<!-- 
select trunc(100.56789,3)
-->


# 문자열 함수

# SURSTR / SUBSTR / SUBSTRING
- 문자열의 일부만 출력
- select substr(문자열, 시작 위치, 길이)
<!-- 
select substr('hello world', 3, 5)
-->


# LEFT / RIGHT
- 문자열을 왼쪽 / 오른쪽 에서 얼만큼 자를 지 설정한 후에 조회
- select left(문자열,길이)
<!-- 
select left('064-000-0000',3)
-->

<!-- 
select left(email,3)
from users
-->

- select right(문자열,길이)
<!-- 
select right('064-000-1234',4)
-->

<!-- 
select right(email,3)
from users
-->


# CONCAT
- 여러 문자열을 하나로 연결
<!-- 
select concat('paul', '-', 'lab')
-->

<!-- 
select concat(first_name, ',', last_name)
from users
-->

- 연결연산자(||)으로도 연결이 가능
<!-- 
select 'first_name'||'last_name'
-->

<!-- 
select first_name || ',' || last_name
from users
-->


# LOWER / UPPER
- 문자열을 모두 소문자 / 대문자로 변경
<!-- 
select lower('Abc')
-->

<!-- 
select upper('Abc')
-->


# REPLACE
- 바꾸고 싶은 값으로 대상 값을 교체
<!-- 
select replace('hello world', 'world', 'sql')
-->

<!-- 
select replace(gender, 'M', 'Man')
from users;
-->


# LENGTH
- 문자열의 길이를 출력, COUNT와 비교해서 기억!!
<!-- 
select length('hello world')
-->

<!-- 
select length('hello world')
-->


# POSITION
- 문자열의 위치를 구하며 여기에서 INDEX는 1부터 시작하고 찾는 문자가 없을 경우 0을 반환
<!-- 
select POSITION('b' IN 'abcdef');
-->

<!-- 
select POSITION('@' IN email)
from users
-->

# coalesce
- coalesce은 해당 컬럼에 NULL값이 있는 경우 다른 값으로 채워넣을 수 있음
<!-- 이 예시의 경우 데이터 추가 후 가능! -->
<!--
select coalesce(name, '담당자 지정 안됨')
from `weniv.weniv_event`
-->


# 형 변환

# 문자열

- 문자열 -> 숫자 바꾸기
- 문자열 -> 자연수(INTEGER)
- 문자열 -> FLOAT

<!-- select CAST('123' AS INT);
select '123' + '123' # 에러;
select CAST('123' AS INT) + CAST('123' AS INT);
select CAST('123.123' AS FLOAT);
select CAST('123' AS NUMERIC);
select CAST('123.123' AS NUMERIC);

select '123'::INT;
select '123.123'::NUMERIC;
select '123.123'::TEXT; -->

- SELECT CAST(문자열 AS NUMERIC)
- SELECT CAST(문자열 AS INT)
- SELECT CAST(문자열 AS FLOAT)


# 숫자
- SELECT CAST(숫자 AS TEXT)


# 날짜
- SELECT DATE('2011-12-01 11:12:34')  :  날짜만 조회
- SELECT '2011-12-01 11:12:34'::DATE;  :  날짜만 조회
- SELECT '2011-12-01 11:12:34'::TIME;  :  시간만 조회
- SELECT '2011-12-01 11:12:34'::TIMESTAMP;  :  날짜, 시간 모두 조회


# 날짜 함수
https://paullabworkspace.notion.site/15-b954bdbb91d640b1a58e6de9b6cb9176


# 가장 많이 쓰이는 함수(외우지 않아도 됨!)
SELECT TO_CHAR(DATE '2023-01-25', 'YY/MM/DD') AS KR_format;
SELECT TO_CHAR(DATE '2023-01-25', 'YYYY/MM/DD') AS KR_format;
SELECT TO_CHAR(TIMESTAMP '2023-01-25 15:30:00', 'YY/MM/DD HH24:MI:SS') AS KR_format;


# 날짜 차이 구하기
select delivered_at - created_at 
from orders
where status = 'Complete'


# 연습문제
1. 상품정보(products) 테이블에서 상품의 id, 상품명(name), 판매가격(retail_price)를 조회합니다. 
판매가격은 소수점 2자리에서 반올림 합니다.
<!-- 
select
	id,
	name,
	round (retail_price, 2) as retail_price
from products;
-->

2. 회원(users) 테이블에서 회원아이디(id), 이메일(email), 가입연도(signup_year)을 조회하세요.
<!-- 
select
	id,
	email,
	extract(year from created_at) as signup_year
from users;
-->