from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from flagstone import models
import io
from django.http import FileResponse
from .filters import PraasaFilter
from reportlab.pdfgen import canvas
# from flagstone.forms import UserForm, UserProfileInfoForm, DateWidgetForm 
from django.urls import reverse_lazy  
from flagstone.utils import render_to_pdf
from django.template.loader import get_template
from django.views.generic import (View,TemplateView, 
								ListView, 
								DetailView, 
								CreateView, 
								UpdateView,
								DeleteView)
from io import BytesIO
from xhtml2pdf import pisa
# Create your views here.

# def index(request):
# 	return render(request, 'flagstone/index.html')

class IndexListView(ListView):
	model = models.SplashPage
	def get_context_data(self, **kwargs):
		context = super(IndexListView, self).get_context_data(**kwargs)
		context['shuttle_list'] = models.Shuttle.objects.all()
		context['rental_list'] = models.Rental.objects.all()
		# context['festival_list'] = Festival.objects.all()
		# And so on for more models
		return context

def tables(request):
	return render(request, 'flagstone/z_table_building.html')





def some_view(request):
	# Create a file-like buffer to receive PDF data.
	buffer = io.BytesIO()
	# Create the PDF object, using the buffer as its "file."
	p = canvas.Canvas(buffer)
	# Draw things on the PDF. Here's where the PDF generation happens.
	# See the ReportLab documentation for the full list of functionality.
	p.drawString(100, 100, "Hello world.")
	# Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()
	# FileResponse sets the Content-Disposition header so that browsers
	# present the option to save the file.
	buffer.seek(0)
	return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

class GeneratePDF(View):
	def get(self, request, *args, **kwargs):
		model = models.Customer
		template = get_template('flagstone/rental_detail.html')
		context = {		
			'last_name':{{model.last_name}},
			'first_name':{{model.first_name}},
			'phone':{{model.phone}},
			'email':{{model.email}},
			'rental_date':{{model.rental_date}},
			'return_date':{{model.return_date}},
			'total_days':{{model.total_days}},
			'van_number':{{model.van_number}},
			'daily_rate':{{model.daily_rate}},
			'daily_allowed_miles':{{model.daily_allowed_miles}},
			'mileage_over_rate':{{model.mileage_over_rate}},
			'odometer_out':{{model.odometer_out}},
			'notes_out':{{model.notes_out}},
			'date_returned':{{model.date_returned}},
			'odometer_in':{{model.odometer_in}},
			'notes_in':{{model.notes_in}},
			'us_insurance_rate':{{model.us_insurance_rate}},
			'mexico_insurance_rate':{{model.mexico_insurance_rate}},
			'roadside_assistance_rate':{{model.roadside_assistance_rate}},
			'additional_driver_rate':{{model.additional_driver_rate}},
			'hitch_rate':{{model.hitch_rate}},
			'luggage_rack_rate':{{model.luggage_rack_rate}},
			'airport_access_fee':{{model.airport_access_fee}},
			'airport_pickup_fee':{{model.airport_pickup_fee}},
			'drop_fee':{{model.drop_fee}},
			'misc_fee':{{model.misc_fee}},
			'misc_fee_text':{{model.misc_fee_text}},
			'subtotal':{{model.subtotal}},
			'surcharge':{{model.surcharge}},
			'lic_tax':{{model.lic_tax_sub}},
			'sales_tax':{{model.sales_tax_sub}},
			'total_due':{{model.total_due}},
			'days_over_charge':{{model.days_over_charge}},
			'actual_miles_driven':{{model.actual_miles_driven}},
			'miles_allowed':{{model.miles_allowed}} ,
			'miles_over':{{model.miles_over}},
			'mileage_over_charge':{{model.mileage_over_charge}},
			'closing_total':{{model.final_total}},
		}
		html = template.render(context)
		return HttpResponse(html)

############################################################################
############################################################################
############################################################################
############################################################################

class CustomerListView(ListView):
	context_object_name = 'customer_list'
	model = models.Customer 

class CustomerDetailView(DetailView):
	context_object_name = 'customer_detail'
	model = models.Customer

	template_name = 'flagstone/customer_detail.html' 

	def render_to_pdf(template_src, context_dict={}):
	    template = get_template(template_src)
	    html  = template.render(context_dict)
	    result = BytesIO()
	    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	    if not pdf.err:
	        return HttpResponse(result.getvalue(), content_type='application/pdf')
	    return None
	# pdf = render_to_pdf('flagstone/customer_detail.html')
	# return HttpResponse(pdf, content_type='application/pdf')

class CustomerCreateView(CreateView):
	fields = ('affiliate_info',
				'first_name',
				'last_name', 
				'phone', 
				'email', 
				'street', 
				'city', 
				'state', 
				'z_code',
				'd_lic_num', 
				'd_lic_exp', 
				'd_dob', 
				'name_on_cc', 
				'cc_num', 
				'cc_exp', 
				'cc_cv', 
				)
	model = models.Customer

class CustomerUpdateView(UpdateView):
	fields = ('affiliate_info',
				'first_name',
				'last_name', 
				'phone', 
				'email', 
				'street', 
				'city', 
				'state', 
				'z_code',
				'd_lic_num', 
				'd_lic_exp', 
				'd_dob', 
				'cc_num', 
				'cc_exp', 
				'cc_cv', 
				)
	model = models.Customer

class CustomerDeleteView(DeleteView):
	model = models.Customer
	success_url = reverse_lazy('flagstone:customer_list')


############################################################################
############################################################################
############################################################################
############################################################################

class ShuttleListView(ListView):
	model = models.Shuttle

class ShuttleDetailView(DetailView):
	context_object_name = 'shuttle_detail'
	model = models.Shuttle
	template_name = 'flagstone/shuttle_detail.html' 

class ShuttleCreateView(CreateView):
	fields = ('cost',
		'status_type',
		'event_name',
		'org_name',
		'customer_info',
		'shuttle_type',
		'payment_status',
		'driver_info',
		'van_info',
		'primary_pickup_location',
		'primary_pickup_date',
		'primary_pickup_time',
		'primary_dropoff',
		'primary_ground_notes',
		'departure_pickup_location',
		'departure_pickup_date',
		'departure_pickup_time',
		'departure_dropoff',
		'departing_ground_notes',
		'arrival_date',
		'arrival_time',
		'arrival_airport',
		'arrival_airline',
		'arrival_flight',
		'drop_location',
		'arrival_notes',
		'pickup_location',
		'pickup_time',
		'departure_date',
		'departure_time',
		'departure_airport',
		'departure_airline',
		'departure_flight',
		'departing_notes',
		'notes',
		)


	model = models.Shuttle

class ShuttleUpdateView(UpdateView):
	fields = ('cost',
		'status_type',
		'event_name',
		'org_name',
		'customer_info',
		'shuttle_type',
		'payment_status',
		'driver_info',
		'van_info',
		'primary_pickup_location',
		'primary_pickup_date',
		'primary_pickup_time',
		'primary_dropoff',
		'primary_ground_notes',
		'departure_pickup_location',
		'departure_pickup_date',
		'departure_pickup_time',
		'departure_dropoff',
		'departing_ground_notes',
		'arrival_date',
		'arrival_time',
		'arrival_airport',
		'arrival_airline',
		'arrival_flight',
		'drop_location',
		'arrival_notes',
		'pickup_location',
		'pickup_time',
		'departure_date',
		'departure_time',
		'departure_airport',
		'departure_airline',
		'departure_flight',
		'departing_notes',
		'notes',
		)


	model = models.Shuttle

class ShuttleDeleteView(DeleteView):
	model = models.Shuttle
	success_url = reverse_lazy('flagstone:home')


############################################################################
############################################################################
############################################################################
############################################################################

class CustomerCARFListView(ListView):
	model = models.CustomerCARF 
	context_object_name = 'carf_list'


class CustomerCARFDetailView(DetailView):
	model = models.CustomerCARF 
	context_object_name = 'carf_detail'
	template_name = 'flagstone/carf_detail.html'



class CustomerCARFCreateView(CreateView):
	model = models.CustomerCARF
	context_object_name = 'carf_form'
	template_name = 'flagstone/carf_form.html'

	fields = ('first_name', 
			'last_name', 
			'phone', 
			'email', 
			'seats', 
			'reservation_status', 
			'reservation_type', 
			'cost', 
			'cc_number', 
			'cc_exp', 
			'cc_cv', 
			'arrival_date', 
			'arrival_flight', 
			'arrival_time', 
			'departure_date', 
			'departure_flight', 
			'departure_time', 
			'drop_location', 
			'pickup_location', 
			'pickup_time', 
			'notes', )

class CustomerCARFUpdateView(UpdateView):
	model = models.CustomerCARF
	context_object_name = 'carf_update'
	template_name = 'flagstone/carf_form.html'

	fields = ('first_name', 
			'last_name', 
			'phone', 
			'email', 
			'seats', 
			'reservation_status', 
			'reservation_type', 
			'cost', 
			'cc_number', 
			'cc_exp', 
			'cc_cv', 
			'arrival_date', 
			'arrival_flight', 
			'arrival_time', 
			'departure_date', 
			'departure_flight', 
			'departure_time', 
			'drop_location', 
			'pickup_location', 
			'pickup_time', 
			'notes', )

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




############################################################################
############################################################################
############################################################################
############################################################################
class PRAASA_March2020ListView(ListView):
	model = models.PRAASA_March2020
	context_object_name = 'praasa_list'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = PraasaFilter(self.request.GET, queryset=self.get_queryset())
		return context 

class PRAASA_March2020DetailView(DetailView):
	model = models.PRAASA_March2020
	context_object_name = 'praasa_detail'
	template_name = 'flagstone/praasa_detail.html' 

class PRAASA_March2020CreateView(CreateView):
	model = models.PRAASA_March2020
	fields = ('first_name',
				'shuttle_type',
				'status_box',
				'last_name',
				'cost',
				'total_due_status',
				'phone',
				'email',
				'z_code',
				'cc_num',
				'cc_exp',
				'cc_cv',
				'arrival_date',
				'arrival_time',
				'arrival_airport',
				'arrival_airline',
				'arrival_flight',
				'drop_location',
				'arrival_notes',
				'pickup_location',
				'pickup_time',
				'departure_date',
				'departure_time',
				'departure_airport',
				'departure_airline',
				'departure_flight',
				'departing_notes',)
	
class PRAASA_March2020UpdateView(UpdateView):
	model = models.PRAASA_March2020
	fields = ('first_name',
				'shuttle_type',
				'status_box',
				'last_name',
				'cost',
				'total_due_status',
				'phone',
				'email',
				'z_code',
				'cc_num',
				'cc_exp',
				'cc_cv',
				'arrival_date',
				'arrival_time',
				'arrival_airport',
				'arrival_airline',
				'arrival_flight',
				'drop_location',
				'arrival_notes',
				'pickup_location',
				'pickup_time',
				'departure_date',
				'departure_time',
				'departure_airport',
				'departure_airline',
				'departure_flight',
				'departing_notes',)

class PRAASA_March2020DeleteView(DeleteView):
	model = models.PRAASA_March2020

'''

class IndexView(ListView):
    context_object_name = 'home_list'    
    template_name = 'contacts/index.html'
    queryset = Individual.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['roles'] = Role.objects.all()
        context['venue_list'] = Venue.objects.all()
        context['festival_list'] = Festival.objects.all()
        # And so on for more models
        return context
'''

# class IndexListView(ListView):
# 	context_object_name = 'index_list'
# 	model = models.Rental
# 	template_name = 'flagstone:index_list.html'
	# def get_context_data(self, **kwargs):
	# 	context = super(IndexListView, self).get_context_data(**kwargs)
	# 	context['shuttle_list'] = models.Shuttle.objects.all()
		
	# 	return context

class RentalListView(ListView):
	
	model = models.Rental

	def get_context_data(self, **kwargs):
		context = super(RentalListView, self).get_context_data(**kwargs)
		context['shuttle_list'] = models.Shuttle.objects.all()
		
		return context


class RentalDetailView(DetailView):
	context_object_name = 'rental_detail'
	model = models.Rental
	template_name = 'flagstone/rental_detail.html' 

class RentalCreateView(CreateView):
	fields = ('total_due_status',
			'final_total_status',
			'status_type',
			'customer',
			'van_number',
			'rental_date',
			'return_date',
			'date_returned',
			'rental_time',
			'return_time',
			'time_returned',
			'odometer_in',
			'odometer_out',
			'misc_charge_text',
			'org_name',
			'fuel_charge',
			'cleaning_charge',
			'damage_charge',
			'misc_charge',
			'notes_out',
			'notes_in',
			'daily_rate',
			'additional_driver_rate',
			'mexico_insurance_rate',
			'roadside_assistance_rate',
			'us_insurance_rate',
			'hitch_rate',
			'luggage_rack_rate',
			'daily_allowed_miles',
			'mileage_over_rate',
			'lic_tax',
			'sales_tax',
			'surcharge',
			'airport_access_fee',
			'airport_pickup_fee',
			'drop_fee',
			'misc_fee',
			'misc_fee_text',
			)
	model = models.Rental
	
class RentalUpdateView(UpdateView):
	fields = ('total_due_status',
			'final_total_status',
			'status_type',
			'customer',
			'van_number',
			'rental_date',
			'return_date',
			'date_returned',
			'rental_time',
			'return_time',
			'time_returned',
			'odometer_in',
			'odometer_out',
			'misc_charge_text',
			'org_name',
			'fuel_charge',
			'cleaning_charge',
			'damage_charge',
			'misc_charge',
			'notes_out',
			'notes_in',
			'daily_rate',
			'additional_driver_rate',
			'mexico_insurance_rate',
			'roadside_assistance_rate',
			'us_insurance_rate',
			'hitch_rate',
			'luggage_rack_rate',
			'daily_allowed_miles',
			'mileage_over_rate',
			'lic_tax',
			'sales_tax',
			'surcharge',
			'airport_access_fee',
			'airport_pickup_fee',
			'drop_fee',
			'misc_fee',
			'misc_fee_text',
			)
	model = models.Rental

'''
'misc_charge_text',
'org_name',

total_due_status
final_total_status
status_type
org_name
customer
van_number
rental_date
return_date
date_returned
odometer_in
odometer_out
fuel_charge
cleaning_charge
damage_charge
misc_charge
misc_charge_text
notes_out
notes_in
daily_rate
additional_driver_rate
mexico_insurance_rate
roadside_assistance_rate
us_insurance_rate
hitch_rate
luggage_rack_rate
daily_allowed_miles
mileage_over_rate
lic_tax
sales_tax
surcharge
airport_access_fee
airport_pickup_fee
drop_fee
misc_fee
misc_fee_text
'''


class RentalDeleteView(DeleteView):
	model = models.Rental
	success_url = reverse_lazy('flagstone:home')

############################################################################
############################################################################
############################################################################
############################################################################

class VanListView(ListView):
	model = models.Van

class VanDetailView(DetailView):
	context_object_name = 'van_detail'
	model = models.Van
	template_name = 'flagstone/van_detail.html' 

class VanCreateView(CreateView):
	fields = ('van_num', 'vin', 'year_make_model', 'plate', 'tag_exp')
	model = models.Van

class VanUpdateView(UpdateView):
	fields = ('van_num', 'vin', 'year_make_model', 'plate', 'tag_exp')
	model = models.Van

class VanDeleteView(DeleteView):
	model = models.Van
	success_url = reverse_lazy('flagstone:home')

############################################################################
############################################################################
############################################################################
############################################################################

class VanInspectionLogListView(ListView):
	model = models.VanInspectionLog

class VanInspectionLogDetailView(DetailView):
	context_object_name = 'vaninspectionlog_detail'
	model = models.VanInspectionLog
	template_name = 'flagstone/vaninspectionlog_detail.html' 

class VanInspectionLogCreateView(CreateView):
	fields = ('van_info', 
			'inspector_info', 
			'inspection_date', 
			'inspection_time', 
			'inspection_note', )
	model = models.VanInspectionLog

class VanInspectionLogUpdateView(UpdateView):
	fields = ('van_info', 
			'inspector_info', 
			'inspection_date', 
			'inspection_time', 
			'inspection_note', )
	model = models.VanInspectionLog

class VanInspectionLogDeleteView(DeleteView):
	model = models.VanInspectionLog
	success_url = reverse_lazy('flagstone:home')



############################################################################
############################################################################
############################################################################
############################################################################

class VanMaintenanceLogListView(ListView):
	model = models.VanMaintenanceLog

class VanMaintenanceLogDetailView(DetailView):
	context_object_name = 'vanmaintenancelog_detail'
	model = models.VanMaintenanceLog
	template_name = 'flagstone/vanmaintenancelog_detail.html' 

class VanMaintenanceLogCreateView(CreateView):
	fields = ('van_information', 
			'maintenance_type', 
			'maintenance_location', 
			'maintenance_date', 
			'maintenance_time', 
			'inspection_note', )
	model = models.VanMaintenanceLog

class VanMaintenanceLogUpdateView(UpdateView):
	fields = ('van_information', 
			'maintenance_type', 
			'maintenance_location', 
			'maintenance_date', 
			'maintenance_time', 
			'inspection_note', )
	model = models.VanMaintenanceLog

class VanMaintenanceLogDeleteView(DeleteView):
	model = models.VanMaintenanceLog
	success_url = reverse_lazy('flagstone:home')





############################################################################
############################################################################
############################################################################
############################################################################

class OrganizationListView(ListView):
	model = models.Organization 
	
class OrganizationDetailView(DetailView):
	context_object_name = 'organization_detail'
	model = models.Organization
	template_name = 'flagstone/organization_detail.html' 
	
class OrganizationCreateView(CreateView):	
	fields = ('orginazation_name',
			'org_contact',
			'org_address',
			'org_phone')
	model = models.Organization
class OrganizationUpdateView(UpdateView):
	fields = ('orginazation_name',
			'org_contact',
			'org_address',
			'org_phone')
	model = models.Organization
class OrganizationDeleteView(DeleteView):
	model = models.Organization
	success_url = reverse_lazy('flagstone:home')



############################################################################
############################################################################
############################################################################
############################################################################

class AdobeDriverListView(ListView):
	model = models.AdobeDriver
	
class AdobeDriverDetailView(DetailView):
	context_object_name = 'adobedriver_detail'
	model = models.AdobeDriver
	template_name = 'flagstone/adobedriver_detail.html' 

class AdobeDriverCreateView(CreateView):
	model = models.AdobeDriver
	fields = ('first_name', 
				'last_name', 
				'phone', 
				'email', 
				'street', 
				'city', 
				'state', 
				'z_code', 
				'd_lic_num', 
				'd_lic_exp', 
				'd_dob', 
				'date_of_hire', 
				 )

class AdobeDriverUpdateView(UpdateView):
	model = models.AdobeDriver
	fields = ('first_name', 
				'last_name', 
				'phone', 
				'email', 
				'street', 
				'city', 
				'state', 
				'z_code', 
				'd_lic_num', 
				'd_lic_exp', 
				'd_dob', 
				'date_of_hire', 
				 )

class AdobeDriverDeleteView(DeleteView):
	model = models.AdobeDriver
	success_url = reverse_lazy('flagstone:adobedriver_list')

############################################################################
############################################################################
############################################################################
############################################################################


class TimeSheetListView(ListView):
	model = models.TimeSheet
	
class TimeSheetDetailView(DetailView):
	context_object_name = 'timesheet_detail'
	model = models.TimeSheet
	template_name = 'flagstone/timesheet_detail.html' 

class TimeSheetCreateView(CreateView):
	model = models.TimeSheet
	fields = ('name', 
			'week_ending', 
			'sun_time', 
			'mon_time', 
			'tue_time', 
			'wed_time', 
			'thu_time', 
			'fri_time', 
			'sat_time',
			 )

class TimeSheetUpdateView(UpdateView):
	model = models.TimeSheet
	fields = ('name', 
			'week_ending', 
			'sun_time', 
			'mon_time', 
			'tue_time', 
			'wed_time', 
			'thu_time', 
			'fri_time', 
			'sat_time',
			 )

class TimeSheetDeleteView(DeleteView):
	model = models.TimeSheet
	success_url = reverse_lazy('flagstone:adobedriver_list')





############################################################################
############################################################################
############################################################################
############################################################################




class DriverAssignmentListView(ListView):
	model = models.DriverAssignment 
	
class DriverAssignmentDetailView(DetailView):
	context_object_name = 'driverassignment_detail'
	model = models.DriverAssignment
	template_name = 'flagstone/driverassignment_detail.html' 
class DriverAssignmentCreateView(CreateView):
	
	fields = ('driver', 
			'van', 
			'pudo', 
			'ap_pudo', 
			'sp_serv', 
			'sp_evnt', )
	model = models.DriverAssignment
class DriverAssignmentUpdateView(UpdateView):
	fields = ('driver', 
			'van', 
			'pudo', 
			'ap_pudo', 
			'sp_serv', 
			'sp_evnt', )
	model = models.DriverAssignment
class DriverAssignmentDeleteView(DeleteView):
	model = models.DriverAssignment
	success_url = reverse_lazy('flagstone:home')



def register(request):

	registered = False

	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user 
			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']
			profile.save()
			registered = True
		else:
			print(user_form.errors,profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()
	return render(request, 'flagstone/registration.html',
				 {'user_form':user_form,
				 'profile_form':profile_form,
				 'registered':registered})

@login_required
def special(request):
	return HttpResponse("You are logged in, NICE!! :) ")


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse,('index'))


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse,('index'))
			else:
				return HttpResponse('Account Not Active')
		else:
			print('Someone tried to login and failed!')
			print(f'Username: {username}     password: {[password]}')
			return HttpResponse('invalid login details supplied!')
	else:
		return render(request,'flagstone/login.html', {})