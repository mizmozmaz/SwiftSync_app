def get_user_name(user_id: int | None) -> str:
    """Returns a user's name. Edge case: user_id is None."""
    if user_id is None:
        raise ValueError("user_id cannot be None")
    return f"User_{user_id}"  # Mock logic