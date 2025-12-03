import gi
import json
import service
import servicefetcher
import traceback

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk

with open("butler/config/app.json", mode="r", encoding="utf-8") as file:
     appInfos = json.load(file)

class ServiceGrid(Gtk.Box):
     def __init__(self, serviceList, **kwargs):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, **kwargs)
        grid = Gtk.Grid()
        headerServiceId = Gtk.Button(label="ID")
        headerDescription = Gtk.Button(label="Description")
        headerState = Gtk.Button(label="State")
        grid.attach(headerServiceId, 0,0,1,1)
        grid.attach(headerDescription, 1,0,1,1)
        grid.attach(headerState, 2,0,1,1)

        indexRow = 1
        for element in serviceList:
            elementSrvId = Gtk.Button(label=element.serviceId)
            elementSrvDesc = Gtk.Button(label=element.description)
            elementSrvState = Gtk.Button(label=element.state)
            grid.attach(elementSrvId, 0, indexRow,1,1)
            grid.attach(elementSrvDesc, 1, indexRow,1,1)
            grid.attach(elementSrvState, 2, indexRow,1,1)
            indexRow += 1
        self.append(grid)

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(application=kwargs.pop("application", None), default_width=400, title="Butler")

        #initialize service grid
        srvList = servicefetcher.getServiceList("all")
        srvGridWidget = ServiceGrid(srvList)

        #append widgets to box
        box = Gtk.CenterBox()
        self.set_child(box)
        box.set_start_widget(srvGridWidget)


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id=appInfos["applicationId"])
        GLib.set_application_name(appInfos["applicationName"])
        
    def do_activate(self):
        #build window
        try:
            window = MainWindow(application=self)
            window.present()
        except Exception as e:
            print("Error during activation", e)
            traceback.print_exc()
            dlg = Gtk.MessageDialog(
              transient_for=self.window if hasattr(self, "window") else None,
             flags=0,
             message_type=Gtk.MessageType.ERROR,
             buttons=Gtk.ButtonsType.CLOSE,
             text="Error during start"
            )
            dlg.format_secondary_text(str(e))
            dlg.run()
            dlg.destroy()