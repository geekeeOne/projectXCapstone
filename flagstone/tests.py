from django.test import TestCase

# Create your tests here.

'invoice_id':{{invoice_id}},
'last_name':{{customer.last_name}},
'first_name':{{customer.first_name}},
'phone':{{customer.phone}},
'email':{{customer.email}},
'rental_date':{{rental_date}},
'return_date':{{return_date}},
'total_days':{{total_days}},
'van_number':{{van_number}},
'daily_rate':{{daily_rate}},
'daily_allowed_miles':{{daily_allowed_miles}},
'mileage_over_rate':{{mileage_over_rate}},
'odometer_out':{{odometer_out}},
'notes_out':{{notes_out}},
'date_returned':{{date_returned}},
'odometer_in':{{odometer_in}},
'notes_in':{{notes_in}},
'us_insurance_rate':{{us_insurance_rate}},
'mexico_insurance_rate':{{mexico_insurance_rate}},
'roadside_assistance_rate':{{roadside_assistance_rate}},
'additional_driver_rate':{{additional_driver_rate}},
'hitch_rate':{{hitch_rate}},
'luggage_rack_rate':{{luggage_rack_rate}},
'airport_access_fee':{{airport_access_fee}},
'airport_pickup_fee':{{airport_pickup_fee}},
'drop_fee':{{drop_fee}},
'misc_fee':{{misc_fee}},
'misc_fee_text':{{misc_fee_text}},
'subtotal':{{subtotal}},
'surcharge':{{surcharge}},
'lic_tax':{{lic_tax_sub}},
'sales_tax':{{sales_tax_sub}},
'total_due':{{total_due}},
'days_over_charge':{{days_over_charge}},
'actual_miles_driven':{{actual_miles_driven}},
'miles_allowed':{{miles_allowed}} ,
'miles_over':{{miles_over}},
'mileage_over_charge':{{mileage_over_charge}},
'closing_total':{{final_total}},



{{total_due_status}}
{{final_total_status}}
{{status_type}}
{{customer}}
{{van_number}}
{{rental_date}}
{{return_date}}
{{date_returned}}
{{odometer_in}}
{{odometer_out}}
{{fuel_charge}}
{{cleaning_charge}}
{{damage_charge}}
{{misc_charge}}
{{notes_out}}
{{notes_in}}
{{daily_rate}}
{{additional_driver_rate}}
{{mexico_insurance_rate}}
{{roadside_assistance_rate}}
{{us_insurance_rate}}
{{hitch_rate}}
{{luggage_rack_rate}}
{{daily_allowed_miles}}
{{mileage_over_rate}}
{{drop_fee}}
{{lic_tax}}
{{sales_tax}}
{{surcharge}}
{{airport_access_fee}}
{{airport_pickup_fee}}
{{drop_fee}}
{{misc_fee}}
{{misc_fee_tex}}


<p><strong> Mileage Over Rate</strong> </p>
			<p>{{form.mileage_over_rate}}</p>	






















<td class="text-center"
<p><strong>total_due_status</strong></p>
<p>{{form.total_due_status}}</p>
<p><strong>final_total_status</strong></p>
<p>{{form.final_total_status}}</p>
<p><strong>status_type</strong></p>
<p>{{form.status_type}}</p>
</td>

<td class="text-center"
<p><strong>customer</strong></p>
<p>{{form.customer}}</p>
<p><strong>van_number</strong></p>
<p>{{form.van_number}}</p>
</td>

<td class="text-center"
<p><strong>rental_date</strong></p>
<p>{{form.rental_date}}</p>
<p><strong>return_date</strong></p>
<p>{{form.return_date}}</p>
<p><strong>date_returned</strong></p>
<p>{{form.date_returned}}</p>
</td>

<td class="text-center"
<p><strong>odometer_in</strong></p>
<p>{{form.odometer_in}}</p>
<p><strong>odometer_out</strong></p>
<p>{{form.odometer_out}}</p>
</td>

<td class="text-center"
<p><strong>notes_out</strong></p>
<p>{{form.notes_out}}</p>
<p><strong>notes_in</strong></p>
<p>{{form.notes_in}}</p>
</td>

<td class="text-center"
<p><strong>fuel_charge</strong></p>
<p>{{form.fuel_charge}}</p>
<p><strong>cleaning_charge</strong></p>
<p>{{form.cleaning_charge}}</p>
<p><strong>damage_charge</strong></p>
<p>{{form.damage_charge}}</p>
<p><strong>misc_charge</strong></p>
<p>{{form.misc_charge}}</p>
</td>

<td class="text-center"
<p><strong>daily_rate</strong></p>
<p>{{form.daily_rate}}</p>
<p><strong>additional_driver_rate</strong></p>
<p>{{form.additional_driver_rate}}</p>
<p><strong>mexico_insurance_rate</strong></p>
<p>{{form.mexico_insurance_rate}}</p>
<p><strong>roadside_assistance_rate</strong></p>
<p>{{form.roadside_assistance_rate}}</p>
<p><strong>us_insurance_rate</strong></p>
<p>{{form.us_insurance_rate}}</p>
<p><strong>hitch_rate</strong></p>
<p>{{form.hitch_rate}}</p>
<p><strong>luggage_rack_rate</strong></p>
<p>{{form.luggage_rack_rate}}</p>
</td>

<td class="text-center"
<p><strong>daily_allowed_miles</strong></p>
<p>{{form.daily_allowed_miles}}</p>
<p><strong>mileage_over_rate</strong></p>
<p>{{form.mileage_over_rate}}</p>
</td>

<td class="text-center"
<p><strong>lic_tax</strong></p>
<p>{{form.lic_tax}}</p>
<p><strong>sales_tax</strong></p>
<p>{{form.sales_tax}}</p>
<p><strong>surcharge</strong></p>
<p>{{form.surcharge}}</p>
</td>

<td class="text-center"
<p><strong>drop_fee</strong></p>
<p>{{form.drop_fee}}</p>
<p><strong>airport_access_fee</strong></p>
<p>{{form.airport_access_fee}}</p>
<p><strong>airport_pickup_fee</strong></p>
<p>{{form.airport_pickup_fee}}</p>
<p><strong>drop_fee</strong></p>
<p>{{form.drop_fee}}</p>
<p><strong>misc_fee</strong></p>
<p>{{form.misc_fee}}</p>
<p><strong>misc_fee_text</strong></p>
<p>{{form.misc_fee_text}}</p>