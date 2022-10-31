from typing import Set
import dotenv

import pydantic

dotenv.load_dotenv()


class AuthorizationConfig(pydantic.BaseSettings):
    realms: Set[str] = pydantic.Field(set(), env="AUTHORIZATION_REALMS")
    issuers: Set[pydantic.AnyHttpUrl] = pydantic.Field(
        set(), env="AUTHORIZATION_ISSUERS"
    )
    audience: str = pydantic.Field("urn:eric.smaxwill:postbox", env="AUTHORIZATION_AUDIENCE")


class Config(pydantic.BaseSettings):
    # The env this is running in
    ENVIRONMENT: str

    DISABLE_SECURITY: bool = False

    # Dynamo Table Name from Env Vars
    DYNAMODB_TABLE_NAME: str

    # Anything here forwards to the boto sdks
    CLIENT_EXTRA: dict = {}

    S3_BUCKET_NAME: str

    SENTRY_DSN: pydantic.AnyUrl
    SENTRY_RELEASE: str

    DELETE_AFTER_FORWARDING: bool = True

    VERIFIED_SENDER: pydantic.EmailStr = pydantic.EmailStr(
        "forwarder@postbox.smaxwill.com"
    )

    authorization: AuthorizationConfig = AuthorizationConfig()  # type: ignore


_default_authorization = AuthorizationConfig(
    realms={"devportal"},
    issuers={"https://passport.smaxwill.com/devportal"}, # type: ignore
    audience="urn:eric.smaxwill:postbox",
)

settings = Config(authorization=_default_authorization)  # type: ignore
