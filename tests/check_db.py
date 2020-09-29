import psycopg2
from django.conf import settings


def test_db_exists():
    connection = psycopg2.connect(
        f"user='{settings.DATABASES['default']['USER']}' "
        f"host='{settings.DATABASES['default']['HOST']}' password='{settings.DATABASES['default']['PASSWORD']}' "
        f"port={settings.DATABASES['default']['PORT']}'"
    )
    if connection is not None:
        connection.autocommit = True

        cur = connection.cursor()

        cur.execute("SELECT datname FROM pg_database;")

        list_database = cur.fetchall()

        assert (settings.DATABASES['default']['NAME'], ) in list_database
