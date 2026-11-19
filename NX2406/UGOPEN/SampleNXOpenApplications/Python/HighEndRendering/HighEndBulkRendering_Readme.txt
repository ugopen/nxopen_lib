'===================================================================================
'
'       Copyright (c) 2020 Siemens Digital Industries Software Inc.
'                            All Rights Reserved.
'
'===================================================================================
'    

------------------------------------------------------------------------------------
                        HighEndBulkRendering Example
------------------------------------------------------------------------------------

-----------
Description
-----------

    This example demonstrates how to use the High End Render Image API to create a sequence of images.
    The High End Render Image API takes the current scene defined in NX and creates a ray traced image 
    produced in our Ray Traced Studio application. The API uses settings defined in the Ray Traced Studio
    Preferences dialog, such as image pixel width, pixel height, DPI, image file type, and render time limit.
    
    This example uses the API, along with the ModelingView.Rotate API, to create a simple 360 degree turntable 
    effect. The example will rotate the part model 2 degrees about the WCS Origin (World Coordinate System), 
    render the current scene for 15 seconds, and save a 720p image file at "C:\Temp\BulkRenderResults". 
    This process will repeat 180 times to create 180 individual 720p images. 

    To process these images into an .mp4 or .avi file, post-processing applications like FFmpeg can be used.
    Movie creation from a sequence of images can also be done via the default Microsoft Photos application.

    To modify pixel dimensions to 1080p (1920x1080) or 4k (3840x2160), adjust lines 45-46 in the example application. 
    For example, to generate 1080p images:

        # pixel width and height
        iRayPlusStudioPreferencesBuilder2.IRayPlusStudioStaticImagePixelWidth = 1920
        iRayPlusStudioPreferencesBuilder2.IRayPlusStudioStaticImagePixelHeight = 1080

    To modify the render time for each frame, adjust line 49 in the example application. Larger render times 
    allow Ray Traced Studio to generate sharper, more resolved images. For example, to 5 minutes to render each frame:

        # Set time limit for the render "HH:MM:SS"
        time_limit_per_frame = "00:05:00"

    To increase the amount of frames to render, adjust line 83 in the example application. By increasing the 
    amount of frames, the rotation angle between each frame will decrease. This will allow for a slower, smoother 
    turntable animation. To modify the number of frames to render:

        # Define amount of High End Rendered frames to create. 
        frames = 1000
        

--------------
Files required
--------------

    1. HighEndBulkRendering.py

    All the above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/Python/HighEndRendering

------------
Build steps
------------

   Windows
  ---------
    -NA-
  
   Linux
   -------
    -NA-
   
----------------------------
Settings before Launching NX
----------------------------
    -NA-

----------------------------
Settings after Launching NX
----------------------------
    -NA-

-----------------------
Example execution steps
-----------------------
    
   Windows
  ---------
    1. Launch NX.
    
    2. Open part desired to be rendered

    3. Set WCS origin that will be the centerpoint of rotation for the turntable effect.

    4. Run the HighEndBulkRendering.py
    
	
   Linux
   -------	
    -NA-  
	
------
Notes
------
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."

