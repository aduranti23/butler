import gi
import json

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk

with open("config/app.json", mode="r", encoding="utf-8") as file:
     appInfos = json.load(file)

class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id=appInfos["applicationId"])
        GLib.set_application_name(appInfos["applicationName"])

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="Butler")
        window.present()

