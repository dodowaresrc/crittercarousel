import json
from typing import Any

from fastapi.responses import JSONResponse


class FormattedJSONResponse(JSONResponse):

     def render(self, content:Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            sort_keys=True
        ).encode("utf-8")
