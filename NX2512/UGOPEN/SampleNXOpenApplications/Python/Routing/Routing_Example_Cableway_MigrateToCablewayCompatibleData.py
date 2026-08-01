#===================================================================================================
#                                       Copyright 2025 Siemens
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
#    An example program that migrates data from pre-NX2412 cableway assembly parts to cableway compatible data.
#
#
#==================================================================================================
import NXOpen
import NXOpen.Assemblies
import NXOpen.MechanicalRouting
import NXOpen.RoutingCommon

#--------------------------------------------------------------------------------------------------
def main() :
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work

    # Open all the components within assembly.
    componentsToOpen = [NXOpen.Assemblies.Component.Null] * 1
    componentsToOpen[0] = workPart.ComponentAssembly.RootComponent
    workPart.ComponentAssembly.OpenComponents(NXOpen.Assemblies.ComponentAssembly.OpenOption.WholeAssembly, componentsToOpen)

    # Fully load the work part.
    theRoutingCommonRoutingManager = NXOpen.RoutingCommon.RoutingManager.GetRoutingManager(theSession)
    theRoutingCommonRoutingManager.LoadData(workPart)

    # Migrate data from pre-NX2412 cableway assembly parts to cableway compatible data.
    routingManager = NXOpen.MechanicalRouting.RoutingManager.GetRoutingManager(theSession)
    routingManager.MigrateToCablewayCompatibleData(workPart)

if __name__ == '__main__':
    main()
