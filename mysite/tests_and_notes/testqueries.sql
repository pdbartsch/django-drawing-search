
-- ctrl + shift + q

select NewName from drawsearch_search where LocationNumber = 525 and DrawingNumber = 101 and Discipline like '%arch%';


select count(*) as "Number of rows"
from drawsearch_search
where LocationNumber = 525 and DrawingNumber = 101 and Discipline like '%architectural%';


select count(*) as "Number of rows" from draw where LocationNumber = 489 and DrawingNumber = 101;

select drawsearch_search.id, drawsearch_search.NewName, drawsearch_search.DrawingDate
from drawsearch_search 
where LocationNumber = 525 
and DrawingNumber = 101 
and Discipline like '%arch%';