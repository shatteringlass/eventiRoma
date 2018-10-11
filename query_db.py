#!/usr/bin/env python3

def fetch(db, sql):
    import sqlite3 as sl3

    conn = sl3.connect(db)
    c = conn.cursor()

    c.execute(sql)

    return c
