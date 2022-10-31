from datetime import datetime
import typing

import pydantic


class AntispamSettings(pydantic.BaseModel):
    check_spam: bool = True
    check_av: bool = True
    check_spf: bool = True
    check_dkim: bool = True
    check_dmarc: bool = False


class Postbox(pydantic.BaseModel, validate_all=True, validate_assignment=True):
    enabled: bool = True
    created_at: datetime = pydantic.Field(default_factory=datetime.utcnow)

    forwarding_to: typing.Set[pydantic.EmailStr] = set()
    allowed_senders: typing.Set[pydantic.EmailStr] = set()
    expires_at: typing.Optional[datetime] = None

    spam_settings: AntispamSettings = AntispamSettings()

    @property
    def expires(self) -> bool:
        """
        Does the postbox expire?
        :return: True if the postbox ever expires, False if it does not.
        """
        return False if self.expires_at is None else True

    @property
    def is_expired(self) -> bool:
        """
        Is the Postbox currently expired?
        :return: True if the current time is greater than the expiration date
        """
        if not self.expires:
            return False

        # expires_at can be None, but that case is covered by the `expires` call above
        return datetime.utcnow() > self.expires_at  # type: ignore
