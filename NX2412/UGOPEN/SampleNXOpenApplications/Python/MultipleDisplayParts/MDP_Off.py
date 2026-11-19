#===================================================================================
# 
#       Copyright 2014 Siemens Product Lifecycle Management Software Inc. 
#                           All Rights Reserved.
# 
#   
#===================================================================================
# File Description:
#  MDP example turning MDP off
#
#===================================================================================
#

import NXOpen

def main():

    theSession = NXOpen.Session.GetSession()
    theUI = NXOpen.UI.GetUI()
    theMessageBox = theUI.NXMessageBox

    theSession.Parts.SetAllowMultipleDisplayedParts(False)

    theMDPStatus = theSession.Parts.AllowMultipleDisplayedParts
	
    theStatusString =""
	
    if theMDPStatus == NXOpen.PartCollection.MultipleDisplayedPartStatus.Disabled:
        theStatusString = "Disabled"
    elif theMDPStatus == NXOpen.PartCollection.MultipleDisplayedPartStatus.DisabledByCustomer:
        theStatusString = "DisabledByCustomer"
    else: 
        theStatusString = "Enabled"
	
    theMessageBox.Show(
        "Multiple Display Part Status", 
        NXOpen.NXMessageBox.DialogType.Information,
        "The status is {}.".format(theStatusString))

if __name__ == "__main__":
    main()
