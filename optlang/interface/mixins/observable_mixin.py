# -*- coding: utf-8 -*-

# Copyright 2017 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

from weakref import proxy

__all__ = ("ObservableMixin",)


class ObservableMixin(object):
    """
    Provide a method to set an observable on an inheriting class.

    Trying to access methods of the observable may raise an
    ``AttributeError`` if it is not set (``None``) or a ``ReferenceError`` if
    the observable no longer exists.

    """

    def __init__(self, **kwargs):
        super(ObservableMixin, self).__init__(**kwargs)
        self._observable = None

    def set_observable(self, observable):
        """Set the instance's observable."""
        self._observable = proxy(observable)
