import os

# import sentry_sdk
# from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from mangum import Mangum

from postbox.config import settings

if settings.SENTRY_DSN is not None:
    release_version = os.getenv("SENTRY_RELEASE", None)
    if release_version:
        release = f"postbox@{release_version}"
    else:
        release = "postbox@local"

    # sentry_sdk.init(
    #     dsn=settings.SENTRY_DSN,
    #     environment=settings.ENVIRONMENT,
    #     traces_sample_rate=1,
    #     release=release,
    # )
    from postbox.app import create_app

    # asgi_handler = Mangum(SentryAsgiMiddleware(app), lifespan="off")
else:
    from postbox.app import create_app

    asgi_handler = Mangum(create_app(), lifespan="off")


def handler(event, context):
    try:
        response = asgi_handler(event, context)
        return response
    except Exception as e:
        # sentry_sdk.capture_exception(e)
        print(e)
        return {"statusCode": 500, "body": str(e)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "postbox.app:create_app", host="127.0.0.1", port=8000, reload=True, factory=True
    )
