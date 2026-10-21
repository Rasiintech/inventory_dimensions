app_name = "inventory_dimensions"
app_title = "Inventory Dimensions"
app_publisher = "8848 Digital LLP"
app_description = "Inventory Dimensions"
app_email = "nandhini@8848digital.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/inventory_dimensions/css/inventory_dimensions.css"
# app_include_js = "/assets/inventory_dimensions/js/inventory_dimensions.js"

# include js, css files in header of web template
# web_include_css = "/assets/inventory_dimensions/css/inventory_dimensions.css"
# web_include_js = "/assets/inventory_dimensions/js/inventory_dimensions.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "inventory_dimensions/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Delivery Note": "inventory_dimensions/customizations/delivery_note/delivery_note.js",
	"Sales Invoice": "inventory_dimensions/customizations/sales_invoice/sales_invoice.js",
	"Stock Entry": "inventory_dimensions/customizations/stock_entry/stock_entry.js",
	"Stock Reconciliation": "inventory_dimensions/customizations/stock_reconciliation/stock_reconciliation.js",
	"Purchase Receipt": "inventory_dimensions/customizations/purchase_receipt/purchase_receipt.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "inventory_dimensions.utils.jinja_methods",
# 	"filters": "inventory_dimensions.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "inventory_dimensions.install.before_install"
# after_install = "inventory_dimensions.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "inventory_dimensions.uninstall.before_uninstall"
# after_uninstall = "inventory_dimensions.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "inventory_dimensions.utils.before_app_install"
# after_app_install = "inventory_dimensions.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

after_migrate = "inventory_dimensions.migrate.after_migrate"
# before_app_uninstall = "inventory_dimensions.utils.before_app_uninstall"
# after_app_uninstall = "inventory_dimensions.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "inventory_dimensions.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Stock Entry": "inventory_dimensions.inventory_dimensions.customizations.stock_entry.stock_entry.OverideStockEntry"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"inventory_dimensions.tasks.all"
# 	],
# 	"daily": [
# 		"inventory_dimensions.tasks.daily"
# 	],
# 	"hourly": [
# 		"inventory_dimensions.tasks.hourly"
# 	],
# 	"weekly": [
# 		"inventory_dimensions.tasks.weekly"
# 	],
# 	"monthly": [
# 		"inventory_dimensions.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "inventory_dimensions.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "inventory_dimensions.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "inventory_dimensions.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["inventory_dimensions.utils.before_request"]
# after_request = ["inventory_dimensions.utils.after_request"]

# Job Events
# ----------
# before_job = ["inventory_dimensions.utils.before_job"]
# after_job = ["inventory_dimensions.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"inventory_dimensions.auth.validate"
# ]
