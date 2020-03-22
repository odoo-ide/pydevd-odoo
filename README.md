# pydevd-odoo

[PyDev.Debugger](https://github.com/fabioz/PyDev.Debugger) is the Python debugger used
in PyDev, PyCharm, VSCode. This plugin aims to make the debugger works better for Odoo.

## Odoo Recordset
[Recordsets](https://www.odoo.com/documentation/13.0/reference/orm.html#recordsets) is a fundamental concept in Odoo.
A recordset is an ordered collection of records of the same model. Trying to read a field
on multiple ids recordset will raise an error. Because PyDev.Debugger recognizes a recordset as a
non-collection object so the error will be raise when evaluating its attributes. This plugin helps
PyDev.Debugger correctly evaluate an multiple ids recordset.