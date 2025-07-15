{
    "name":"Appointment Pre-book Tracker",
    "version":"18.0.1.0.0",
    "category":"Website/Appointments",
    "summary":"Track appointment form views, confirms, and cancellations",
    "description":"Module adds a prebook model to log visitor actions on appointment forms",
    "depends":["website_appointment"],
    "data":[
        "security/ir.model.access.csv",
        "views/appointment_prebook_views.xml",
    ],
    "installable":True,
    "application":False,
    "auto_install":False,
}