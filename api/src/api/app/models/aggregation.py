# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from app.models.tag import Tag

from pydantic import AnyUrl, EmailStr, Field, validator  # noqa: F401
from app.models.compartment_aggregation import CompartmentAggregation


class Aggregation(CompartmentAggregation):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Aggregation - a model defined in OpenAPI

        name: The name of this Aggregation [Optional].
        description: The description of this Aggregation [Optional].
        tags: The tags of this Aggregation [Optional].
        id: The id of this Aggregation.
    """

    id: str = Field(alias="id")
    name: Optional[str] = Field(alias="name", default=None)
    description: Optional[str] = Field(alias="description", default=None)
    tags: Optional[List[Tag]] = Field(alias="tags", default=None)

Aggregation.update_forward_refs()
