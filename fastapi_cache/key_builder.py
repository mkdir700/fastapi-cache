import hashlib
from typing import Any, Callable, Optional

from starlette.requests import Request
from starlette.responses import Response


def default_key_builder(
    func: Callable[..., Any],
    namespace: str = "",
    request: Optional[Request] = None,
    response: Optional[Response] = None,
    args: Optional[tuple[Any, ...]] = None,
    kwargs: Optional[dict[str, Any]] = None,
) -> str:
    from fastapi_cache import FastAPICache

    prefix = f"{FastAPICache.get_prefix()}:{namespace}:"
    cache_key = (
        prefix
        + hashlib.md5(  # nosec:B303
            f"{func.__module__}:{func.__name__}:{args}:{kwargs}".encode()
        ).hexdigest()
    )
    return cache_key
