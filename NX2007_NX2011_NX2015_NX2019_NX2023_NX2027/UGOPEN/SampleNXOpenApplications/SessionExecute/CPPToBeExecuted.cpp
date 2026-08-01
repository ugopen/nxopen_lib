//----------------------------------------------------------------------------
//                  Copyright (c) 2018 Siemens
//                      All rights reserved
//----------------------------------------------------------------------------
// 
//
// CPPToBeExecuted.cpp
//
// Description:
//   This is an example of running a C++ DLL using Session.Execute. 
//
//   This source file is the only file required for this project, however this project also requires 
//   the DLL from the project "CPPToBeExecuted" to run.
//   
//
//----------------------------------------------------------------------------


//CPPToBeExecuted

// Mandatory UF Includes
#include <uf.h>
#include <uf_object_types.h>

// Internal Includes
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/UI.hxx>

// Internal+External Includes
#include <NXOpen/Annotations.hxx>
#include <NXOpen/Assemblies_Component.hxx>
#include <NXOpen/Assemblies_ComponentAssembly.hxx>
#include <NXOpen/AssemDebugSession.hxx>
#include <NXOpen/BasePart.hxx>
#include <NXOpen/Body.hxx>
#include <NXOpen/BodyCollection.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/ExpressionCollection.hxx>
#include <NXOpen/Face.hxx>
#include <NXOpen/Features_BlockFeatureBuilder.hxx>
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_FeatureCollection.hxx>
#include <NXOpen/FileNew.hxx>
#include <NXOpen/GeometricUtilities_BooleanOperation.hxx>
#include <NXOpen/Line.hxx>
#include <NXOpen/LogFile.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Point.hxx>
#include <NXOpen/PointCollection.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/Unit.hxx>
#include <NXOpen/UnitCollection.hxx>
#include <uf.h>
#include <uf_ui_types.h>
#include <uf_ui.h>
#include <uf_exit.h>
#include <uf_text.h>






// Std C++ Includes
#include <iostream>
#include <sstream>

using namespace NXOpen;
using std::string;
using std::exception;
using std::stringstream;
using std::endl;
using std::cout;
using std::cerr;




//------------------------------------------------------------------------------
// NXOpen c++ test class 
//------------------------------------------------------------------------------
class ClassToExecute
{
    // class members
public:
    static Session *theSession;
    static DebugSession *theDebugSession;

    ClassToExecute(char* args);
    ~ClassToExecute();
    

private:
    Part* NewPart(Session* theSession);
    void CreateBlock(Session * theSession, Part * workPart, char* size);
    ClassToExecute();
    BasePart *workPart, *displayPart;
};

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(ClassToExecute::theSession) = NULL;

//------------------------------------------------------------------------------
// Constructor 
//------------------------------------------------------------------------------
ClassToExecute::ClassToExecute(char* args)
{
    try
    {
        char* size;
        // Handle the input arguments. Each language has its own expected argument 
        // which changes the size of the created block
        if (strcmp(args, "C# Args") == 0)
        {
            size = "10";
        }
        else if (strcmp(args, "Java Args") == 0)
        {
            size = "50";
        }
        else if (strcmp(args, "Python Args") == 0)
        {
            size = "300";
        }
        else
        {
            return;
        }

        ClassToExecute::theSession = NXOpen::Session::GetSession();

        // Create a new part to create the block
        Part* workPart = NewPart(theSession);

        // Create a block with the dimensions specified by the different language specific arguments
        CreateBlock(theSession, workPart, size);
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        throw;
    }
}

Part* ClassToExecute::NewPart(Session* theSession)
{
    theSession->LogFile()->WriteLine("----------------------------------------------");
    theSession->LogFile()->WriteLine("  Menu: 'File->'New...");
    theSession->LogFile()->WriteLine("----------------------------------------------");
    NXOpen::Session::UndoMarkId markId1;
    markId1 = theSession->SetUndoMark(NXOpen::Session::MarkVisibilityVisible, "'Start");

    NXOpen::FileNew *fileNew1;
    fileNew1 = theSession->Parts()->FileNew();

    theSession->SetUndoMarkName(markId1, "''New Dialog");

    NXOpen::Session::UndoMarkId markId2;
    markId2 = theSession->SetUndoMark(NXOpen::Session::MarkVisibilityInvisible, "'New");

    theSession->DeleteUndoMark(markId2, NULL);

    NXOpen::Session::UndoMarkId markId3;
    markId3 = theSession->SetUndoMark(NXOpen::Session::MarkVisibilityInvisible, "'New");

    fileNew1->SetTemplateFileName("model-plain-1-mm-template.prt");

    fileNew1->SetUseBlankTemplate(false);

    fileNew1->SetApplicationName("ModelTemplate");

    fileNew1->SetUnits(NXOpen::Part::UnitsMillimeters);

    fileNew1->SetRelationType("");

    fileNew1->SetUsesMasterModel("No");

    fileNew1->SetTemplateType(NXOpen::FileNewTemplateTypeItem);

    fileNew1->SetTemplatePresentationName("Model");

    fileNew1->SetItemType("");

    fileNew1->SetSpecialization("");

    fileNew1->SetCanCreateAltrep(false);

    fileNew1->SetNewFileName("CPPExecuteBlock.prt");

    fileNew1->SetMasterFileName("");

    fileNew1->SetMakeDisplayedPart(true);

    fileNew1->SetDisplayPartOption(NXOpen::DisplayPartOptionAllowAdditional);

    NXOpen::NXObject *nXObject2;
    nXObject2 = fileNew1->Commit();

    NXOpen::Part *workPart(theSession->Parts()->Work());
    NXOpen::Part *displayPart(theSession->Parts()->Display());
    theSession->DeleteUndoMark(markId3, NULL);

    fileNew1->Destroy();

    theSession->ApplicationSwitchImmediate("UG_APP_MODELING");

    return workPart;
}

void ClassToExecute::CreateBlock(Session * theSession, Part * workPart, char* size)
{
    theSession->LogFile()->WriteLine("----------------------------------------------");
    theSession->LogFile()->WriteLine("  Menu: 'Insert->'Design Feature->'Block...");
    theSession->LogFile()->WriteLine("----------------------------------------------");
    Session::UndoMarkId markId4;
    markId4 = theSession->SetUndoMark(Session::MarkVisibilityVisible, "'Start");

    Features::Feature *nullNXOpen_Features_Feature(NULL);
    Features::BlockFeatureBuilder *blockFeatureBuilder1;
    blockFeatureBuilder1 = workPart->Features()->CreateBlockFeatureBuilder(nullNXOpen_Features_Feature);

    blockFeatureBuilder1->BooleanOption()->SetType(GeometricUtilities::BooleanOperation::BooleanTypeCreate);

    std::vector<Body *> targetBodies1(1);
    Body *nullNXOpen_Body(NULL);
    targetBodies1[0] = nullNXOpen_Body;
    blockFeatureBuilder1->BooleanOption()->SetTargetBodies(targetBodies1);

    blockFeatureBuilder1->BooleanOption()->SetType(GeometricUtilities::BooleanOperation::BooleanTypeCreate);

    std::vector<Body *> targetBodies2(1);
    targetBodies2[0] = nullNXOpen_Body;
    blockFeatureBuilder1->BooleanOption()->SetTargetBodies(targetBodies2);

    theSession->SetUndoMarkName(markId4, "''Block Dialog");

    Point3d coordinates1(0.0, 0.0, 0.0);
    Point *point1;
    point1 = workPart->Points()->CreatePoint(coordinates1);

    Unit *unit1(dynamic_cast<Unit *>(workPart->UnitCollection()->FindObject("MilliMeter")));
    Expression *expression1;
    expression1 = workPart->Expressions()->CreateSystemExpressionWithUnits("0", unit1);

    Session::UndoMarkId markId5;
    markId5 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "'Block");

    theSession->DeleteUndoMark(markId5, NULL);

    Session::UndoMarkId markId6;
    markId6 = theSession->SetUndoMark(Session::MarkVisibilityInvisible, "'Block");

    blockFeatureBuilder1->SetType(Features::BlockFeatureBuilder::TypesOriginAndEdgeLengths);

    blockFeatureBuilder1->SetOriginPoint(point1);

    Point3d originPoint1(0.0, 0.0, 0.0);
    blockFeatureBuilder1->SetOriginAndLengths(originPoint1, size, size, size);

    blockFeatureBuilder1->SetBooleanOperationAndTarget(Features::Feature::BooleanTypeCreate, nullNXOpen_Body);

    Features::Feature *feature1;
    feature1 = blockFeatureBuilder1->CommitFeature();

    theSession->DeleteUndoMark(markId6, NULL);

    theSession->SetUndoMarkName(markId4, "'Block");

    blockFeatureBuilder1->Destroy();

    workPart->Expressions()->Delete(expression1);
}

//------------------------------------------------------------------------------
// Destructor
//------------------------------------------------------------------------------
ClassToExecute::~ClassToExecute()
{
}

//------------------------------------------------------------------------------
// Entry point(s) for unmanaged internal NXOpen C/C++ programs
//------------------------------------------------------------------------------
//  Explicit Execution
extern "C" DllExport void ufusr( char *parm, int *returnCode, int rlen )
{
    try
    {
        // Create NXOpen C++ class instance
        ClassToExecute *theMyClass;
        theMyClass = new ClassToExecute(parm);
        delete theMyClass;
    }
    catch (...)
    {
        UI::GetUI()->NXMessageBox()->Show("Exception", NXOpen::NXMessageBox::DialogTypeError, "Unknown Exception.");
    }
}


//------------------------------------------------------------------------------
// Unload Handler
//------------------------------------------------------------------------------
extern "C" DllExport int ufusr_ask_unload()
{
    return (int)NXOpen::Session::LibraryUnloadOptionImmediately;
}


