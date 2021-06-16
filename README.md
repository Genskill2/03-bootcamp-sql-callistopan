# Introduction

This exercise consists of 3 parts to test multiple aspects of
SQL. Each one will require you to write a separate SQL file. It will
be evaluated using sqlite so please use sqlite types and syntax.

# Exercises
## Table creation

Create a file called `create.sql` which contains SQL code to do the following

*publisher*

     | id          | name | country |
     | primary key | text | text    |

*books*

     | id          | title | publisher                   |
     | primary key | text  | foreign key to publisher.id |

*subjects*

     | id          | name |
     | primary key | text |

*books_subjects*

    | book                    | subject                    |
    | foreign key to books.id | foreign key to subjects.id |

## Insertion
Create a file called `insert.sql` which contains SQL code to do the following.

Insert the following information into the tables. These will have to
be inserted into multiple tables. The information below is the
combined info. Please pay attention to capitalisation, punctuation and
spelling. Subjects is a comma separated list. You have to enter each
subject separately into the `subjects` table and then create the many to
many mappings using the `books_subjects` table.

| Book name                        | Publisher | Subjects                    |
|----------------------------------|-----------|-----------------------------|
| The C Programming Language       | PHI       | C, UNIX, Technology         |
| The Go Programming Language      | PHI       | Go, Technology              |
| The UNIX Programming Environment | PHI       | UNIX, Technology            |
| Cryptonomicon                    | Harper    | Technology, Science Fiction |
| Deep Work                        | GCP       | Technology, Productivity    |
| Atomic Habits                    | Avery     | Productivity, Psychology    |
| The City and The City            | Del Rey   | Science Fiction, Politics   |
| The Great War for Civilisation   | Vintage   | Politics, History           |

The publisher countries are as follows

| Publisher     | Country |
|---------------|---------|
| PHI           | India   |
| Harper        | USA     |
| GCP           | USA     |
| Avery         | USA     |
| Del Rey       | UK      |
| Vintage       | UK      |

## Querying
### All books by PHI
Creating a file called `query1.sql` which will contain a query that
will print the names of all books by published by PHI.

### All books published by UK publishers
Creating a file called `query2.sql` which will contain a query that
will print the names and publishers of all books by published by
publishers in the UK

### All books on Technology or Politics
Creating a file called `query3.sql` which will contain a query that
will print the names of all the books on "Technology" or
"Politics". (*hint* consider using the IN condition in your where clause).

### All books on Technology
Create a file called `query4.sql` which will contain a query that will
print all the subjects of the book with name "Atomic Habits".


## Updating
### Change PHI to Prentice Hall
Write a file called `update1.sql` which will contain a SQL statement to change the name of the publisher PHI to "Prentice Hall"

## Deleting
### Delete all Science Fiction
Write a file called `delete1.sql` that contains a SQL statement to
delete the subject 'History'. The subject must be removed from the
tables and from all the books. You will need two
queries for this. First to delete all the history mappings in the
`books_subjects` table. Then to delete the subject itself. To do the
former, you can use subqueries (e.g. delete from books_subject where
id in (...))




