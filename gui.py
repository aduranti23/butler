import gi

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk

class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.magicwilbur.Butler")
        GLib.set_application_name("Butler")

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="Butler")
        window.present()

