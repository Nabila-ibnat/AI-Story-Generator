def build_story_prompt(user_prompt: str) -> tuple[str, str]:
    """
    Build a structured system + user message pair for story generation.

    Returns:
        (system_message, user_message)
    """
    system_message = (
        "You are a world-class creative fiction writer. "
        "When given a short prompt, you write a complete, engaging, and well-structured story. "
        "Your stories have a clear beginning, middle, and end. "
        "They include vivid descriptions, compelling characters, and meaningful themes. "
        "Write in a rich narrative style suitable for all ages unless the prompt implies otherwise. "
        "Do not include any meta-commentary — output the story text only."
    )

    user_message = (
        f"Write a complete short story based on the following prompt:\n\n"
        f"\"{user_prompt}\"\n\n"
        f"The story should be engaging, creative, and between 300–600 words."
    )

    return system_message, user_message
