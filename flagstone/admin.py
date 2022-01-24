from django.contrib import admin
from import_export.admin import ImportExportModelAdmin 
from .models import *

@admin.register(AdobeDriver, 
				Customer, 
				Van, 
				VanInspectionLog, 
				VanMaintenanceLog, 
				Rental, 
				Organization, 
				TimeSheet, 
				DriverAssignment, 
				Shuttle,
				PRAASA_March2020,
				CustomerCARF,
				)

class ViewAdmin(ImportExportModelAdmin):
	pass
