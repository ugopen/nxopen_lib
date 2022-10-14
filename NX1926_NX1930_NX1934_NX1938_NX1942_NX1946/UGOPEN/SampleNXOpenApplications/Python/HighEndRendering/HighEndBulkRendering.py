#===================================================================================
# 
#       Copyright 2020 Siemens Digital Industries Software Inc. 
#                           All Rights Reserved.
# 
#   
#=============================================================================
#File description: Sample NX/Open Application for High End Render Image Creation
#=============================================================================
#
#==============================================================================
#   Purpose:  This file contains Python source to guide you in the
#   process of generating a series of high end rendered images using NX Ray 
#   Traced Studio via NXOpen
#==============================================================================

#------------------------------------------------------------------------------
# These imports are needed for the following template code
#------------------------------------------------------------------------------
import NXOpen
from NXOpen import UF, Display, BasePart


def defineImageSettings(theSession, workPart):
    """ Defines the High End Rendering Settings for the frame to be generated

    Args:
        theSession: the current session
        workPart: the current work part
    """
    
    iRayPlusStudioEditorBuilder2 = workPart.Views.CreateIrayPlusStudioEditorBuilder()
    
    # Static image file type. Supported types: .Jpg, .Png, and .Tif
    iRayPlusStudioEditorBuilder2.IRayPlusStudioStaticImageFileFormat = NXOpen.Display.IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageFileFormatType.Jpg
    
    # Set static image size to UserDefined to open more output image settings
    iRayPlusStudioEditorBuilder2.IRayPlusStudioStaticImageSize = NXOpen.Display.IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageSizeType.UserDefined
    
    # Pixel Dimensions for 720p
    pixel_width_720p = 1280
    pixel_height_720p = 720
    
    # pixel width and height
    iRayPlusStudioEditorBuilder2.IRayPlusStudioStaticImagePixelWidth = pixel_width_720p
    iRayPlusStudioEditorBuilder2.IRayPlusStudioStaticImagePixelHeight = pixel_height_720p
    
    # Set time limit for the render "HH:MM:SS"
    time_limit_per_frame = "00:00:15"
    iRayPlusStudioEditorBuilder2.StaticIRayPlusStudioTime.DateItem.Time = time_limit_per_frame
    
    # Commit render settings changes
    nXObject6 = iRayPlusStudioEditorBuilder2.Commit()
    

def rotate(workPart, vector, origin, frames):
    """Rotates a part

    Args:
        workPart: The part to rotate.
        vector: vector containing axis to modify
        origin: origin point of the camera position
        frames: total number of frames for bulk render
    """
    
    rotation_angle = 360.0/frames

    workPart.ModelingViews.WorkView.Rotate(origin, vector, rotation_angle)
    

def generateImages():
    """Will attempt to save an image of the current view of the part.
    """
    # Get session and workpart
    session = NXOpen.Session.GetSession()
    workPart = session.Parts.Work
    
    # Set High end render output image settings
    defineImageSettings(session, workPart)
    
    
    # Define amount of High End Rendered frames to create. 
    frames = 180
    
    # Begin incremental rotation around model
    for x in range(0, frames):
        
        # Rotate part around Z-Axis of WCS Origin
        rotate(workPart, NXOpen.Vector3d(0.0, 0.0, 1.0), workPart.WCS.Origin, frames)
            

        # Define the location of the generated frames here
        frame_location = "C:\\Temp\\BulkRenderResults"
        
        # Create high end rendered image
        results = workPart.Views.CreateHighEndRenderImage(frame_location)
        
        # Output results for the current frame
        logRenderResults(session, results)
    
    # Destroy the session
    workPart.Views.DestroyHighEndRenderSession()
    
    
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
    
    generateImages()


if __name__ == '__main__':
    main()


