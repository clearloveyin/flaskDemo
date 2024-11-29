from .schema import DemoSchema
from backend.lib.base import BaseResource, error_interceptor


class DemoApi(BaseResource):
    get_schema = DemoSchema

    @error_interceptor
    async def get(self, data: DemoSchema):
        _id = data.id
        name = data.name
        result = {"id": _id, "name": name}
        return self.done(result)
