//===============================================================================
//
//                   Copyright (c) 2010 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//====================================================================================
//File description: NXOpen example for Extrude creation by modifying C++ journal
//====================================================================================
//

#include <uf_defs.h>
#include <uf_ui.h>
#include <uf.h>
#include <sstream>
#include <NXOpen/NXException.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/CurveFeatureRule.hxx>
#include <NXOpen/Direction.hxx>
#include <NXOpen/DirectionCollection.hxx>
#include <NXOpen/Features_ExtrudeBuilder.hxx>
#include <NXOpen/Features_FeatureCollection.hxx>
#include <NXOpen/GeometricUtilities_BooleanOperation.hxx>
#include <NXOpen/GeometricUtilities_Extend.hxx>
#include <NXOpen/GeometricUtilities_FeatureOffset.hxx>
#include <NXOpen/GeometricUtilities_FeatureOptions.hxx>
#include <NXOpen/GeometricUtilities_Limits.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/ScRuleFactory.hxx>
#include <NXOpen/SectionCollection.hxx>
#include <NXOpen/SelectionIntentRule.hxx>
#include <NXOpen/Sketch.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/NXMessageBox.hxx>


using namespace NXOpen;
using namespace std;

extern "C" DllExport int ufusr_ask_unload()
{
    return (int)Session::LibraryUnloadOptionImmediately;
}

// **** Added Code ****

//Method that returns sketch after user selection
NXOpen::Sketch* SelectSketch()
{	
	
	UI *theUI = UI::GetUI();

	NXOpen::Selection::SelectionScope scope = Selection::SelectionScopeWorkPart;
	NXOpen::Selection::SelectionAction action = Selection::SelectionActionClearAndEnableSpecific;
	std::vector<NXOpen::Selection::MaskTriple>selectionMask_array(1);
	selectionMask_array[0].Type = UF_sketch_type;
	selectionMask_array[0].Subtype = 0;
	selectionMask_array[0].SolidBodySubtype = 0;
	NXOpen::TaggedObject *selectedObject = NULL;
	Point3d cursor;
	cursor.X = 0.0;
	cursor.Y = 0.0;
	cursor.Z = 0.0;

	theUI->SelectionManager()->SelectTaggedObject("Select Sketch","Sketch Selection",scope,action,true,false,selectionMask_array,&selectedObject,&cursor);

	Sketch *sketch1(dynamic_cast<Sketch *>(selectedObject));
	if(sketch1==NULL)
	{
		return NULL;
	}

	return sketch1;	

}

//^^^^^^^^^^^^^^^^^^^^^

extern "C" DllExport void ufusr(char *param, int *retCode, int paramLen)
{
	// **** Added Code ****
	// Initialize the API environment
	int errorcode = UF_initialize();



	char labels[][16] = {"Start Limit","End Limit"};
	int noOfitems = 2;
	double limits[2] = {0.0,1.0};
	int *ip5 = NULL;
	int response;
	NXOpen::Sketch* sketch1 = NULL;

	//Method SelectSketch is called for user to select sketch
	sketch1 =  SelectSketch();
	if(sketch1 == NULL)
	{
		return;
	}
	//Below method launches dialog for asking start and end limits from the user
	response = uc1609("Start and End Limit", labels ,noOfitems,limits, ip5);


	//If User Input is Ok Program will continue else terminates
	if((response == 3) || (response == 4))
	{

	}
	else
	{
		return ;
	}	


	std::stringstream start;
	std::stringstream end;
	start<<limits[0];
	end<<limits[1];

	//^^^^^^^^^^^^^^^^^^^^^



	Session *theSession = Session::GetSession();
	Part *workPart(theSession->Parts()->Work());
	Part *displayPart(theSession->Parts()->Display());
    // ----------------------------------------------
    //   Menu: Insert->Design Feature->Extrude...
    // ----------------------------------------------


    Session::UndoMarkId markId1;
    markId1 = theSession->SetUndoMark(Session::MarkVisibilityVisible, "Start");
    
    Section *section1;
    section1 = workPart->Sections()->CreateSection(0.00095, 0.001, 0.5);
    
    Features::Feature *nullFeatures_Feature(NULL);
    
	//Inititalizing ExtrudeBuilder with NULL Feature.
    Features::ExtrudeBuilder *extrudeBuilder1;
    extrudeBuilder1 = workPart->Features()->CreateExtrudeBuilder(nullFeatures_Feature);
    extrudeBuilder1->SetSection(section1);
    
 
    
   
    //Boolean Type is set to Create
    extrudeBuilder1->BooleanOperation()->SetType(GeometricUtilities::BooleanOperation::BooleanTypeCreate);
    
	// **** Added Code ****

    //Stat end Endlimits are the inputs from the user in the strings start and end.
	extrudeBuilder1->Limits()->StartExtend()->Value()->SetRightHandSide(start.str());    
    extrudeBuilder1->Limits()->EndExtend()->Value()->SetRightHandSide(end.str());

	//^^^^^^^^^^^^^^^^^^^^^
    
	//Default offset values are kept
    extrudeBuilder1->Offset()->StartOffset()->SetRightHandSide("0");    
    extrudeBuilder1->Offset()->EndOffset()->SetRightHandSide("0.25");    
        
    
	theSession->SetUndoMarkName(markId1, "'Extrude Dialog");
    section1->SetAllowedEntityTypes(Section::AllowTypesOnlyCurves);
    
	
    
    std::vector<Features::Feature *> features1(1);
  	features1[0] = sketch1->Feature();

    CurveFeatureRule *curveFeatureRule1;
    curveFeatureRule1 = workPart->ScRuleFactory()->CreateRuleCurveFeature(features1);

    
    section1->AllowSelfIntersection(false);
    
    std::vector<SelectionIntentRule *> rules1(1);
    rules1[0] = curveFeatureRule1;

	// **** Added Code **** 

	//Accepting all the geometry from the sketch
	std::vector<NXObject *> geoms = sketch1->GetAllGeometry();
	NXObject *nXObject1 = geoms[0];

	//^^^^^^^^^^^^^^^^^^^^^

	
    NXObject *nullNXObject(NULL);
    Point3d helpPoint1(4.0, 2.58864289093996, 2.22930704874002);

	// **** Added Code ****
	
	//The selected sketch is added to the section
    section1->AddToSection(rules1, nXObject1, nullNXObject, nullNXObject, helpPoint1, Section::ModeCreate);
	
	//^^^^^^^^^^^^^^^^^^^^^
    
	//Setting up the direction 
    Direction *direction1;
    direction1 = workPart->Directions()->CreateDirection(sketch1, SenseForward, SmartObject::UpdateOptionWithinModeling);
    
    extrudeBuilder1->SetDirection(direction1);
    extrudeBuilder1->SetParentFeatureInternal(false);
    
	//CommitFeature emethod will create Extrude
    Features::Feature *feature1;
    feature1 = extrudeBuilder1->CommitFeature();


    theSession->SetUndoMarkName(markId1, "Extrude");
    extrudeBuilder1->Destroy();
    
	// **** Added Code ****

	// Terminate the API environment
	errorcode = UF_terminate();

	//^^^^^^^^^^^^^^^^^^^^^
}



