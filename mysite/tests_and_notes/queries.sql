-- ctrl shift Q  to run


SELECT * FROM draw WHERE LocationNumber = 525;

SELECT * FROM draw WHERE LocationNumber = 505;

select NewName from draw where LocationNumber = 525 and DrawingNumber = 101 and Discipline like '%arch%';


select count(*) as "Number of rows"
from draw
where LocationNumber = 525 and DrawingNumber = 101 and Discipline like '%architectural%';


select count(*) as "Number of rows" from draw where LocationNumber = 489 and DrawingNumber = 101;

SELECT count(*) AS "Number of results" FROM draw;

-- between and including these years, order by
SELECT draw.NewName, draw.DrawingDate
FROM draw
WHERE draw.DrawingDate BETWEEN 2017 AND 2018
AND draw.LocationNumber BETWEEN 500 AND 600
ORDER BY draw.LocationNumber, draw.DrawingDate ASC;


-- look for problem files
SELECT draw.NewName, draw.LocationNumber, draw.DrawingDate, draw.ProjectTitle
FROM draw
WHERE draw.LocationNumber BETWEEN 0 AND 9
ORDER BY draw.ProjectTitle, draw.LocationNumber ASC;
