import csv
from fastapi.responses import StreamingResponse
from io import StringIO
from fastapi import APIRouter

router=APIRouter(
    prefix="/csv",
    tags=["EXPORT"]
)


@router.get("/")
def export_csv():

    output=StringIO()
    writer=csv.writer(output)

    writer.writerow(["ID","NAME","AGE"])
    writer.writerow(["1","Krushna","23"])
    writer.writerow(["2","Rutuja","22"])


    output.seek(0)


    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition":"attachment; filename=users.csv"
        }
    )