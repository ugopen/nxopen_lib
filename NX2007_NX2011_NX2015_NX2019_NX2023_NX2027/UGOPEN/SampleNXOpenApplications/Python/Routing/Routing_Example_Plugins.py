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
#    A python script that implements example Routing plugins.
#
#
#===================================================================================================
import NXOpen
import NXOpen.UF
import NXOpen.Routing
import collections

#---------------------------------------------------------------------------------------------------
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

#---------------------------------------------------------------------------------------------------
def importExportPlugin( filename ):
    try:
        echo( "\n*** Python importExport plugin called with " + filename )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def routeNodeNamePlugin():
    try:
        echo( "\n*** Python routeNodeName plugin" )

        return "RNx"

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def routeSectionNamePlugin():
    try:
        echo( "\n*** Python routeSectionName plugin" )

        return "RSx"

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def wrappedOverstockLengthCalculationPlugin( overstock ):
    try:
        echo( "\n*** Python Wrapped Overstock Length Calculation plugin called with overstock tag " + str( overstock.Tag ) )

        return 10.0

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def wrappedOverstockLengthCalculationPlugin( overstock ):
    try:
        echo( "\n*** Python Wrapped Overstock Length Calculation plugin called with overstock tag " + str( overstock.Tag ) )

        return 10.0

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def filterBlankingPlugin( segmentOrComponent, logicalAttributeTitle, logicalAttributeValue, variableBuildString ):
    try:
        echo( "\n*** Python Filter Blanking plugin called with object tag tag " + str( segmentOrComponent.Tag ) )

        theSession = NXOpen.Session.GetSession()

        electricalPreferences = theSession.Preferences.RoutingApplicationView.RoutingElectrical;

        apvAttributeTitle = electricalPreferences.GetFilterBlankingAttribute()

        echo( "    APV Attribute Title    : " + apvAttributeTitle);
        echo( "    Logical Attribute Title: " + logicalAttributeTitle);

        if logicalAttributeTitle != apvAttributeTitle:
            echo( "    (Not the same attribute titles. Ignoring this object.)" );
            return False

        logicalAttributeValue = logicalAttributeValue.upper()

        blankTheObject = logicalAttributeValue == "YES"  or logicalAttributeValue == "TRUE" or logicalAttributeValue == "1"

        echo( "    Logical Attribute Value: " + logicalAttributeValue )
        echo( "    Variable Build String  : " + variableBuildString )

        if blankTheObject:
            echo( "    Blank the object!" )

        echo( "" )

        return blankTheObject

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def bomPlugin():
    try:

        echo( "\n*** Python Bill of Materials plugin called." )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def autoroutePlugin( connections ):
    try:
        echo( "\n*** Python autoroute plugin called with " + str( len( connections ) ) + " connections." )

        for connection in connections:
            echo( "  Connection Tag " + str( connection.Tag ) )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def manualroutePlugin( connections ):
    try:
        echo( "\n*** Python manualroute plugin called with " + str( len( connections ) ) + " connections." )

        for connection in connections:
            echo( "  Connection Tag " + str( connection.Tag ) )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def unroutePlugin( connections ):
    try:
        echo( "\n*** Python unroute plugin called with " + str( len( connections ) ) + " connections." )

        for connection in connections:
            echo( "  Connection Tag " + str( connection.Tag ) )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def navigatorObjectSelectedPlugin( navigatorType, selectionType, selectedObjects ):
    try:
        message = "\n*** Python navigatorObjectSelected plugin called with"

        if selectionType == NXOpen.Routing.CustomManager.SelectionType.Selected:
            message += " selected"
        else:
            message += " deselected"

        if navigatorType == NXOpen.Routing.CustomManager.NavigatorType.Connection:
            message += " in the Connection Navigator."
        else:
            message += " in the Component Navigator."

        echo( message )

        for selectedObject in selectedObjects:
            echo( "  Object Tag " + str( selectedObject.Tag ) )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def validateFormboardPlugin( harnessDevices ):
    try:
        echo( "\n*** Python validateFormboard plugin called with " + str( len( harnessDevices ) ) + " harness devices." )

        for harnessDevice in harnessDevices:
            echo( "  Harness Tag " + str( harnessDevice.Tag ) )

        return True

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def disciplineChangedPlugin( previousDisciplineName, newDisciplineName ):
    try:
        echo( "\n*** Python Discipline Changed plugin called." )
        echo("    Previous discipline name '" + previousDisciplineName + "'");
        echo("    New discipline name      '" + newDisciplineName + "'");

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def specificationChangedPlugin( previousSpecificationName, newSpecificationName ):
    try:
        echo( "\n*** Python Specification Changed plugin called." )
        echo("    Previous specification name '" + previousSpecificationName + "'");
        echo("    New specification name      '" + newSpecificationName + "'");

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def sortConnectionsPlugin( sortConnectionsData ):
    try:
        stockDevices = sortConnectionsData.GetStockDevicesToSort()

        echo( "\n*** Python sortConnectionsPlugin plugin called with " + str( len( stockDevices ) ) + " stock devices." )

        stockDeviceTags = []
        for stockDevice in stockDevices:
            echo( "  Stock Device Tag " + str( stockDevice.Tag ) )
            stockDeviceTags.append( stockDevice.Tag )

        stockDeviceTags.sort()

        echo( "" )
        sortedStockDevices = []
        for stockDeviceTag in stockDeviceTags:
            echo( "  Sorted Stock Device Tag " + str( stockDeviceTag ) )
            sortedStockDevices.append( NXOpen.TaggedObjectManager.GetTaggedObject( stockDeviceTag ) )

        sortConnectionsData.SetSortedStockDevices( sortedStockDevices )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def choosePartPlugin( choosePartData ):
    try:

        # At this point, you could open the part to get some of the part attributes from it.
        # For this example, we are just going to return a few default values to Routing.
        choosePartData.SetPartName( "Blind_flange_EN1092.prt" );
        choosePartData.SetPartNumber("ExamplePartNumber001");
        choosePartData.SetMemberName(""); # No member name since this is not a member of a part family.

        # Some example attributes.

        exampleCharacteristics = NXOpen.Session.GetSession().Preferences.RoutingApplicationView.PartPreferences.PartLibrary.CreateCriteria();
        exampleCharacteristics.SetCharacteristic("USER_CHARX_TITLE1", "User_charx_value1");
        exampleCharacteristics.SetCharacteristic("USER_CHARX_TITLE2", "User_charx_value2");

        choosePartData.SetCharacteristics(exampleCharacteristics);

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def stockComponentNamePlugin( dataObject ):
    try:

        if not hasattr(stockComponentNamePlugin, "stockNumberCounter"):
            stockComponentNamePlugin.stockNumberCounter = 0  # it doesn't exist yet, so initialize it

        stockComponentNamePlugin.stockNumberCounter += 1

        stockName = "StockComponent_" + str( stockComponentNamePlugin.stockNumberCounter );
        homeFolder = "";

        ufSession = NXOpen.UF.UFSession.GetUFSession()
        isManagedMode = ufSession.Uf.IsUgmanagerActive()
        if isManagedMode:
            ugmgr = ufSession.Ugmgr

            rootFolderTag = ugmgr.AskRootFolder()
            homeFolder = ugmgr.AskFolderName( rootFolderTag )

        dataObject.ComponentName = stockName;
        dataObject.RenameComponentPartFlag = True;

        dataObject.NativeFileName = stockName;
        dataObject.NativePath = ""; # An empty path means the current directory.
        dataObject.ManagedModeFolderName = homeFolder + ":StockComponents";
        dataObject.ManagedModeItemName = stockName;
        dataObject.ManagedModeItemRevision = "A";
        dataObject.ManagedModeItemType = "Item";

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def startup( argc, args ):
    try:

        customManager = NXOpen.Session.GetSession().RouteCustomManager

        customManager.SetHrnPreImportPlugin( importExportPlugin )
        customManager.SetHrnPostExportPlugin( importExportPlugin )
        customManager.SetCmpPreImportPlugin( importExportPlugin )
        customManager.SetCmpPostExportPlugin( importExportPlugin )
        customManager.SetPlmXmlPreImportPlugin( importExportPlugin )
        customManager.SetPlmXmlPostExportPlugin( importExportPlugin )
        customManager.SetPlmXmlRouteNodeNamePlugin( routeNodeNamePlugin )
        customManager.SetPlmXmlRouteSectionNamePlugin( routeSectionNamePlugin )
        customManager.SetWrappedOverstockLengthCalculationPlugin( wrappedOverstockLengthCalculationPlugin )
        customManager.SetFilterBlankingPlugin( filterBlankingPlugin )
        customManager.SetBomPlugin( bomPlugin )
        customManager.SetAutoRoutePlugin( autoroutePlugin )
        customManager.SetManualRoutePlugin( manualroutePlugin )
        customManager.SetUnroutePlugin( unroutePlugin )
        customManager.SetNavigatorObjectSelectedPlugin( navigatorObjectSelectedPlugin )
        customManager.SetValidateFormboardPlugin( validateFormboardPlugin )
        customManager.SetDisciplineChangedPlugin( disciplineChangedPlugin )
        customManager.SetSpecificationChangedPlugin( specificationChangedPlugin )
        customManager.SetSortConnectionsPlugin( sortConnectionsPlugin )
        customManager.SetChoosePartPlugin( choosePartPlugin )

        # Routing calls the stock component name plugin when creating permanent stock using the
        # Convert to Stock as Components command.
        customManager.SetStockComponentNamePlugin( stockComponentNamePlugin );

        # Routing calls the temporary stock component name plugin when you are creating stocks
        # on the fly in Stock as Components mode.
        customManager.SetTemporaryStockComponentNamePlugin( stockComponentNamePlugin );

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

    return 0 # No errors.
