import duckdb

result = duckdb.sql("SELECT 42 as answer").fetchall()
print(result)