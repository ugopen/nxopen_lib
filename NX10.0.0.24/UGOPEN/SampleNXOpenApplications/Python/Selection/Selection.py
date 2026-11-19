#===================================================================================
# 
#       Copyright 2014 Siemens Product Lifecycle Management Software Inc. 
#                           All Rights Reserved.
# 
#   
#===================================================================================
# File Description:
#
# This example demonstrates alternatives to the code recorded while performing a
# 'Select All' using various filtering methods before an operation.  The example
# shows how filtering by type, detailed type, layers, display attributes and color
# can be accomplished via automation. The example gets the datums on the work part
# that satisfy the filtering criteria and blanks the datums.  The code assumes that
# the example part file, Selection_datums.prt or a part with datums is already opened.
#
#===================================================================================
#

import NXOpen

def main():

    marksRecycled = False
    undoUnavailable = False
    undoMark = 0
    length = 0

    theSession = NXOpen.Session.GetSession()
    theUI = NXOpen.UI.GetUI()
    theMessageBox = theUI.NXMessageBox

    #  FILTERING BY TYPE:
    #  Use in place of the journal code for "Select All" with filter
    #  type set to "Datums".
    undoMark = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Blank")
    workPart = theSession.Parts.Work
    datums = workPart.Datums
    ddoList = list(datums)

    theSession.DisplayManager.BlankObjects(ddoList)

    theSession.DisplayManager.MakeUpToDate()
    theMessageBox.Show(
        "Filtering By Type", NXOpen.NXMessageBox.DialogType.Information,
        "%d datums were blanked." % len(ddoList))

    marksRecycled, undoUnavailable = theSession.UndoLastNVisibleMarks(1)


    #  FILTERING BY DETAILED TYPE:
    #  Use in place of the journal code for "Select All" with detailed filter type
    #  set to "Datums - Datum Planes".
    undoMark = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Blank")

    length = 0
    for obj in datums:
        if isinstance(obj,NXOpen.DatumPlane):
            obj.Blank()
            length = length + 1

    theSession.DisplayManager.MakeUpToDate()
    theMessageBox.Show(
        "Filtering By Detailed Type", 
        NXOpen.NXMessageBox.DialogType.Information,
        "%d datum planes were blanked." % length)

    marksRecycled, undoUnavailable = theSession.UndoLastNVisibleMarks(1)


    #  FILTERING BY LAYER:
    #  Use in place of the journal code for "Select All" with filter type
    #  set to "Layers - 10".
    undoMark = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Blank")

    length = 0
    for obj in theSession.Parts.Work.Datums:
        if obj.Layer == 10:
            obj.Blank()
            length = length + 1

    theSession.DisplayManager.MakeUpToDate()
    theMessageBox.Show(
        "Filtering By Layer", 
        NXOpen.NXMessageBox.DialogType.Information,
        "%d datums on layer 10 were blanked." % length)
    marksRecycled, undoUnavailable = theSession.UndoLastNVisibleMarks(1)


    #  FILTERING BY DISPLAY ATTRIBUTES:
    #  Use in place of the journal code for "Select All" with filter type
    #  set to "Display Attributes - Dashed, Thick Width".
    undoMark = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Blank")

    length = 0
    for obj in theSession.Parts.Work.Datums:
        if (obj.LineFont == NXOpen.DisplayableObject.ObjectFont.Dashed and
            obj.LineWidth == NXOpen.DisplayableObject.ObjectWidth.Thick):
            obj.Blank()
            length = length + 1

    theSession.DisplayManager.MakeUpToDate()
    theMessageBox.Show(
        "Filtering By Display Attributes", 
        NXOpen.NXMessageBox.DialogType.Information,
        "%d datums with dashed line font and thick width were blanked." % length)

    marksRecycled, undoUnavailable = theSession.UndoLastNVisibleMarks(1)

    #  FILTERING BY COLOR:
    #  Use in place of the journal code for "Select All" with filter type
    #  set to "Color - 134".
    undoMark = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Blank")

    length = 0
    for obj in theSession.Parts.Work.Datums:
        if obj.Color == 134:
            obj.Blank()
            length = length + 1

    theSession.DisplayManager.MakeUpToDate()
    theMessageBox.Show(
        "Filtering By Color", 
        NXOpen.NXMessageBox.DialogType.Information,
        "%d datums with color 134 were blanked." % length)

    marksRecycled, undoUnavailable = theSession.UndoLastNVisibleMarks(1)

if __name__ == "__main__":
    main()
