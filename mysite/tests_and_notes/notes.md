https://djangobook.com/django-forms/


`sqlite3`

<!-- create a new db -->
`sqlite3 drawings.db`

`.open db.sqlite3`

CREATE TABLE `draw` (
  `ID` int(11) NOT NULL,
  `OldName` varchar(255) DEFAULT NULL,
  `NewName` varchar(255) DEFAULT NULL,
  `LocationNumber` int(11) DEFAULT NULL,
  `DrawingNumber` int(11) DEFAULT NULL,
  `ProjectTitle` varchar(255) DEFAULT NULL,
  `ProjectNumber` varchar(255) DEFAULT NULL,
  `DrawingDate` year(4) DEFAULT NULL,
  `SheetTitle` varchar(255) DEFAULT NULL,
  `SheetNumber` varchar(255) DEFAULT NULL,
  `Discipline` varchar(255) DEFAULT NULL,
  `DrawingVersion` varchar(255) DEFAULT NULL,
  `Notes` varchar(255) DEFAULT NULL,
  `PhysicalLocation` varchar(255) DEFAULT NULL
);

`.tables`

`.schema draw`
`.schema drawsearch_search`

`.mode csv`

`.import data/draw.csv draw`
`.import ../data/draw.csv drawsearch_search`

select count(*) as "Number of rows" from drawsearch_search;

select NewName from draw where LocationNumber = 525 and DrawingNumber = 101 and Discipline like '%arch%';


select count(*) as "Number of rows"
from draw
where LocationNumber = 525 and DrawingNumber = 101 and Discipline like '%architectural%';


select count(*) as "Number of rows" from draw where LocationNumber = 489 and DrawingNumber = 101;

`drop table draw;`


# Paul's quick django notes

-`django-admin startproject mysite`

-`python manage.py runserver`

-`python manage.py startapp polls`

-`python manage.py makemigrations polls`

-`python manage.py migrate`



-`python manage.py shell`

- `pip install django-crispy-forms` then make changes in settings