# -*- coding: UTF-8 -*-

import tkinter.ttk
from tkinter import *
from distutils.core import setup



class MainApplication(tkinter.Frame):
    @classmethod
    def main(cls):
        root = tkinter.Tk()
        app = cls(root)
        app.master.title('Sunnova Snapshot Tool')
        root.resizable(True, True)
        root.mainloop()

    def __init__(self, parent=None, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.grid(sticky=N+E+S+W)

        # Var-Declaration
        self.h = 600
        self.w = 1200
        self.widget_fr_opts = dict(relief='groove', borderwidth=1, bg='#EFEFFB')

        #  Widget-Creation
        self.rootframe = RootFrame(self)
        self._visible_ = self.rootframe  # internal updater what frame is visible - starting with rootframe on init
        self.statusbar = Statusbar(self)
        self.navbar = Navbar(self)
        self.main_db = MainDB(self)

        #  Widget-Design

        # Widget-Arrangement
        self.grid_rowconfigure(0, minsize=self.h * 0.95)
        self.grid_rowconfigure(1, minsize=self.h * 0.05)
        self.grid_columnconfigure(0, minsize=self.w*0.15)
        self.grid_columnconfigure(1, minsize=self.w*0.85)
        self.navbar.grid(sticky=N+S+E+W, column=0, row=0)
        self.main_db.grid(sticky=N+E+S+W, column=1, row=0)
        self.rootframe.grid(sticky=N+E+S+W, column=1, row=0)
        self.statusbar.grid(sticky=W+E, column=0, columnspan=2, row=1)

        self.grid_columnconfigure(1, weight=1)
        self.statusbar.columnconfigure(0, weight=1)
        self.rootframe.columnconfigure(0, weight=1)
        self.main_db.columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.navbar.rowconfigure(4, weight=1)
        self.rootframe.rowconfigure(0, weight=1)
        self.main_db.rowconfigure(0, weight=1)

        self.rootframe.lift(self.main_db)

    def visualize(self, master):
        """Lifts master to upper Level"""
        master.lift(self.rootframe)
        self._visible_ = master

    def event_handler(self):
        pass

    def start_subapp(self, app):
        self.visualize(app)
        app.activate_content()


class RootFrame(tkinter.Frame):
    """General Launcher Frame as a Placeholder"""

    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        #  Var-Daclaration
        self.widget_fr_opts = dict(relief='sunken', borderwidth=1)
        self.widget_grid_opts = dict(sticky=N+E+S+W, padx=1, pady=1)

        #  Widget-Creation
        self.Image = tkinter.ttk.Label(self, text='Upload PDF\'s within the side menu', anchor='center')

        #  Widget-Design
        self.configure(**self.widget_fr_opts)

        #  Widget-Arrangement
        self.Image.grid(column=0, row=0, **self.widget_grid_opts)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


class Navbar(tkinter.Frame):
    """vertical NavBar"""

    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        #  Var-Daclaration
        self._info_ = tkinter.StringVar()
        self.widget_fr_opts = dict(relief='groove', borderwidth=1)
        self.widget_grid_opts = dict(sticky=N+E+S+W, padx=1, pady=1)
        self.widget_grid_subopts = dict(sticky=W+N+E, padx=1, pady=1)
        self._statusbar = parent.statusbar

        #  Widget-Creation -- Active Buttons On Program Window
        self._info_.set('Menu:\n    Actions')
        self.TextInfo = tkinter.ttk.Label(self, textvariable=self._info_)
        self.Btn_Progress = tkinter.ttk.Button(self, text='Start Progress',
                                               command=lambda: self.statusbar_input('Starting Extraction ...'))   # some code being started
        self.Btn_Database = tkinter.ttk.Button(self, text='Database',
                                               command=lambda: parent.start_subapp(parent.main_db))  # Database window is lifted and content initialized
        
       
        
        
        self.Btn_Exit = tkinter.ttk.Button(self, text='Exit', command=parent.quit)

        #  Widget-Design
        self.configure(**self.widget_fr_opts)

        #  Widget-Arrangement
        self.TextInfo.grid(column=0, row=1, **self.widget_grid_subopts)
        self.Btn_Progress.grid(column=0, row=2, **self.widget_grid_subopts)
        self.Btn_Database.grid(column=0, row=3, **self.widget_grid_subopts)
        self.Btn_Exit.grid(column=0, row=4, **self.widget_grid_subopts)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)

    def statusbar_input(self, comm: str):
        self._statusbar.start()
        self._statusbar._info_.set(comm)

class Statusbar(tkinter.Frame):
    """Status-Bar at the bottom"""

    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        #  Var-Daclaration
        self.prgrvalue = tkinter.IntVar()
        self._info_ = tkinter.StringVar()
        self._user_ = 'some user'
        self.widget_fr_opts = dict(relief='sunken', borderwidth=1)
        self.widget_grid_opts = dict(padx=1, pady=1)
        self.widget_grid_subopts = dict(padx=1, pady=1)  # sticky=W + E,

        #  Widget-Creation
        self._info_.set('Scanning ...')
        self.prgrvalue.set(0)
        self.TextInfo = tkinter.ttk.Label(self, textvariable=self._info_)
        self.UserInfo = tkinter.ttk.Label(self, textvariable=self._user_)
        self.progress_ = tkinter.ttk.Progressbar(self)
        self.Btn_Move = tkinter.ttk.Button(self, text='Move it', command=lambda: self.start())  # just for initial testing, will be removed later
        self.Btn_Stop = tkinter.ttk.Button(self, text='Stop it', command=lambda: self.stop())

        #  Widget-Design
        self.configure(**self.widget_fr_opts)
        self.progress_.configure(length=200, mode='determinate', orient=tkinter.HORIZONTAL)

        #  Widget-Arrangement
        self.progress_.grid(sticky=W+E, column=0, row=0, **self.widget_grid_subopts)
        self.TextInfo.grid(column=1, row=0, **self.widget_grid_subopts)
        self.UserInfo.grid(column=2, row=0, padx=1, pady=1)  # sticky=E,
        self.Btn_Move.grid(column=3, row=0, **self.widget_grid_subopts)
        self.Btn_Stop.grid(column=4, row=0, **self.widget_grid_subopts)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, minsize=200)
        self.grid_columnconfigure(2, minsize=200)

    def start(self):
        # just testing
        self.progress_.start()

    def stop(self):
        # just testing
        self.progress_.stop()


class MainDB(tkinter.Frame):
    """Frame for visualizing database."""

    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        #  Var-Daclaration
        self._activated_ = False
        self._source_ = None
        self.combotext = tkinter.StringVar()
        self.combotext.set('Please choose a tab...')
        self.widget_fr_opts = dict(relief='sunken', borderwidth=1)
        self.widget_grid_opts = dict(sticky=N+E+S+W, padx=1, pady=1)

        #  Widget-Creation
        #  CREATION OF TOOLS TO MANIPULATE DATABASE
        self.toolframe = tkinter.Frame(self, width=100, height=50, relief='groove', borderwidth=1)
        self.combo = tkinter.ttk.Combobox(self.toolframe, textvariable=self.combotext)
        # more to come

        #  CREATION OF DATABASE'WINDOW
        self.dbframe = tkinter.Frame(self, width=100, relief='groove', borderwidth=1)
        self.db_treeview = tkinter.ttk.Treeview(self.dbframe, columns=('size', 'modified'), selectmode='extended')
        #  more to come

        #  Widget-Design

        #  Widget-Arrangement
        self.toolframe.grid(column=0, row=0, sticky=N+E+W, padx=1, pady=1)
        self.combo.grid(column=0, row=0, sticky=N+E, padx=1, pady=1)
        self.dbframe.grid(column=0, row=1,  sticky=NSEW, padx=1, pady=1)
        self.db_treeview.grid(column=0, row=0, sticky=NSEW, padx=1, pady=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.dbframe.grid_columnconfigure(0, weight=1)
        self.dbframe.grid_rowconfigure(0, weight=1, minsize=600)
        self.toolframe.grid_columnconfigure(0, weight=1)
        self.toolframe.grid_rowconfigure(0, weight=1)

    def activate_content(self):
        pass

    def db_connector(self, comm: str, save=False) -> bool:
        #  some connection code
        pass


if __name__ == '__main__':

    UserScreen = MainApplication.main()
