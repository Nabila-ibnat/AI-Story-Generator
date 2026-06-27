from fastapi import APIRouter, HTTPException
from app.Story.story_schema import StoryRequest, StoryResponse, ErrorResponse
from app.Story.openai_service import generate_story

router = APIRouter()


@router.post(
    "/generate",
    response_model=StoryResponse,
    responses={500: {"model": ErrorResponse}},
    summary="Generate a story from a prompt",
    description="Accepts a one-line prompt and returns a complete AI-generated story.",
)
async def generate_story_endpoint(request: StoryRequest):
    """
    Generate a creative story based on the provided prompt.

    - **prompt**: A one-line text prompt (5–500 characters)
    """
    try:
        story = await generate_story(request.prompt)
        return StoryResponse(success=True, story=story)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"success": False, "error": str(e)},
        )
