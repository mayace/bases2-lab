from os import environ

SQLS_DRIVER = environ.get("SQLS_DRIVER", "SQL Server")
SQLS_HOST = environ.get("SQLS_HOST", "localhost\\SQLEXPRESS")
SQLS_DB = environ.get("SQLS_DB")
SQLS_USER = environ.get("SQLS_USER")
SQLS_PASS = environ.get("SQLS_PASS")


MONGO_HOST = environ.get("MONGO_HOST")
MONGO_PORT = environ.get("MONGO_PORT", 27017)
MONGO_DB = environ.get("MONGO_DB")


MONGODB_SETTINGS = {
    "db": MONGO_DB, "host": MONGO_HOST, "port": int(MONGO_PORT),
}

SQLS_CONN_STR = "Driver={};Server={};Database={};UID={};PWD={};".format(SQLS_DRIVER,
                                                                        SQLS_HOST, SQLS_DB, SQLS_USER, SQLS_PASS,)
