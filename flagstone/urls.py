from django.urls import path
from flagstone import views

app_name = 'flagstone'

urlpatterns = [
	# path('index_list/', views.IndexListView.as_view(), name='index_list'),
	path('customer_list/', views.CustomerListView.as_view(), name='customer_list'),
	path('customer_list/<int:pk>', views.CustomerDetailView.as_view(), name='customer_detail'),
	path('create_customer/', views.CustomerCreateView.as_view(), name='create_customer'),
	path('update_customer/<int:pk>', views.CustomerUpdateView.as_view(), name='update_customer'),
	path('delete_customer/<int:pk>', views.CustomerDeleteView.as_view(), name='delete_customer'),

	path('', views.IndexListView.as_view(), name='home'),
	path('rental_statement/<int:pk>', views.RentalDetailView.as_view(), name='rental_statement'),
	path('rental_list/', views.RentalListView.as_view(), name='rental_list'),
	path('rental_list/<int:pk>', views.RentalDetailView.as_view(), name='rental_detail'),
	path('rental_detail/<int:pk>', views.RentalDetailView.as_view(), name='rental_detail_pdf'),
	path('create_rental/', views.RentalCreateView.as_view(), name='create_rental'),
	path('update_rental/<int:pk>', views.RentalUpdateView.as_view(), name='update_rental'),
	path('delete_rental/<int:pk>', views.RentalDeleteView.as_view(), name='delete_rental'),


	path('shuttle_list/', views.ShuttleListView.as_view(), name='shuttle_list' ),
	path('shuttle_statememt/<int:pk>', views.ShuttleDetailView.as_view(), name='shuttle_statement'),
	path('shuttle_list/<int:pk>', views.ShuttleDetailView.as_view(), name='shuttle_detail' ),
	path('shuttle_create/', views.ShuttleCreateView.as_view(), name='shuttle_create' ),
	path('shuttle_update/<int:pk>', views.ShuttleUpdateView.as_view(), name='shuttle_update' ),
	path('shuttle_delete/<int:pk>', views.ShuttleDeleteView.as_view(), name='shuttle_delete' ),


	path('praasa_list/', views.PRAASA_March2020ListView.as_view(), name='praasa_list' ),
	path('praasa_statememt/<int:pk>', views.PRAASA_March2020DetailView.as_view(), name='praasa_statement'),
	path('praasa_list/<int:pk>', views.PRAASA_March2020DetailView.as_view(), name='praasa_detail' ),
	path('praasa_create/', views.PRAASA_March2020CreateView.as_view(), name='praasa_create' ),
	path('praasa_update/<int:pk>', views.PRAASA_March2020UpdateView.as_view(), name='update_praasa' ),
	path('praasa_delete/<int:pk>', views.PRAASA_March2020DeleteView.as_view(), name='praasa_delete' ),

	path('carf_list/', views.CustomerCARFListView.as_view(), name='carf_list' ),
	path('carf_statememt/<int:pk>', views.CustomerCARFDetailView.as_view(), name='carf_statement'),
	path('carf_list/<int:pk>', views.CustomerCARFDetailView.as_view(), name='carf_detail' ),
	path('carf_form/', views.CustomerCARFCreateView.as_view(), name='carf_form' ),
	path('carf_update/<int:pk>', views.CustomerCARFUpdateView.as_view(), name='carf_update' ),
	# path('carf_delete/<int:pk>', views.CustomerCARFDeleteView.as_view(), name='carf_delete' ),



	path('van_list/', views.VanListView.as_view(), name='van_list'),
	path('van_list/<int:pk>', views.VanDetailView.as_view(), name='van_detail'),
	path('create_van/', views.VanCreateView.as_view(), name='create_van'),
	path('update_van/<int:pk>', views.VanUpdateView.as_view(), name='update_van'),
	path('delete_van/<int:pk>', views.VanDeleteView.as_view(), name='delete_van'),

	path('pdf/<int:pk>', views.GeneratePDF.as_view(), name='pdf'),

	path('tables/', views.tables, name='tables'),
	path('register/', views.register, name='register'),
	path('user_login/', views.user_login,name='user_login'),
	path('some_view/', views.some_view, name='some_view'),

	path('organization_list/', views.OrganizationListView.as_view(), name='organization_list'),
	path('organization_detail/<int:pk>', views.OrganizationDetailView.as_view(), name='organization_detail'),
	path('organization_create/', views.OrganizationCreateView.as_view(), name='organization_create'),
	path('organization_update/<int:pk>', views.OrganizationUpdateView.as_view(), name='organization_update'),
	path('organization_delete/<int:pk>', views.OrganizationDeleteView.as_view(), name='organization_delete'),


	path('driver_list/', views.AdobeDriverListView.as_view(), name='adobedriver_list'),
	path('driver_list/<int:pk>', views.AdobeDriverDetailView.as_view(), name='adobedriver_detail'),
	path('driver_detail/<int:pk>', views.AdobeDriverDetailView.as_view(), name='adobedriver_detail'),

	path('driver_create/', views.AdobeDriverCreateView.as_view(), name='adobedriver_create'),

	path('driver_update/<int:pk>', views.AdobeDriverUpdateView.as_view(), name='adobedriver_update'),
	path('driver_delete/<int:pk>', views.AdobeDriverDeleteView.as_view(), name='adobedriver_delete'),


	path('vanmaintenancelog_list/', views.VanMaintenanceLogListView.as_view(), name='vanmaintenancelog_list'),
	path('vanmaintenancelog_list/<int:pk>', views.VanMaintenanceLogDetailView.as_view(), name='vanmaintenancelog_detail'),
	path('vanmaintenancelog_create/', views.VanMaintenanceLogCreateView.as_view(), name='vanmaintenancelog_create'),
	path('vanmaintenancelog_update/<int:pk>', views.VanMaintenanceLogUpdateView.as_view(), name='vanmaintenancelog_update'),
	path('vanmaintenancelog_delete/<int:pk>', views.VanMaintenanceLogDeleteView.as_view(), name='vanmaintenancelog_delete'),

	path('vaninspectionlog_list/', views.VanInspectionLogListView.as_view(), name='vaninspectionlog_list'),
	path('vaninspectionlog_list/<int:pk>', views.VanInspectionLogDetailView.as_view(), name='vaninspectionlog_detail'),
	path('vaninspectionlog_create/', views.VanInspectionLogCreateView.as_view(), name='vaninspectionlog_create'),
	path('vaninspectionlog_update/<int:pk>', views.VanInspectionLogUpdateView.as_view(), name='vaninspectionlog_update'),
	path('vaninspectionlog_delete/<int:pk>', views.VanInspectionLogDeleteView.as_view(), name='vaninspectionlog_delete'),

	path('timesheet_list/', views.TimeSheetListView.as_view(), name='timesheet_list'),
	path('timesheet_list/<int:pk>', views.TimeSheetDetailView.as_view(), name='timesheet_detail'),
	path('timesheet_create/', views.TimeSheetCreateView.as_view(), name='timesheet_create'),
	path('timesheet_update/<int:pk>', views.TimeSheetUpdateView.as_view(), name='timesheet_update'),
	path('timesheet_delete/<int:pk>', views.TimeSheetDeleteView.as_view(), name='timesheet_delete'),

	path('driverassignment_list/', views.DriverAssignmentListView.as_view(), name='driverassignment_list'),
	path('driverassignment_list/<int:pk>', views.DriverAssignmentDetailView.as_view(), name='driverassignment_detail'),
	path('driverassignment_create/', views.DriverAssignmentCreateView.as_view(), name='driverassignment_create'),
	path('driverassignment_update/<int:pk>', views.DriverAssignmentUpdateView.as_view(), name='driverassignment_update'),
	path('driverassignment_delete/<int:pk>', views.DriverAssignmentDeleteView.as_view(), name='driverassignment_delete'),

	
	# path('driverreview_list/', views.DriverReviewListView.as_view(), name='driverreview_list'),
	# path('driverreview_list/<int:pk>', views.DriverReviewDetailView.as_view(), name='driverreview_detail'),
	# path('driverreview_create/', views.DriverReviewCreateView.as_view(), name='driverreview_create'),
	# path('driverreview_update/<int:pk>', views.DriverReviewUpdateView.as_view(), name='driverreview_update'),
	# path('driverreview_delete/<int:pk>', views.DriverReviewDeleteView.as_view(), name='driverreview_delete'),


]



'''
Organization_Affiliate
Event
ShuttleService
AirportShuttleService
SpecialShuttle
SpecialEvent
DriverReview
'''








































