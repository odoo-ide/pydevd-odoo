import sys
from collections import OrderedDict

from _pydevd_bundle.pydevd_extension_api import TypeResolveProvider, StrPresentationProvider
from _pydevd_bundle.pydevd_resolver import defaultResolver


class OdooRecordSetProvider(object):
    def can_provide(self, type_object, type_name):
        if self._is_odoo_type_object(type_object):
            return True
        if self._is_flectra_type_object(type_object):
            return True
        return False

    def _is_odoo_type_object(self, type_object):
        try:
            from odoo import models
            return issubclass(type_object, models.BaseModel)
        except ImportError:
            return False

    def _is_flectra_type_object(self, type_object):
        try:
            from flectra import models
            return issubclass(type_object, models.BaseModel)
        except ImportError:
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
        s = str(val)
        if len(val) == 1:
            fname = getattr(val, '_rec_name', None)
            if fname:
                name = getattr(val, fname, None)
                if name:
                    s += ' ⇨ %s' % name
        return s


if not sys.platform.startswith("java"):
    TypeResolveProvider.register(OdooRecordSetProvider)
    StrPresentationProvider.register(OdooRecordSetProvider)
