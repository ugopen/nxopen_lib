//===============================================================================
//
//                   Copyright 2016 Siemens PLM Software Inc.
//                     Unpublished - All rights reserved
//===============================================================================
// SelectionSubscriberExample.cpp
//
//File description: NX/Open example to demonstrate usage of the SelectionSubscriber class.
//
// This example instantiates a SelectionSubscriber that is left loaded until the
// session terminates. (A subsequent execution of the dll will delete and recreate
// the myClass and SelectionSubscriber.)
//
// Anytime the set of selected objects changes due to any user interaction, the
// SelectionSubscriber will print the current selected set of tags out to the Listing Window.
//
// The dll may be executed while in Global Selection, or while in a command. It may be
// executed with or without objects already selected.
//
// No additional files are required to build or execute the dll.
// There are no OS specific instructions.
//
//===============================================================================
//

// Mandatory UF Includes
#include <uf.h>
#include <uf_object_types.h>

// Internal Includes
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/UI.hxx>

// Internal+External Includes
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Session.hxx>

#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Selection.hxx>
#include <NXOpen/SelectionSubscriber.hxx>

#include <vector>
#include <map>

// Std C++ Includes
#include <iostream>
#include <sstream>

using namespace NXOpen;

//------------------------------------------------------------------------------
// NXOpen c++ test class 
//------------------------------------------------------------------------------
class MyClass
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;

    MyClass();
    ~MyClass();

    void do_it();
    void print(const NXString &);
    void print(const std::string &);
    void print(const char*);
    void printCount(const char * msg, size_t count);

private:

    void onSelectionChangeCB(bool clearAll, std::vector<TaggedObject*> deselectedObjects, std::vector<TaggedObject*> selectedObjects);

    Part *workPart, *displayPart;
    NXMessageBox *mb;
    ListingWindow *lw;
    LogFile *lf;

    NXOpen::Selection* selMgr;
    NXOpen::SelectionSubscriber* selSub;

    std::map<tag_t, TaggedObject*> myMap;
};

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(MyClass::theSession) = NULL;
UI *(MyClass::theUI) = NULL;

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

    workPart = theSession->Parts()->Work();
    displayPart = theSession->Parts()->Display();

    // Get the Selection Manager pointer, and use it to create a SelectionSubscriber.
    selMgr = UI::GetUI()->SelectionManager();
    selSub = selMgr->CreateSelectionSubscriber();

    // Register a MyClass member method as the onSelectionChangeCB for the subscriber object.
    selSub->RegisterOnSelectionChangeCallback(
        NXOpen::make_callback(this, &MyClass::onSelectionChangeCB));

    // Deactivate the SelectionSubscriber until activated by do_it().
    selSub->Deactivate();
    if (!selSub->IsActive())
    {
        print("SelectionSubscriber is deactivated. onSelectionChangeCB will NOT be called.");
    }
}

//------------------------------------------------------------------------------
// Destructor
//------------------------------------------------------------------------------
MyClass::~MyClass()
{
    print("\nMyClass::~MyClass():  Deleting the SelectionSubscriber\n");

    delete selSub;
}

//------------------------------------------------------------------------------
// Print string to listing window or stdout
//------------------------------------------------------------------------------
void MyClass::print(const NXString &msg)
{
    if (!lw->IsOpen())
    {
        lw->Open();
    }
    lw->WriteLine(msg);
}
void MyClass::print(const std::string &msg)
{
    if (!lw->IsOpen())
    {
        lw->Open();
    }
    lw->WriteLine(msg);
}
void MyClass::print(const char * msg)
{
    if (!lw->IsOpen())
    {
        lw->Open();
    }
    lw->WriteLine(msg);
}

void MyClass::printCount(const char * msg, size_t count)
{
    if (!lw->IsOpen())
    {
        lw->Open();
    }
    std::stringstream stringBuffer;
    stringBuffer << msg;
    stringBuffer << count;
    print(stringBuffer.str());
}

void MyClass::onSelectionChangeCB(bool clearAll, std::vector<TaggedObject*> deselectedObjects, std::vector<TaggedObject*> selectedObjects)
{
    // Query whether or not Global Selection (the state of NOT being in a command) is active.
    bool globalSelectionActive = selMgr->IsGlobalSelectionActive();
    std::stringstream buffer;
    buffer << "onSelectionChangeCB: (" << (globalSelectionActive ? "IN" : "NOT in") << " Global Selection)" << std::endl;
    buffer << "clearAll = " << (clearAll ? "True" : "False") << "; deselectedObjects size = " << deselectedObjects.size()
        << "; selectedObjects size = " << selectedObjects.size() << std::endl;
    print(buffer.str());

    if (clearAll)
    {
        myMap.clear();
    }
    else
    {
        // If clearAll was true, deselectedObjects will be empty.
        for (auto iter = deselectedObjects.begin(); iter != deselectedObjects.end(); ++iter)
        {
            myMap.erase((*iter)->Tag());
        }
    }

    // Always check selectedObjects, even if clearAll was true.
    for (auto iter = selectedObjects.begin(); iter != selectedObjects.end(); ++iter)
    {
        // Add selected tagged object to map, using tag of the object as the map key
        myMap[(*iter)->Tag()] = *iter;
    }

    printCount("Selected count = ", myMap.size());

    // Print out tags of selected objects
    // Two options are shown. The first option just prints out the 
    // tag used as a key in the map. The second option accesses the 
    // tagged object used as the value in the map and prints out the 
    // tag from that tagged object.
    for (auto mapIter = myMap.begin(); mapIter != myMap.end(); ++mapIter)
    {
        std::stringstream buffer;
        // Option to access tag directly from map key
        // Uncomment following line to use this option
        //buffer << mapIter->first << std::endl;
        // Option to access tag from tagged object used as map value
        // Uncomment following line to use this option
        buffer << (mapIter->second)->Tag() << std::endl;
        print(buffer.str());

    }
}


//------------------------------------------------------------------------------
// Do something
//------------------------------------------------------------------------------
void MyClass::do_it()
{
    // Reactivate the SelectionSubscriber.
    selSub->Activate();
    if (selSub->IsActive())
        print("SelectionSubscriber is Active again!");

    // Load myMap with all currently selected objects in the active command, or if no
    // active command then in Global Selection.
    int selCount = selMgr->GetNumSelectedObjects();
    for (int ii = 0; ii < selCount; ++ii)
    {
        TaggedObject* tagObj = selMgr->GetSelectedTaggedObject(ii);
        myMap[tagObj->Tag()] = tagObj;
    }

    // Copy the tagged objects in the map into a local vector, just to 
    // illustrate the usage of the Request* functions below.
    std::vector<TaggedObject*> objVector;
    for (auto mapIter = myMap.begin(); mapIter != myMap.end(); ++mapIter)
    {
        // The selected tagged objects are the values in the map, so
        // we add the values to the vector. Map iterators are std::pair
        // objects, with the first of the pair being the key, and the 
        // second of the pair being the value.
        objVector.push_back(mapIter->second);
    }

    // No net change to the selected set here; just demonstrating APIs.
    selMgr->RequestDeselections(objVector);
    printCount("After selMgr->RequestDeselections(objVector): selected count = ",
        selMgr->GetNumSelectedObjects());

    selMgr->RequestSelections(objVector);
    printCount("After selMgr->RequestSelections(objVector): selected count = ",
        selMgr->GetNumSelectedObjects());

    // If Global Selection is active, clear and repopulate the Global Selection select set.
    if (selMgr->IsGlobalSelectionActive())
    {
        print("Global Selection IS Active.");

        selMgr->ClearGlobalSelectionList();
        printCount("After selMgr->ClearGlobalSelectionList(): selected count = ",
            selMgr->GetNumSelectedObjects());

        selMgr->RequestSelections(objVector);
        printCount("After selMgr->RequestSelections(objVector): selected count = ",
            selMgr->GetNumSelectedObjects());
    }
    else
    {
        print("Global Selection is NOT Active.");
    }
}

//------------------------------------------------------------------------------
// Entry point(s) for unmanaged internal NXOpen C/C++ programs
//------------------------------------------------------------------------------
//  Explicit Execution
extern "C" DllExport void ufusr(char *parm, int *returnCode, int rlen)
{
    // Only support one instantiation of MyClass.
    static MyClass *theMyClass = nullptr;
    if (theMyClass != nullptr)
        delete theMyClass;

    try
    {
        // Create MyClass instance; leave this object, and the SelectionSubscriber
        // it creates, intact until the session terminates. (See usage of
        // Session::LibraryUnloadOptionAtTermination in ufusr_ask_unload() below.)
        theMyClass = new MyClass();
        theMyClass->do_it();
    }
    catch (const NXException& e1)
    {
        UI::GetUI()->NXMessageBox()->Show("NXException", NXOpen::NXMessageBox::DialogTypeError, e1.Message());
    }
    catch (const std::exception& e2)
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
    return (int)NXOpen::Session::LibraryUnloadOptionAtTermination;
}
