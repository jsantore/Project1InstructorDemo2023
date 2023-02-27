import getData
import DatabaseStuff


def test_get_data():
    """for this test we are just getting the data from wufoo, getting the Entries and counting them"""
    json_data = getData.get_wufoo_data()
    entries = json_data["Entries"]
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


def test_data_inserted():
    # if I had covered fixtures, I would used them for the database setup,
    # since I have not I'll do it manually
    connection, cursor = DatabaseStuff.open_db("test.db")
    DatabaseStuff.create_entries_table(cursor)
    test_entry = {
        "EntryId": "11",
        "Field2": "Dr.",
        "Field3": "Pallavi",
        "Field4": "Mathew",
        "Field6": "Software Eng -MTS",
        "Field7": "AMD",
        "Field8": "pallavi@amd.com",
        "Field9": "",
        "Field11": "Course Project",
        "Field12": "",
        "Field13": "",
        "Field14": "",
        "Field15": "",
        "Field16": "",
        "Field17": "",
        "Field113": "Philosophy",
        "Field112": "Create an situation where you and your husband work for arch-rivals AMD and intel so you can't ever talk about work at home between the two of you, but on the other hand, you don't have to worry about both of you being laid off at the same time.",
        "Field115": "Yes",
        "DateCreated": "2023-02-10 08:15:49",
        "CreatedBy": "public",
        "DateUpdated": "",
        "UpdatedBy": None,
    }
    # this is the 'function under test'
    DatabaseStuff.add_entries_to_db(cursor, [test_entry])
    # let's see if it went into
    cursor.execute("SELECT first_name, org, course_project FROM WuFooData WHERE entryID = 11")
    record = cursor.fetchone()
    assert record[0] == "Pallavi"
    assert record[1] == "AMD"
    assert record[2] == "Course Project"
