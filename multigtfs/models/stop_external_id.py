#
# Copyright 2018 Jakub Dorňák
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
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from jsonfield import JSONField

from multigtfs.models.base import models, Base
from multigtfs.models.stop import Stop


@python_2_unicode_compatible
class StopExternalId(Base):
    """An External Id of the stop.

    This implements stop_external_ids.txt in the GTFS feed.
    """
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    external_type = models.CharField(
        max_length=255, blank=True,
        help_text="Type of the external id")
    external_id = models.CharField(
        max_length=255, blank=True,
        help_text="Value of the external id")
    extra_data = JSONField(default={}, blank=True, null=True)

    def __str__(self):
        return "%s-%s-%s" % (self.stop, self.external_type, self.external_id)

    class Meta:
        db_table = 'stop_external_id'
        app_label = 'multigtfs'

    _column_map = (
        ('stop_id', 'stop__stop_id'),
        ('type', 'external_type'),
        ('id', 'external_id'),
    )
    _filename = 'stop_external_ids.txt'
    _rel_to_feed = 'stop__feed'
    _sort_order = ('stop__stop_id', 'external_type')
    _unique_fields = ('stop_id', 'type')
