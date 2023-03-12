import json
import os
from typing import Any

from fastapi.responses import JSONResponse


class FormattedJSONResponse(JSONResponse):

     def render(self, content:Any) -> bytes:

        string_response = json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            sort_keys=True
        ) + os.linesep

        return string_response.encode("UTF-8")
