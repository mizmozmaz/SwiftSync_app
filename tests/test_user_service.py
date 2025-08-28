import pytest
from src.user_service import get_user_name
from src.user_service import get_user_name, get_user_email

def test_get_user_name():
    assert get_user_name(1) == "User_1"
    # Missing: Test for `user_id=None` (edge case).github/PULL_REQUEST_TEMPLATE.m

def test_get_user_email():
    assert get_user_email(1) == "user_1@example.com"
    # Missing: Test for None case
