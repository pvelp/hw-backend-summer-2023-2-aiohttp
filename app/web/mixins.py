from aiohttp.abc import StreamResponse
from aiohttp.web_exceptions import HTTPUnauthorized


class AuthRequiredMixin:
    async def iter_(self) -> StreamResponse:
        if not getattr(self.request, "admin", None):
            raise HTTPUnauthorized
        return await super(AuthRequiredMixin, self).iter_()
