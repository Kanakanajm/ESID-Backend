# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class MovementData(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    MovementData - a model defined in OpenAPI

        cell: The cell of this MovementData [Optional].
        incoming: The incoming of this MovementData [Optional].
        outgoing: The outgoing of this MovementData [Optional].
        timestamp: The timestamp of this MovementData [Optional].
    """

    cell: Optional[str] = Field(alias="cell", default=None)
    incoming: Optional[float] = Field(alias="incoming", default=None)
    outgoing: Optional[float] = Field(alias="outgoing", default=None)
    timestamp: Optional[str] = Field(alias="timestamp", default=None)

MovementData.update_forward_refs()
