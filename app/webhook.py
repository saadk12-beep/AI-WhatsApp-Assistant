from fastapi import APIRouter, Request

router = APIRouter(prefix="/webhook", tags=["Periskope"])


@router.post("/periskope")
async def receive_message(request: Request):

    payload = await request.json()

    print("\n==========================")
    print("NEW PERISKOPE WEBHOOK")
    print("==========================")
    print(payload)
    print("==========================\n")

    return {
        "success": True
    }