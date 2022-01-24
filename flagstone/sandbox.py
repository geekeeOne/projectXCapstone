class FlightInfo(models.Model):
	airports = (('TIA', 'KTUS'), ('SKY', 'SkyHarbor'))
	airline_list = (('Alaska', 'Alaska'), 
					('Allegiant', 'Allegiant'), 
					('American Airlines', 'AA'), 
					('Frontier', 'Frontier'), 
					('Southwest', 'Southwest'), 
					('Sun Country', 'Sun Country'), 
					('United', 'United'), 
					('Other', 'Other'))
	render_type = (('paid', 'paid'), ('unpaid', 'unpaid'), ('on-hold', 'on-hold'))
	status_type = models.CharField(max_length=7, choices=render_type)
	event_name = models.ForeignKey(EventName, on_delete=models.DO_NOTHING)
	customer_name = models.ForeignKey(Rental, on_delete=models.DO_NOTHING)
	arrival_date = models.DateField()
	arrival_time = models.TimeField()
	airport_location = models.CharField(max_length=9, choices=airports)
	arriving_airline = models.CharField(max_length=25, choices=airline_list)
	drop_location = models.CharField(max_length=256)
	pickup_location = models.CharField(max_length=256)
	departure_date = models.DateField()
	departure_time = models.TimeField()
	airport_location = models.CharField(max_length=9, choices=airports)
	departing_airline = models.CharField(max_length=25, choices=airline_list)
	pickup_location = models.CharField(max_length=256)
	notes = models.TextField()

	def __str__(self):
		fl_info = f'{self.event_name}--{self.customer_name}' 
		return fl_info
class AirportShuttleService(models.Model):


	airports = (('TIA', 'Tucson'), ('SKY', 'SkyHarbor'))
	airline_list = (('Alaska', 'Alaska'), 
					('Allegiant', 'Allegiant'), 
					('American Airlines', 'AA'), 
					('Frontier', 'Frontier'), 
					('Southwest', 'Southwest'), 
					('Sun Country', 'Sun Country'), 
					('United', 'United'), 
					('Other', 'Other'))
	render_type = (('paid', 'paid'), ('unpaid', 'unpaid'), ('on-hold', 'on-hold'))
	status_type = models.CharField(max_length=7, choices=render_type, blank=True)
	event_location = models.CharField(max_length=25, blank=True)
	event_name = models.ForeignKey(EventName, on_delete=models.DO_NOTHING, blank=True)
	customer_name = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True)
	arrival_date = models.DateField(blank=True)
	arrival_time = models.TimeField(blank=True)
	arrival_airport = models.CharField(max_length=9, choices=airports, blank=True)
	arrival_airline = models.CharField(max_length=25, choices=airline_list, blank=True)
	arrival_flight = models.CharField(max_length=16, blank=True)
	drop_location = models.CharField(max_length=256, blank=True)
	departure_date = models.DateField(blank=True)
	departure_time = models.TimeField(blank=True)
	departure_airport = models.CharField(max_length=9, choices=airports, blank=True)
	departure_airline = models.CharField(max_length=25, choices=airline_list, blank=True)
	departure_flight = models.CharField(max_length=16, blank=True)
	pickup_location = models.CharField(max_length=256, blank=True)
	pickup_time = models.TimeField(blank=True)
	notes = models.TextField(blank=True)

	def __str__(self):
		fl_info = f'{self.event_name}--{self.customer_name}' 
		return fl_info
	def get_absolute_url(self):
		return reverse('flagstone:ap_shuttle_detail', kwargs={'pk':self.pk})