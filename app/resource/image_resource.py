import importlib
from .. import cache
from app.core.utils import api_key_required
from flask_restful import Resource


class Image(Resource):
    @api_key_required
    @cache.cached()
    def get(self, name, limit):
        module = importlib.import_module(f"app.core.providers.{name}")
        module = getattr(module, name.title())
        provider = module()
        return provider.get(limit)
