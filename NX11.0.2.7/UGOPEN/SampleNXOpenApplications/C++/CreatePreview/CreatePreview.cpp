//===============================================================================
//
//                   Copyright 2016 Siemens PLM Software Inc.
//                     Unpublished - All rights reserved
//===============================================================================
// File description: NXOpen example for creation of fitted previews for
// Disclosed Model Views
//===============================================================================
//

/* Include files */
#include <sstream>
#include <iostream>

using std::ostringstream;
using std::endl;    
using std::ends;
using std::cerr;

#include <NXOpen/BasePart.hxx>
#include <NXOpen/LogFile.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/View.hxx>
#include <NXOpen/ViewCollection.hxx>
#include <NXOpen/ViewUIManager.hxx>
#include <uf.h>
#include <uf_exit.h> 
#include <uf_ui.h>  

using namespace NXOpen;

/*****************************************************************************
 **  Activation Methods
 *****************************************************************************/
/**  Explicit Activation
 **  This entry point is used to activate the application explicitly, as in
 **  "File->Execute UG/Open->User Function..." */

extern DllExport void ufusr( char *parm, int *returnCode, int rlen )
{
    /* Initialize the API environment */
    int errorcode = UF_initialize();
        
    //Get the current session and the display part session
    Session *theSession = Session::GetSession();
    Part *workPart(theSession->Parts()->Work());
    Part *displayPart(theSession->Parts()->Display());
    
    UI* uiPt = UI::GetUI();
    ViewUIManager* viewUIManager = uiPt->UI::ViewUIManager();

    Session::UndoMarkId markId1;
    markId1 = theSession->SetUndoMark(Session::MarkVisibilityVisible, "Create Model View Preview");
 
    //Get disclosed model views in the work part
    std::vector<NXOpen::View *> disclosedViews;
    disclosedViews = displayPart->Views()->GetDisclosedModelViews();
 
    std::vector<bool> checkPreview;
    std::vector<NXOpen::View *> previewCreated;

    for (int i = 0; i < disclosedViews.size(); i++)
    {
        //Check if disclosed model views have a preview
        bool hasPreview = disclosedViews[i]->View::HasPreview();
        checkPreview.push_back( hasPreview );
        //If no preview exists, create a fitted preview for the disclosed model view
        if (!hasPreview)
        {
            viewUIManager->CreatePreview(disclosedViews[i], true);
            previewCreated.push_back(disclosedViews[i]);
        }
    }

    if (previewCreated.size() > 0)
    {
        //If any previews were created, write to the syslog the name of the part and the model view for which the preview was created
        theSession->LogFile()->Write("Previews were created for these disclosed model views:");
        for (int a = 0; a < previewCreated.size(); a++)
        {
            NXString partName = workPart->NXObject::Name();
            NXString viewName = (previewCreated[a])->NXObject::Name();
 
            theSession->LogFile()->Write("\n\t");
            theSession->LogFile()->Write(partName);    
            theSession->LogFile()->Write(":\t");   
            theSession->LogFile()->Write(viewName);
        }
    }
    
    bool flag = true;
    for (int j = 0; j < disclosedViews.size(); j++)
    {
        if ( !(checkPreview[j]) )
        {
            if ( !(disclosedViews[j]->View::HasPreview()) )
            // if a disclosed view still does not have a preview, write to the syslog the name of the part and the model view
            {
                if (flag)
                {
                    theSession->LogFile()->Write("\nPreviews could not be generated for these disclosed model views:");
                    flag = false;
                }

                NXString partName = workPart->NXObject::Name();
                NXString viewName = (disclosedViews[j])->NXObject::Name();
                
                theSession->LogFile()->Write("\n\t");
                theSession->LogFile()->Write(partName);
                theSession->LogFile()->Write(":\t");
                theSession->LogFile()->Write(viewName);
            }
        }
    }    
    theSession->LogFile()->Write("\n");

    /* Terminate the API environment */
    errorcode = UF_terminate();
}

/*      Unload Handler
 **     This function specifies when to unload your application from Unigraphics.
 **     If your application registers a callback (from a MenuScript item or a
 **     User Defined Object for example), this function MUST return
 **     "UF_UNLOAD_UG_TERMINATE". */
extern int ufusr_ask_unload( void )
{
    return( UF_UNLOAD_IMMEDIATELY );
}
