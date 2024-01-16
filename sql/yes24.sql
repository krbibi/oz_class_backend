-- use yes24;

-- select title, author from books;
-- select * from books where rating >= 8.0;
-- select title, review from books where review >= 100 order by review desc;
-- select title,price from books where price<20000 order by price desc;
-- select * from books where ranking_weeks >= 4 order by ranking_weeks desc;
-- select * from books where author = '자청 저'
-- select * from books where publisher = '웅진지식하우스';

-- select author, Count(*) as books_count from books group by author order by books_count desc;
-- 저자를 그룹으로 묶은다음에 북 테이블에서 저자 별로 카운트해서 정리

-- select publisher, count(*) as publishing_count from books group by publisher
-- order by publishing_count desc;
-- select author,avg(rating) as rating_avg from books group by author order by rating
-- select * from books where ranking = 1;
-- select title, sales, review from books order by sales desc, review desc limit 10;
-- select * from books order by publishing desc limit 5;

--

-- select author, avg(rating) as rating_avg from books group by author order by rating_avg desc;
-- select publishing, count(*) from books group by publishing
-- select title, price from books;
-- select * from books order by review desc limit 5;
-- select ranking, avg(review) from books group by ranking;

-- select title, rating from books 
-- where rating > (select avg(rating) from books)
-- order by rating desc;

-- select title, price,publisher from books
-- where price > (select avg(price) from books)
-- order by price desc;

-- select title, sales from books
-- where sales < (select avg(sales) from books);

-- select author,title from books 
-- where author = (select author from books group by author order by count(*) desc limit 1);

-- update books set rating = rating +1 where publisher = '웅진하우스'

-- select author,avg(rating),avg(sales) from books 
-- group by author order by avg(rating) desc,avg(sales) desc;

-- select publishing,avg(price) from books group by publishing 
-- order by publishing desc;

-- select publisher, count(*) as book_count, sum(review) as review_sum 
-- from books group by publisher order by book_count desc;
-- select ranking, avg(sales) from books group by ranking 
-- select price, avg(review), avg(rating) from books group by price;

--  select publisher, author, avg(sales) as avg_sales 
--  from books
--  group by publisher, author
--  order by publisher, avg_sales desc;

-- select title, review,price,sales
-- from books
-- where review > (select avg(review) from books) and price < (select avg(price) from books);

-- SELECT author, COUNT(*) as num_books
-- FROM Books
-- GROUP BY author
-- ORDER BY num_books DESC

-- SELECT author, MAX(sales) as max_sales
-- FROM Books
-- GROUP BY author;

-- SELECT YEAR(publishing) as year, COUNT(*) as num_books, AVG(price) as avg_price
-- FROM Books
-- GROUP BY year;

-- SELECT publisher, count(*), MAX(rating) - MIN(rating) as rating_difference
-- FROM Books
-- GROUP BY publisher
-- having count(*) >=2
-- ORDER BY rating_difference DESC;

-- SELECT title, rating / sales as ratio
-- FROM Books
-- WHERE author = '특정 저자'
-- ORDER BY ratio DESC
-- LIMIT 1;

