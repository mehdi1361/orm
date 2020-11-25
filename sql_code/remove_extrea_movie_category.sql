create temporary table valid_table as (
select min(id) min_id, category_id, film_id
from movie_film_category
group by category_id, film_id);

select * from valid_table;
delete from movie_film_category where id not in (select min_id from valid_table);

drop table valid_table;