//===============================================================================
//
//                   Copyright (c) 2010 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//========================================================================================
//File description: NX/Open example to Cycle the Drawing sheets and Drawing Note Creation
//========================================================================================
//

/* Include files */
#   include <sstream>
#   include <iostream>
using std::ostringstream;
using std::endl;    
using std::ends;
using std::cerr;


#include <uf.h>
#include <uf_ui.h>
#include <uf_defs.h>
#include <string.h>
#include <sstream>
#include <iostream>
#include <NXOpen/NXException.hxx>
#include <NXOpen/Drawings_DraftingViewCollection.hxx>
#include <NXOpen/Drawings_DrawingSheetCollection.hxx>
#include <NXOpen/Drawings_SectionView.hxx>
#include <NXOpen/Drawings_UpdateViewsBuilder.hxx>
#include <NXOpen/Annotations_AnnotationManager.hxx>
#include <NXOpen/Annotations_Note.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/Preferences_AnnotationPreferences.hxx>

using namespace std;
using namespace NXOpen;
using namespace NXOpen::Annotations;


/*****************************************************************************
 **  Activation Methods
 *****************************************************************************/
/*  Explicit Activation
 **      This entry point is used to activate the application explicitly, as in
 **      "File->Execute UG/Open->User Function..." */
extern DllExport void ufusr( char *parm, int *returnCode, int rlen )
{
    /* Initialize the API environment */
    int errorcode = UF_initialize();
    
    /* Add your application code here */
    Session *theSession = Session::GetSession();
    Part *workPart(theSession->Parts()->Work());
    Part *displayPart(theSession->Parts()->Display());
    
    
    //Getting Drawing sheets into collection of the workpart
    Drawings::DrawingSheetCollection *drawingsheets = workPart->DrawingSheets();
    Drawings::DrawingSheetCollection::iterator it;
    Drawings::DrawingSheet *mysheet;
    
    /*----------------------------------------------
     Here we loop through all the sheets in the part.
     For each sheet, we open the sheet, update all views in it,
     And then pop-up a message box listing the 
     views on the sheet.  This could be modified to plot out
     the sheets instead.
     ----------------------------------------------*/
    for(it=drawingsheets->begin();it!=drawingsheets->end();it++)
    {
        
        mysheet = *it;
        mysheet->Open();
        // ----------------------------------------------
        //   Menu: Edit->View->Update Views...
        // ----------------------------------------------
        theSession->Parts()->Work()->DraftingViews()->UpdateViews(Drawings::DraftingViewCollection::ViewUpdateOptionAll,mysheet);
        
        Annotations::LetteringPreferences *letteringPreferences1;
        letteringPreferences1 = workPart->Annotations()->Preferences()->GetLetteringPreferences();
        
        
        //Setting Lettering Preferences
        Annotations::Lettering Annotations_Lettering1;
        Annotations_Lettering1.Size = 0.35;
        Annotations_Lettering1.CharacterSpaceFactor = 1;
        Annotations_Lettering1.AspectRatio = 1.0;
        Annotations_Lettering1.LineSpaceFactor = 1.0;
        Annotations_Lettering1.Cfw.Color = 2;
        Annotations_Lettering1.Cfw.Font = 1;
        Annotations_Lettering1.Cfw.Width = Annotations::LineWidthThin;
        letteringPreferences1->SetGeneralText(Annotations_Lettering1);
        
        workPart->Annotations()->Preferences()->SetLetteringPreferences(letteringPreferences1);
        // ----------------------------------------------
        //   Menu: Insert->Annotation...
        // ----------------------------------------------
        Annotations::UserSymbolPreferences *userSymbolPreferences1 = theSession->Parts()->Work()->Annotations()->NewUserSymbolPreferences(UserSymbolPreferences::SizeTypeScaleAspectRatio,1,1);
        UF_system_info_t info;
        UF_ask_system_info(&info);
        std::ostringstream buffer; 
        buffer << info.date_buf; 
        NXOpen::NXString currDate = buffer.str(); 
        string date = currDate.GetText();
        size_t pos1 = date.find_first_of(" ");
        date = date.substr(0,pos1);
        currDate = date;
        
        
        std::vector<NXString> stringArray1(1);
        stringArray1[0]=currDate.GetText();
        std::vector<NXString> stringArray2(2);        
        stringArray2[0]="Printed On";
        stringArray2[1]=currDate.GetText();
        
        
        NXOpen::Point3d point3d1(30.643873924,1.999761255 ,0);
        
        //NULL INPUT TO BE CHANGED
        //The below method will create a note.
        
        NXOpen::Annotations::Note *note1 = theSession->Parts()->Work()->Annotations()->CreateNote(stringArray2,point3d1,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
        delete userSymbolPreferences1;
        delete letteringPreferences1;
        
        // ----------------------------------------------
        //   Printing Drafting views
        // ----------------------------------------------
        std::vector<NXOpen::Drawings::DraftingView *> dfviews = mysheet->GetDraftingViews();
        NXOpen::NXString sheet_name = "Printing Sheet: " + mysheet->Name();
        std::vector<NXOpen::NXString >sheet_names(1);
        UI *theUI = UI::GetUI();         
        
        //Collecting View names and copying to String
        for(int i=0;i!=dfviews.size();i++)
        {
            if(i==0)
            {
                sheet_names[0] = "Sheet contains following views: \n" + dfviews[i]->Name();
            }
            else
            {
                sheet_names[0] =  sheet_names[0] +"\n"+ dfviews[i]->Name();
                
            }
        }
        
        //Displaying the Drawing sheet view names
        theUI->NXMessageBox()->Show(sheet_name.GetText(), NXOpen::NXMessageBox::DialogTypeInformation,sheet_names[0].GetText());
        
        // ----------------------------------------------
        //   Menu: Edit->Delete...
        // ----------------------------------------------
        theSession->UpdateManager()->ClearErrorList();
        Session::UndoMarkId markId1;
        markId1 = theSession->SetUndoMark(Session::MarkVisibilityVisible, "Delete");
        
        int err1;
        err1 = theSession->UpdateManager()->AddToDeleteList(note1);
        
        int err2;
        err2= theSession->UpdateManager()->DoUpdate(markId1);
        
        
    }
    
    /* Terminate the API environment */
    errorcode = UF_terminate();
}

/*****************************************************************************
 **  Utilities
 *****************************************************************************/

/* Unload Handler
 **     This function specifies when to unload your application from Unigraphics.
 **     If your application registers a callback (from a MenuScript item or a
 **     User Defined Object for example), this function MUST return
 **     "UF_UNLOAD_UG_TERMINATE". */
extern int ufusr_ask_unload( void )
{
    return( UF_UNLOAD_IMMEDIATELY );
}

