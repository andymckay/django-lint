# -*- coding: utf-8 -*-
from logilab import astng

from pylint.interfaces import IASTNGChecker
from pylint.checkers import BaseChecker
from pylint.checkers.utils import safe_infer

class ViewsChecker(BaseChecker):
    __implements__ = IASTNGChecker

    name = 'django_views_checker'
    msgs = {
        'W9001': ('Not using httponly', '',),
    }

    def visit_callfunc(self, node):
        self.check_cookie(node)

    def check_cookie(self, node):
        for child in node.get_children():
            for sub in child.get_children():
                if getattr(sub, 'name', '') == 'HttpResponse':
                    httponly = False
                    for arg in node.args:
                        if isinstance(arg, astng.Keyword):
                            httponly = (arg.arg == 'httponly' and
                                        arg.value.value == True)
                    if not httponly:
                        self.add_message('W9001', node=node)
                