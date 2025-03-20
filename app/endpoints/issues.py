from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def report_issue(issue: dict):
    """
    Dummy endpoint for reporting user issues.
    """
    # Logic to process the issue (store in DB, notify support, etc.)
    return {"message": "Issue reported successfully.", "issue": issue}
