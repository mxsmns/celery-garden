from celery_garden import foo


def test_bar() -> None:
    assert foo.bar() == 5
