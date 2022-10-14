//=============================================================================
//
//                   Copyright (c) 2010 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//===============================================================================
//File description: Sample NX/Open Application for Title Block generation through 
//Symbol file
//===============================================================================
//
//==============================================================================
//  WARNING!!  This file is overwritten by the Block Styler while generating
//  the automation code. Any modifications to this file will be lost after
//  generating the code again.
//==============================================================================

//==============================================================================
//  Purpose:  This TEMPLATE file contains C++ source to guide you in the
//  construction of your Block application dialog. The generation of your
//  dialog file (.dlx extension) is the first step towards dialog construction
//  within NX.  You must now create a NX Open application that
//  utilizes this file (.dlx).
//
//  The information in this file provides you with the following:
//
//  1.  Help on how to load and display your Block UI Styler dialog in NX
//      using APIs provided in NXOpen.BlockStyler namespace
//  2.  The empty callback methods (stubs) associated with your dialog items
//      have also been placed in this file. These empty methods have been
//      created simply to start you along with your coding requirements.
//      The method name, argument list and possible return values have already
//      been provided for you.
//==============================================================================


//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include "TitleBlock.hpp"
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(GenerateTitle::theSession) = NULL;
UI *(GenerateTitle::theUI) = NULL;

//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
GenerateTitle *theGenerateTitle;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
GenerateTitle::GenerateTitle()
{
    try
    {
        // Initialize the NX Open C++ API environment
        GenerateTitle::theSession = NXOpen::Session::GetSession();
        GenerateTitle::theUI = UI::GetUI();
        theDialogName = "TitleBlock.dlx";
        theDialog = GenerateTitle::theUI->CreateDialog(theDialogName.c_str());
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &GenerateTitle::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &GenerateTitle::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &GenerateTitle::update_cb));
        theDialog->AddInitializeHandler(make_callback(this, &GenerateTitle::initialize_cb));
        theDialog->AddFocusNotifyHandler(make_callback(this, &GenerateTitle::focusNotify_cb));
        theDialog->AddKeyboardFocusNotifyHandler(make_callback(this, &GenerateTitle::keyboardFocusNotify_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &GenerateTitle::dialogShown_cb));
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        GenerateTitle::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
        throw;
    }
}

//------------------------------------------------------------------------------
// Destructor for NX Styler class
//------------------------------------------------------------------------------
GenerateTitle::~GenerateTitle()
{
    if (theDialog != NULL)
    {
        delete theDialog;
        theDialog = NULL;
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
//            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\ugii\menus\custom_dirs.dat
//
//    You can create the dialog using one of the following way:
//
//    1. USER EXIT
//
//        1) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
//        2) Invoke the Shared Library through File->Execute->NX Open menu.
//
//------------------------------------------------------------------------------
extern "C" DllExport void  ufusr(char *param, int *retcod, int param_len)
{
    try
    {
        theGenerateTitle = new GenerateTitle();
        // The following method shows the dialog immediately
        theGenerateTitle->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        GenerateTitle::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    if(theGenerateTitle != NULL)
    {
        delete theGenerateTitle;
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
extern "C" DllExport int ufusr_ask_unload()
{
    //return (int)Session::LibraryUnloadOptionExplicitly;
    return (int)Session::LibraryUnloadOptionImmediately;
    //return (int)Session::LibraryUnloadOptionAtTermination;
}

//------------------------------------------------------------------------------
// Following method cleanup any housekeeping chores that may be needed.
// This method is automatically called by NX.
//------------------------------------------------------------------------------
extern "C" DllExport void ufusr_cleanup(void)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        GenerateTitle::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int GenerateTitle::Show()
{
    try
    {
        theDialog->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        GenerateTitle::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void GenerateTitle::initialize_cb()
{
    try
    {
        partName = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("partName"));
        authorName = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("authorName"));
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        GenerateTitle::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void GenerateTitle::dialogShown_cb()
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        GenerateTitle::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int GenerateTitle::apply_cb()
{
    int errorCode = 0;
    try
    {
        //---- Enter your callback code here -----
        Session *theSession = Session::GetSession();
        Part *workPart(theSession->Parts()->Work());
        Part *displayPart(theSession->Parts()->Display());

        //Getting Part Name into String
        NXOpen::BlockStyler::PropertyList *partNameProps = partName->GetProperties();
        NXOpen::NXString partName1 = partNameProps->GetString("WideValue");
        delete partNameProps;

        //Getting Author Name into String
        NXOpen::BlockStyler::PropertyList *authNameProps = authorName->GetProperties();
        NXOpen::NXString authorName1 = authNameProps->GetString("WideValue");
        delete authNameProps;

        //Getting Current Date into String
        UF_system_info_t info;
        UF_ask_system_info(&info);
        
            
        //Now the info.date_buf contains date and time seperated be space
        //from which date will be extracted
        NXOpen::NXString currDate = info.date_buf;        
        string date = currDate.GetText();
        size_t pos1 = date.find_first_of(" ");
        date = date.substr(0,pos1);
        currDate = date;        

        // ----------------------------------------------
        //   Menu: Insert->Annotation...
        // ----------------------------------------------

        Session::UndoMarkId markId1;
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityVisible,  "Create Annotation");


        Annotations::LetteringPreferences *letteringPreferences1;
        letteringPreferences1 = workPart->Annotations()->Preferences()->GetLetteringPreferences();


        // ----------------------------------------------------------------------
        //   For this example, we need the set the lettering preferences so the
        //   Text will align correctly in the title block
        // ----------------------------------------------------------------------
        Annotations::Lettering annotations_Lettering1;
        annotations_Lettering1.Size = 0.125;
        annotations_Lettering1.CharacterSpaceFactor = 1;
        annotations_Lettering1.AspectRatio = 1.0;
        annotations_Lettering1.LineSpaceFactor = 1.0;
        annotations_Lettering1.Cfw.Color = 2;
        annotations_Lettering1.Cfw.Font = 1;
        annotations_Lettering1.Cfw.Width = Annotations::LineWidthThin;
        letteringPreferences1->SetGeneralText(annotations_Lettering1);

        workPart->Annotations()->Preferences()->SetLetteringPreferences(letteringPreferences1);

        

        Annotations::UserSymbolPreferences *userSymbolPreferences1;
        userSymbolPreferences1 = theSession->Parts()->Work()->Annotations()->NewUserSymbolPreferences(Annotations::UserSymbolPreferences::SizeTypeScaleAspectRatio,1,1);

        // -------------------------------------------------------------------------------------
        //   We need to load in the custom sybmol of the simple title block that has three lines
        // -------------------------------------------------------------------------------------
        NXString name = theSession->Parts()->Work()->FullPath();
        string fullpath = name.GetText();
        size_t pos = fullpath.find_last_of("\\"); ;
        fullpath = fullpath.substr(0,(pos-1));
        name = fullpath;
        name = name +"special.sbf";
        theSession->Parts()->Work()->Annotations()->CurrentSbfFile() = name;
        double *symbWidth= new double,*symbHgt = new double;
        NXOpen::SymbolFont *symbolFont1 =  theSession->Parts()->Work()->Annotations()->LoadSymbolFontFromSbfFile("TITLE4  ",symbWidth,symbHgt);

        
        // ----------------------------------------------
        //   This adds table into the location
        // ----------------------------------------------
        std::vector<NXString> stringArray1(1) ; 
        stringArray1[0]= "<%TITLE4>";

        NXOpen::Point3d point3d1(12.9219405594406, 2.3166958041958, 0);
        Annotations::Note *note1 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray1,point3d1,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        // ----------------------------------------------------------
        //   This adds in the note for the Part Name title entry
        //   
        //  We set up an association, to the title block note, so 
        //  when the title block is moved the text will travel with it
        //------------------------------------------------------------

        stringArray1[0]= "<C3.250>Part Name<C>";
        NXOpen::Point3d point3d2(0, 0, 0);
        Annotations::Note *note2 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray1,point3d2,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);

        // ----------------------------------------------
        //   Menu: Edit->Placement->Origin Tool
        // ----------------------------------------------
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData2;

        annotation_AssociativeOriginData2.OriginType = Annotations::AssociativeOriginTypeOffsetFromText;
        View *nullView(NULL);
        annotation_AssociativeOriginData2.View = nullView;
        annotation_AssociativeOriginData2.ViewOfGeometry = nullView;
        Point *nullPoint(NULL);
        annotation_AssociativeOriginData2.PointOnGeometry = nullPoint;
        annotation_AssociativeOriginData2.VertAnnotation = NULL;
        annotation_AssociativeOriginData2.VertAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData2.HorizAnnotation = NULL;
        annotation_AssociativeOriginData2.HorizAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData2.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData2.DimensionLine = 0;
        annotation_AssociativeOriginData2.AssociatedView = nullView;
        annotation_AssociativeOriginData2.AssociatedPoint = nullPoint;
        annotation_AssociativeOriginData2.OffsetAnnotation = note1;
        annotation_AssociativeOriginData2.OffsetAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData2.XOffsetFactor = -70;
        annotation_AssociativeOriginData2.YOffsetFactor = 8 ;
        NXOpen::Point3d point3d3(2.54694055944056, 3.3166958041958, 0);
        note2->SetAssociativeOrigin(annotation_AssociativeOriginData2,point3d3);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");

        // ----------------------------------------------------------
        //   This adds in the note for the Author title entry
        //   
        //  We set up an association, to the title block note, so 
        //  when the title block is moved the text will travel with it
        //------------------------------------------------------------

        stringArray1[0]= "<C3.250>Author<C>";
        Annotations::Note *note3 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray1,point3d2,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);

        // ----------------------------------------------
        //   Menu: Edit->Placement->Origin Tool
        // ----------------------------------------------

        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData3;

        annotation_AssociativeOriginData3.OriginType = Annotations::AssociativeOriginTypeOffsetFromText;
        annotation_AssociativeOriginData3.View = NULL;
        annotation_AssociativeOriginData3.ViewOfGeometry = NULL;
        annotation_AssociativeOriginData3.PointOnGeometry = NULL;
        annotation_AssociativeOriginData3.VertAnnotation = NULL;
        annotation_AssociativeOriginData3.VertAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData3.HorizAnnotation = NULL;
        annotation_AssociativeOriginData3.HorizAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData3.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData3.DimensionLine = 0;
        annotation_AssociativeOriginData3.AssociatedView = NULL;
        annotation_AssociativeOriginData3.AssociatedPoint = NULL;
        annotation_AssociativeOriginData3.OffsetAnnotation = note1;
        annotation_AssociativeOriginData3.OffsetAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData3.XOffsetFactor = -70;
        annotation_AssociativeOriginData3.YOffsetFactor = 1 ;
        NXOpen::Point3d point3d5(1.92194055944056, 2.4416958041958, 0);
        note3->SetAssociativeOrigin(annotation_AssociativeOriginData3,point3d5);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");

        // ----------------------------------------------------------
        //   This adds in the note for the Date title entry
        //   
        //  We set up an association, to the title block note, so 
        //  when the title block is moved the text will travel with it
        //------------------------------------------------------------
    
        stringArray1[0]= "<C3.250>Revision Date<C>";
        Annotations::Note *note4 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray1,point3d2,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);

        // ----------------------------------------------
        //   Menu: Edit->Placement->Origin Tool
        // ----------------------------------------------

        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData4;

        annotation_AssociativeOriginData4.OriginType = Annotations::AssociativeOriginTypeOffsetFromText;
        annotation_AssociativeOriginData4.View = NULL;
        annotation_AssociativeOriginData4.ViewOfGeometry = NULL;
        annotation_AssociativeOriginData4.PointOnGeometry = NULL;
        annotation_AssociativeOriginData4.VertAnnotation = NULL;
        annotation_AssociativeOriginData4.VertAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData4.HorizAnnotation = NULL;
        annotation_AssociativeOriginData4.HorizAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData4.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData4.DimensionLine = 0;
        annotation_AssociativeOriginData4.AssociatedView = NULL;
        annotation_AssociativeOriginData4.AssociatedPoint = NULL;
        annotation_AssociativeOriginData4.OffsetAnnotation = note1;
        annotation_AssociativeOriginData4.OffsetAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData4.XOffsetFactor = -70;
        annotation_AssociativeOriginData4.YOffsetFactor = -7 ;
        NXOpen::Point3d point3d7(3.42194055944056, 1.4416958041958, 0);
        note4->SetAssociativeOrigin(annotation_AssociativeOriginData4,point3d7);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");


        // ----------------------------------------------------------
        //   This adds in the note for the Part name
        //   
        //  We set up an association, to the title block note, so 
        //  when the title block is moved the text will travel with it
        //------------------------------------------------------------
        
        stringArray1[0]=  "<C3.250>" + partName1 + "<C>";
        Annotations::Note *note5 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray1,point3d2,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);

        // ----------------------------------------------
        //   Menu: Edit->Placement->Origin Tool
        // ----------------------------------------------

        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData5;

        annotation_AssociativeOriginData5.OriginType = Annotations::AssociativeOriginTypeOffsetFromText;
        annotation_AssociativeOriginData5.View = NULL;
        annotation_AssociativeOriginData5.ViewOfGeometry = NULL;
        annotation_AssociativeOriginData5.PointOnGeometry = NULL;
        annotation_AssociativeOriginData5.VertAnnotation = NULL;
        annotation_AssociativeOriginData5.VertAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData5.HorizAnnotation = NULL;
        annotation_AssociativeOriginData5.HorizAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData5.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData5.DimensionLine = 0;
        annotation_AssociativeOriginData5.AssociatedView = NULL;
        annotation_AssociativeOriginData5.AssociatedPoint = NULL;
        annotation_AssociativeOriginData5.OffsetAnnotation = note1;
        annotation_AssociativeOriginData5.OffsetAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData5.XOffsetFactor = 40;
        annotation_AssociativeOriginData5.YOffsetFactor = 8;
        NXOpen::Point3d point3d9(33.1533828382838, 3.8529702970297, 0);
        note5->SetAssociativeOrigin(annotation_AssociativeOriginData5,point3d9);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");


        // ----------------------------------------------------------
        //   This adds in the note for the Author name
        //   
        //  We set up an association, to the title block note, so 
        //  when the title block is moved the text will travel with it
        //------------------------------------------------------------
        
        stringArray1[0]=  "<C3.250>" + authorName1 + "<C>";
        Annotations::Note *note6 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray1,point3d2,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);

        // ----------------------------------------------
        //   Menu: Edit->Placement->Origin Tool
        // ----------------------------------------------

        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData6;

        annotation_AssociativeOriginData6.OriginType = Annotations::AssociativeOriginTypeOffsetFromText;
        annotation_AssociativeOriginData6.View = NULL;
        annotation_AssociativeOriginData6.ViewOfGeometry = NULL;
        annotation_AssociativeOriginData6.PointOnGeometry = NULL;
        annotation_AssociativeOriginData6.VertAnnotation = NULL;
        annotation_AssociativeOriginData6.VertAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData6.HorizAnnotation = NULL;
        annotation_AssociativeOriginData6.HorizAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData6.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData6.DimensionLine = 0;
        annotation_AssociativeOriginData6.AssociatedView = NULL;
        annotation_AssociativeOriginData6.AssociatedPoint = NULL;
        annotation_AssociativeOriginData6.OffsetAnnotation = note1;
        annotation_AssociativeOriginData6.OffsetAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData6.XOffsetFactor = 40;
        annotation_AssociativeOriginData6.YOffsetFactor = 1;
        NXOpen::Point3d point3d11(33.1533828382838, 2.9779702970297, 0);
        note6->SetAssociativeOrigin(annotation_AssociativeOriginData6,point3d11);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");


        // ----------------------------------------------------------
        //   This adds in the note for the Date 
        //   
        //  We set up an association, to the title block note, so 
        //  when the title block is moved the text will travel with it
        //------------------------------------------------------------
    
        stringArray1[0]=  "<C3.250>" + currDate + "<C>";
        Annotations::Note *note7 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray1,point3d2,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);

        // ----------------------------------------------
        //   Menu: Edit->Placement->Origin Tool
        // ----------------------------------------------

        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData7;

        annotation_AssociativeOriginData7.OriginType = Annotations::AssociativeOriginTypeOffsetFromText;
        annotation_AssociativeOriginData7.View = NULL;
        annotation_AssociativeOriginData7.ViewOfGeometry = NULL;
        annotation_AssociativeOriginData7.PointOnGeometry = NULL;
        annotation_AssociativeOriginData7.VertAnnotation = NULL;
        annotation_AssociativeOriginData7.VertAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData7.HorizAnnotation = NULL;
        annotation_AssociativeOriginData7.HorizAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData7.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData7.DimensionLine = 0;
        annotation_AssociativeOriginData7.AssociatedView = NULL;
        annotation_AssociativeOriginData7.AssociatedPoint = NULL;
        annotation_AssociativeOriginData7.OffsetAnnotation = note1;
        annotation_AssociativeOriginData7.OffsetAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData7.XOffsetFactor = 40;
        annotation_AssociativeOriginData7.YOffsetFactor = -7;
        NXOpen::Point3d point3d13(33.1533828382838, 2.9779702970297, 0);
        note7->SetAssociativeOrigin(annotation_AssociativeOriginData7,point3d13);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");

        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);
        delete letteringPreferences1;
        delete userSymbolPreferences1;    

    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        GenerateTitle::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int GenerateTitle::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        if(block == partName)
        {
        //---------Enter your code here-----------
        }
        else if(block == authorName)
        {
        //---------Enter your code here-----------
            
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        GenerateTitle::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int GenerateTitle::ok_cb()
{
    int errorCode = 0;
    try
    {
        errorCode = apply_cb();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        GenerateTitle::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: focusNotify_cb
//This callback is executed when any block (except the ones which receive keyboard entry such as Integer block) receives focus.
//------------------------------------------------------------------------------
void GenerateTitle::focusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        GenerateTitle::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: keyboardFocusNotify_cb
//This callback is executed when block which can receive keyboard entry, receives the focus.
//------------------------------------------------------------------------------
void GenerateTitle::keyboardFocusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        GenerateTitle::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}
