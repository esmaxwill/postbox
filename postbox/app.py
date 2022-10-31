import fastapi
from fastapi.encoders import jsonable_encoder


def create_app():
    app = fastapi.FastAPI(title="Postbox", description="Email forwarding as a service")
    # app.include_router(oidc_router)
    # app.include_router(route_router)
    # app.include_router(client_router)
    # app.include_router(orcapi_router)
    # app.include_router(tex_router)

    # app.add_exception_handler(
    #     fastapi.exceptions.RequestValidationError, validation_exception_handler
    # )
    # app.add_exception_handler(OidcError, oidc_exception_handler)

    # return SentryAsgiMiddleware(app)
    return app
