//----------------------------------------------------------------------------
//                  Copyright (c) 2023 Siemens
//                      All rights reserved
//----------------------------------------------------------------------------
// 
//----------------------------------------------------------------------------

//CPPExecutor
//
// Mandatory UF Includes
#include <uf.h>
#include <uf_object_types.h>

// Internal Includes
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/UI.hxx>

// Internal+External Includes
#include <NXOpen/Annotations.hxx>
#include <NXOpen/Assemblies_Component.hxx>
#include <NXOpen/Assemblies_ComponentAssembly.hxx>
#include <NXOpen/Body.hxx>
#include <NXOpen/BodyCollection.hxx>
#include <NXOpen/Face.hxx>
#include <NXOpen/Line.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/NXVariant.hxx>

// Std C++ Includes
#include <iostream>
#include <sstream>
#include <vector>
#include <filesystem>

using namespace NXOpen;
using namespace std::string_literals;
using std::string;
using std::exception;
using std::stringstream;
using std::endl;
using std::cout;
using std::cerr;

struct ProgramToExecuteEntry
{
    NXOpen::NXString pathToBinary;
    NXOpen::NXString className;
};

//------------------------------------------------------------------------------
// NXOpen c++ test class 
//------------------------------------------------------------------------------
class MyClass
{
    // class members
public:
    static Session* theSession;

    static UI* theUI;


    MyClass();
    ~MyClass();

    void do_it(char* parm);
    void CallExecutor(NXOpen::NXString PathToBinaries);
    void ExecuteProgram(ProgramToExecuteEntry programsToExecute, std::vector<NXOpen::NXVariant> args);
    void print(const NXString&);
    void print(const string&);
    void print(const char*);


private:
    BasePart* workPart, * displayPart;


    NXMessageBox* mb;
    ListingWindow* lw;
    LogFile* lf;

};

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session* (MyClass::theSession) = NULL;

UI* (MyClass::theUI) = NULL;


void MyClass::CallExecutor(NXOpen::NXString PathToBinaries)
{
    theSession->ListingWindow()->Open();
    theSession->ListingWindow()->WriteLine("CallExecute from C++ Executor Program.");

    // Pass in five different arguments
    std::vector<NXOpen::NXVariant> args;
    args.push_back(1);
    args.push_back(3.14);
    args.push_back(false);
    // Please note, do attemp to use a raw const char * as this will get converted to a bool
    // args.push_back("A String Argument");
    // so instead of this use below or 
    args.push_back(NXOpen::NXString("A String Argument"));
    // Or this option, please note you will need to use string_literals (see top using statement)
    // args.push_back("A String Argument"s);
    // For more infomation on this topic, see NXVariant.hxx documentation.

    args.push_back(theSession->Parts()->Work());

    std::vector<ProgramToExecuteEntry> programsToExecute;
    ProgramToExecuteEntry cppProgram;
    cppProgram.pathToBinary = PathToBinaries + "\\CPPToBeExecuted.dll";
    cppProgram.className = nullptr;
    programsToExecute.push_back(cppProgram);

    ProgramToExecuteEntry csProgram;
    csProgram.pathToBinary = PathToBinaries + "\\CSToBeExecuted.dll";
    csProgram.className = "CSToBeExecuted";
    programsToExecute.push_back(csProgram);

    ProgramToExecuteEntry javaProgram;
    javaProgram.pathToBinary = PathToBinaries + "\\JavaToBeExecuted.class";
    javaProgram.className = "JavaToBeExecuted";
    programsToExecute.push_back(javaProgram);

    ProgramToExecuteEntry pythonProgram;
    pythonProgram.pathToBinary = PathToBinaries + "\\PythonToBeExecuted.py";
    pythonProgram.className = nullptr;
    programsToExecute.push_back(pythonProgram);


    for(ProgramToExecuteEntry program : programsToExecute)
    {
        ExecuteProgram(program, args);
    }
}
void MyClass::ExecuteProgram(ProgramToExecuteEntry programsToExecute, std::vector<NXVariant> args)
{
    print("\nAttempting to execute " + programsToExecute.pathToBinary);

    std::filesystem::path pathToDll{ programsToExecute.pathToBinary.GetText() };

    if (std::filesystem::exists(pathToDll))
    {
        theSession->Execute(programsToExecute.pathToBinary, programsToExecute.className, "ExecuteMe", args);
    }
    else
    {
        print(programsToExecute.pathToBinary + " does not exist --- skipping");
    }
}


//------------------------------------------------------------------------------
// Constructor 
//------------------------------------------------------------------------------
MyClass::MyClass()
{

    // Initialize the NX Open C++ API environment
    MyClass::theSession = NXOpen::Session::GetSession();

    MyClass::theUI = UI::GetUI();

    mb = theUI->NXMessageBox();
    lw = theSession->ListingWindow();
    lf = theSession->LogFile();

    workPart = theSession->Parts()->BaseWork();
    displayPart = theSession->Parts()->BaseDisplay();
}

//------------------------------------------------------------------------------
// Destructor
//------------------------------------------------------------------------------
MyClass::~MyClass()
{

}

//------------------------------------------------------------------------------
// Print string to listing window or stdout
//------------------------------------------------------------------------------
void MyClass::print(const NXString& msg)
{

    if (!lw->IsOpen()) lw->Open();
    lw->WriteLine(msg);

}

void MyClass::print(const string& msg)
{

    if (!lw->IsOpen()) lw->Open();
    lw->WriteLine(msg);

}

void MyClass::print(const char* msg)
{

    if (!lw->IsOpen()) lw->Open();
    lw->WriteLine(msg);

}



//------------------------------------------------------------------------------
 //Do something
//------------------------------------------------------------------------------
void MyClass::do_it(char* parm)
{

    CallExecutor(parm);

}


//------------------------------------------------------------------------------
// Entry point(s) for unmanaged internal NXOpen C/C++ programs
//------------------------------------------------------------------------------
  //  Explicit Execution
extern "C" DllExport void ufusr(char* parm, int* returnCode, int rlen)
{
    try
    {
        // Create NXOpen C++ class instance
        MyClass* theMyClass;
        theMyClass = new MyClass();
        theMyClass->do_it(parm);
        delete theMyClass;
    }
    catch (const NXException& e1)
    {
        UI::GetUI()->NXMessageBox()->Show("NXException", NXOpen::NXMessageBox::DialogTypeError, e1.Message());
    }
    catch (const exception& e2)
    {
        UI::GetUI()->NXMessageBox()->Show("Exception", NXOpen::NXMessageBox::DialogTypeError, e2.what());
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
    // Unloads the image when NX session terminates
    return (int)Session::LibraryUnloadOptionImmediately;

}

