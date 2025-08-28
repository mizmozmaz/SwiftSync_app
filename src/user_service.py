def get_user_email(user_id: int) -> str:
    """Returns a user's email. Edge case: user_id is None."""
    if user_id is None:
        raise ValueError("user_id cannot be None")
    return f"user_{user_id}@example.com"