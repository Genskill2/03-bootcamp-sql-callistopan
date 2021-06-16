import sqlite3
import os.path

import pytest


@pytest.fixture(scope="package")
def db():
    if os.path.exists("db.sqlite"):
        os.unlink("db.sqlite")
    f = sqlite3.connect("db.sqlite")
    c = f.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    c.close()
    return f

def run_query(dbconn, statement):
    cur = dbconn.cursor()
    cur.execute(statement)
    items = cur.fetchall()
    cur.close()
    return items

def test_create_and_insert(db):
    cur = db.cursor()
    with open("create.sql") as f:
        cur.executescript(f.read())
    cur.close()

    cur = db.cursor()
    with open("insert.sql") as f:
        cur.executescript(f.read())
    cur.close()

    items = run_query(db, "select name from publisher")
    assert set (x[0] for x in items) == set(["PHI","Harper","GCP","Avery","Del Rey","Vintage"]), "Publisher mismatch"

    items = run_query(db, "select title from books")
    assert set(x[0] for x in items) == set(["The C Programming Language","The Go Programming Language","The UNIX Programming Environment","Cryptonomicon","Deep Work","Atomic Habits","The City and The City","The Great War for Civilisation"]), "Book titles mismatch"

    items = run_query(db, "select name from subjects")  
    assert set(x[0] for x in items) == set(["C","UNIX","Technology","Science Fiction","Productivity","Psychology","Politics","History","Go"]), "Subjects mismatch"


def test_run_query1(db):
    with open("query1.sql") as f:
        query = f.read()
        items = run_query(db, query)
    assert set(x[0] for x in items) == set(["The C Programming Language", "The Go Programming Language", "The UNIX Programming Environment"])

def test_run_query2(db):
    with open("query2.sql") as f:
        query = f.read()
        items = run_query(db, query)
    expected = set([("The City and The City", "Del Rey"),
                    ("The Great War for Civilisation","Vintage")])

    assert set(items) == expected

    
def test_run_query3(db):
    with open("query3.sql") as f:
        query = f.read()
        items = run_query(db, query)
    expected = set(['The C Programming Language', 'The Go Programming Language', 'The UNIX Programming Environment', 'Cryptonomicon', 'Deep Work', 'The City and The City', 'The Great War for Civilisation'])

    assert set(x[0] for x in items) == expected

def test_run_query4(db):
    with open("query4.sql") as f:
        query = f.read()
        items = run_query(db, query)
    expected = set(["Productivity", "Psychology"])
    assert set(x[0] for x in items) == expected

def test_run_update1(db):
    cur = db.cursor()
    with open("update1.sql") as f:
        cur.executescript(f.read())
    cur.close()

    items = run_query(db, "select name from publisher")
    assert set (x[0] for x in items) == set(["Prentice Hall","Harper","GCP","Avery","Del Rey","Vintage"]), "Publisher mismatch"
    
def test_run_delete(db):
    cur = db.cursor()
    with open("delete1.sql") as f:
        cur.executescript(f.read())
    cur.close()

    items = run_query(db, "select s.name from books b, subjects s, books_subjects bs where b.id = bs.book and s.id = bs.subject and b.title = 'The Great War for Civilisation'");
    expected = set(["Politics"])
    assert set(x[0] for x in items) == expected

    items = run_query(db, "select name from subjects")  
    assert set(x[0] for x in items) == set(["C","UNIX","Technology","Science Fiction","Productivity","Psychology","Politics","Go"]), "Subjects mismatch"

    
