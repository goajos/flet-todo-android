from typing import Optional

from pydantic import BaseModel, ConfigDict


class Schema(BaseModel):
    id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)
