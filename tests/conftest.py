def pytest_configure():
    from django.conf import settings

    settings.configure(
        DEBUG_PROPAGATE_EXCEPTIONS=True,
        DATABASES={
            "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
        },
        SECRET_KEY="not important here",
        ROOT_URLCONF="tests.main_urls",
        MIDDLEWARE=(
            "django.middleware.common.CommonMiddleware",
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
        ),
        INSTALLED_APPS=(
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "tests",
            "rest_framework",
        ),
        PASSWORD_HASHERS=("django.contrib.auth.hashers.MD5PasswordHasher",),
        REST_FRAMEWORK={
            "EXCEPTION_HANDLER": "rest_framework_friendly_errors.handlers."
            "friendly_exception_handler"
        },
        LANGUAGE_CODE="pl",
    )

    try:
        import django

        django.setup()
    except AttributeError:
        pass
