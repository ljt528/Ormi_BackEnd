# 연습문제
3. 회원(users) 테이블에서 가입연도(signup_year), 연도별 가입자(user_count)를 조회하세요.

select
	extract(year from created_at) as signup_year,
	count(id) as user_count
from users
group by extract(year from created_at)
order by signup_year;


4. 가입회원들이 시간대별 가입자수를 확인하려고 합니다.
회원(users) 테이블에서 0~23으로 표시되는 시간대(hour), 시간대별 가입자 수(user_count)를 조회하세요.
정렬 순서는 시간대(hour)순입니다.

select
	extract(hour from created_at) as signup_hour,
	count(id) as user_count
from users
group by extract(hour from created_at)
order by signup_hour;


5. 특정 연도의 월별 주문건수
주문정보(orders) 테이블에서 2020년도의 월별 주문건수를 조회하세요.
조회항목은 연도, 월, 주문건수 입니다.

select 
    extract(year from created_at) as year,
    extract(month from created_at) as month,
    count(order_id) as order_count
from orders
where extract(year from created_at) = 2020
group by extract(year from created_at), extract(month from created_at)
order by year, month

select 
    extract(year from created_at) as year,
    extract(month from created_at) as month,
    count(order_id) as order_count
from orders
where extract(year from created_at) = 2020
group by year, month
order by year, month

select 
    extract(year from created_at) as year,
    extract(month from created_at) as month,
    count(order_id) as order_count
from orders
where extract(year from created_at) = 2020
group by 1, 2
order by 1, 2

# 조건분기

# CASE
SELECT 안에 써줌

CASE WHEN 
	조건 
THEN 
	참일경우_실행구문 
ELSE 
	거짓일경우_실행구문 
END


# 연습문제 6-7
회원(users) 테이블에서 가입연도(signup_year), 연도별 가입자(user_count)를 조회하세요.
select 
    extract(year from created_at) as signup_year,
    count(id) as user_count
from users
group by extract(year from created_at)
order by signup_year


시간대별 회원가입수
select 
    extract(hour from created_at) as signup_hour,
    count(id) as user_count
from users
group by extract(hour from created_at)
order by signup_hour

# 연습문제 6-9
특정 연도의 월별 주문건수
주문정보(orders) 테이블에서 2020년도의 월별 주문건수를 조회하세요.
조회항목은 연도, 월, 주문건수 입니다.
select 
    extract(year from created_at) as year,
    extract(month from created_at) as month,
    count(order_id) as order_count
from orders
where extract(year from created_at) = 2020
group by extract(year from created_at), extract(month from created_at)
order by year, month

select 
    extract(year from created_at) as year,
    extract(month from created_at) as month,
    count(order_id) as order_count
from orders
where extract(year from created_at) = 2020
group by year, month
order by year, month

select 
    extract(year from created_at) as year,
    extract(month from created_at) as month,
    count(order_id) as order_count
from orders
where extract(year from created_at) = 2020
group by 1, 2
order by 1, 2

# 연습문제 7-1
주문정보(orders) 테이블에서 order_id, gender, gender_label(gender의 값에 따른 성별을 한글로 표시)을 해주세요.

필드명 : gender_label
gender가 F 이면 '여성'
gender가 M 이면 '남성'
결과로 표시할 필드
order_id
gender
gender_label
정렬순서 : order_id 오름차순

select 
    order_id,
    gender,
    case
        when gender = 'F' then '여성'
        when gender = 'M' then '남성'
    end as gender_label
from orders
order by order_id

select 
    order_id,
    gender,
    case gender
        when 'F' then '여성'
        when 'M' then '남성'
    end as gender_label
from orders
order by order_id


# 연습문제 7-2
회원(users) 테이블에서 다음 정보를 조회하세요.

1. 조회 항목
유저아이디 - id,
가입연도 - year
가입월 - month
가입일 - day
이용경로(traffic_source) 한글 텍스트 -  traffic_source_label
Search → 검색엔진
Organic → 검색결과
Email → 이메일
Display → 디스플레이 광고
Facebook → 페이스북

2. 정렬순서
id 오름차순

select 
    id,
    extract(year from created_at) as year,
    extract(month from created_at) as month,
    extract(day from created_at) as day,
    case traffic_source
        when 'Search'   then '검색엔진'
        when 'Organic'  then '검색결과'
        when 'Email'    then '이메일'
        when 'Display'  then '디스플레이 광고'
        when 'Facebook' then '페이스북'
    end as traffic_source_label
from users

# 연습문제 7-3
회원(users) 테이블에서 가입연도별 이용경로(traffic_source)별 가입자수를 조회하세요.

조회 항목
year
Search
Organic
Email
Display
Facebook
Total

정렬순서
year 오름차순

select 
    extract(year from created_at) as year,
    count(case when traffic_source = 'Search' then 1 end) as Search,
    count(case when traffic_source = 'Organic' then 1 end) as Organic,
    count(case when traffic_source = 'Email' then 1 end) as Email,
    count(case when traffic_source = 'Display' then 1 end) as Display,
    count(case when traffic_source = 'Facebook' then 1 end) as Facebook,
    count(id) as total
from users
group by year
order by year

select 
    extract(year from created_at) as year,
    sum(case when extract(quarter from created_at) = 1 then sale_price end) as q1,
    sum(case when extract(quarter from created_at) = 2 then sale_price end) as q2,
    sum(case when extract(quarter from created_at) = 3 then sale_price end) as q3,
    sum(case when extract(quarter from created_at) = 4 then sale_price end) as q4,
    round(sum(sale_price), 2) as total
from order_items
where status = 'Complete'
group by year
order by year


# 연습문제 8-1
회원(users) 테이블과 주문정보(orders) 테이블을 이용하여 모든 주문내역에 회원정보를 표시하세요.

조회 항목 :
주문ID(order_id)
주문한 상품 수량(num_of_item)
회원 이름(first_name, last_name)
주소(street_address)
우편번호(postal_code)
도시(city)
국가(country)

select 
    o.order_id ,
    o.num_of_item ,
    concat(u.first_name, ' ', u.last_name) as user_name,
    u.street_address ,
    u.postal_code ,
    u.city ,
    u.country 
from orders o 
join users u on o.user_id = u.id 

# 연습문제 8-2
회원(users) 테이블과 주문정보(orders) 테이블을 이용하여 상품을 주문한 회원의 국가가 ‘United States’이면서 주문 상태가 처리중(Processing)인 정보를 조회하시오. 

조회 항목
주문ID(order_id)
회원 이름(first_name, last_name)
주소(street_address)
우편번호(postal_code)
도시(city)
국가(country)
주문한 상품 수량(num_of_item)
조건 : 국가가 ‘United States’이면서 주문 상태가 처리중(Processing)

select 
    o.order_id ,
    concat(u.first_name, ' ', u.last_name) as user_name,
    u.street_address,
    u.postal_code,
    u.city,
    u.country,
    o.num_of_item
from orders o 
join users u on o.user_id = u.id
where u.country = 'United States'
and o.status = 'Processing'

# 연습문제 8-3
회원(users) 테이블과 주문정보(orders) 테이블을 이용하여 국가별 총 상품 주문주(total_order_count)을 조회하시오.

조회 항목 : 국가명(country), 국가별 총 상품 주문주(total_order_count)
정렬 : 국가별 총 상품 주문주(total_order_count)이 많은 순으로 정렬

