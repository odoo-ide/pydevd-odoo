import sys
from collections import OrderedDict

from _pydevd_bundle.pydevd_extension_api import TypeResolveProvider, StrPresentationProvider
from _pydevd_bundle.pydevd_resolver import defaultResolver


class OdooRecordSetProvider(object):
    def can_provide(self, type_object, type_name):
        try:
            from odoo import models
            return isinstance(type_object, models.MetaModel)
        except:
            return False

    def resolve(self, obj, attr):
        try:
            _id = int(attr)
        except:
            return getattr(obj, attr)
        else:
            return obj[_id]

    def get_dictionary(self, obj):
        if len(obj) > 1:
            d = OrderedDict()
            for idx, r in enumerate(obj):
                d[str(idx)] = r
            return d
        return defaultResolver.get_dictionary(obj)

    def get_str(self, val):
        s = str(val.ids)
        if len(val) == 1:
            name = getattr(val, 'name', None)
            if name:
                s += ' ⇨ %s' % name
        return s


if not sys.platform.startswith("java"):
    TypeResolveProvider.register(OdooRecordSetProvider)
    StrPresentationProvider.register(OdooRecordSetProvider)
