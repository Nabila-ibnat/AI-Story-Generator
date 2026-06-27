from pydantic import BaseModel, Field


class StoryRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_length=5,
        max_length=500,
        example="A lonely robot discovers a hidden forest.",
        description="A one-line prompt to generate a story from.",
    )


class StoryResponse(BaseModel):
    success: bool
    story: str


class ErrorResponse(BaseModel):
    success: bool = False
    error: str
