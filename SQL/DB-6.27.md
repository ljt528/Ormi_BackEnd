DBeaver는 커서있는곳에서 실행됨
Ctrl + Enter : 실행
''홑따옴표만 씀
* 모든 컬럼을 가져오라는 뜻
id : 별칭달아주기
distinct : 중복제거, select에 써야 함!!!
limit (숫자);  :  숫자만큼의 데이터만 뽑아냄, 제일 뒤에 써야 함!!!

select 검색하는기능 + '식'
select 'hello' + 'world' 오류
합치기 ① select 'hello' || 'world' 가능
합치기 ② select concat('hello', ' ', 'world');
select id, first_name from "users“


1. 회원(userss) 테이블의 모든 데이터를 조회하세요.
select * from "users“;

2. 회원(userss) 테이블의 이메일(email) 정보를 조회하세요.
select email from "users“;

3. 회원(users) 테이블의 이름(first_name), 성(lastname), 이메일(email), 국가 정보(country)를 조회하세요.
select first_name, last_name, email, country from "users“;

4. 회원(users) 테이블의 id, 이름(first_name), 성(last_name), first_name이랑 last_name을 합친 값, 이메일(email), 국가 정보(country)를 조회하세요.
select id, first_name, last_name, (first_name || last_name) , email, country from "users“;

5. 상품정보(products) 테이블의 id, 카테고리(category), 이름(name), 판매가격(retail_price), 비용(cost)을 조회하세요.
select id, category, name, retail_price, cost from products;

6. 상품정보(products) 테이블의 id, 카테고리(category), 이름(name), 판매가격(retail_price), 비용(cost), 판매이익(판매가격 - 비용)을 조회하세요.
select id, category, name, retail_price, cost, retail_price - cost from products;






# 별칭달기1
select 
	id as product_id,
	category as product_category,
	name as product_name,
	retail_price as product_retail_price,
	cost as product_cost,
	retail_price - cost as product_profit
from products;


# 별칭달기2
select 
	a.id as product_id,
	a.category as product_category,
	a.name as product_name,
	a.retail_price as product_retail_price,
	a.cost as product_cost,
	a.retail_price - a.cost as product_profit
from products as a;



# 중복제거 1
select
    distinct country
from users;

# 중복제거 2(묶어서 생각함)
select
    distinct country, city
from users;


7. 상품정보(products) 테이블에서 5개 레코드만 조회하세요.
select
    *
from products limit 5;


8. 주문정보(orders) 테이블에서 상태정보(status)를 중복제거하여 아래와 같이 결과가 나오도록 조회하세요.
select
    distinct status
from orders;

9. 상품정보(products) 테이블에서 카테고리(category)를 중복제거하여 아래와 같이 조회하세요.

select
    distinct category
from products;


10. 상품정보(products) 테이블에서 카테고리(category), 브랜드(brand)를 중복제거하여 30개 조회하세요.

각 결과 컬럼의 이름은 다음과 같이 지정하세요.

카테고리 → product_category
브랜드 → product_brand

select
    distinct
    category as product_category,
    brand as product_brand
from products
limit 30;


11. 상품정보(products) 테이블에서 id, 카테고리(category), 이름(name), 판매가격(retail_price), 비용(cost), 판매이익(판매가격 - 비용), 수익율을 조회하세요.

비용 1000원, 판매가 1200원 일 경우

수익율은 (1,200-1,000)/1,000*100 = 20% 입니다.

수익율 : (판매가 - 비용) / 비용 x 100

각 컬럼의 이름은 다음과 같이 표현합니다.

id → product_id
카테고리 → product_category
상품명 → product_name
판매가격 → product_price
비용 → product_cost
판매이익 → product_profit
수익율 → product_profit_rate

<!-- 
select
    id as product_id,
    category as  product_category,
    name as product_name,
    retail_price as product_price,
    cost as product_cost,
    retail_price - cost as product_profit,
    (retail_price - cost) / cost * 100 as product_profit_rate
from products;
-->



