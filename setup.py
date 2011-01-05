#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-lint -- Static analysis tool for Django projects and applications
# Copyright (C) 2008-2009 Chris Lamb <chris@chris-lamb.co.uk>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

setup_args = dict(
    name='django_lint',
    packages=[
        'DjangoLint',
        'DjangoLint.AstCheckers',
    ],
    author='Chris Lamb',
    author_email='chris@chris-lamb.co.uk',
)

try:
    from setuptools import setup
    setup_args['entry_points'] = {
        "console_scripts" : ['django-lint = DjangoLint.script:main',]
    }
except ImportError:
    from distutils.core import setup
    setup_args['scripts']=['django-lint',]

setup(**setup_args)
