import psycopg_pool


pgpool = psycopg_pool.AsyncConnectionPool(
    """
    dbname=wishstore_db
    user=postgres
    host=localhost
    port=5432
    """
)
