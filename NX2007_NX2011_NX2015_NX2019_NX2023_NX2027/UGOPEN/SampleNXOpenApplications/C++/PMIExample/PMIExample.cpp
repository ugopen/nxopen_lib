//===============================================================================
//
//                   Copyright (c) 2010 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//===============================================================================
//File description: NX/Open example for creation of PMI dimension.
//===============================================================================
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
#include <uf_exit.h>    
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Annotations_AnnotationManager.hxx>
#include <NXOpen/Annotations_DimensionCollection.hxx>
#include <NXOpen/Drawings_BaseView.hxx>
#include <NXOpen/Drawings_DraftingViewCollection.hxx>
#include <NXOpen/Edge.hxx>
#include <NXOpen/Features_Cylinder.hxx>
#include <NXOpen/Features_FeatureCollection.hxx>
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
    
    
    /* Add your application code here */
    
    //Getting the Current Session and the display part session
    Session *theSession = Session::GetSession();
    Part *workPart(theSession->Parts()->Work());
    Part *displayPart(theSession->Parts()->Display());
    
    //----------------------------------------------
    //Creates a diamemter dimension on an arc
    //----------------------------------------------
    
    Session::UndoMarkId markId1;
    markId1 = theSession->SetUndoMark(Session::MarkVisibilityVisible, "Create Dimension");
    
    Annotations::DimensionData *dimensionData1 = workPart->Annotations()->NewDimensionData();
    Annotations::Associativity *associativity1 = workPart->Annotations()->NewAssociativity();
    
    Features::Cylinder *cylinder1(dynamic_cast<Features::Cylinder *>(workPart->Features()->FindObject("CYLINDER(0)")));
    
    
    Edge *edge1(dynamic_cast<Edge *>(cylinder1->FindObject("EDGE * 3 * 1")));
    associativity1->SetFirstObject(edge1);
    associativity1->SetSecondObject(NULL);
    Drawings::BaseView *baseView1(dynamic_cast<Drawings::BaseView *>(workPart->DraftingViews()->FindObject("TOP@1")));
    associativity1->SetObjectView(baseView1);
    
    
    associativity1->SetPointOption(Annotations::AssociativityPointOptionNone);
    associativity1->SetLineOption(Annotations::AssociativityLineOptionNone);
    
    
    std::vector<Annotations::Associativity *> associativity2(1);
    associativity2[0] = associativity1;
    dimensionData1->SetAssociativity(1, associativity2);;
    
    Point3d origin(50,50,0);
    
    //This method will create a dimension on the edge.
    Annotations::DiameterDimension *diameterDimension = workPart->Dimensions()->CreateDiameterDimension(dimensionData1,origin);
    
    delete dimensionData1;
    delete associativity1;
    
    
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

