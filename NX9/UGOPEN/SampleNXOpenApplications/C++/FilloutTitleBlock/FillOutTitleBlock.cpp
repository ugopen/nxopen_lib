//=============================================================================
//
//                   Copyright (c) 2010 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//===============================================================================
//File description: Sample NX/Open Application for filling Title Block of a 
//Drawing Sheet
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
#include "FillOutTitleBlock.hpp"
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(FillOutTitleBlock::theSession) = NULL;
UI *(FillOutTitleBlock::theUI) = NULL;

//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
FillOutTitleBlock *theFillOutTitleBlock;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
FillOutTitleBlock::FillOutTitleBlock()
{
    try
    {
        // Initialize the NX Open C++ API environment
        FillOutTitleBlock::theSession = NXOpen::Session::GetSession();
        FillOutTitleBlock::theUI = UI::GetUI();
        theDialogName = "FillOutTitleBlock.dlx";
        theDialog = FillOutTitleBlock::theUI->CreateDialog(theDialogName.c_str());
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &FillOutTitleBlock::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &FillOutTitleBlock::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &FillOutTitleBlock::update_cb));
        theDialog->AddInitializeHandler(make_callback(this, &FillOutTitleBlock::initialize_cb));
        theDialog->AddFocusNotifyHandler(make_callback(this, &FillOutTitleBlock::focusNotify_cb));
        theDialog->AddKeyboardFocusNotifyHandler(make_callback(this, &FillOutTitleBlock::keyboardFocusNotify_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &FillOutTitleBlock::dialogShown_cb));
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        FillOutTitleBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
        throw;
    }
}

//------------------------------------------------------------------------------
// Destructor for NX Styler class
//------------------------------------------------------------------------------
FillOutTitleBlock::~FillOutTitleBlock()
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
//            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_ROOT_DIR\menus\custom_dirs.dat
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
        theFillOutTitleBlock = new FillOutTitleBlock();
        // The following method shows the dialog immediately
        theFillOutTitleBlock->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        FillOutTitleBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    delete theFillOutTitleBlock;
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
        FillOutTitleBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int FillOutTitleBlock::Show()
{
    try
    {
        theDialog->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        FillOutTitleBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void FillOutTitleBlock::initialize_cb()
{
    try
    {
        group0 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("group0"));
        compName = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("compName"));
        dwgName = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("dwgName"));
        dwgNo = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("dwgNo"));
        cageCode = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("cageCode"));
        revision = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("revision"));
        dwgScale = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("dwgScale"));
        sheetNo = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("sheetNo"));
        sheetNo1 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("sheetNo1"));
        sheetNoOf = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("sheetNoOf"));
        sheetNo2 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("sheetNo2"));
        separator0 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("separator0"));
        contractNo = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("contractNo"));
        separator02 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("separator02"));
        design = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("design"));
        desSign = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("desSign"));
        separator01 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("separator01"));
        lead = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("lead"));
        leadSign = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("leadSign"));
        separator03 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("separator03"));
        str = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("str"));
        strSign = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("strSign"));
        separator04 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("separator04"));
        me = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("me"));
        meSign = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("meSign"));
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        FillOutTitleBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void FillOutTitleBlock::dialogShown_cb()
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        FillOutTitleBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int FillOutTitleBlock::apply_cb()
{
    int errorCode = 0;
    try
    {
        //---- Enter your callback code here -----
        
        //Getting current work part and display part
        Part *workPart(theSession->Parts()->Work());
        Part *displayPart(theSession->Parts()->Display());


        // ----------------------------------------------
        //   Menu: Insert->Annotation...
        // ----------------------------------------------

        Session::UndoMarkId markId1;
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityVisible,  "Create Annotation");

        //Getting and setting lettering preferences
        Annotations::LetteringPreferences *letteringPreferences1;
        letteringPreferences1 = workPart->Annotations()->Preferences()->GetLetteringPreferences();

        Annotations::Lettering annotations_Lettering1;
        annotations_Lettering1.Size = 0.075;
        annotations_Lettering1.CharacterSpaceFactor = 1;
        annotations_Lettering1.AspectRatio = 1.0;
        annotations_Lettering1.LineSpaceFactor = 1.0;
        annotations_Lettering1.Cfw.Color = 2;
        annotations_Lettering1.Cfw.Font = 1;
        annotations_Lettering1.Cfw.Width = Annotations::LineWidthThin;
        letteringPreferences1->SetGeneralText(annotations_Lettering1);

        Annotations::UserSymbolPreferences *userSymbolPreferences1;
        userSymbolPreferences1 = theSession->Parts()->Work()->Annotations()->NewUserSymbolPreferences(Annotations::UserSymbolPreferences::SizeTypeScaleAspectRatio,1,1);

        //Getting company name
        NXOpen::BlockStyler::PropertyList *compNameProps = compName->GetProperties();
        NXOpen::NXString compName1 = compNameProps->GetString("Value");
        delete compNameProps;

        std::vector<NXString> stringArray1(1) ; 
        stringArray1[0]= "<C1.750>" + compName1 + "<C>";

        //Creates note in the following location for company name
        NXOpen::Point3d point3d1(3.5527136788005e-015,  0, 0);
        Annotations::Note *note1 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray1,point3d1,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::NoteCollection *notes =   theSession->Parts()->Work()->Notes();
        Annotations::NoteCollection::iterator it;
        Annotations::Note *drfNote = NULL;
        Annotations::Note *baseNote = NULL;

        //This will align the company Name and drawing name with the sheet note "1"
        std::vector<NXString> refNote(1);
        NXString mainNote = "1";

        for(it=notes->begin();it!=notes->end();++it)
        {
            drfNote = dynamic_cast<NXOpen::Annotations::Note*>(*it);
            refNote = drfNote->GetText();            
            if(!(strcmp(refNote[0].GetText(),mainNote.GetText())))
            {
                baseNote = drfNote;
                break;
            }
        }

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData1;
        annotation_AssociativeOriginData1.OriginType = Annotations::AssociativeOriginTypeVerticallyAligned;
        View *nullView(NULL);
        annotation_AssociativeOriginData1.View = nullView;
        annotation_AssociativeOriginData1.ViewOfGeometry = nullView;
        Point *nullPoint(NULL);
        annotation_AssociativeOriginData1.PointOnGeometry = nullPoint;
        annotation_AssociativeOriginData1.VertAnnotation = baseNote;
        annotation_AssociativeOriginData1.VertAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData1.HorizAnnotation = NULL;
        annotation_AssociativeOriginData1.HorizAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData1.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData1.DimensionLine = 0;
        annotation_AssociativeOriginData1.AssociatedView = nullView;
        annotation_AssociativeOriginData1.AssociatedPoint = nullPoint;
        annotation_AssociativeOriginData1.OffsetAnnotation = NULL;
        annotation_AssociativeOriginData1.OffsetAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData1.XOffsetFactor = 0;
        annotation_AssociativeOriginData1.YOffsetFactor = 0 ;
        NXOpen::Point3d point3d2(19.000771102, 2.452293886, 0);
        note1->SetAssociativeOrigin(annotation_AssociativeOriginData1,point3d2);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");

        //Getting drawing name
        NXOpen::BlockStyler::PropertyList *dwgNameProps = dwgName->GetProperties();
        NXOpen::NXString dwgName1 = dwgNameProps->GetString("Value");
        delete dwgNameProps;

        std::vector<NXString> stringArray2(1) ; 
        stringArray2[0]= "<C1.750>" + dwgName1 + "<C>";


        //Creates note in the following location for drawing name
        NXOpen::Point3d point3d3(0,  0, 0);
        Annotations::Note *note2 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray2,point3d3,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData2;

        annotation_AssociativeOriginData2.OriginType = Annotations::AssociativeOriginTypeVerticallyAligned;
        annotation_AssociativeOriginData2.View = nullView;
        annotation_AssociativeOriginData2.ViewOfGeometry = nullView;
        annotation_AssociativeOriginData2.PointOnGeometry = nullPoint;
        annotation_AssociativeOriginData2.VertAnnotation = baseNote;
        annotation_AssociativeOriginData2.VertAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData2.HorizAnnotation = NULL;
        annotation_AssociativeOriginData2.HorizAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData2.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData2.DimensionLine = 0;
        annotation_AssociativeOriginData2.AssociatedView = nullView;
        annotation_AssociativeOriginData2.AssociatedPoint = nullPoint;
        annotation_AssociativeOriginData2.OffsetAnnotation = NULL;
        annotation_AssociativeOriginData2.OffsetAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData2.XOffsetFactor = 0;
        annotation_AssociativeOriginData2.YOffsetFactor = 0 ;
        NXOpen::Point3d point3d4(18.837754787,1.757329219, 0);
        note2->SetAssociativeOrigin(annotation_AssociativeOriginData2,point3d4);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");

        //This will align the drawing number with the sheet note "SHEET"
        mainNote = "SHEET";
        for(it=notes->begin();it!=notes->end();++it)
        {
            drfNote = dynamic_cast<NXOpen::Annotations::Note*>(*it);
            refNote = drfNote->GetText();
            if(!(strcmp(refNote[0].GetText(),mainNote.GetText())))
            {
                baseNote = drfNote;
                break;
            }
        }

        //Getting drawing number
        NXOpen::BlockStyler::PropertyList *dwgNoProps = dwgNo->GetProperties();
        NXOpen::NXString dwgNo1 = dwgNoProps->GetString("Value");
        delete dwgNoProps;

        std::vector<NXString> stringArray3(1) ; 
        stringArray3[0]= "<C1.750>" + dwgNo1 + "<C>";


        //Creates note in the following location for drawing number
        NXOpen::Point3d point3d5(0,  0, 0);
        Annotations::Note *note3 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray3,point3d5,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData3;

        annotation_AssociativeOriginData3.OriginType = Annotations::AssociativeOriginTypeVerticallyAligned;
        annotation_AssociativeOriginData3.View = nullView;
        annotation_AssociativeOriginData3.ViewOfGeometry = nullView;
        annotation_AssociativeOriginData3.PointOnGeometry = nullPoint;
        annotation_AssociativeOriginData3.VertAnnotation = baseNote;
        annotation_AssociativeOriginData3.VertAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData3.HorizAnnotation = NULL;
        annotation_AssociativeOriginData3.HorizAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData3.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData3.DimensionLine = 0;
        annotation_AssociativeOriginData3.AssociatedView = nullView;
        annotation_AssociativeOriginData3.AssociatedPoint = nullPoint;
        annotation_AssociativeOriginData3.OffsetAnnotation = NULL;
        annotation_AssociativeOriginData3.OffsetAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData3.XOffsetFactor = 0;
        annotation_AssociativeOriginData3.YOffsetFactor = 0 ;
        NXOpen::Point3d point3d6(19.9682496681978,1.12301455264456, 0);
        note3->SetAssociativeOrigin(annotation_AssociativeOriginData3,point3d6);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");

        //Getting cage code
        NXOpen::BlockStyler::PropertyList *cageCodeProps = cageCode->GetProperties();
        NXOpen::NXString cageCode1 = cageCodeProps->GetString("Value");
        delete cageCodeProps;

        std::vector<NXString> stringArray15(1) ; 
        stringArray15[0]= "<C1.750>" + cageCode1 + "<C>";

        //Creates note in the following location for cage code
        NXOpen::Point3d point3d28(0,  0, 0);
        Annotations::Note *note15 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray15,point3d28,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData12;

        annotation_AssociativeOriginData12.OriginType = Annotations::AssociativeOriginTypeHorizontallyAligned;
        annotation_AssociativeOriginData12.View = nullView;
        annotation_AssociativeOriginData12.ViewOfGeometry = nullView;
        annotation_AssociativeOriginData12.PointOnGeometry = nullPoint;
        annotation_AssociativeOriginData12.VertAnnotation = NULL;
        annotation_AssociativeOriginData12.VertAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData12.HorizAnnotation = note3;
        annotation_AssociativeOriginData12.HorizAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData12.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData12.DimensionLine = 0;
        annotation_AssociativeOriginData12.AssociatedView = nullView;
        annotation_AssociativeOriginData12.AssociatedPoint = nullPoint;
        annotation_AssociativeOriginData12.OffsetAnnotation = NULL;
        annotation_AssociativeOriginData12.OffsetAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData12.XOffsetFactor = 0;
        annotation_AssociativeOriginData12.YOffsetFactor = 0 ;
        NXOpen::Point3d point3d29(18.15128456730, 1.15312961892, 0);
        note15->SetAssociativeOrigin(annotation_AssociativeOriginData12,point3d29);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");


        //Getting revision
        NXOpen::BlockStyler::PropertyList *revisionProps = revision->GetProperties();
        NXOpen::NXString revision1 = revisionProps->GetString("Value");
        delete revisionProps;

        std::vector<NXString> stringArray16(1) ; 
        stringArray16[0]= "<C1.750>" + revision1 + "<C>";

        //Creates note in the following location for revision
        NXOpen::Point3d point3d30(0,  0, 0);
        Annotations::Note *note16 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray16,point3d30,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData13;

        annotation_AssociativeOriginData13.OriginType = Annotations::AssociativeOriginTypeHorizontallyAligned;
        annotation_AssociativeOriginData13.View = nullView;
        annotation_AssociativeOriginData13.ViewOfGeometry = nullView;
        annotation_AssociativeOriginData13.PointOnGeometry = nullPoint;
        annotation_AssociativeOriginData13.VertAnnotation = NULL;
        annotation_AssociativeOriginData13.VertAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData13.HorizAnnotation = note3;
        annotation_AssociativeOriginData13.HorizAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData13.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData13.DimensionLine = 0;
        annotation_AssociativeOriginData13.AssociatedView = nullView;
        annotation_AssociativeOriginData13.AssociatedPoint = nullPoint;
        annotation_AssociativeOriginData13.OffsetAnnotation = NULL;
        annotation_AssociativeOriginData13.OffsetAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData13.XOffsetFactor = 0;
        annotation_AssociativeOriginData13.YOffsetFactor = 0 ;
        NXOpen::Point3d point3d31(21.31267062712, 1.16180900112, 0);
        note16->SetAssociativeOrigin(annotation_AssociativeOriginData13,point3d31);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");


        //Getting sheet numbers
        NXOpen::BlockStyler::PropertyList *sheetNo1Props = sheetNo1->GetProperties();
        int sheet1No = sheetNo1Props->GetInteger("Value");
        std::stringstream buf;
        buf<<sheet1No;
        NXOpen::NXString sheetNo1Text = buf.str();        
        delete sheetNo1Props;

        NXOpen::BlockStyler::PropertyList *sheetNo2Props = sheetNo2->GetProperties();
        int sheet2No = sheetNo2Props->GetInteger("Value");
        std::stringstream buf1;
        buf1<<sheet2No;
        NXOpen::NXString sheetNo2Text = buf1.str();        
        delete sheetNo2Props;

        std::vector<NXString> stringArray4(1) ; 
        stringArray4[0]= sheetNo1Text+ " of " + sheetNo2Text;

        //Creates note in the following location for sheet number
        NXOpen::Point3d point3d7(3.5527136788005e-015,  0, 0);
        Annotations::Note *note4 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray4,point3d7,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        NXOpen::Point3d point3d8(20.7831713732126,  0.870402351045622, 0);
        note4->SetAnnotationOrigin(point3d8);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");

        //Getting sheet scale
        NXOpen::BlockStyler::PropertyList *dwgScaleProps = dwgScale->GetProperties();
        NXOpen::NXString dwgScale1 = dwgScaleProps->GetString("Value");
        delete dwgScaleProps;

        std::vector<NXString> stringArray5(1) ; 
        stringArray5[0]= dwgScale1;

        NXOpen::Point3d point3d9(3.5527136788005e-015, 0, 0);
        Annotations::Note *note5 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray5,point3d9,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData4;

        annotation_AssociativeOriginData4.OriginType = Annotations::AssociativeOriginTypeHorizontallyAligned;
        annotation_AssociativeOriginData4.View = nullView;
        annotation_AssociativeOriginData4.ViewOfGeometry = nullView;
        annotation_AssociativeOriginData4.PointOnGeometry = nullPoint;
        annotation_AssociativeOriginData4.VertAnnotation = NULL;
        annotation_AssociativeOriginData4.VertAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData4.HorizAnnotation = note4;
        annotation_AssociativeOriginData4.HorizAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData4.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData4.DimensionLine = 0;
        annotation_AssociativeOriginData4.AssociatedView = nullView;
        annotation_AssociativeOriginData4.AssociatedPoint = nullPoint;
        annotation_AssociativeOriginData4.OffsetAnnotation = NULL;
        annotation_AssociativeOriginData4.OffsetAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData4.XOffsetFactor = 0;
        annotation_AssociativeOriginData4.YOffsetFactor = 0 ;
        NXOpen::Point3d point3d10(17.9351793970217, 0.870402351045622, 0);
        note5->SetAssociativeOrigin(annotation_AssociativeOriginData4,point3d10);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");


        //Getting contract number
        NXOpen::BlockStyler::PropertyList *contractNoProps = contractNo->GetProperties();
        NXOpen::NXString contractNo1 = contractNoProps->GetString("Value");
        delete contractNoProps;

        std::vector<NXString> stringArray6(2); 

        stringArray6[0]= "Contract No.";
        stringArray6[1]= contractNo1;

        NXOpen::Point3d point3d11(3.5527136788005e-015, 0, 0);
        Annotations::Note *note6 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray6,point3d11,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        NXOpen::Point3d point3d12(16.3033007829268,  2.57503988424, 0);
        note6->SetAnnotationOrigin(point3d12);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");

        //Getting the string value
        NXOpen::BlockStyler::PropertyList *meProps = me->GetProperties();
        NXOpen::NXString me1 = meProps->GetString("Value");
        delete meProps;

        
        std::vector<NXString> stringArray7(1); 
        stringArray7[0]= "<C0.75>ME: " + me1 + "<C>";
        NXOpen::Point3d point3d13(15.8690005415459, 1.1187076082971, 0);
        Annotations::Note *note7 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray7,point3d13,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");

        //Getting the string value
        NXOpen::BlockStyler::PropertyList *strProps = str->GetProperties();
        NXOpen::NXString str1 = strProps->GetString("Value");
        delete strProps;

        
        std::vector<NXString> stringArray8(1); 
        stringArray8[0]= "<C0.75>STR: " + str1 + "<C>";
        NXOpen::Point3d point3d14(0,0,0);
        Annotations::Note *note8 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray8,point3d14,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData5;

        annotation_AssociativeOriginData5.OriginType = Annotations::AssociativeOriginTypeVerticallyAligned;
        annotation_AssociativeOriginData5.View = nullView;
        annotation_AssociativeOriginData5.ViewOfGeometry = nullView;
        annotation_AssociativeOriginData5.PointOnGeometry = nullPoint;
        annotation_AssociativeOriginData5.VertAnnotation = note7;
        annotation_AssociativeOriginData5.VertAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData5.HorizAnnotation = NULL;
        annotation_AssociativeOriginData5.HorizAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData5.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData5.DimensionLine = 0;
        annotation_AssociativeOriginData5.AssociatedView = nullView;
        annotation_AssociativeOriginData5.AssociatedPoint = nullPoint;
        annotation_AssociativeOriginData5.OffsetAnnotation = NULL;
        annotation_AssociativeOriginData5.OffsetAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData5.XOffsetFactor = 0;
        annotation_AssociativeOriginData5.YOffsetFactor = 0 ;
        NXOpen::Point3d point3d15(15.8690005415459, 1.38024175993132, 0);
        note8->SetAssociativeOrigin(annotation_AssociativeOriginData5,point3d15);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");

        //Getting the string value
        NXOpen::BlockStyler::PropertyList *leadProps = lead->GetProperties();
        NXOpen::NXString lead1 = leadProps->GetString("Value");
        delete leadProps;

        std::vector<NXString> stringArray9(1); 
        stringArray9[0]= "<C0.75>Lead: " + lead1 + "<C>";
        NXOpen::Point3d point3d16(0,0,0);
        Annotations::Note *note9 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray9,point3d16,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData6;

        annotation_AssociativeOriginData6.OriginType = Annotations::AssociativeOriginTypeVerticallyAligned;
        annotation_AssociativeOriginData6.View = nullView;
        annotation_AssociativeOriginData6.ViewOfGeometry = nullView;
        annotation_AssociativeOriginData6.PointOnGeometry = nullPoint;
        annotation_AssociativeOriginData6.VertAnnotation = note8;
        annotation_AssociativeOriginData6.VertAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData6.HorizAnnotation = NULL;
        annotation_AssociativeOriginData6.HorizAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData6.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData6.DimensionLine = 0;
        annotation_AssociativeOriginData6.AssociatedView = nullView;
        annotation_AssociativeOriginData6.AssociatedPoint = nullPoint;
        annotation_AssociativeOriginData6.OffsetAnnotation = NULL;
        annotation_AssociativeOriginData6.OffsetAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData6.XOffsetFactor = 0;
        annotation_AssociativeOriginData6.YOffsetFactor = 0 ;
        NXOpen::Point3d point3d17(15.8690005415459, 1.63351693835603, 0);
        note9->SetAssociativeOrigin(annotation_AssociativeOriginData6,point3d17);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");

        //Getting the string value
        NXOpen::BlockStyler::PropertyList *designProps = design->GetProperties();
        NXOpen::NXString design1 = designProps->GetString("Value");
        delete designProps;

        std::vector<NXString> stringArray10(1); 
        stringArray10[0]= "<C0.75>Design: " + design1 + "<C>";
        NXOpen::Point3d point3d18(0,0,0);
        Annotations::Note *note10 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray10,point3d18,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData7;

        annotation_AssociativeOriginData7.OriginType = Annotations::AssociativeOriginTypeVerticallyAligned;
        annotation_AssociativeOriginData7.View = nullView;
        annotation_AssociativeOriginData7.ViewOfGeometry = nullView;
        annotation_AssociativeOriginData7.PointOnGeometry = nullPoint;
        annotation_AssociativeOriginData7.VertAnnotation = note9;
        annotation_AssociativeOriginData7.VertAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData7.HorizAnnotation = NULL;
        annotation_AssociativeOriginData7.HorizAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData7.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData7.DimensionLine = 0;
        annotation_AssociativeOriginData7.AssociatedView = nullView;
        annotation_AssociativeOriginData7.AssociatedPoint = nullPoint;
        annotation_AssociativeOriginData7.OffsetAnnotation = NULL;
        annotation_AssociativeOriginData7.OffsetAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData7.XOffsetFactor = 0;
        annotation_AssociativeOriginData7.YOffsetFactor = 0 ;
        NXOpen::Point3d point3d19(15.8690005415459, 1.88403912571091, 0);
        note10->SetAssociativeOrigin(annotation_AssociativeOriginData7,point3d19);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");

        //Getting the string value
        NXOpen::BlockStyler::PropertyList *desSignProps = desSign->GetProperties();
        NXOpen::NXString desSign1 = desSignProps->GetString("Value");
        delete desSignProps;

        std::vector<NXString> stringArray11(1); 
        stringArray11[0]= "<C0.75>" + desSign1 + "<C>";
        NXOpen::Point3d point3d20(0,0,0);
        Annotations::Note *note11 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray11,point3d20,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData8;

        annotation_AssociativeOriginData8.OriginType = Annotations::AssociativeOriginTypeHorizontallyAligned;
        annotation_AssociativeOriginData8.View = nullView;
        annotation_AssociativeOriginData8.ViewOfGeometry = nullView;
        annotation_AssociativeOriginData8.PointOnGeometry = nullPoint;
        annotation_AssociativeOriginData8.VertAnnotation = NULL;
        annotation_AssociativeOriginData8.VertAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData8.HorizAnnotation = note10;
        annotation_AssociativeOriginData8.HorizAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData8.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData8.DimensionLine = 0;
        annotation_AssociativeOriginData8.AssociatedView = nullView;
        annotation_AssociativeOriginData8.AssociatedPoint = nullPoint;
        annotation_AssociativeOriginData8.OffsetAnnotation = NULL;
        annotation_AssociativeOriginData8.OffsetAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData8.XOffsetFactor = 0;
        annotation_AssociativeOriginData8.YOffsetFactor = 0 ;
        NXOpen::Point3d point3d21(16.8574927841817, 1.88403912571091, 0);
        note11->SetAssociativeOrigin(annotation_AssociativeOriginData8,point3d21);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");

        //Getting lead date value
        NXOpen::BlockStyler::PropertyList *leadSignProps = leadSign->GetProperties();
        NXOpen::NXString leadSign1 = leadSignProps->GetString("Value");
        delete leadSignProps;

        std::vector<NXString> stringArray12(1); 
        stringArray12[0]= "<C0.75>" + leadSign1 + "<C>";
        NXOpen::Point3d point3d22(0,0,0);
        Annotations::Note *note12 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray12,point3d22,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData9;

        annotation_AssociativeOriginData9.OriginType = Annotations::AssociativeOriginTypeHorizontallyAligned;
        annotation_AssociativeOriginData9.View = nullView;
        annotation_AssociativeOriginData9.ViewOfGeometry = nullView;
        annotation_AssociativeOriginData9.PointOnGeometry = nullPoint;
        annotation_AssociativeOriginData9.VertAnnotation = NULL;
        annotation_AssociativeOriginData9.VertAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData9.HorizAnnotation = note9;
        annotation_AssociativeOriginData9.HorizAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData9.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData9.DimensionLine = 0;
        annotation_AssociativeOriginData9.AssociatedView = nullView;
        annotation_AssociativeOriginData9.AssociatedPoint = nullPoint;
        annotation_AssociativeOriginData9.OffsetAnnotation = NULL;
        annotation_AssociativeOriginData9.OffsetAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData9.XOffsetFactor = 0;
        annotation_AssociativeOriginData9.YOffsetFactor = 0 ;
        NXOpen::Point3d point3d23(16.8574927841817, 1.63351693835603, 0);
        note12->SetAssociativeOrigin(annotation_AssociativeOriginData9,point3d21);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");

        //Getting STR date value
        NXOpen::BlockStyler::PropertyList *strSignProps = strSign->GetProperties();
        NXOpen::NXString strSign1 = strSignProps->GetString("Value");
        delete strSignProps;

        std::vector<NXString> stringArray13(1); 
        stringArray13[0]= "<C0.75>" + strSign1 + "<C>";
        NXOpen::Point3d point3d24(0,0,0);
        Annotations::Note *note13 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray13,point3d24,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData10;

        annotation_AssociativeOriginData10.OriginType = Annotations::AssociativeOriginTypeHorizontallyAligned;
        annotation_AssociativeOriginData10.View = nullView;
        annotation_AssociativeOriginData10.ViewOfGeometry = nullView;
        annotation_AssociativeOriginData10.PointOnGeometry = nullPoint;
        annotation_AssociativeOriginData10.VertAnnotation = NULL;
        annotation_AssociativeOriginData10.VertAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData10.HorizAnnotation = note8;
        annotation_AssociativeOriginData10.HorizAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData10.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData10.DimensionLine = 0;
        annotation_AssociativeOriginData10.AssociatedView = nullView;
        annotation_AssociativeOriginData10.AssociatedPoint = nullPoint;
        annotation_AssociativeOriginData10.OffsetAnnotation = NULL;
        annotation_AssociativeOriginData10.OffsetAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData10.XOffsetFactor = 0;
        annotation_AssociativeOriginData10.YOffsetFactor = 0 ;
        NXOpen::Point3d point3d25(16.8574927841817, 1.38024175993132, 0);
        note13->SetAssociativeOrigin(annotation_AssociativeOriginData10,point3d25);

        theSession->UpdateManager()->DoUpdate(markId1);
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "Create Annotation");

        //Getting ME date value
        NXOpen::BlockStyler::PropertyList *meSignProps = meSign->GetProperties();
        NXOpen::NXString meSign1 = meSignProps->GetString("Value");
        delete meSignProps;

        std::vector<NXString> stringArray14(1); 
        stringArray14[0]= "<C0.75>" + meSign1 + "<C>";
        NXOpen::Point3d point3d26(0,0,0);
        Annotations::Note *note14 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray14,point3d26,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        theSession->SetUndoMarkVisibility(markId1, "Create Annotation", Session::MarkVisibilityVisible);

        Annotations::Annotation::AssociativeOriginData annotation_AssociativeOriginData11;

        annotation_AssociativeOriginData11.OriginType = Annotations::AssociativeOriginTypeHorizontallyAligned;
        annotation_AssociativeOriginData11.View = nullView;
        annotation_AssociativeOriginData11.ViewOfGeometry = nullView;
        annotation_AssociativeOriginData11.PointOnGeometry = nullPoint;
        annotation_AssociativeOriginData11.VertAnnotation = NULL;
        annotation_AssociativeOriginData11.VertAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData11.HorizAnnotation = note7;
        annotation_AssociativeOriginData11.HorizAlignmentPosition = Annotations::AlignmentPositionMidCenter;
        annotation_AssociativeOriginData11.AlignedAnnotation = NULL;
        annotation_AssociativeOriginData11.DimensionLine = 0;
        annotation_AssociativeOriginData11.AssociatedView = nullView;
        annotation_AssociativeOriginData11.AssociatedPoint = nullPoint;
        annotation_AssociativeOriginData11.OffsetAnnotation = NULL;
        annotation_AssociativeOriginData11.OffsetAlignmentPosition = Annotations::AlignmentPositionTopLeft;
        annotation_AssociativeOriginData11.XOffsetFactor = 0;
        annotation_AssociativeOriginData11.YOffsetFactor = 0 ;
        NXOpen::Point3d point3d27(16.8349491151104, 1.1187076082971, 0);
        note14->SetAssociativeOrigin(annotation_AssociativeOriginData11,point3d27);

        theSession->UpdateManager()->DoUpdate(markId1);

        delete  letteringPreferences1;
        delete    userSymbolPreferences1;

    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        FillOutTitleBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int FillOutTitleBlock::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        if(block == compName)
        {
        //---------Enter your code here-----------
        }
        else if(block == dwgName)
        {
        //---------Enter your code here-----------
        }
        else if(block == dwgNo)
        {
        //---------Enter your code here-----------
        }
        else if(block == cageCode)
        {
        //---------Enter your code here-----------
            
        }
        else if(block == revision)
        {
        //---------Enter your code here-----------
            
        }
        else if(block == dwgScale)
        {
        //---------Enter your code here-----------
        }
        else if(block == sheetNo)
        {
        //---------Enter your code here-----------
        }
        else if(block == sheetNo1)
        {
        //---------Enter your code here-----------
        }
        else if(block == sheetNoOf)
        {
        //---------Enter your code here-----------
        }
        else if(block == sheetNo2)
        {
        //---------Enter your code here-----------
        }
        else if(block == separator0)
        {
        //---------Enter your code here-----------
            
        }
        else if(block == contractNo)
        {
        //---------Enter your code here-----------
        }
        else if(block == separator02)
        {
        //---------Enter your code here-----------
        }
        else if(block == design)
        {
        //---------Enter your code here-----------
        }
        else if(block == desSign)
        {
        //---------Enter your code here-----------
        }
        else if(block == separator01)
        {
        //---------Enter your code here-----------
        }
        else if(block == lead)
        {
        //---------Enter your code here-----------
        }
        else if(block == leadSign)
        {
        //---------Enter your code here-----------
        }
        else if(block == separator03)
        {
        //---------Enter your code here-----------
        }
        else if(block == str)
        {
        //---------Enter your code here-----------
        }
        else if(block == strSign)
        {
        //---------Enter your code here-----------
        }
        else if(block == separator04)
        {
        //---------Enter your code here-----------
        }
        else if(block == me)
        {
        //---------Enter your code here-----------
        }
        else if(block == meSign)
        {
        //---------Enter your code here-----------
        }

        

    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        FillOutTitleBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int FillOutTitleBlock::ok_cb()
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
        FillOutTitleBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: focusNotify_cb
//This callback is executed when any block (except the ones which receive keyboard entry such as Integer block) receives focus.
//------------------------------------------------------------------------------
void FillOutTitleBlock::focusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        FillOutTitleBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: keyboardFocusNotify_cb
//This callback is executed when block which can receive keyboard entry, receives the focus.
//------------------------------------------------------------------------------
void FillOutTitleBlock::keyboardFocusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        FillOutTitleBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}
