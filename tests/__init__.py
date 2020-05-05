# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

try:
    from trytond.modules.tryton_submodule.tests.test_tryton_submodule import suite  # noqa: E501
except ImportError:
    from .test_tryton_submodule import suite

__all__ = ['suite']
