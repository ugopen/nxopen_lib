#----------------------------------------------------------------------------
# Copyright 2012 Siemens Product Lifecycle Management Software Inc.
# All Rights Reserved.
#----------------------------------------------------------------------------
# 
#
# python_part_callbacks.py
#
# Description:
#     This simple demo registers part callbacks for every available reason
#     via the Python language.
#
#     TODO: Rewrite below documentation for Python
#
#     After compiling and linking this demo program, the output class or jar needs
#     to be placed in a folder called startup (for example c:\\user_dir\\startup).
#     Also the UGII_USER_DIR enviornment variable needs to point to the startup
#     directory's parent folder (for example: UGII_USER_DIR=c:\\user_dir).
#     Once you have the startup directory and user dir environment variable
#     set up, start NX.  The part callbacks will be registered at startup.
#     Now anytime you create new, open, save, save as, close, modify, rename,
#     or change the workpart your callbacks will be executed.
#
#     To demo all of the available part callbacks at runtime - compile and link
#     execute_all_part_callbacks.c.
#     Then start NX and go to File->Execute->NX Open and select your compiled
#     execute_all_callbacks program.
#
#---------------------------------------------------------------------------/

import NXOpen

the_python_part_callbacks = None
idPartCreated1 = 0
idPartOpened1 = 0
idPartSaved1 = 0
idPartSavedAs1 = 0
idPartClosed1 = 0
idPartModified1 = 0
idPartRenamed1 = 0
idWorkPartChanged1 = 0

#registered = False

# Called manually from File->Execute->NX Open
def main(args):
    try:
        #global registered
        #registered = False
        session = NXOpen.Session.GetSession()
        initializeCallbacks(session)
    except Exception as ex:
        print(ex)

# Initialize Callbacks - registers the part callbacks with NX
def initializeCallbacks(session):
    try:
        #global registered
        #if not registered:
        partCreatedCallbacks = PythonPartCreatedCallbacks(session)
        idPartCreated1 = partCreatedCallbacks.GetCallbackId()
        partOpenedCallbacks = PythonPartOpenedCallbacks(session)
        idPartOpened1 = partOpenedCallbacks.GetCallbackId()
        partSavedCallbacks = PythonPartSavedCallbacks(session)
        idPartSaved1 = partSavedCallbacks.GetCallbackId()
        partSavedAsCallbacks = PythonPartSavedAsCallbacks(session)
        idPartSavedAs1 = partSavedAsCallbacks.GetCallbackId()
        partClosedCallbacks = PythonPartClosedCallbacks(session)
        idPartClosed1 = partClosedCallbacks.GetCallbackId()
        partModifiedCallbacks = PythonPartModifiedCallbacks(session)
        idPartModified1 = partModifiedCallbacks.GetCallbackId()
        partRenamedCallbacks = PythonPartRenamedCallbacks(session)
        idPartRenamed1 = partRenamedCallbacks.GetCallbackId()
        partWorkPartChangedCallbacks = PythonWorkPartChangedCallbacks(session)
        idWorkPartChanged1 = partWorkPartChangedCallbacks.GetCallbackId()
        #registered = True
    except Exception as ex:
        session.ListingWindow.Open()
        session.ListingWindow.WriteLine(str(ex))

class BasePartCallback (object):
    def __init__(self, session):
        self.session = session
        self.lw = session.ListingWindow
        self._id = None
        
    def GetCallbackId(self):
        return self._id

# python_part_callbacks class used to demo all of the available part related callback functions in the java language
#class PythonPartCreatedCallbacks (BasePartCallback, NXOpen.PartCollection.PartCreatedHandler):
class PythonPartCreatedCallbacks (BasePartCallback):
    def __init__(self, session):
        super(PythonPartCreatedCallbacks, self).__init__(session)
        self._id = session.Parts.AddPartCreatedHandler(self.PartCreatedHandler)

    # Called when a new part is created
    # Prints the name of the created part to the listing window
    def PartCreatedHandler(self, part):
        try:
            self.lw.Open()
            self.lw.WriteLine("    Python created: %s" % part.FullPath)
        except Exception as ex:
            print(ex)

#class PythonPartOpenedCallbacks (BasePartCallback, NXOpen.PartCollection.PartOpenedHandler):
class PythonPartOpenedCallbacks (BasePartCallback):
    def __init__(self, session):
        super(PythonPartOpenedCallbacks, self).__init__(session)
        self._id = session.Parts.AddPartOpenedHandler(self.PartOpenedHandler)

    # Called when a part is opened
    # Prints the name of the opened part to the listing window
    def PartOpenedHandler(self, part):
        try:
            self.lw.Open()
            self.lw.WriteLine("    Python opened: %s" % part.FullPath)
        except Exception as ex:
            print(ex)

#class PythonPartSavedCallbacks (BasePartCallback, NXOpen.PartCollection.PartSavedHandler):
class PythonPartSavedCallbacks (BasePartCallback):
    def __init__(self, session):
        super(PythonPartSavedCallbacks, self).__init__(session)
        self._id = session.Parts.AddPartSavedHandler(self.PartSavedHandler)

    # Called when a part is saved
    # Prints the name of the saved part to the listing window
    def PartSavedHandler(self, part):
        try:
            self.lw.Open()
            self.lw.WriteLine("    Python saved: %s" % part.FullPath)
        except Exception as ex:
            print(ex)

#class PythonPartSavedAsCallbacks (BasePartCallback, NXOpen.PartCollection.PartSavedAsHandler):
class PythonPartSavedAsCallbacks (BasePartCallback):
    def __init__(self, session):
        super(PythonPartSavedAsCallbacks, self).__init__(session)
        self._id = session.Parts.AddPartSavedAsHandler(self.PartSavedAsHandler)

    # Called when a part is saved as
    # Prints the name of the saved as part to the listing window
    def PartSavedAsHandler(self, part):
        try:
            self.lw.Open()
            self.lw.WriteLine("    Python saved as: %s" % part.FullPath)
        except Exception as ex:
            print(ex)

#class PythonPartClosedCallbacks (BasePartCallback, NXOpen.PartCollection.PartClosedHandler):
class PythonPartClosedCallbacks (BasePartCallback):
    def __init__(self, session):
        super(PythonPartClosedCallbacks, self).__init__(session)
        self._id = session.Parts.AddPartClosedHandler(self.PartClosedHandler)

    # Called when a part is closed
    # Prints the name of the closed part to the listing window
    def PartClosedHandler(self, part):
        try:
            self.lw.Open()
            self.lw.WriteLine("    Python closed: %s" % part.FullPath)
        except Exception as ex:
            print(ex)

#class PythonPartModifiedCallbacks (BasePartCallback, NXOpen.PartCollection.PartModifiedHandler):
class PythonPartModifiedCallbacks (BasePartCallback):
    def __init__(self, session):
        super(PythonPartModifiedCallbacks, self).__init__(session)
        self._id = session.Parts.AddPartModifiedHandler(self.PartModifiedHandler)
  
    # Called when a part is modified for the first time
    # Prints the name of the modified part to the listing window
    def PartModifiedHandler(self, part):
        try:
            self.lw.Open()
            self.lw.WriteLine("    Python modified: %s" % part.FullPath)
        except Exception as ex:
            print(ex)

#class PythonPartRenamedCallbacks (BasePartCallback, NXOpen.PartCollection.PartRenamedHandler):
class PythonPartRenamedCallbacks (BasePartCallback):
    def __init__(self, session):
        super(PythonPartRenamedCallbacks, self).__init__(session)
        self._id = session.Parts.AddPartRenamedHandler(self.PartRenamedHandler)

    # Called when a part is renamed
    # Prints the name of the renamed part to the listing window
    def PartRenamedHandler(self, part):
        try:
            self.lw.Open()
            self.lw.WriteLine("    Python renamed: %s" % part.FullPath)
        except Exception as ex:
            print(ex)
    
#class PythonWorkPartChangedCallbacks (BasePartCallback, NXOpen.PartCollection.WorkPartChangedHandler):
class PythonWorkPartChangedCallbacks (BasePartCallback):
    def __init__(self, session):
        super(PythonWorkPartChangedCallbacks, self).__init__(session)
        self._id = session.Parts.AddWorkPartChangedHandler(self.WorkPartChangedHandler)

    # Called when the workpart changes
    # Prints the name of old workpart and new workpart to the listing window
    def WorkPartChangedHandler(self, part):
        try:
            self.lw.Open()
            self.lw.WriteLine("    Python work part changed: %s" % part.FullPath)
            if (part == None):
                self.lw.WriteLine("        Old Work Part: None")
            else:
                self.lw.WriteLine("        Old Work Part: %s" % part.FullPath)
            if (self.session.Parts.BaseWork == None):
                self.lw.WriteLine("        New Work Part: None")
            else:
                self.lw.WriteLine("        New Work Part: %s" % self.session.Parts.BaseWork.FullPath)
        except Exception as ex:
            print(ex)

if __name__ == '__main__':
    main("")

