import psycopg2

dbname = 'tuiizpof'
user = 'tuiizpof'  # ElephantSQL happens to use same name for db and user
password = "wouldn'tyouliketoknow"  # Sensitive! Don't share/commit
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_conn

pg_curs = pg_conn.cursor()

create_table_statement = """
CREATE TABLE test_table (
    id SERIAL PRIMARY KEY,
    name varchar(40) NOT NULL,
    data JSONB
);
"""

pg_curs.execute(create_table_statement)
pg_conn.commit()

pg_curs.execute('SELECT * FROM test_table;')
pg_curs.fetchall()

insert_statement = """
INSERT INTO test_table (name, data) VALUES
(
  'Zaphod Beeblebrox',
  '{"key": "value", "key2": true}'::JSONB
)
"""

pg_curs.execute(insert_statement)
pg_conn.commit()

pg_curs.execute('SELECT * FROM test_table;')
pg_curs.fetchall()

pg_curs.close()