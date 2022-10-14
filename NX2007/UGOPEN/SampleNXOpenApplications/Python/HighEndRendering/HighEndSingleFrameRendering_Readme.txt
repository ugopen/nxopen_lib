'===================================================================================
'
'       Copyright (c) 2020 Siemens Digital Industries Software Inc.
'                            All Rights Reserved.
'
'===================================================================================
'    

------------------------------------------------------------------------------------
                        HighEndSingleFrameRendering Example
------------------------------------------------------------------------------------

-----------
Description
-----------

    This example demonstrates how to use the High End Render Image API to create an static image.
    The High End Render Image API takes the current scene defined in NX and creates a ray traced image 
    produced in our Ray Traced Studio application. The API uses settings defined in the Ray Traced Studio
    Preferences dialog, such as image pixel width, pixel height, DPI, image file type, and render time limit.

    The example will conduct a 1 minute render and will save a 1080p image of the scene at "C:\Temp\SingleFrameRenderingResult".

    To modify pixel dimensions to 720p (1280x720) or 4k (3840x2160), adjust lines 45-46 in the example application. 
    For example, to generate a 4k image:

        # pixel width and height
        iRayPlusStudioPreferencesBuilder2.IRayPlusStudioStaticImagePixelWidth = 3840
        iRayPlusStudioPreferencesBuilder2.IRayPlusStudioStaticImagePixelHeight = 2160

    To modify the render time for each frame, adjust line 49 in the example application. Larger render times 
    allow Ray Traced Studio to generate sharper, more resolved images. For example, to assign 30 minutes to render the image:

        # Set time limit for the render "HH:MM:SS"
        time_limit_per_frame = "00:30:00"



--------------
Files required
--------------

    1. HighEndSingleFrameRendering.py

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

    3. Set up scene as desired

    4. Run HighEndSingleFrameRendering.py
    
	
   Linux
   -------	
    -NA-  
	
------
Notes
------
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."

