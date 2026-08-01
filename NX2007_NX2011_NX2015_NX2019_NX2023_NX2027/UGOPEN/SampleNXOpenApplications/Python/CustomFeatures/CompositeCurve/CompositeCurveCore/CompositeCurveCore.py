#===================================================================================
# 
#       Copyright 2016 Siemens Product Lifecycle Management Software Inc. 
#                           All Rights Reserved.
# 
#   
#=============================================================================
#File description: Sample NX/Open Application for Custom feature 
#=============================================================================
#
#==============================================================================
#   Purpose:  This TEMPLATE file contains Python source to guide you in the
#   construction of core library for custom feature.
# 
#   The information in this file provides you with the following:
# 
#   1.  Help on how to write Core library for custom feature
#       using APIs provided in NXOpen namespace
#   2.  The empty callback methods (stubs) associated with custom feature
#       have also been placed in this file. These empty methods have been
#       created simply to start you along with your coding requirements.
#       The method name, argument list and possible return values have already
#       been provided for you.
#==============================================================================

#------------------------------------------------------------------------------
# These imports are needed for the following template code
#------------------------------------------------------------------------------
import NXOpen
import NXOpen.Features

#------------------------------------------------------------------------------
# Represents NXOpen application cls
#------------------------------------------------------------------------------
class CompositeCurveCore:
    # static class members
    theSession = None
    
    #------------------------------------------------------------------------------
    # Constructor for class
    #------------------------------------------------------------------------------
    def __init__(self):
        try:
            theSession = NXOpen.Session.GetSession()

            cfClass = theSession.CustomFeatureClassManager.GetClassFromName("NXOpen.CustomFeature.SampleCompositeCurve")   
            # Add create feature geometry callback, 
            # when invoked output geometry of feature should be created in this callback.
            cfClass.AddCreateFeatureGeometryHandler(CompositeCurveCore.createGeometry_cb)
            # Add information callback
            # This is invoked when user does RMB on feature in navigator and select information option.
            cfClass.AddInformationHandler(CompositeCurveCore.information_cb)
            
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            raise ex        


    @staticmethod
    def ExtractCurve(curve):
        
        extractCurve = None

        session = NXOpen.Session.GetSession()

        restoreVisibilty = curve.Visibility

        curve.SetVisibility(NXOpen.SmartObjectVisibilityOption.Visible)

        extractedCurve  = session.Parts.Work.Curves.CreateExtractedCurve(curve, 0, 0, NXOpen.Xform.Null, 0.01, NXOpen.SmartObjectUpdateOption.WithinModeling)

        extractedCurve.SetVisibility(NXOpen.SmartObjectVisibilityOption.Visible)

        extractedCurve.RedisplayObject()

        extractedCurve.RemoveParameters()

        curve.SetVisibility(restoreVisibilty)

        return extractedCurve


    @staticmethod
    def createGeometry_cb(event):
        
        error = 0

        customFeature = event.GetCustomFeature()

        if customFeature != None:

            cFData = customFeature.FeatureData
            
            sectionAttrib = None

            if cFData != None and cFData.HasCustomAttribute("sectionAttrib", NXOpen.Features.CustomAttributeType.Tag):

                sectionAttrib = cFData.CustomTagAttributeByName("sectionAttrib")

                sectionObj = sectionAttrib.Value
                
                objects =[]
                try:
                    objects = sectionObj.EvaluateAndAskOutputEntities()
                except:
                    event.ErrorCode = 1
                    return 0

                if len(objects) < 1:
                    # Section is empty after evaluation, this is error condition
                    event.ErrorCode = 1
                    return error
                
                trackingObjectList = []

                for object in objects:

                    extractedCurve = CompositeCurveCore.ExtractCurve(object)

                    trackObject = event.CreateTrackingDataForNXObject(extractedCurve);

                    sourceEntities = [object]

                    trackObject.AddTagSourceEntities(sourceEntities)

                    trackingObjectList.append(trackObject)

                event.AppendOutputTrackingData(trackingObjectList)
        return error


    @staticmethod
    def information_cb(informationEvent):
        error = 0
        informationEvent.SetInformation("Custom information of feature")
        return error


    @staticmethod
    def WriteToListingWindow(string):
        theSession = NXOpen.Session.GetSession()
        theSession.ListingWindow.Open()
        theSession.ListingWindow.WriteLine(string)
        theSession.ListingWindow.Close()
        return None

    #------------------------------------------------------------------------------
    # Method Name: Dispose
    #------------------------------------------------------------------------------
    def Dispose(self):
        pass

    
def main():
    theCompositeCurveCore = None
    try:
        theCompositeCurveCore =  CompositeCurveCore()
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        NXOpen.UI.GetUI().NXMessageBox.Show("Custom Feature", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    finally:
        if theCompositeCurveCore != None:
            theCompositeCurveCore.Dispose()
            theCompositeCurveCore = None
    
if __name__ == '__main__':
    main()
