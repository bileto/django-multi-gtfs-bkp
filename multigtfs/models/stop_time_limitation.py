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
from multigtfs.models.trip import Trip


@python_2_unicode_compatible
class StopTimeLimitation(Base):
    """An Limitation of the stop.

    This implements stop_time_limitations.txt in the GTFS feed.
    """
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    group_id = models.IntegerField()
    extra_data = JSONField(default={}, blank=True, null=True)

    def __str__(self):
        return "%s-%s-%s" % (self.trip, self.stop.stop_id, self.group_id)

    class Meta:
        db_table = 'stop_time_limitation'
        app_label = 'multigtfs'

    _column_map = (
        ('trip_id', 'trip__trip_id'),
        ('stop_id', 'stop__stop_id'),
        ('group_id', 'group_id'),
    )
    _filename = 'stop_time_limitations.txt'
    _rel_to_feed = 'trip__route__feed'
    _sort_order = ('trip__trip_id', 'group_id')
    _unique_fields = ('trip_id', 'stop_id', 'group_id')
