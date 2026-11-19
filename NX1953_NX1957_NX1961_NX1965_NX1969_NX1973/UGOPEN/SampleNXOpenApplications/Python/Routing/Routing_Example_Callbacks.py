#===================================================================================================
#               Copyright 2017 Siemens Product Lifecycle Management Software Inc.
#===================================================================================================
#
#    NOTE:  NX Development provides programming examples for illustration only.
#    NX Development assumes you are familiar with the programming language
#    demonstrated in these examples, and the tools used to create and debug NX/Open
#    programs. GTAC support professionals can help explain the functionality of
#    a particular procedure, but neither GTAC nor NX Development will modify
#    these examples to provide added functionality or construction procedures.
#
#File description:
#
#    A python script that implements example Routing callbacks.
#
#
#===================================================================================================
import NXOpen
import NXOpen.Routing

#-----------------------------------------------------------------------------------------------
def echo( message ):
    try:
        syslog = NXOpen.Session.GetSession().LogFile
        syslog.WriteLine( message )

        listingWindow = NXOpen.Session.GetSession().ListingWindow
        listingWindow.Open()
        listingWindow.WriteLine( message )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#-----------------------------------------------------------------------------------------------
def autorouteCallback( objects ):
    try:
        echo( "\n*** Python autoroute callback called with " + str( len( objects ) ) + " objects." )

        for object in objects:
            echo( "  Object Tag " + str( object.Tag ) )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#-----------------------------------------------------------------------------------------------
def unrouteCallback( objects ):
    try:
        echo( "\n*** Python unroute callback called with " + str( len( objects ) ) + " objects." )

        for object in objects:
            echo( "  Object Tag " + str( object.Tag ) )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

  
#-----------------------------------------------------------------------------------------------
def startup( argc, args ):
    try:

        customManager = NXOpen.Session.GetSession().RouteCustomManager

        customManager.AddCallback( NXOpen.Routing.CustomManager.CallbackReason.WireRouteAuto, autorouteCallback )
        customManager.AddCallback( NXOpen.Routing.CustomManager.CallbackReason.WireUnroute,   unrouteCallback )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

    return 0 # No errors.


