//===============================================================================
//
//                   Copyright (c) 2010 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//===============================================================================
//File description: NX/Open example showing Selection options while blanking Datums
//===============================================================================
//

/* Include files */
#include <sstream>
#include <iostream>
using std::ostringstream;
using std::endl;    
using std::ends;
using std::cerr;

#include <uf.h>
#include <uf_ui.h>
#include <uf_exit.h>
#include <uf_defs.h>
#include <NXOpen/NXException.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/DatumAxis.hxx>
#include <NXOpen/DatumCollection.hxx>
#include <NXOpen/DatumPlane.hxx>
#include <NXOpen/DisplayManager.hxx>
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Session.hxx>
#include <sstream>
#include <NXOpen/UI.hxx>
#include <NXOpen/NXMessageBox.hxx>
using namespace NXOpen;

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
    
    
    /* TODO: Add your application code here */
    Session *theSession = Session::GetSession();
    Part *workPart(theSession->Parts()->Work());
    Part *displayPart(theSession->Parts()->Display());
    
    
    // FILTERING BY TYPE:
    // Use in place of the journal code for "Select All" with filter
    // type set to "Datums".
    
    Session::UndoMarkId undoMark;
    undoMark = theSession->SetUndoMark(Session::MarkVisibilityVisible, "Hide");
    NXOpen::DatumCollection::iterator it;
    std::vector<DisplayableObject *> disp_objs;
    NXOpen::DatumCollection *part_datums = theSession->Parts()->Work()->Datums();
    int i=0;
    
    for(it = part_datums->begin();it!= part_datums->end();it++)
    { 
        disp_objs.push_back(*it);
        
    }
    
    theSession->DisplayManager()->BlankObjects(disp_objs);
    theSession->DisplayManager()->MakeUpToDate();
    size_t count = disp_objs.size();
    
    std::stringstream stringBuffer;
    stringBuffer<<count;
    NXOpen::NXString msgstring;
    msgstring = stringBuffer.str()+" Datums were blanked";
    
    UI *theUI = UI::GetUI();
    theUI->NXMessageBox()->Show("Datums Blank Status", NXOpen::NXMessageBox::DialogTypeInformation,msgstring.GetText());
    
    // ----------------------------------------------
    //   Menu: Edit->Undo List-> 'Hide
    // ----------------------------------------------
    bool marksRecycled1;
    bool undoUnavailable1;
    theSession->UndoLastNVisibleMarks(1, &marksRecycled1, &undoUnavailable1);    
    
    
    
    // FILTERING BY DETAILED TYPE:
    // Use in place of the journal code for "Select All" with detailed filter type
    // set to "Datums - Datum Planes".
    
    /*CODE TO BE WRITTEN*/
    undoMark = theSession->SetUndoMark(Session::MarkVisibilityVisible, "Hide");
    int length =0;
    i=0;
    for(it = part_datums->begin();it!= part_datums->end();it++)
    {
        disp_objs.push_back(*it);
        DatumPlane *datumPlane1(dynamic_cast<DatumPlane *> (disp_objs[i]));
        if(datumPlane1 != NULL)
        {
            disp_objs[i]->Blank();
            length++;
            
        }
        i++;
    }
    
    std::stringstream stringBuffer0;
    stringBuffer0<<length;
    NXOpen::NXString msgstring0;
    
    msgstring0 = stringBuffer0.str()+" datum planes were blanked.";
    theSession->DisplayManager()->MakeUpToDate();
    theUI->NXMessageBox()->Show("Datum planes Blank Status", NXOpen::NXMessageBox::DialogTypeInformation,msgstring0.GetText());
    
    // ----------------------------------------------
    //   Menu: Edit->Undo List-> 'Hide
    // ----------------------------------------------    
    theSession->UndoLastNVisibleMarks(1, &marksRecycled1, &undoUnavailable1);
    
    
    
    
    
    // FILTERING BY LAYER:
    // Use in place of the journal code for "Select All" with filter type
    // set to "Layers - 10".
    
    undoMark = theSession->SetUndoMark(Session::MarkVisibilityVisible, "Hide");
    length =0;
    i=0;
    for(it = part_datums->begin();it!= part_datums->end();it++)
    {      
        
        disp_objs.push_back(*it);
        int layer_no;
        layer_no = disp_objs[i]->Layer();
        if(layer_no==10)
        {
            disp_objs[i]->Blank();
            length++;
        }
        i++;        
        
    }
    
    std::stringstream stringBuffer1;
    stringBuffer1<<length;
    NXOpen::NXString msgstring1;
    
    msgstring1 = stringBuffer1.str()+" Datums on layer 10 were blanked";
    theSession->DisplayManager()->MakeUpToDate();
    theUI->NXMessageBox()->Show("Layer 10 Blank Status", NXOpen::NXMessageBox::DialogTypeInformation,msgstring1.GetText());
    
    // ----------------------------------------------
    //   Menu: Edit->Undo List-> 'Hide
    // ----------------------------------------------    
    theSession->UndoLastNVisibleMarks(1, &marksRecycled1, &undoUnavailable1);
    
    
    
    // FILTERING BY DISPLAY ATTRIBUTES:
    // Use in place of the journal code for "Select All" with filter type
    // set to "Display Attributes - Dashed, Thick Width".
    
    undoMark = theSession->SetUndoMark(Session::MarkVisibilityVisible, "Hide");
    length =0;i=0;
    for(it = part_datums->begin();it!= part_datums->end();it++)
    {      
        
        disp_objs.push_back(*it);
        
        
        if(disp_objs[i]->LineFont()== NXOpen::DisplayableObject::ObjectFontDashed && disp_objs[i]->LineWidth()==  NXOpen::DisplayableObject::ObjectWidthThick )
        {
            disp_objs[i]->Blank();
            length++;
        }
        i++;                     
    }
    std::stringstream stringBuffer2;
    stringBuffer2<<length;
    NXOpen::NXString msgstring2;
    
    msgstring2 = stringBuffer2.str()+" datums with dashed line font and thick width were blanked.";
    theSession->DisplayManager()->MakeUpToDate();
    theUI->NXMessageBox()->Show("Blank status on Line Font and Width", NXOpen::NXMessageBox::DialogTypeInformation,msgstring2.GetText());
    
    // ----------------------------------------------
    //   Menu: Edit->Undo List-> 'Hide
    // ----------------------------------------------    
    theSession->UndoLastNVisibleMarks(1, &marksRecycled1, &undoUnavailable1);
    
    
    
    
    //FILTERING BY COLOR:
    //Use in place of the journal code for "Select All" with filter type
    //set to "Color - 134".
    
    undoMark = theSession->SetUndoMark(Session::MarkVisibilityVisible, "Hide");
    length =0;
    i=0;
    for(it = part_datums->begin();it!= part_datums->end();it++)
    {      
        
        disp_objs.push_back(*it);
        
        
        if((disp_objs[i]->Color()) == 134 )
        {
            disp_objs[i]->Blank();
            length++;
        }
        i++;                     
    }
    std::stringstream stringBuffer3;
    stringBuffer3<<length;
    NXOpen::NXString msgstring3;
    
    msgstring3 = stringBuffer3.str()+" datums with color 134 were blanked.";
    theSession->DisplayManager()->MakeUpToDate();
    theUI->NXMessageBox()->Show("Color Blank Status", NXOpen::NXMessageBox::DialogTypeInformation,msgstring3.GetText());
    
    // ----------------------------------------------
    //   Menu: Edit->Undo List-> 'Hide
    // ----------------------------------------------    
    theSession->UndoLastNVisibleMarks(1, &marksRecycled1, &undoUnavailable1);        
    
    
    
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

