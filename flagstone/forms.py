from django import forms
from django.contrib.auth.models import User

from flagstone.models import UserProfileInfo, Rental

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('portfolio_site', 'profile_pic')

# class RentalForm(forms.ModelForm):
# 	class Meta():
# 		model = Rental 
# 		rental_date = DateTimeField()

class DateWidgetForm(forms.DateInput):
	input_type = 'date'

class TimeWidgetForm(forms.DateTimeInput):
	input_type = 'time'

class NewRentalForm(forms.ModelForm):
	class Meta():
		model = Rental 
		fields = [
			'status_type', 
			'customer', 
			'van_number', 
			'rental_date', 
			'return_date', 
			'daily_rate', 
			'additional_driver_rate', 
			'mexico_insurance_rate', 
			'roadside_assistance_rate', 
			'us_insurance_rate', 
			'hitch_rate', 
			'luggage_rack_rate', 
			'daily_allowed_miles', 
			'mileage_over_rate', 
			'drop_fee', 
			'lic_tax', 
			'sales_tax', 
			'surcharge', 
			'airport_access_fee', 
			'airport_pickup_fee', 
			'drop_fee', 
			'misc_fee', 
			'misc_fee_text', 
			'date_returned', 
			'odometer_in', 
			'odometer_out', 
			'total_due_status', 
			'final_total_status',
		]

		widgets = {
			'rental_date': DateWidgetForm(),
			'return_date': TimeWidgetForm()
		}

	# ## additional driver add on ## ForeignKey model was throwing errors
	# lic_class = (('A', 'Class A'), ('B', 'Class B'), ('C', 'Class C'), ('D', 'Class D-Operator'))
	# damage_type = (('0', 'Undamaged'), ('1', 'Damaged'), ('2', 'Preexisting Damage') )

# customer
# rental_date
# return_date
# van_rented
# status_type
# daily_rate
# allowed_daily_miles
# mileage_over_rate
# additional_driver_fee
# mexico_insurance
# roadside_assistance
# additional_driver_01_first_name
# additional_driver_01_last_name
# additional_driver_01_phone
# additional_driver_01_email
# additional_driver_01_z_code
# additional_driver_01_d_lic_num
# additional_driver_01_d_lic_class
# additional_driver_01_d_lic_exp
# additional_driver_01_d_dob
# additional_driver_02_first_name
# additional_driver_02_last_name
# additional_driver_02_phone
# additional_driver_02_email
# additional_driver_02_z_code
# additional_driver_02_d_lic_num
# additional_driver_02_d_lic_class
# additional_driver_02_d_lic_exp
# additional_driver_02_d_dob
# surcharge
# lic_tax
# city_sales_tax
# airport_access_fee
# drop_fee
# date_returned
# late_charge
# miles_over_fee
# cleaning_fee
# other_fee
# fuel_charge
# notes
# gas_out
# odometer_out
# van_out_text
# odometer_in
# gas_in
# van_in_text
# windshield_out
# grill_out
# front_bumper_out
# rear_bumper_out
# backdoor_out
# backdoor_widow_out
# seats_out
# carpet_out
# driver_side_seat_out
# driver_side_front_tire_out
# driver_side_rear_tire_out
# driver_side_window_out
# driver_side_rear_window_out
# driver_side_mid_window_out
# driver_side_front_quarter_panel_out
# driver_side_mid_panel_out
# driver_side_rear_quarter_panel_out
# pass_side_seat_out
# pass_side_front_tire_out
# pass_side_rear_tire_out
# pass_side_window_out
# pass_side_rear_window_out
# pass_side_mid_window_out
# pass_side_front_quarter_panel_out
# pass_side_mid_panel_out
# pass_side_rear_quarter_panel_out
# windshield_retrun
# grill_retrun
# front_bumper_retrun
# rear_bumper_retrun
# backdoor_retrun
# backdoor_widow_retrun
# seats_retrun
# carpet_retrun
# driver_side_seat_retrun
# driver_side_front_tire_retrun
# driver_side_rear_tire_retrun
# driver_side_window_retrun
# driver_side_rear_window_retrun
# driver_side_mid_window_retrun
# driver_side_front_quarter_panel_retrun
# driver_side_mid_panel_retrun
# driver_side_rear_quarter_panel_retrun
# pass_side_seat_retrun
# pass_side_front_tire_retrun
# pass_side_rear_tire_retrun
# pass_side_window_retrun
# pass_side_rear_window_retrun
# pass_side_mid_window_retrun
# pass_side_front_quarter_panel_retrun
# pass_side_mid_panel_retrun
# pass_side_rear_quarter_panel_retrun