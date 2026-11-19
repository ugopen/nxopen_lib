#===================================================================================
# 
#       Copyright 2020 Siemens Digital Industries Software Inc. 
#                           All Rights Reserved.
# 
#   
#=============================================================================
# File description: Sample NX/Open Application for High End Render Image Creation
#=============================================================================
#
#==============================================================================
#   Purpose:  This file contains Python source to demonstrate the process
#   of generating a high end rendered image using NX Ray Traced Studio
#   via NXOpen
#==============================================================================

#------------------------------------------------------------------------------
# These imports are needed for the following template code
#------------------------------------------------------------------------------
import NXOpen
from NXOpen import Display, BasePart


def defineImageSettings(theSession, iRayPlusStudioEditorBuilder):
    """ Defines the High End Rendering Settings for the frame to be generated

    Args:
        theSession: the current session
        iRayPlusStudioEditorBuilder: the IrayPlusStudioEditorBuilder
    """
    
    
    # Static image file type. Supported types: .Jpg, .Png, and .Tif
    iRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageFileFormat = NXOpen.Display.IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageFileFormatType.Jpg
    
    # Set static image size to UserDefined to open more output image settings
    iRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageSize = NXOpen.Display.IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageSizeType.UserDefined
    
    # Pixel Dimensions for 1080p Resolution
    pixel_width_1080p = 1920
    pixel_height_1080p = 1080
    
    # pixel width and height
    iRayPlusStudioEditorBuilder.IRayPlusStudioStaticImagePixelWidth = pixel_width_1080p
    iRayPlusStudioEditorBuilder.IRayPlusStudioStaticImagePixelHeight = pixel_height_1080p
    
    # Set time limit for the render "HH:MM:SS"
    time_limit_per_frame = "00:01:00"
    iRayPlusStudioEditorBuilder.StaticIRayPlusStudioTime.DateItem.Time = time_limit_per_frame
    
    # Commit render settings changes
    nXObject1 = iRayPlusStudioEditorBuilder.Commit()
    

def generateImage():
    """ Will attempt to save an image of the current view of the part.
    
    Args:
        None
    """
    # Get session and workpart
    session = NXOpen.Session.GetSession()
    workPart = session.Parts.Work
    
    # Set High end render output image settings
    iRayPlusStudioEditorBuilder = workPart.Views.CreateIrayPlusStudioEditorBuilder()
    defineImageSettings(session, iRayPlusStudioEditorBuilder)
    
    # Define the location of the generated frames here
    frame_location = "C:\\Temp\\SingleFrameRenderResult"
    
    # Create High End Rendered Image
    results = workPart.Views.CreateHighEndRenderImage(frame_location)
    
    # Output results for the current frame
    logRenderResults(session, results)

    # Destroy the rendering session
    workPart.Views.DestroyHighEndRenderSession()

    # Destroy the builder
    iRayPlusStudioEditorBuilder.Destroy()
    
    
    
def logRenderResults(session, results):
    """Logs a message containing render results information in the listing window

    Args:
        session: The session to log the message for
        results: results structure containing information of the render
    """
    
    elapsedTime = "Elapsed Time (initialization to image save): " + str(results.Seconds)
    numIters = "Iterations: " + str(results.Iterations)
    msg = (elapsedTime + ",  " + numIters)
    
    listing_window = session.ListingWindow
    
    if not listing_window.IsOpen:
        session.ListingWindow.Open()
    listing_window.WriteLine(msg)
  

def main():
    
    generateImage()


if __name__ == '__main__':
    main()


