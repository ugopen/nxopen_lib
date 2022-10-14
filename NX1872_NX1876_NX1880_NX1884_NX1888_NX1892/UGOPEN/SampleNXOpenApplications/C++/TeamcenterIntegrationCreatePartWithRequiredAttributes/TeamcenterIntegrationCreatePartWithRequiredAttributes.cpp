/*=============================================================================
Copyright 2018 Siemens Product Lifecycle Management Software Inc.
All Rights Reserved.
===============================================================================
File description:
This is an example to show how to create a part in NX with item type that has
required attributes defined in Teamcenter. These attributes must be specified
to be able to create part.


=============================================================================*/

// Open C Headers
#include <uf.h>
#include <uf_ugmgr.h>

// NX Open C++ Headers
#include <NXOpen/FileNew.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/NXString.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/PDM_LogicalObject.hxx>
#include <NXOpen/PDM_PartOperationBuilder.hxx>
#include <NXOpen/PDM_PartOperationCreateBuilder.hxx>
#include <NXOpen/PDM_PdmSession.hxx>
#include <NXOpen/PDM_SmartSaveBuilder.hxx>
#include <NXOpen/PDM_SmartSaveContext.hxx>
#include <NXOpen/PDM_SmartSaveObject.hxx>
#include <NXOpen/Session.hxx>


// Std C++ Headers
#include <iostream>
#include <sstream>


void CreateCAE0ConfigItem()
{
    // Initialize the NX Open C++ API environment
    NXOpen::Session *theSession = NXOpen::Session::GetSession();
    NXOpen::PDM::PdmSession *thePdmSession = theSession->PdmSession();

    NXOpen::FileNew *fileNew = theSession->Parts()->FileNew();
    fileNew->SetUseBlankTemplate(true);
    fileNew->SetTemplateType(NXOpen::FileNewTemplateTypeItem);

    // CreateBuilder 
    NXOpen::PDM::PartOperationCreateBuilder *partOperationCreateBuilder = thePdmSession->CreateCreateOperationBuilder(NXOpen::PDM::PartOperationBuilder::OperationTypeCreate);

    fileNew->SetPartOperationCreateBuilder(partOperationCreateBuilder);

    partOperationCreateBuilder->SetOperationSubType(NXOpen::PDM::PartOperationCreateBuilder::OperationSubTypeFromTemplate);
    partOperationCreateBuilder->SetModelType("master");
    partOperationCreateBuilder->SetItemType("CAE0Config");

    // Create the LogicalObject representing pre-creation information for Item Type CAE0Config
    std::vector<NXOpen::PDM::LogicalObject *> logicalObjects;
    partOperationCreateBuilder->CreateLogicalObjects(logicalObjects);

    // Ask builder to autoassign values for attributes on LogicalObject
    std::vector<NXOpen::NXObject *> objects2(1);
    objects2[0] = logicalObjects[0];
    partOperationCreateBuilder->AutoAssignAttributes(objects2);

    // Return the actual array of objects holding actual attributes for given LogicalObject
    std::vector<NXOpen::NXObject* > attrSrcObjs = logicalObjects[0]->GetUserAttributeSourceObjects();

    // Iterate all attribute source objects to find required attributes
    for (auto& attrSrcObj : attrSrcObjs)
    {
        //Must pass argument true to include unset AttributeInformation 
        std::vector<NXOpen::NXObject::AttributeInformation> attrInfos = attrSrcObj->GetUserAttributes(true);

        for (auto& attrInfo : attrInfos)
        {
            //Note : From BMIDE we know the title for required attributes present on CAE0Config
            //       So below code block will show how to set the attributes on object

            // find required and unset attributes
            if (attrInfo.Required && attrInfo.Unset)
            {
                if (0 == strcmp(attrInfo.Title.GetLocaleText(),"Item:revision:ItemRevision:cae0ConfigType"))
                {
                    attrInfo.StringValue = "AnalysisDashboard";
                }
                else if (0 == strcmp(attrInfo.Title.GetLocaleText(), "Item:revision:ItemRevision:cae0VisibleScope"))
                {
                    attrInfo.StringValue = "Site";
                }
                else 
                {
                    // Found attributed on CAE0Config which is unset and we don't have code logic written for its assignment
                    std::stringstream errMsg;
                    errMsg << "Need to assign valid value to TC attribute \"" << attrInfo.Title.GetLocaleText() << "\" found on CAE0Config";
                    throw std::exception(errMsg.str().c_str());
                }

                attrSrcObj->SetUserAttribute(attrInfo, NXOpen::Update::Option::OptionLater);
            }
        }
    }

    // Validate the attributes entered against Teamcenter definitions
    partOperationCreateBuilder->Validate();

    //Create filenames for the parts being created
    partOperationCreateBuilder->CreateSpecificationsForLogicalObjects(logicalObjects);

    // This will create the part in session
    fileNew->Commit();

    std::cout << "Part successfully created" << std::endl;
}

// Main routine
int main(int argc, char* argv[])
{
    if (argc == 0)
    {
        std::cout << "No arguments passed" << std::endl;
        return 0;
    }

    // Start a UGMGR session using Open C API
    int status = UF_UGMGR_initialize(argc, (const char **)argv);

    if (status != 0)
    {
        std::cout << "Failed to initialize UGMGR session" << std::endl;
        return 0;
    }

    std::cout << std::endl << "UGMGR session started " << std::endl;

    try
    {
        CreateCAE0ConfigItem();
    }
    catch (const NXOpen::NXException& e1)
    {
        std::cerr << "NXException: " << e1.ErrorCode() << std::endl;
        std::cerr << e1.Message() << std::endl;
    }
    catch (const std::exception& e2)
    {
        std::cerr << "Exception: " << e2.what() << std::endl;
    }
    catch (...)
    {
        std::cerr << "Unknown Exception: " << std::endl;
    }

    // Terminate the UGMGR session using Open C API
    UF_terminate();
    std::cout << std::endl << "UGMGR session terminated" << std::endl;
    return 0;
}
