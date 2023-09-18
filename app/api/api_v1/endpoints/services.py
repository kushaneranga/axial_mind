from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from app.controllers import ParagraphStructure

router = APIRouter(
    prefix="/services",
    tags=["services"],
    responses={404: {"description": "Not in AxialMind Url"}},
)


class ParagraphRequest(BaseModel):
    paragraph: str
    options: List[int]


class ParagraphResponse(BaseModel):
    processed_paragraph: str


@router.post("/manipulate-paragraph", response_model=ParagraphResponse, status_code=201)
async def manipulate_paragraph(data: ParagraphRequest):
    paragraph_obj = ParagraphStructure(data.paragraph)
    match (data.options):
        case 0:
            paragraph_obj.capitalize_first_letter()
    return {"processed_paragraph": paragraph_obj.paragraph}
