from fastapi import FastAPI, Path, status
from fastapi.responses import JSONResponse
from main import db_name
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
from serverDB import CubesDB


# original tutorial https://eliran9692.medium.com/build-an-application-with-fastapi-from-scratch-9654e0e4476f
# modified here to work with sprint2 needs


def api_reply(data):
    if not data:
        return JSONResponse(
            {"message": "No Cubes Data Found"}, status_code=HTTP_404_NOT_FOUND
        )
    result = prepare_result(data)
    return JSONResponse(result, status_code=HTTP_200_OK)


def prepare_result(data):
    if not isinstance(data, list):
        data = [data]
    result = []
    for location, entry in enumerate(data):
        result.append(
            {
                "entryID": entry[0],
                "prefix": entry[1],
                "first_name": entry[2],
                "last_name": entry[3],
                "title": entry[4],
                "org": entry[5],
                "email": entry[6],
                "website": entry[7],
                "course_project": True
                if len(entry[8]) > 0
                else False,  # inline if to assign true if the string was not ''
                "guest_speaker": True if len(entry[9]) > 0 else False,
                "site_visit": True if len(entry[10]) > 0 else False,
                "job_shadow": True if len(entry[11]) > 0 else False,
                "internship": True if len(entry[12]) > 0 else False,
                "career_panel": True if len(entry[13]) > 0 else False,
                "networking_event": True if len(entry[14]) > 0 else False,
                "subject_area": entry[15],
                "description": entry[16],
                "funding": entry[17],
                "created_date": entry[18],
            }
        )
    return result


def get_cubes_data_from_db() -> list:
    with CubesDB(db_name) as cursor:
        cursor.execute("""SELECT * FROM WuFooData""")
        return cursor.fetchall()


app = FastAPI()
cubes_database = CubesDB(db_name)


@app.get("/")
def root():
    data_from_db = get_cubes_data_from_db()
    display_data = api_reply(data_from_db)
    return display_data
