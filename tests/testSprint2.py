import getData
import DatabaseStuff


def test_get_data():
    """ for this test we are just getting the data from wufoo, getting the Entries and counting them"""
    json_data = getData.get_wufoo_data()
    entries = json_data['Entries']
    assert len(entries) >= 10


def test_table_created():
    """There were several ways to do this, some of them include wrapping inserts in try/except blocks
    but I took an easy way and just check to make sure my table is in the meta deable sqlite_master"""
    connection, cursor = DatabaseStuff.open_db("test.db")
    DatabaseStuff.create_entries_table(cursor)
    cursor.execute("SELECT Count() FROM SQLITE_MASTER WHERE name = ?", ["WuFooData"])
    record = cursor.fetchone()
    number_of_rows = record[0]  # the number is the first )and only) item in the tuple
    assert number_of_rows == 1
