from pydantic.version import VERSION as PYDANTIC_VERSION

PYDANTIC_V2 = PYDANTIC_VERSION.startswith("2.")

if not PYDANTIC_V2:
    from pydantic import BaseModel, BaseSettings, Extra, Field, PrivateAttr, SecretStr

    BaseModel = BaseModel
    BaseSettings = BaseSettings
    Field = Field
    SecretStr = SecretStr
    Extra = Extra
    PrivateAttr = PrivateAttr
