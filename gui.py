import gi
import json
import service
import servicefetcher

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk

with open("config/app.json", mode="r", encoding="utf-8") as file:
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

class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id=appInfos["applicationId"])
        GLib.set_application_name(appInfos["applicationName"])
        
    def do_activate(self):
        #initialize grid
        srvList = servicefetcher.getServiceList("all")
        srvGridWidget = ServiceGrid(srvList)

        #build window
        window = Gtk.Window(application=self, title="Butler")
        window.set_child(srvGridWidget)
        window.present()



