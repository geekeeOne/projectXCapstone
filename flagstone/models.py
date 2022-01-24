from __future__ import unicode_literals
from django.db.models import Count, F, Value
from django.db.models.functions import Length, Upper
from django.contrib.auth.models import User
from django.urls import reverse
from Adobe_ProjectX import settings
from datetime import datetime
from django.db import models
import pytz

############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
## Faux Model used to load a ListView importing rental_list & shuttle_list to allow FE access to db-CRUD access
class SplashPage(models.Model):
	rogerDodger = models.CharField(max_length=1, default='o')


class CustomerCARF(models.Model):

	arrival_flight_list = (('SW-0364 (DEN)', 'SW-0364 (DEN)'), 
							('UN-0440 (DEN)', 'UN-0440 (DEN)'), 
							('AL-0648 (SEA)', 'AL-0648 (SEA)'),
							('AA-0649 (DFW)', 'AA-0649 (DFW)'), 
							('SC-0663 (LAS)', 'SC-0663 (LAS)'),
							('DL-0780 (SEA)', 'DL-0780 (SEA)'), 
							('AA-1097 (DFW)', 'AA-1097 (DFW)'), 
							('AA-1162 (ORD)', 'AA-1162 (ORD)'), 
							('AA-1207 (DFW)', 'AA-1207 (DFW)'), 
							('SW-1350 (SAN)', 'SW-1350 (SAN)'), 
							('AA-1441 (DFW)', 'AA-1441 (DFW)'), 
							('SW-1488 (MKE-SJC)', 'SW-1488 (MKE-SJC)'),
							('SW-1506 (LAX)', 'SW-1506 (LAX)'),
							('SW-1546 (LBB-DEN)', 'SW-1546 (LBB-DEN)'), 
							('DL-1739 (ATL)', 'DL-1739 (ATL)'), 
							('SW-1948 (OAK-LAX)', 'SW-1948 (OAK-LAX)'), 
							('AL-1996 (SEA)', 'AL-1996 (SEA)'), 
							('AA-1998 (DFW)', 'AA-1998 (DFW)'), 
							('AA-2003 (PHX)', 'AA-2003 (PHX)'), 
							('AA-2017 (PHX)', 'AA-2017 (PHX)'), 
							('UN-2034 (ORD)', 'UN-2034 (ORD)'), 
							('AA-2228 (ORD)', 'AA-2228 (ORD)'), 
							('SW-2430 (SAN)', 'SW-2430 (SAN)'), 
							('SW-2467 (MDW)', 'SW-2467 (MDW)'), 
							('SW-2603 (SLC-LAX)', 'SW-2603 (SLC-LAX)'),
							('AA-2710 (DFW)', 'AA-2710 (DFW)'),
							('DL-2714 (MSP)', 'DL-2714 (MSP)'), 
							('AA-2732 (PHX)', 'AA-2732 (PHX)'),  
							('DL-2789 (ATL)', 'DL-2789 (ATL)'), 
							('AA-2824 (DFW)', 'AA-2824 (DFW)'), 
							('AA-3046 (LAX)', 'AA-3046 (LAX)'),
							('AL-3437 (PDX)', 'AL-3437 (PDX)'), 
							('AL-3446 (PDX)', 'AL-3446 (PDX)'), 
							('DL-3589 (LAX)', 'DL-3589 (LAX)'), 
							('DL-3803 (SLC)', 'DL-3803 (SLC)'), 
							('DL-3880 (LAX)', 'DL-3880 (LAX)'), 
							('DL-3989 (LAX)', 'DL-3989 (LAX)'), 
							('SW-4112 (SNA-LAS)', 'SW-4112 (SNA-LAS)'),  
							('SW-4183 (ONT-LAX)', 'SW-4183 (ONT-LAX)'), 
							('DL-4545 (SLC)', 'DL-4545 (SLC)'), 
							('UN-4659 (DEN)', 'UN-4659 (DEN)'), 
							('UN-5307 (DEN)', 'UN-5307 (DEN)'),
							('UN-5396 (SFO)', 'UN-5396 (SFO)'), 
							('UN-5487 (IAH)', 'UN-5487 (IAH)'), 
							('UN-5527 (SF0)', 'UN-5527 (SF0)'),
							('UN-5572 (DEN)', 'UN-5572 (DEN)'), 
							('UN-5678 (DEN)', 'UN-5678 (DEN)'), 
							('AA-5737 (PHX)', 'AA-5737 (PHX)'), 
							('UN-5802 (SFO)', 'UN-5802 (SFO)'), 
							('AA-5820 (PHX)', 'AA-5820 (PHX)'), 
							('AA-5826 (PHX)', 'AA-5826 (PHX)'), 
							('AA-5870 (PHX)', 'AA-5870 (PHX)'), 
							('UN-5887 (SFO)', 'UN-5887 (SFO)'), 
							('AA-6063 (LAX)', 'AA-6063 (LAX)'), 
							('UN-6100 (IAH)', 'UN-6100 (IAH)'), 
							('UN-6121 (IAH)', 'UN-6121 (IAH)'), 
							('UN-6177 (IAH)', 'UN-6177 (IAH)'), 
							('UN-6215 (IAH)', 'UN-6215 (IAH)'), )


	departing_flight_list = (('SW-2595 (SAN)', 'SW-2595 (SAN)'), 
							('SW-2057 (DEN)', 'SW-2057 (DEN)'), 
							('SW-1948 (LAS)', 'SW-1948 (LAS)'), 
							('SW-2467 (LAX)', 'SW-2467 (LAX)'), 
							('SW-2394 (SJC)', 'SW-2394 (SJC)'), 
							('SW-2603 (DEN)', 'SW-2603 (DEN)'), 
							('SW-0683 (LAX)', 'SW-0683 (LAX)'), 
							('SW-2385 (SAN)', 'SW-2385 (SAN)'), 
							
							('AA-5899 (PHX)', 'AA-5899 (PHX)'), 
							('AA-2818 (DFW)', 'AA-2818 (DFW)'), 
							('AA-5805 (PHX)', 'AA-5805 (PHX)'), 
							('AA-2311 (ORD)', 'AA-2311 (ORD)'), 
							('AA-2047 (DFW)', 'AA-2047 (DFW)'), 
							('AA-2003 (PHX)', 'AA-2003 (PHX)'), 
							('AA-2486 (DFW)', 'AA-2486 (DFW)'), 
							('AA-5826 (PHX)', 'AA-5826 (PHX)'), 
							('AA-1162 (ORD)', 'AA-1162 (ORD)'), 
							('AA-2199 (DFW)', 'AA-2199 (DFW)'), 
							('AA-5820 (PHX)', 'AA-5820 (PHX)'), 
							('AA-1097 (DFW)', 'AA-1097 (DFW)'), 
							('AA-6063 (LAX)', 'AA-6063 (LAX)'), 
							('AA-2017 (PHX)', 'AA-2017 (PHX)'), 

							('UN-6126 (IAH)', 'UN-6126 (IAH)'), 
							('UN-5479 (DEN)', 'UN-5479 (DEN)'), 
							('UN-5626 (IAH)', 'UN-5626 (IAH)'), 
							('UN-2074 (ORD)', 'UN-2074 (ORD)'), 
							('UN-1629 (IAH)', 'UN-1629 (IAH)'), 
							('UN-5595 (SFO)', 'UN-5595 (SFO)'), 
							('UN-1618 (DEN)', 'UN-1618 (DEN)'), 
							('UN-6366 (IAH)', 'UN-6366 (IAH)'), 
							('UN-7411 (DEN)', 'UN-7411 (DEN)'), 
							('UN-5912 (SFO)', 'UN-5912 (SFO)'), 

							('DL-4440 (LAX)', 'DL-4440 (LAX)'), 
							('DL-3803 (SLC)', 'DL-3803 (SLC)'), 
							('DL-3589 (LAX)', 'DL-3589 (LAX)'), 
							('DL-2789 (ATL)', 'DL-2789 (ATL)'), 
							('DL-0780 (SEA)', 'DL-0780 (SEA)'), 
							('DL-2714 (MSP)', 'DL-2714 (MSP)'), 
							('DL-3556 (LAX)', 'DL-3556 (LAX)'), 

							('AL-1993 (SEA)', 'AL-1993 (SEA)'), 
							('AL-3447 (PDX)', 'AL-3447 (PDX)'), 
							('AL-0641 (SEA)', 'AL-0641 (SEA)'), 
							('AL-3497 (PDX)', 'AL-3497 (PDX)'),
							('SC-0664 (MSP)', 'SC-0664 (MSP)'), )
	# create the lists needed for the models

	status_list = (('Reserved', 'Reserved'), 
				('Cancelled', 'Cancelled'), 
				('Paid-Self', 'Paid-Self'), 
				('Paid-Other', 'Paid-Other'), )

	reservation_type_list = (('One Way Arrival', 'One Way Arrival'), 
							('One Way Departure', 'One Way Departure'), 
							('Round Trip', 'Round Trip'), )

	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	phone = models.CharField(max_length=128, blank=True)
	email = models.CharField(max_length=128, blank=True)

	seats = models.PositiveIntegerField(default=1)
	reservation_status = models.CharField(max_length=28, choices=status_list, default='Reserved')
	reservation_type = models.CharField(max_length=28, choices=reservation_type_list, default='Round Trip')
	cost = models.DecimalField(max_digits=5, decimal_places=2, default=55.00)
	cc_number = models.CharField(max_length=28, blank=True)
	cc_exp = models.CharField(max_length=28, blank=True)
	cc_cv = models.CharField(max_length=28, blank=True)

	arrival_date = models.DateField(blank=True, null=True, default='2020-03-20')
	arrival_flight = models.CharField(max_length=28, choices=arrival_flight_list, blank=True, null=True)
	arrival_time = models.TimeField(blank=True, null=True)

	departure_date = models.DateField(blank=True, null=True, default='2020-03-22')
	departure_flight = models.CharField(max_length=28, choices=departing_flight_list, blank=True, null=True)
	departure_time = models.TimeField(blank=True, null=True)

	drop_location = models.CharField(max_length=28, default="Starpass")
	pickup_location = models.CharField(max_length=28, default="Starpass")
	pickup_time = models.TimeField(blank=True, null=True)
	notes = models.TextField(blank=True)

	
	class Meta:
		ordering = ['arrival_time']

	def confirmation_number(self):
		return f'CARF0320-{self.last_name[0:4].upper()}{self.first_name[0:4].upper()}-{self.phone[-4:]}'

	def final_list(self):
		return f'{self.last_name}, {self.first_name}  {self.seats} {self.reservation_status} {self.reservation_type}'

	def arrival_list(self):
		return f'{self.arrival_date}:{self.arrival_time} - {self.first_name} {self.last_name} - {self.phone}'

	def departure_list(self):
		return f'{self.departure_date}:{self.departure_time} - {self.first_name} {self.last_name} - {self.phone}'
	def name(self):
		return f'{self.last_name}, {self.first_name}'

	def get_absolute_url(self):
		return reverse('flagstone:carf_detail', kwargs={'pk':self.pk})

	def __str__(self):
		return f'{self.last_name}, {self.first_name}'

# first_name
# last_name
# phone
# email
# seats
# reservation_status
# reservation_type
# cc_number
# cc_exp
# cc_cv
# arrival_date
# arrival_flight
# arrival_time
# departure_date
# departure_flight
# departure_time
# drop_location
# pickup_location
# pickup_time
# notes



# Arrivals


# SW-1350 (SAN)
# SW-1546 (LBB-DEN)
# SW-1948 (OAK-LAX)
# SW-2467 (MDW)
# SW-4112 (SNA-LAS)
# SW-2603 (SLC-LAX)
# SW-4183 (ONT-LAX)
# SW-1488 (MKE-SJC)
# SW-0364 (DEN)
# SW-1506 (LAX)
# SW-2430 (SAN)
# AA-1998 (DFW)
# AA-2003 (PHX)
# AA-2710 (DFW)
# AA-5826 (PHX)
# AA-1162 (ORD)
# AA-2824 (DFW)
# AA-5820 (PHX)
# AA-1097 (DFW)
# AA-6063 (LAX)
# AA-1441 (DFW)
# AA-2017 (PHX)
# AA-1207 (DFW)
# AA-5737 (PHX)
# AA-5870 (PHX)
# AA-3046 (LAX)
# AA-2228 (ORD)
# AA-2732 (PHX)
# AA-0649 (DFW)
# UN-5572 (DEN)
# UN-5802 (SFO)
# UN-6121 (IAH)
# UN-2034 (ORD)
# UN-0440 (DEN)
# UN-5487 (IAH)
# UN-6177 (IAH)
# UN-4659 (DEN)
# UN-5678 (DEN)
# UN-5527 (SF0)
# UN-5307 (DEN)
# UN-5887 (SFO)
# UN-6100 (IAH)
# UN-5396 (SFO)
# UN-6215 (IAH)
# DL-3803 (SLC)
# DL-3589 (LAX)
# DL-2789 (ATL)
# DL-0780 (SEA)
# DL-2714 (MSP)
# DL-3880 (LAX)
# DL-3989 (LAX)
# DL-1739 (ATL)
# DL-4545 (SLC)
# AL-3446 (PDX)
# AL-0648 (SEA)
# AL-3437 (PDX)
# AL-1996 (SEA)
# SC-0663 (LAS)



# Departures



# AA-5899 (PHX)
# AA-2818 (DFW)
# AA-5805 (PHX)
# AA-2311 (ORD)
# AA-2047 (DFW)
# AA-2003 (PHX)
# AA-2486 (DFW)
# AA-5826 (PHX)
# AA-1162 (ORD)
# AA-2199 (DFW)
# AA-5820 (PHX)
# AA-1097 (DFW)
# AA-6063 (LAX)
# AA-2017 (PHX)
# DL-4440 (LAX)
# DL-3803 (SLC)
# DL-3589 (LAX)
# DL-2789 (ATL)
# DL-0780 (SEA)
# DL-2714 (MSP)
# DL-3556 (LAX)
# AL-1993 (SEA)
# AL-3447 (PDX)
# AL-0641 (SEA)
# AL-3497 (PDX)
# UN-6126 (IAH)
# UN-5479 (DEN)
# UN-5626 (IAH)
# UN-2074 (ORD)
# UN-1629 (IAH)
# UN-5595 (SFO)
# UN-1618 (DEN)
# UN-6366 (IAH)
# UN-7411 (DEN)
# UN-5912 (SFO)
# SW-2595 (SAN)
# SW-2057 (DEN)
# SW-1948 (LAS)
# SW-2467 (LAX)
# SW-2394 (SJC)
# SW-2603 (DEN)
# SW-0683 (LAX)
# SW-2385 (SAN)
# SC-0664 (MSP)

class PRAASA_March2020(models.Model):
	payment_rendered = (('PAID IN FULL', 'PAID IN FULL'), ('PAYMENT DUE', 'PAYMENT DUE'), ('PAY ON ARRIVAL', 'PAY ON ARRIVAL'))
	shuttle_types = (('Round Trip', 'Round Trip'), ('One Way', 'One Way'))
	active_inactive = (('INACTIVE', 'INACTIVE'), ('ACTIVE', 'ACTIVE'), ('COMPLETED', 'COMPLETED'))
	payment_standings = (('PAID IN FULL', 'PAID IN FULL'), ('PAYMENT DUE', 'PAYMENT DUE'), ('DELINQUENT', 'DELINQUENT'))
	airline_list = (('Alaska Airlines', 'Alaska Airlines'),
					('Allegiant', 'Allegiant'),
					('American Airlines', 'American Airlines'),
					('Delta Air Lines', 'Delta Air Lines'),
					('Eurowings', 'Eurowings'),
					('Frontier Airlines', 'Frontier Airlines'),
					('Southwest Airlines', 'Southwest Airlines'),
					('Sun Country Airlines', 'Sun Country Airlines'),
					('United Airlines', 'United Airlines'),
					('Other', 'Other'))

	status_list = (('Arrived', 'Arrived'), ('Return Trip', 'Return Trip'), ('Active', 'Active'), ('Inactive', 'Inactive')) 
	status_box = models.CharField(max_length=56, choices=status_list, default='Active')
	shuttle_type = models.CharField(max_length=56, choices=shuttle_types, default='Round Trip')
	cost = models.DecimalField(max_digits=5, decimal_places=2, default=40.00)
	total_due_status = models.CharField(max_length=56, choices=payment_standings, default='PAYMENT DUE')
	first_name = models.CharField(max_length=256, blank=True)
	last_name = models.CharField(max_length=256, blank=True)
	phone = models.CharField(max_length=28, blank=True)
	email = models.EmailField(unique=True, blank=True, null=True)
	z_code = models.CharField(max_length=16, blank=True)
	cc_num = models.CharField(max_length=56, blank=True)
	cc_exp = models.CharField(max_length=56, blank=True)
	cc_cv = models.CharField(max_length=6, blank=True)
	arrival_date = models.DateField(blank=True, null=True)
	arrival_time = models.TimeField(blank=True, null=True)
	arrival_airport = models.CharField(max_length=29, default="Tucson International", blank=True)
	arrival_airline = models.CharField(max_length=25, choices=airline_list, blank=True)
	arrival_flight = models.CharField(max_length=16, blank=True)
	drop_location = models.CharField(max_length=256, default='Westin La Paloma', blank=True)
	arrival_notes = models.TextField(blank=True)
	pickup_location = models.CharField(max_length=256,blank=True)
	pickup_time = models.TimeField(blank=True, null=True)
	departure_date = models.DateField(blank=True, null=True)
	departure_time = models.TimeField(blank=True, null=True)
	departure_airport = models.CharField(max_length=29, default='Tucson International', blank=True)
	departure_airline = models.CharField(max_length=25, choices=airline_list, blank=True)
	departure_flight = models.CharField(max_length=16, blank=True)
	departing_notes = models.TextField(blank=True)

	class Meta:
		ordering = ['arrival_time']

	def name(self):
		return f'{self.first_name} {self.last_name}'
	def __str__(self):
		return f'{self.name()}-{self.arrival_date}-{self.arrival_time}-{self.arrival_airline}-{self.arrival_flight}'

	def get_absolute_url(self):
		return reverse('flagstone:praasa_detail', kwargs={'pk':self.pk})

	def praasa_id(self):
		return f'PRA-20-{self.last_name[0:4].upper()}{self.first_name[0:4].upper()}'

	


############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################	

class AdobeDriver(models.Model):
	first_name = models.CharField(max_length=32)
	last_name = models.CharField(max_length=32)
	phone = models.CharField(max_length=32, blank=True)
	email = models.EmailField(blank=True)
	street = models.CharField(max_length=56, blank=True)
	city = models.CharField(max_length=56, blank=True)
	state = models.CharField(max_length=56, blank=True)
	z_code = models.CharField(max_length=16, blank=True)
	d_lic_num = models.CharField(max_length=56, blank=True)
	d_lic_exp = models.CharField(max_length=56, blank=True)
	d_dob = models.CharField(max_length=56, blank=True)
	date_of_hire = models.DateField(blank=True)
	notes = models.TextField(blank=True)

	def get_absolute_url(self):
			return reverse('flagstone:adobedriver_detail', kwargs={'pk':self.pk})

	def __str__(self):
			return f'{self.last_name}, {self.first_name}'

############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

class Organization(models.Model):
	orginazation_name = models.CharField(max_length=128)
	# org_contact = models.ForeignKey(Customer, on_delete=models.CASCADE)
	org_address = models.CharField(max_length=256, blank=True)
	org_phone = models.CharField(max_length=128, blank=True)
	org_notes = models.TextField(blank=True)
	def __str__(self):
		return self.orginazation_name

############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

class Customer(models.Model):
	affiliate_info = models.ForeignKey(Organization, on_delete=models.CASCADE, default='Self')
	first_name = models.CharField(max_length=32)
	last_name = models.CharField(max_length=32)
	phone = models.CharField(max_length=32, blank=True)
	email = models.EmailField(blank=True)
	street = models.CharField(max_length=56, blank=True)
	city = models.CharField(max_length=56, blank=True)
	state = models.CharField(max_length=56, blank=True)
	z_code = models.CharField(max_length=16, blank=True)

	d_lic_num = models.CharField(max_length=56, blank=True)
	d_lic_exp = models.CharField(max_length=56, blank=True)
	d_dob = models.CharField(max_length=56, blank=True)

	name_on_cc = models.CharField(max_length=56,blank=True)
	cc_num = models.CharField(max_length=56, blank=True)
	cc_exp = models.CharField(max_length=56, blank=True)
	cc_cv = models.CharField(max_length=6, blank=True)
	customer_notes = models.TextField(blank=True)

	def get_absolute_url(self):
		return reverse('flagstone:customer_detail', kwargs={'pk':self.pk})

	def __str__(self):
		return f'{self.last_name}, {self.first_name}'


############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################	
	
class Van(models.Model):
	van_num = models.CharField(max_length=4)
	vin = models.CharField(max_length=60, blank=True)
	year_make_model = models.CharField(max_length=72, blank=True)
	plate = models.CharField(max_length=16, blank=True)
	tag_exp = models.DateField()
	notes = models.TextField(blank=True)

	def get_absolute_url(self):
		return reverse('flagstone:van_detail', kwargs={'pk':self.pk})
	def __str__(self):
		return f'{self.van_num}-{self.plate}'


############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

class VanInspectionLog(models.Model):
	inspector = (('Customer', 'Customer'), ('Paul', 'Paul'), ('Cary', 'Cary'), ('Mike', 'Mike'), ('Rolf', 'Rolf'), ('Kathy', 'Kathy'), ('Ruben', 'Ruben'), ('Martin', 'Martin'), ('Other', 'Other'))
	van_info = models.ForeignKey(Van, on_delete=models.CASCADE)
	inspector_info = models.CharField(max_length=24, choices=inspector)
	inspection_date = models.DateField()
	inspection_time = models.TimeField()
	inspection_note = models.TextField()

	def get_absolute_url(self):
		return reverse('flagstone:vaninspectionlog_detail', kwargs={'pk':self.pk})

	def __str__(self):
		return f'{self.inspection_date} - {self.van_info}'

############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

class VanMaintenanceLog(models.Model):
	maintenance_list = (('Oil Change', 'Oil Change'), ('Tires', 'Tires'), ('Body', 'Body'), ('Interior', 'Interior'), ('Mechanical', 'Mechanical'))
	van_information = models.ForeignKey(Van, on_delete=models.CASCADE)
	maintenance_type = models.CharField(max_length=56, choices=maintenance_list)
	maintenance_location = models.CharField(max_length=56)
	maintenance_date = models.DateField()
	maintenance_time = models.TimeField()
	inspection_note = models.TextField()

	def get_absolute_url(self):
		return reverse('flagstone:vanmaintenancelog_detail', kwargs={'pk':self.pk})

	def __str__(self):
		return f'{self.maintenance_date} - {self.van_information}'


############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

class Rental(models.Model):

	payment_standings1 = (('PAID IN FULL', 'PAID IN FULL'), ('PAYMENT DUE', 'PAYMENT DUE'), ('DELINQUENT', 'DELINQUENT'))
	payment_standings2 = (('PAID IN FULL', 'PAID IN FULL'), ('PAYMENT DUE', 'PAYMENT DUE'), ('DELINQUENT', 'DELINQUENT'))
	payment_standings3 = (('PAID IN FULL', 'PAID IN FULL'), ('PAYMENT DUE', 'PAYMENT DUE'), ('DELINQUENT', 'DELINQUENT'))
	payment_standings4 = (('PAID IN FULL', 'PAID IN FULL'), ('PAYMENT DUE', 'PAYMENT DUE'), ('DELINQUENT', 'DELINQUENT'))
	active_inactive = (('INACTIVE', 'INACTIVE'), ('ACTIVE', 'ACTIVE'), ('VAN OUT', 'VAN OUT'), ('VAN IN', 'VAN IN'), ('COMPLETED', 'COMPLETED'))
	### initial process
	total_due_status = models.CharField(max_length=56, choices=payment_standings3, default='PAYMENT DUE')
	final_total_status = models.CharField(max_length=56, choices=payment_standings4, default='PAYMENT DUE')
	status_type = models.CharField(max_length=26, choices=active_inactive, default='ACTIVE')
	org_name = models.ForeignKey(Organization, on_delete=models.CASCADE, default='NaaN')
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default='NaaN')
	van_number = models.ForeignKey(Van, on_delete=models.CASCADE)
	rental_date = models.DateField(blank=True)
	return_date = models.DateField(blank=True)
	## create timedelta to fill the following
	date_returned = models.DateField(blank=True, null=True)
	rental_time = models.TimeField(blank=True, null=True)
	return_time = models.TimeField(blank=True, null=True)
	time_returned = models.TimeField(blank=True, null=True)

	odometer_in = models.PositiveIntegerField(default=0, blank=True)
	odometer_out = models.PositiveIntegerField(default=0, blank=True)
	fuel_charge = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	cleaning_charge = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	damage_charge = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	misc_charge = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	misc_charge_text = models.TextField(max_length=500, blank=True)
	notes_out = models.TextField(max_length=500, blank=True)
	notes_in = models.TextField(max_length=500, blank=True)
	daily_rate = models.DecimalField(max_digits=6, decimal_places=2, default=144.95)
	additional_driver_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0) # $5.00
	mexico_insurance_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0) # '$41.95'
	roadside_assistance_rate = models.DecimalField(max_digits=6, decimal_places=2, default=4.95) # $4.95
	us_insurance_rate = models.DecimalField(max_digits=6, decimal_places=2, default=36.95)
	hitch_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0) # $10.00
	luggage_rack_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0) # $5.00
	daily_allowed_miles = models.PositiveIntegerField(default=200)
	mileage_over_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0.20)
	drop_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00) # $100.00
	
	lic_tax = models.DecimalField(max_digits=6, decimal_places=2, default=0.05)	
	sales_tax = models.DecimalField(max_digits=6, decimal_places=3, default=0.081)	
	surcharge = models.DecimalField(max_digits=6, decimal_places=2, default=4.95)

	airport_access_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00) # 10% of actual fee???
	airport_pickup_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00) # $100.00
	misc_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00) # $1,000,000.00 :)
	misc_fee_text = models.TextField(max_length=100, blank=True)

	class Meta:
		ordering = ['rental_date', 'rental_time']
	def invoice_id(self):
		v_id = f'{self.rental_date.month}-{self.rental_date.day}-{self.rental_date.year}-{self.customer.last_name[0:3].upper()}{self.customer.first_name[0:3].upper()}-{self.van_number.van_num}'
		return v_id

	def total_days(self):
		num_of_days = self.return_date - self.rental_date
		return num_of_days.days

	def daily_rate_subtotal(self):
		d_rate_sub = self.total_days() * self.daily_rate
		subtotal = round(d_rate_sub, 2)
		return d_rate_sub


	def add_driver_rate_subtotal(self):
		subt = self.total_days() * self.additional_driver_rate
		subtotal = round(subt, 2)
		return subtotal

	def mex_ins_subtotal(self):
		subt = self.total_days() * self.mexico_insurance_rate
		subtotal = round(subt, 2)
		return subtotal

	def rd_side_asst_subtotal(self):
		subt = self.total_days() * self.roadside_assistance_rate
		subtotal = round(subt, 2)
		return subtotal

	def us_ins_subtotal(self):
		subt = self.total_days()* self.us_insurance_rate
		subtotal = round(subt, 2)
		return subtotal

	def hitch_rate_subtotal(self):
		subt = self.total_days() * self.hitch_rate
		subtotal = round(subt, 2)
		return subtotal

	def luggage_rack_subtotal(self):
		subt = self.total_days() * self.luggage_rack_rate
		subtotal = round(subt, 2)
		return subtotal
	
	def variable_rates_subtotal(self):
		subt = self.daily_rate_subtotal() + self.add_driver_rate_subtotal() + self.mex_ins_subtotal() + self.rd_side_asst_subtotal() + self.us_ins_subtotal() + self.luggage_rack_subtotal()
		subtotal = round(subt, 2)
		return subtotal

	def lic_tax_sub(self):
		subt = self.lic_tax * self.variable_rates_subtotal()
		subtotal = round(subt, 2)
		return subtotal

	def sales_tax_sub(self):
		subt = self.sales_tax * self.variable_rates_subtotal()
		subtotal = round(subt, 2)
		return subtotal

	def taxes_sub(self):
		t_sub = self.surcharge + self.lic_tax_sub() + self.sales_tax_sub()
		return t_sub

	def ancillary_fees(self):
		subt = self.airport_access_fee + self.airport_pickup_fee + self.airport_access_fee + self.drop_fee + self.misc_fee
		subtotal = round(subt, 2)
		return subtotal

	def subtotal(self):
		subt = self.variable_rates_subtotal() + self.ancillary_fees()
		return subt
	###
	def static_rates_subtotal(self):
		subt = self.lic_tax_sub() + self.sales_tax_sub() +self.surcharge + self.ancillary_fees()
		subtotal = round(subt, 2)
		return subtotal
	###
	def total_due(self):
		subt = self.static_rates_subtotal() + self.variable_rates_subtotal()
		subtotal = round(subt, 2)
		return subtotal

	def days_over(self):
		d_over = self.date_returned - self.return_date
		return d_over.days

	def days_over_charge(self):
		foobar = self.days_over() * self.daily_rate
		subtotal = round(foobar, 2)
		return subtotal

	def actual_miles_driven(self):
		foobar = self.odometer_in - self.odometer_out
		return foobar

	def miles_allowed(self):
		foobar = self.total_days() * self.daily_allowed_miles
		return foobar

	def miles_over(self):
		foobar = self.actual_miles_driven() - self.miles_allowed()
		if foobar <= 0:
			return 0
		elif foobar >= 1:
			foobar = self.actual_miles_driven() - self.miles_allowed()
			return foobar

	def mileage_over_charge(self):
		if self.miles_over() <= 0:
			return 0
		elif self.miles_over() >= 1:
			foobar = self.miles_over() * self.mileage_over_rate
			subtotal = round(foobar, 2)
			return subtotal
	###
	def final_total(self):
		foobar = self.mileage_over_charge() + self.days_over_charge() + self.fuel_charge + self.cleaning_charge + self.damage_charge + self.misc_charge
		subtotal = round(foobar, 2)
		return subtotal

	def get_absolute_url(self):
		return reverse('flagstone:rental_detail', kwargs={'pk':self.pk})

	def __str__(self):
		title = f'{self.customer} : {self.rental_date} - {self.van_number}'
		return title


############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

class Shuttle(models.Model):
	type_list = (('AP', 'AP'), ('SH', 'SH'))
	payment_rendered = (('PAID IN FULL', 'PAID IN FULL'), ('PAYMENT DUE', 'PAYMENT DUE'), ('DELINQUENT', 'DELINQUENT'))
	active_inactive = (('INACTIVE', 'INACTIVE'), ('ACTIVE', 'ACTIVE'), ('COMPLETED', 'COMPLETED'))

	airport_list = (('TIA', 'Tucson'), ('SKY', 'SkyHarbor'))
	airline_list = (('Advanced Air', 'Advanced Air'),
					('Air Canada', 'Air Canada'),
					('Alaska Airlines', 'Alaska Airlines'),
					('Allegiant', 'Allegiant'),
					('American Airlines', 'American Airlines'),
					('Boutique Air', 'Boutique Air'),
					('British Airways', 'British Airways'),
					('Condor Airlines', 'Condor Airlines'),
					('Contour Airlines', 'Contour Airlines'),
					('Delta Air Lines', 'Delta Air Lines'),
					('Eurowings', 'Eurowings'),
					('Frontier Airlines', 'Frontier Airlines'),
					('Hawaiian Airlines', 'Hawaiian Airlines'),
					('JetBlue Airways', 'JetBlue Airways'),
					('JSX-Swift Aviation', 'JSX-Swift Aviation'),
					('Southwest Airlines', 'Southwest Airlines'),
					('Spirit Airlines', 'Spirit Airlines'),
					('Sun Country Airlines', 'Sun Country Airlines'),
					('United Airlines', 'United Airlines'),
					('Volaris', 'Volaris'),
					('WestJet', 'WestJet'),
					('Other', 'Other'))


	cost = models.DecimalField(max_digits=5, decimal_places=2, default=55.00)
	status_type = models.CharField(max_length=26, choices=active_inactive, default='ACTIVE')
	event_name = models.CharField(max_length=256, blank=True)
	org_name = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True)
	customer_info = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)
	shuttle_type = models.CharField(max_length=28, choices=type_list, default='AP')
	payment_status = models.CharField(max_length=25, choices=payment_rendered, default='PAYMENT DUE')
	driver_info = models.ForeignKey(AdobeDriver, on_delete=models.CASCADE, blank=True)
	van_info = models.ForeignKey(Van, on_delete=models.CASCADE, blank=True)

	## Ground Pickup and Drop Off
	primary_pickup_location = models.TextField(blank=True)
	primary_pickup_date = models.DateField(blank=True)
	primary_pickup_time = models.TimeField(blank=True)
	primary_dropoff = models.TextField(blank=True)
	primary_ground_notes = models.TextField(blank=True)

	departure_pickup_location = models.TextField(blank=True)
	departure_pickup_date = models.DateField(blank=True)
	departure_pickup_time = models.TimeField(blank=True)
	departure_dropoff = models.TextField(blank=True)
	departing_ground_notes = models.TextField(blank=True)


	## Airport Pickup and Drop Off
	arrival_date = models.DateField(blank=True)
	arrival_time = models.TimeField(blank=True)
	arrival_airport = models.CharField(max_length=9, choices=airport_list, default="TIA", blank=True)
	arrival_airline = models.CharField(max_length=25, choices=airline_list, blank=True)
	arrival_flight = models.CharField(max_length=16, blank=True)
	drop_location = models.CharField(max_length=256, blank=True)
	arrival_notes = models.TextField(blank=True)
	
	pickup_location = models.CharField(max_length=256,blank=True)
	pickup_time = models.TimeField(blank=True)

	departure_date = models.DateField(blank=True)
	departure_time = models.TimeField(blank=True)
	departure_airport = models.CharField(max_length=9, choices=airport_list, default='Tucson', blank=True)
	departure_airline = models.CharField(max_length=25, choices=airline_list, blank=True)
	departure_flight = models.CharField(max_length=16, blank=True)
	departing_notes = models.TextField(blank=True)
	
	notes = models.TextField(blank=True)

	def invoice_id(self):
		v_id = f'{self.arrival_date.month}-{self.arrival_date.day}-{self.arrival_date.year}-{self.customer_info.last_name[0:3].upper()}{self.customer_info.first_name[0:3].upper()}-{self.shuttle_type}'
		return v_id

	def __str__(self):
		return f'{self.customer_info} {self.arrival_date}'

	def get_absolute_url(self):
		return reverse('flagstone:shuttle_detail', kwargs={'pk':self.pk})

############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

class TimeSheet(models.Model):
	name = models.ForeignKey(AdobeDriver, on_delete=models.CASCADE)
	week_ending = models.DateField()
	sun_time = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
	mon_time = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
	tue_time = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
	wed_time = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
	thu_time = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
	fri_time = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
	sat_time = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
	notes = models.TextField(blank=True)

	def weekly_hrs(self):
		ttl_time = self.sun_time + self.mon_time + self.tue_time + self.wed_time + self.thu_time + self.fri_time + self.sat_time
		return ttl_time

	def __str__(self):
		return f'{self.week_ending} - {self.name} - {self.weekly_hrs()}hrs'

	def get_absolute_url(self):
		return reverse('flagstone:timesheet_detail', kwargs={'pk':self.pk})

############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

class DriverAssignment(models.Model):
	type_list = (('RE', 'RE'), ('SH', 'SH'))
	driver = models.ForeignKey(AdobeDriver, on_delete=models.CASCADE, default='None')
	# van = models.ForeignKey(Van, on_delete=models.CASCADE, default='None')
	event_info = models.CharField(max_length=256, blank=True)
	customer_info = models.ForeignKey(Customer, on_delete=models.CASCADE, default='None')
	org_name = models.ForeignKey(Organization, on_delete=models.CASCADE, default='None')
	notes = models.TextField(blank=True)

	def __str__(self):
		return f'{self.driver}'#- {self.van}'

	def get_absolute_url(self):
		return reverse('flagstone:driverassignment_detail', kwargs={'pk':self.pk})
		