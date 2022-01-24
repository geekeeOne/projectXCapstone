import django_filters
from . models import PRAASA_March2020


class PraasaFilter(django_filters.FilterSet):

	class Meta:
		model = PRAASA_March2020
		fields = {'last_name': ['icontains'],
					'phone': ['icontains'],
					'email': ['icontains'],
					# 'arrival_date': ['icontains'],
					# 'arrival_time':['icontains'],
					# 'arrival_flight':['icontains'],
					}


