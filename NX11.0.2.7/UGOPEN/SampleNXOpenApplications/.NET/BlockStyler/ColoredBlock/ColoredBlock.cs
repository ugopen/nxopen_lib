//=============================================================================
//
//                   Copyright (c) 2008 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Block Styler
//=============================================================================
//

//==============================================================================
//  Purpose:  This TEMPLATE file contains C# source to guide you in the
//  construction of your Block application dialog. The generation of your
//  dialog file (.dlx extension) is the first step towards dialog construction
//  within NX.  You must now create a NX Open application that
//  utilizes this file (.dlx).
//
//  The information in this file provides you with the following:
//
//  1.  Help on how to load and display your Block Styler dialog in NX
//      using APIs provided in NXOpen.BlockStyler namespace
//  2.  The empty callback methods (stubs) associated with your dialog items
//      have also been placed in this file. These empty methods have been
//      created simply to start you along with your coding requirements.
//      The method name, argument list and possible return values have already
//      been provided for you.
//==============================================================================

//------------------------------------------------------------------------------
//These imports are needed for the following template code
//------------------------------------------------------------------------------
using System;
using NXOpen;
using NXOpen.BlockStyler;

//------------------------------------------------------------------------------
//Represents Block Styler application class
//------------------------------------------------------------------------------
public class ColoredBlock
{
    //class members
    private static Session theSession = null;
    private static UI theUI = null;
    public static ColoredBlock theColoredBlock;
    private string theDialogName;
    private NXOpen.BlockStyler.BlockDialog theDialog;
    private NXOpen.BlockStyler.UIBlock group0;// Block type: Group
    private NXOpen.BlockStyler.UIBlock blockHeight;// Block type: Double
    private NXOpen.BlockStyler.UIBlock blockWidth;// Block type: Double
    private NXOpen.BlockStyler.UIBlock blockLength;// Block type: Double
    private NXOpen.BlockStyler.UIBlock blockOrigin;// Block type: Specify Point
    private NXOpen.BlockStyler.UIBlock blockColor;// Block type: Color Picker
    //------------------------------------------------------------------------------
    //Bit Option for Property: SnapPointTypesEnabled
    //------------------------------------------------------------------------------
    public static readonly int              SnapPointTypesEnabled_UserDefined = (1 << 0);
    public static readonly int                 SnapPointTypesEnabled_Inferred = (1 << 1);
    public static readonly int           SnapPointTypesEnabled_ScreenPosition = (1 << 2);
    public static readonly int                 SnapPointTypesEnabled_EndPoint = (1 << 3);
    public static readonly int                 SnapPointTypesEnabled_MidPoint = (1 << 4);
    public static readonly int             SnapPointTypesEnabled_ControlPoint = (1 << 5);
    public static readonly int             SnapPointTypesEnabled_Intersection = (1 << 6);
    public static readonly int                SnapPointTypesEnabled_ArcCenter = (1 << 7);
    public static readonly int            SnapPointTypesEnabled_QuadrantPoint = (1 << 8);
    public static readonly int            SnapPointTypesEnabled_ExistingPoint = (1 << 9);
    public static readonly int             SnapPointTypesEnabled_PointonCurve = (1 <<10);
    public static readonly int           SnapPointTypesEnabled_PointonSurface = (1 <<11);
    public static readonly int         SnapPointTypesEnabled_PointConstructor = (1 <<12);
    public static readonly int     SnapPointTypesEnabled_TwocurveIntersection = (1 <<13);
    public static readonly int             SnapPointTypesEnabled_TangentPoint = (1 <<14);
    public static readonly int                    SnapPointTypesEnabled_Poles = (1 <<15);
    //------------------------------------------------------------------------------
    //Bit Option for Property: SnapPointTypesOnByDefault
    //------------------------------------------------------------------------------
    public static readonly int          SnapPointTypesOnByDefault_UserDefined = (1 << 0);
    public static readonly int             SnapPointTypesOnByDefault_Inferred = (1 << 1);
    public static readonly int       SnapPointTypesOnByDefault_ScreenPosition = (1 << 2);
    public static readonly int             SnapPointTypesOnByDefault_EndPoint = (1 << 3);
    public static readonly int             SnapPointTypesOnByDefault_MidPoint = (1 << 4);
    public static readonly int         SnapPointTypesOnByDefault_ControlPoint = (1 << 5);
    public static readonly int         SnapPointTypesOnByDefault_Intersection = (1 << 6);
    public static readonly int            SnapPointTypesOnByDefault_ArcCenter = (1 << 7);
    public static readonly int        SnapPointTypesOnByDefault_QuadrantPoint = (1 << 8);
    public static readonly int        SnapPointTypesOnByDefault_ExistingPoint = (1 << 9);
    public static readonly int         SnapPointTypesOnByDefault_PointonCurve = (1 <<10);
    public static readonly int       SnapPointTypesOnByDefault_PointonSurface = (1 <<11);
    public static readonly int     SnapPointTypesOnByDefault_PointConstructor = (1 <<12);
    public static readonly int SnapPointTypesOnByDefault_TwocurveIntersection = (1 <<13);
    public static readonly int         SnapPointTypesOnByDefault_TangentPoint = (1 <<14);
    public static readonly int                SnapPointTypesOnByDefault_Poles = (1 <<15);
    
    //------------------------------------------------------------------------------
    //Constructor for NX Styler class
    //------------------------------------------------------------------------------
    public ColoredBlock()
    {
        try
        {
            theSession = Session.GetSession();
            theUI = UI.GetUI();
            theDialogName = "ColoredBlock.dlx";
            theDialog = theUI.CreateDialog(theDialogName);
            theDialog.AddApplyHandler(new NXOpen.BlockStyler.BlockDialog.Apply(apply_cb));
            theDialog.AddInitializeHandler(new NXOpen.BlockStyler.BlockDialog.Initialize(initialize_cb));
            theDialog.AddDialogShownHandler(new NXOpen.BlockStyler.BlockDialog.DialogShown(dialogShown_cb));
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            throw ex;
        }
    }
    //------------------------------- DIALOG LAUNCHING ---------------------------------
    //
    //    Before invoking this application one needs to open any part/empty part in NX
    //    because of the behavior of the blocks.
    //
    //    Make sure the dlx file is in one of the following locations:
    //        1.) From where NX session is launched
    //        2.) $UGII_USER_DIR/application
    //        3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
    //            recommended. This variable is set to a full directory path to a file 
    //            containing a list of root directories for all custom applications.
    //            e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
    //
    //    You can create the dialog using one of the following way:
    //
    //    1. Journal Replay
    //
    //        1) Replay this file through Tool->Journal->Play Menu.
    //
    //    2. USER EXIT
    //
    //        1) Create the Shared Library -- Refer "Block Styler programmer's guide"
    //        2) Invoke the Shared Library through File->Execute->NX Open menu.
    //
    //------------------------------------------------------------------------------
    public static void Main()
    {
        try
        {
            theColoredBlock = new ColoredBlock();
            // The following method shows the dialog immediately
            theColoredBlock.Show();
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.Message);
        }
        finally
        {
            theColoredBlock.Dispose();
        }
    }
    //------------------------------------------------------------------------------
    // This method specifies how a shared image is unloaded from memory
    // within NX. This method gives you the capability to unload an
    // internal NX Open application or user  exit from NX. Specify any
    // one of the three constants as a return value to determine the type
    // of unload to perform:
    //
    //
    //    Immediately : unload the library as soon as the automation program has completed
    //    Explicitly  : unload the library from the "Unload Shared Image" dialog
    //    AtTermination : unload the library when the NX session terminates
    //
    //
    // NOTE:  A program which associates NX Open applications with the menubar
    // MUST NOT use this option since it will UNLOAD your NX Open application image
    // from the menubar.
    //------------------------------------------------------------------------------
     public static int getUnloadOption(string arg)
    {
        return System.Convert.ToInt32(Session.LibraryUnloadOption.Explicitly);
        // return System.Convert.ToInt32(Session.LibraryUnloadOption.Immediately);
        // return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);
    }
    
    //------------------------------------------------------------------------------
    // Following method cleanup any housekeeping chores that may be needed.
    // This method is automatically called by NX.
    //------------------------------------------------------------------------------
    public static void UnloadLibrary(string arg)
    {
        try
        {
            //---- Enter your code here -----
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.Message);
        }
    }
    
    //------------------------------------------------------------------------------
    //This method shows the dialog on the screen
    //------------------------------------------------------------------------------
    public NXOpen.UIStyler.DialogResponse Show()
    {
        try
        {
            theDialog.Show();
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.Message);
        }
        return 0;
    }
    
    //------------------------------------------------------------------------------
    //Method Name: Dispose
    //------------------------------------------------------------------------------
    public void Dispose()
    {
        if(theDialog != null)
        {
            theDialog.Dispose();
            theDialog = null;
        }
    }
    
    //------------------------------------------------------------------------------
    //---------------------Block Styler Callback Functions--------------------------
    //------------------------------------------------------------------------------
    
    //------------------------------------------------------------------------------
    //Callback Name: initialize_cb
    //------------------------------------------------------------------------------
    public void initialize_cb()
    {
        try
        {
            group0 = theDialog.TopBlock.FindBlock("group0");
            blockHeight = theDialog.TopBlock.FindBlock("blockHeight");
            blockWidth = theDialog.TopBlock.FindBlock("blockWidth");
            blockLength = theDialog.TopBlock.FindBlock("blockLength");
            blockOrigin = theDialog.TopBlock.FindBlock("blockOrigin");
            blockColor = theDialog.TopBlock.FindBlock("blockColor");

            // Set the upper-limits and lower-limits
            PropertyList blockHeightProps = blockHeight.GetProperties();
            blockHeightProps.SetDouble("MaximumValue", 100000.0);
            blockHeightProps.SetDouble("MinimumValue", 0.001);
            blockHeightProps.SetDouble("Value", 100.0);
            blockHeightProps.Dispose();
            blockHeightProps = null;

            PropertyList blockWidthProps = blockWidth.GetProperties();
            blockWidthProps.SetDouble("MaximumValue", 100000.0);
            blockWidthProps.SetDouble("MinimumValue", 0.001);
            blockWidthProps.SetDouble("Value", 100.0);
            blockWidthProps.Dispose();
            blockWidthProps = null;

            PropertyList blockLengthProps = blockLength.GetProperties();
            blockLengthProps.SetDouble("MaximumValue", 100000.0);
            blockLengthProps.SetDouble("MinimumValue", 0.001);
            blockLengthProps.SetDouble("Value", 100.0);
            blockLengthProps.Dispose();
            blockLengthProps = null;
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.Message);
        }
    }
    
    //------------------------------------------------------------------------------
    //Callback Name: dialogShown_cb
    //This callback is executed just before the dialog launch. Thus any value set 
    //here will take precedence and dialog will be launched showing that value. 
    //------------------------------------------------------------------------------
    public void dialogShown_cb()
    {
        try
        {
            //---- Enter your callback code here -----
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.Message);
        }
    }
    
    //------------------------------------------------------------------------------
    //Callback Name: apply_cb
    //------------------------------------------------------------------------------
    public int apply_cb()
    {
        int errorCode = 0;
        NXOpen.Features.BlockFeatureBuilder blockFeatureBuilder1 = null;

        try
        {
            Part workPart = theSession.Parts.Work;

            //Get the values from UI Blocks
            PropertyList blockHeightProps = blockHeight.GetProperties();
            double theHeight = blockHeightProps.GetDouble("Value");
            blockHeightProps.Dispose();
            blockHeightProps = null;

            PropertyList blockWidthProps = blockWidth.GetProperties();
            double theWidth = blockWidthProps.GetDouble("Value");
            blockWidthProps.Dispose();
            blockWidthProps = null;

            PropertyList blockLengthProps = blockLength.GetProperties();
            double theLength = blockLengthProps.GetDouble("Value");
            blockLengthProps.Dispose();
            blockLengthProps = null;

            PropertyList blockOriginProps = blockOrigin.GetProperties();
            Point3d originPoint = blockOriginProps.GetPoint("Point");
            blockOriginProps.Dispose();
            blockOriginProps = null;

            PropertyList blockColorProps = blockColor.GetProperties();
            int[] color = blockColorProps.GetIntegerVector("Value");
            blockColorProps.Dispose();
            blockColorProps = null;
                        
            //Create the NX block
            NXOpen.Features.Feature nullFeatures_Feature = null;
            blockFeatureBuilder1 = workPart.Features.CreateBlockFeatureBuilder(nullFeatures_Feature);

            blockFeatureBuilder1.SetOriginAndLengths(originPoint, theLength.ToString(), theHeight.ToString(), theWidth.ToString());

            NXOpen.Features.Feature feature1;
            feature1 = blockFeatureBuilder1.CommitFeature();
            

            // Get the body from Feature
            NXOpen.Features.BodyFeature bodyFeat = (NXOpen.Features.BodyFeature)feature1;
            Body[] bodies = new Body[1];
            bodies = bodyFeat.GetBodies();
            // Apply the color to feature body
            DisplayModification displayModification1 = theSession.DisplayManager.NewDisplayModification();
            displayModification1.ApplyToAllFaces = true;
            displayModification1.NewColor = color[0];
            DisplayableObject[] objects1 = new DisplayableObject[1];
            objects1[0] = bodies[0];
            displayModification1.Apply(objects1);
            displayModification1.Dispose();            
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            errorCode = 1;
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.Message);
        }
        finally 
        {
            if (blockFeatureBuilder1 != null)
            {
                blockFeatureBuilder1.Destroy();
                blockFeatureBuilder1 = null;
            }
        }
        return errorCode;
    }
    
}
