from pydantic import BaseModel

class ImageResponse(BaseModel):
    id: int
    filename: str
    content_type: str
