/*==================================================================================================

                Copyright(c) 2020 Siemens Product Lifecycle Management Software Inc.
                                     All Rights Reserved.

====================================================================================================
File description :
    NXOpen CPP example to show how to create a User Defined Scenario in Simcenter 3D visible in
    Scenario Based Data Visualization Navigator.This scenario merges the selection variables comming
    from different data sources and overrides the default selection of the data definition to match
    the data coming from different data sources.

====================================================================================================

*/

#include <uf_defs.h>
#include <uf_ui.h>
#include <uf.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <utility>

#include <NXOpen/NXException.hxx>
#include <NXOpen/BasePart.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/LogFile.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/PartCollection.hxx>

#include <NXOpen/CAE_PostScenarioDataMatchesInput.hxx>
#include <NXOpen/CAE_PostScenarioDataMatchOutput.hxx>
#include <NXOpen/CAE_PostScenarioMessageCollector.hxx>
#include <NXOpen/CAE_PostScenarioAggregationInput.hxx>
#include <NXOpen/CAE_PostScenarioAggregationOutput.hxx>
#include <NXOpen/CAE_PostScenarioDescriptorBuilder.hxx>
#include <NXOpen/CAE_PostScenarioManager.hxx>
#include <NXOpen/CAE_PostScenarioDescriptorBuilder.hxx>
#include <NXOpen/CAE_PostScenarioDescriptorCollection.hxx>

using namespace NXOpen;
using namespace NXOpen::CAE;

static int registered = 0;
static int idPartCreated1 = 0;
static int idPartOpened1 = 0;

class RelationsScenario;
RelationsScenario* theRelationsScenario;

class RelationsScenario
{
public:
    RelationsScenario()
    {
        InitializeCallbacks();
    }

    /*** Override Callback specific functions ***/

    // Checks if the subdomains are matching
    bool IsValidMatch(PostScenarioDataMatch* match, NXString* expectedType)
    {
        if (match->GetMatchedDependentVariables().size() != 1)
        {
            return false;
        }

        if (match->GetMatchedDependentVariables()[0]->Domain()->GetNumberOfComponents() == 0)
        {
            return false;
        }

        NXString* type = new NXString();
        std::vector<NXString> subtyes;

        match->GetMatchedDependentVariables()[0]->Domain()->GetNthComponent(0, type, subtyes);

        return std::strcmp(expectedType->GetText(), type->GetText()) == 0;
    }

    // Overrides the default selection of the data definition to match the data coming from different data sources.
    NXOpen::CAE::DataMatchOverrideResult Override(BasePart* part, PostScenarioDataMatchesInput* input, PostScenarioMessageCollector* mc, PostScenarioDataMatchOutput* output)
    {
        try
        {
            std::vector<PostScenarioDataMatch*> excitationSlotMatches = input->GetSlotDataMatches("Excitation Functions");
            if (excitationSlotMatches.empty())
            {
                throw NXException::Create("Invalid slot name or no matches for the slot excitation Functions");
            }
            std::vector<PostScenarioDataMatch*> frfSlotMatches = input->GetSlotDataMatches("Frequency Response Functions");
            if (excitationSlotMatches.empty())
            {
                throw NXException::Create("Invalid slot name or no matches for the slot Frequency Response Functions");
            }
            std::vector<PostScenarioDataMatch*> responseSlotMatches = input->GetSlotDataMatches("Response Functions");
            if (excitationSlotMatches.empty())
            {
                throw NXException::Create("Invalid slot name or no matches for the slot Response Functions");
            }

            const std::vector<NXString> preferredDataSources = input->GetNamesOfPreferredDataSources();

            auto preferredMatchCmp = [&preferredDataSources](PostScenarioDataMatch * match1, PostScenarioDataMatch * match2)
            {
                return std::distance(preferredDataSources.begin(), std::find_if(preferredDataSources.begin(), preferredDataSources.end(),
                    [&match1](const NXString & str)
                    {
                        return std::strcmp(match1->DataSourceName().GetText(), str.GetText()) == 0; })) <
                    std::distance(preferredDataSources.begin(), std::find_if(preferredDataSources.begin(), preferredDataSources.end(),
                        [&match2](const NXString & str)
                        {
                            return std::strcmp(match2->DataSourceName().GetText(), str.GetText()) == 0; }));
            };

            // Sort the slots in such a way that the preferred data sources are the first ones in the matched list.
            std::stable_sort(excitationSlotMatches.begin(), excitationSlotMatches.end(), preferredMatchCmp);
            std::stable_sort(frfSlotMatches.begin(), frfSlotMatches.end(), preferredMatchCmp);
            std::stable_sort(responseSlotMatches.begin(), responseSlotMatches.end(), preferredMatchCmp);

            NXString* responseType = new NXString();
            std::vector<NXString> responseTypeSubdomains;
            NXString* excitationType = new NXString();
            std::vector<NXString> excitationTypeSubdomains;

            // Looking for the first valid match for each slot.
            for (PostScenarioDataMatch* frfMatch : frfSlotMatches)
            {
                if (frfMatch->GetMatchedDependentVariables().size() != 1)
                {
                    continue;
                }

                PostScenarioVariableDomain* dependentType = frfMatch->GetMatchedDependentVariables()[0]->Domain(); // NXOpen.CAE.PostScenarioVariableDomain

                int numberOfComponents = dependentType->GetNumberOfComponents();

                if (numberOfComponents != 3)
                {
                    continue;
                }

                dependentType->GetNthComponent(0, responseType, responseTypeSubdomains);
                dependentType->GetNthComponent(numberOfComponents - 1, excitationType, excitationTypeSubdomains);

                NXString excitationDataSource = "";
                NXString excitationDataDefinition = "";
                NXString responseDataSource = "";
                NXString responseDataDefinition = "";

                // Try to find a excitation with matching dependent type.
                for (PostScenarioDataMatch* excitationMatch : excitationSlotMatches)
                {
                    if (!IsValidMatch(excitationMatch, excitationType))
                    {
                        continue;
                    }

                    excitationDataSource = excitationMatch->DataSourceName();
                    excitationDataDefinition = excitationMatch->DataDefinitionName();

                    break;
                }

                if (excitationDataSource.GetText() == "")
                {
                    continue;
                }

                // Try to find a response with matching dependent type.
                for (PostScenarioDataMatch* responseMatch : responseSlotMatches)
                {
                    if (!IsValidMatch(responseMatch, responseType))
                    {
                        continue;
                    }

                    responseDataSource = responseMatch->DataSourceName();
                    responseDataDefinition = responseMatch->DataDefinitionName();

                    break;
                }

                if (responseDataSource.GetText() == "")
                {
                    continue;
                }

                // If there are 3 data sources selected, but one of the selected data source was a match for both
                // the response and the excitation, then one of the selected data sources will be left out.
                // Check if the "unused data source" could be used as a excitation or as a response.
                if (preferredDataSources.size() == 3 && std::strcmp(excitationDataSource.GetText(), responseDataSource.GetText()) == 0)
                {
                    NXString leftOutDataSource = "";

                    for (NXString preferred : preferredDataSources)
                    {
                        if (std::strcmp(frfMatch->DataSourceName().GetText(), preferred.GetText()) != 0
                            && std::strcmp(excitationDataSource.GetText(), preferred.GetText()) != 0
                            && std::strcmp(responseDataSource.GetText(), preferred.GetText()) != 0)
                        {
                            leftOutDataSource = preferred;
                            break;
                        }
                    }

                    if (leftOutDataSource.GetText() != nullptr)
                    {
                        // Check if you have a valid excitation on that data source.
                        for (PostScenarioDataMatch* excitationMatch : excitationSlotMatches)
                        {
                            if (std::strcmp(excitationMatch->DataSourceName().GetText(), leftOutDataSource.GetText()) != 0)
                            {
                                continue;
                            }

                            if (!IsValidMatch(excitationMatch, excitationType))
                            {
                                continue;
                            }

                            excitationDataSource = excitationMatch->DataSourceName();
                            excitationDataDefinition = excitationMatch->DataDefinitionName();

                            break;
                        }

                        // If you didn't find an excitation, try a response.
                        if (excitationDataSource.GetText() == responseDataSource.GetText())
                        {
                            for (PostScenarioDataMatch* responseMatch : responseSlotMatches)
                            {
                                if (std::strcmp(responseMatch->DataSourceName().GetText(), leftOutDataSource.GetText()) != 0)
                                {
                                    continue;
                                }

                                if (!IsValidMatch(responseMatch, responseType))
                                {
                                    continue;
                                }

                                responseDataSource = responseMatch->DataSourceName();
                                responseDataDefinition = responseMatch->DataDefinitionName();

                                break;
                            }
                        }
                    }
                }

                output->SetSlotDataSourceName("Excitation Functions", excitationDataSource, excitationDataDefinition);
                output->SetSlotDataSourceName("Frequency Response Functions", frfMatch->DataSourceName(), frfMatch->DataDefinitionName());
                output->SetSlotDataSourceName("Response Functions", responseDataSource, responseDataDefinition);

                // Cleanup
                delete responseType;
                delete excitationType;

                return NXOpen::CAE::DataMatchOverrideResult::DataMatchOverrideResultOverride;
            }

            // Cleanup
            delete responseType;
            delete excitationType;
        }
        catch (const NXException & e)
        {
            mc->AddInformationLine(e.Message());
        }
        catch (const std::exception & e)
        {
            Session::GetSession()->LogFile()->WriteLine(e.what());
        }

        return NXOpen::CAE::DataMatchOverrideResult::DataMatchOverrideResultUseDefault;
    }

    /*** Aggregated Callback specific functions  ***/

    // Aggregates the nodes with dofs for multiple selection variables of type node and dof 
    void RelationFRFNodeDofAggregation(BasePart* part, PostScenarioAggregationInput* input, PostScenarioMessageCollector* mc, PostScenarioAggregationOutput* output, std::map<const char*, const char*> relationVariables)
    {
        try
        {
            // Create the merged variable
            PostScenarioVariableDomain* outputDomain = part->PostScenarioMgr()->NewVariableDomain();
            outputDomain->AddComponent(relationVariables["variableDomain"], std::vector<NXString>({ NXString(relationVariables["variableSubDomain"]) }));
            output->CreateAggregatedVariable(relationVariables["variableName"],
                NXOpen::CAE::PostScenarioVariantType::PostScenarioVariantTypeUnicodeString,
                outputDomain);

            delete outputDomain;

            std::vector<PostScenarioVariant*> nodes;
            PostScenarioVariant** defaultNode = new PostScenarioVariant*;
            std::vector<PostScenarioVariant*> dofs;
            PostScenarioVariant** defaultDof = new PostScenarioVariant*;
            std::vector<PostScenarioVariant*> nodesFRF;
            PostScenarioVariant** defaultNodeFRF = new PostScenarioVariant*;
            std::vector<PostScenarioVariant*> dofsFRF;
            PostScenarioVariant** defaultDofFRF = new PostScenarioVariant*;

            nodes = input->GetVariableValues(relationVariables["nodeVariableName"], defaultNode);
            dofs = input->GetVariableValues(relationVariables["dofVariableName"], defaultDof);
            nodesFRF = input->GetVariableValues(relationVariables["nodeFRFVariableName"], defaultNodeFRF);
            dofsFRF = input->GetVariableValues(relationVariables["dofFRFVariableName"], defaultNode);

            auto variantComp = [](PostScenarioVariant * variant1, PostScenarioVariant * variant2)
            {
                return std::strcmp(variant1->ToStringRepr().GetText(), variant2->ToStringRepr().GetText()) == -1;
            };

            // Sort nodes
            std::sort(nodes.begin(), nodes.end(), variantComp);
            std::sort(nodesFRF.begin(), nodesFRF.end(), variantComp);

            // Get the common nodes in order
            std::vector<PostScenarioVariant*> commonNodes;
            std::set_intersection(nodes.begin(), nodes.end(), nodesFRF.begin(), nodesFRF.end(), std::back_inserter(commonNodes), variantComp);


            // Sort dofs
            std::sort(dofs.begin(), dofs.end(), variantComp);
            std::sort(dofsFRF.begin(), dofsFRF.end(), variantComp);

            // Get the common dofs in order
            std::vector<PostScenarioVariant*> commonDofs;
            std::set_intersection(dofs.begin(), dofs.end(), dofsFRF.begin(), dofsFRF.end(), std::back_inserter(commonDofs), variantComp);

            // Build default value candidates
            std::vector<std::pair<PostScenarioVariant*, PostScenarioVariant*>> defaultCandidates;

            if (defaultNode != nullptr && defaultDof != nullptr)
            {
                defaultCandidates.push_back(std::make_pair(*defaultNode, *defaultDof));
            }
            if (defaultNodeFRF != nullptr && defaultDofFRF != nullptr)
            {
                defaultCandidates.push_back(std::make_pair(*defaultNodeFRF, *defaultDofFRF));
            }
            if (!(commonNodes.empty() && commonDofs.empty()))
            {
                defaultCandidates.push_back(std::make_pair(commonNodes[0], commonDofs[0]));
            }

            // Iterate over common nodes
            for (PostScenarioVariant* node : commonNodes)
            {
                // Skip unidentified notes
                if (node->GetDataType() == NXOpen::CAE::PostScenarioVariantType::PostScenarioVariantTypeWildcard)
                {
                    continue;
                }

                // Iterate over common dofs
                for (PostScenarioVariant* dof : commonDofs)
                {
                    // Skip unidentified dofs
                    if (dof->GetDataType() == NXOpen::CAE::PostScenarioVariantType::PostScenarioVariantTypeWildcard)
                    {
                        continue;
                    }

                    // Create the aggregated value
                    char* format = new char[256];

                    sprintf(format, "[%s]:+%s", node->ToStringRepr().GetText(), dof->ToStringRepr().GetText());
                    PostScenarioVariant* mergedVariant = part->PostScenarioMgr()->NewVariant();
                    mergedVariant->SetValueAsUnicodeString(format);
                    PostScenarioAggregateValueBuilder* aggregateBuilder = output->NewAggregateValue(mergedVariant);

                    delete[] format;

                    // Set the deaggregated values
                    aggregateBuilder->SetDeaggregates(relationVariables["nodeVariableName"], { node });
                    aggregateBuilder->SetDeaggregates(relationVariables["dofVariableName"], { dof });
                    aggregateBuilder->SetDeaggregates(relationVariables["nodeFRFVariableName"], { node });
                    aggregateBuilder->SetDeaggregates(relationVariables["dofFRFVariableName"], { dof });
                    aggregateBuilder->Commit();

                    delete aggregateBuilder;

                    // Try settting the default value. Default values might be missing
                    if (std::find(defaultCandidates.begin(), defaultCandidates.end(), std::make_pair(node, dof)) != defaultCandidates.end())
                    {
                        output->SetDefaultValue(mergedVariant);
                    }

                    delete mergedVariant;
                }
            }

            // Cleanup
            delete defaultNode;
            delete defaultDof;
            delete defaultNodeFRF;
            delete defaultDofFRF;
        }
        catch (const NXException & e)
        {
            mc->AddInformationLine(e.Message());
        }
        catch (const std::exception & e)
        {
            Session::GetSession()->LogFile()->WriteLine(e.what());
        }
    }

    // Aggregates the excitation nodesand dofs with the frf excitation nodesand dofs
    void RelationExcitationFRFNodeDofAggregation(BasePart* part, PostScenarioAggregationInput* input, PostScenarioMessageCollector* mc, PostScenarioAggregationOutput* output)
    {
        static std::map<const char*, const char*> relationVariables = {
               { "variableDomain", "node"},
               { "variableSubDomain", "excitation"},
               { "variableName", "Node Excitation"},
               { "nodeVariableName", "Excitation Node"},
               { "dofVariableName", "Excitation DOF"},
               { "nodeFRFVariableName", "FRF Excitation Node"},
               { "dofFRFVariableName", "FRF Excitation DOF"}
        };

        // Call your implementation
        RelationFRFNodeDofAggregation(part, input, mc, output, relationVariables);
    }

    // Aggregates the response nodesand dofs with the frf response nodesand dofs
    void RelationResponseFRFNodeDofAggregation(BasePart* part, PostScenarioAggregationInput* input, PostScenarioMessageCollector* mc, PostScenarioAggregationOutput* output)
    {

        static std::map<const char*, const char*> relationVariables = {
            { "variableDomain", "node"},
            { "variableSubDomain", "response"},
            { "variableName", "Node Response"},
            { "nodeVariableName", "Response Node"},
            { "dofVariableName", "Response DOF"},
            { "nodeFRFVariableName", "FRF Response Node"},
            { "dofFRFVariableName", "FRF Response DOF"}
        };

        // Call your implementation
        RelationFRFNodeDofAggregation(part, input, mc, output, relationVariables);
    }

    // Aggregates the excitation subcases with the frf response subcases
    void RelationExcitationResponseSubcaseAggregation(BasePart* part, PostScenarioAggregationInput* input, PostScenarioMessageCollector* mc, PostScenarioAggregationOutput* output)
    {
        try
        {
            PostScenarioVariableDomain* outputDomain = part->PostScenarioMgr()->NewVariableDomain();
            outputDomain->AddComponent("subcase_name", std::vector<NXString>{});
            output->CreateAggregatedVariable("Subcase",
                NXOpen::CAE::PostScenarioVariantType::PostScenarioVariantTypeUnicodeString,
                outputDomain);

            delete outputDomain;

            std::vector<PostScenarioVariant*> excitationSubcases;
            PostScenarioVariant** defaultExcitationSubcase = new PostScenarioVariant*;
            std::vector<PostScenarioVariant*> responseSubcases;
            PostScenarioVariant** defaultResponseSubcase = new PostScenarioVariant*;

            excitationSubcases = input->GetVariableValues("Excitation Subcase", defaultExcitationSubcase);
            responseSubcases = input->GetVariableValues("Response Subcase", defaultResponseSubcase);

            auto variantComp = [](PostScenarioVariant * variant1, PostScenarioVariant * variant2)
            {
                return std::strcmp(variant1->ToStringRepr().GetText(), variant2->ToStringRepr().GetText()) == -1;
            };

            // Sort subcases
            std::sort(excitationSubcases.begin(), excitationSubcases.end(), variantComp);
            std::sort(responseSubcases.begin(), responseSubcases.end(), variantComp);

            // Get the common subcases in order
            std::vector<PostScenarioVariant*> commonSubcases;
            std::set_intersection(excitationSubcases.begin(), excitationSubcases.end(), responseSubcases.begin(), responseSubcases.end(), std::back_inserter(commonSubcases), variantComp);

            // Iterate over common subcases
            for (PostScenarioVariant* commonSubcase : commonSubcases)
            {
                // Skip unidentified subcases
                if (commonSubcase->GetDataType() == NXOpen::CAE::PostScenarioVariantType::PostScenarioVariantTypeWildcard)
                {
                    continue;
                }

                // Create the aggregated value
                PostScenarioVariant* mergedVariant = part->PostScenarioMgr()->NewVariant();
                mergedVariant->SetValueAsUnicodeString(commonSubcase->ToStringRepr());
                PostScenarioAggregateValueBuilder* aggregateBuilder = output->NewAggregateValue(mergedVariant);

                // Set the deaggregated values
                aggregateBuilder->SetDeaggregates("Excitation Subcase", { commonSubcase });
                aggregateBuilder->SetDeaggregates("Response Subcase", { commonSubcase });
                aggregateBuilder->Commit();

                delete aggregateBuilder;

                // Try settting the default value. Default values might be missing
                if (std::strcmp(commonSubcase->ToStringRepr().GetText(), (*defaultExcitationSubcase)->ToStringRepr().GetText()) == 0
                    || std::strcmp(commonSubcase->ToStringRepr().GetText(), (*defaultResponseSubcase)->ToStringRepr().GetText()) == 0)
                {
                    output->SetDefaultValue(mergedVariant);
                }

                delete mergedVariant;
            }

            // Cleanup
            delete defaultExcitationSubcase;
            delete defaultResponseSubcase;
        }
        catch (const NXException& e)
        {
            mc->AddInformationLine(e.Message());
        }
        catch (const std::exception& e)
        {
            Session::GetSession()->LogFile()->WriteLine(e.what());
        }
    }

    /*** Scenario specific functions ***/

    // Describes the scenario
    NXString Description()
    {
        return NXString("This scenario illustrates the usage of multiple data sets, stacked plots, the data set override callback and the aggregation callback.");
    }

    // Creates the scenario
    void PartOpenedOrCreated(BasePart* part)
    {
        Session::GetSession()->LogFile()->WriteLine("Inserting Relations Scenario");

        try
        {
            PostScenarioDescriptorBuilder* builder;
            builder = part->PostScenarioMgr()->PostScenarioDescriptors()->NewPostScenarioDescriptorBuilder();

            // Add the scenario descriptor
            builder->SetXmlText(NXString(R"(<?xml version='1.0' encoding='utf-8'?>
    <!DOCTYPE Scenario SYSTEM 'scenarios.dtd'>
    <!-- See Programmers's Guide / Scenario Descriptors -->
    <Scenario name='Relations Scenario' domainPath='Examples' trigram='REL'>
        <!-- See Programmers's Guide / Input Definitions -->
        <InputDefinition name='Response over Excitation Analysis' defaultSelectionWidgetStyle='list_with_checkbox'>
            <!-- See Programmers's Guide / Slots / Data Slots -->
            <Slot name='Excitation Functions'>
                <!-- See Programmers's Guide / Slots / Data Slots / Variables -->
                <IndependentVariable name='Excitation Frequency'>
                    <AllowedDataTypes>
                        <DataType type='real'/>
                    </AllowedDataTypes>
                    <AllowedDomains>
                        <VariableDomain type='frequency'/>
                    </AllowedDomains>
                </IndependentVariable>
                <SelectionVariable name='Excitation DOF'>
                    <AllowedDataTypes>
                        <DataType type='dof'/>
                    </AllowedDataTypes>
                    <AllowedDomains>
                        <VariableDomain type='dof_name'/>
                    </AllowedDomains>
                </SelectionVariable>
                <SelectionVariable name='Excitation Node'>
                    <AllowedDataTypes>
                        <DataType type='integer'/>
                    </AllowedDataTypes>
                    <AllowedDomains>
                        <VariableDomain type='node'/>
                    </AllowedDomains>
                </SelectionVariable>
                <SelectionVariable name='Excitation Subcase'>
                    <AllowedDomains>
                        <VariableDomain type='subcase_name'/>
                    </AllowedDomains>
                </SelectionVariable>
                <DependentVariable name='Excitation Type'>
                    <AllowedDataTypes>
                        <DataType type='real'/>
                        <DataType type='complex'/>
                    </AllowedDataTypes>
                    <AllowedDomains>
                        <VariableDomain type='displacement'/>
                        <VariableDomain type='rotation'/>
                        <VariableDomain type='velocity'/>
                        <VariableDomain type='angular_velocity'/>
                        <VariableDomain type='acceleration'/>
                        <VariableDomain type='angular_acceleration'/>
                        <VariableDomain type='force'/>
                        <VariableDomain type='moment'/>
                    </AllowedDomains>
                </DependentVariable>
            </Slot>
            <Slot name='Frequency Response Functions'>
                <IndependentVariable name='FRF Frequency'>
                    <AllowedDataTypes>
                        <DataType type='real'/>
                    </AllowedDataTypes>
                    <AllowedDomains>
                        <VariableDomain type='frequency'/>
                    </AllowedDomains>
                </IndependentVariable>
                <SelectionVariable name='FRF Excitation Node'>
                    <AllowedDataTypes>
                        <DataType type='integer'/>
                    </AllowedDataTypes>
                    <AllowedDomains>
                        <VariableDomain type='node' subTypes='excitation'/>
                    </AllowedDomains>
                </SelectionVariable>
                <SelectionVariable name='FRF Excitation DOF'>
                    <AllowedDataTypes>
                        <DataType type='dof'/>
                    </AllowedDataTypes>
                    <AllowedDomains>
                        <VariableDomain type='dof_name' subTypes='dof_excitation'/>
                    </AllowedDomains>
                </SelectionVariable>
                <SelectionVariable name='FRF Response Node'>
                    <AllowedDataTypes>
                        <DataType type='integer'/>
                    </AllowedDataTypes>
                    <AllowedDomains>
                        <VariableDomain type='node' subTypes='response'/>
                    </AllowedDomains>
                </SelectionVariable>
                <SelectionVariable name='FRF Response DOF'>
                    <AllowedDataTypes>
                        <DataType type='dof'/>
                    </AllowedDataTypes>
                    <AllowedDomains>
                        <VariableDomain type='dof_name' subTypes='dof_response'/>
                    </AllowedDomains>
                </SelectionVariable>
                <DependentVariable name='FRF Type'>
                    <AllowedDataTypes>
                        <DataType type='real'/>
                        <DataType type='complex'/>
                    </AllowedDataTypes>
                    <AllowedDomains>
                        <RationalDomain>
                            <Any/>
                            <Over/>
                            <Any/>
                        </RationalDomain>
                    </AllowedDomains>
                </DependentVariable>
            </Slot>
            <Slot name='Response Functions'>
                <IndependentVariable name='Response Frequency'>
                    <AllowedDataTypes>
                        <DataType type='real'/>
                    </AllowedDataTypes>
                    <AllowedDomains>
                        <VariableDomain type='frequency'/>
                    </AllowedDomains>
                </IndependentVariable>
                <SelectionVariable name='Response DOF'>
                    <AllowedDataTypes>
                        <DataType type='dof'/>
                    </AllowedDataTypes>
                    <AllowedDomains>
                        <VariableDomain type='dof_name'/>
                    </AllowedDomains>
                </SelectionVariable>
                <SelectionVariable name='Response Node'>
                    <AllowedDataTypes>
                        <DataType type='integer'/>
                    </AllowedDataTypes>
                    <AllowedDomains>
                        <VariableDomain type='node'/>
                    </AllowedDomains>
                </SelectionVariable>
                <SelectionVariable name='Response Subcase'>
                    <AllowedDomains>
                        <VariableDomain type='subcase_name'/>
                    </AllowedDomains>
                </SelectionVariable>
                <DependentVariable name='Response Type'>
                    <AllowedDataTypes>
                        <DataType type='real'/>
                        <DataType type='complex'/>
                    </AllowedDataTypes>
                    <AllowedDomains>
                        <VariableDomain type='displacement'/>
                        <VariableDomain type='rotation'/>
                        <VariableDomain type='velocity'/>
                        <VariableDomain type='angular_velocity'/>
                        <VariableDomain type='acceleration'/>
                        <VariableDomain type='angular_acceleration'/>
                        <VariableDomain type='force'/>
                        <VariableDomain type='moment'/>
                        <VariableDomain type='pressure'/>
                    </AllowedDomains>
                </DependentVariable>
            </Slot>
            <!-- See Programmers's Guide / Relations / AggregateSetUnion and Programmers's Guide / Callbacks / Data Aggregation -->
            <AggregatedSelectionVariable name='Node Excitation' callback='RelationExcitationFRFNodeDofAggregation'>
                <VariableRef name='Excitation Node'/>
                <VariableRef name='FRF Excitation Node'/>
                <VariableRef name='Excitation DOF'/>
                <VariableRef name='FRF Excitation DOF'/>
            </AggregatedSelectionVariable>
            <AggregatedSelectionVariable name='Node Response' callback='RelationResponseFRFNodeDofAggregation'>
                <VariableRef name='Response Node'/>
                <VariableRef name='FRF Response Node'/>
                <VariableRef name='Response DOF'/>
                <VariableRef name='FRF Response DOF'/>
            </AggregatedSelectionVariable>
            <AggregatedSelectionVariable name='Subcase' callback='RelationExcitationResponseSubcaseAggregation'>
                <VariableRef name='Excitation Subcase'/>
                <VariableRef name='Response Subcase'/>
            </AggregatedSelectionVariable>
                <!-- See Programmers's Guide / Visualizations / Stacked Visualization -->
            <StackedVisualization name='Excitations / FRFs / Contributions and Responses' numPlots='3'>
                <ComplexViewOptions>
                    <ComplexViewOption value='magnitude'/>
                </ComplexViewOptions>
            </StackedVisualization>
            <StackDataAllocation>
                <AllocateStackResultGroup name='Excitation Functions'>
                    <VisualizationRef name='Excitations / FRFs / Contributions and Responses'/>
                </AllocateStackResultGroup>
                <AllocateStackResultGroup name='Frequency Response Functions'>
                    <VisualizationRef name='Excitations / FRFs / Contributions and Responses'/>
                </AllocateStackResultGroup>
                <AllocateStackResultGroup name='Response Functions'>
                    <VisualizationRef name='Excitations / FRFs / Contributions and Responses'/>
                </AllocateStackResultGroup>
            </StackDataAllocation>
        </InputDefinition>
    </Scenario>)"));

            /*** Attach callbacks ***/

            // Add Description
            // Check Programmers's Guide / Callbacks /  Description Callback
            builder->AddDescriptionCallback(make_callback(this, &RelationsScenario::Description));
            // When data is matched with the scenario
            // Check Programmers's Guide / Callbacks / Override Default Data Set Match
            builder->AddDefaultMatchOverrideCallback(make_callback(this, &RelationsScenario::Override));
            // When selection is changed
            // Check Programmers's Guide / Callbacks / Override Default Data Set Match
            builder->AddDataDefinitionChangedOverrideCallback(make_callback(this, &RelationsScenario::Override));
            // Relationship between nodesand dofs(Excitation / Excitation FRF Node - Excitation / Excitation FRF Dof)
            // Check Programmers's Guide / Callbacks / Data Aggregation
            builder->AddAggregationCallback("RelationExcitationFRFNodeDofAggregation", make_callback(this, &RelationsScenario::RelationExcitationFRFNodeDofAggregation));
            // Relationship between nodesand dofs(Response / Response FRF Node - Response / Response FRF Dof)
            builder->AddAggregationCallback("RelationResponseFRFNodeDofAggregation", make_callback(this, &RelationsScenario::RelationResponseFRFNodeDofAggregation));
            // Relationship between subcases(Excitation Subcase - Response FRF Dof)
            builder->AddAggregationCallback("RelationExcitationResponseSubcaseAggregation", make_callback(this, &RelationsScenario::RelationExcitationResponseSubcaseAggregation));

            builder->Commit();

            builder->Destroy();
        }
        catch (const NXException & e)
        {
            char* message = new char[256];
            sprintf(message, "Not a cae part -> %s", e.Message());

            Session::GetSession()->ListingWindow()->Open();
            Session::GetSession()->ListingWindow()->WriteLine(message);
            Session::GetSession()->ListingWindow()->Close();

            delete[] message;
        }
        catch (const std::exception & e)
        {
            Session::GetSession()->LogFile()->WriteLine(e.what());
        }
    }

private:

    void InitializeCallbacks()
    {
        try
        {
            if (registered == 0)
            {
                idPartCreated1 = Session::GetSession()->Parts()->AddPartCreatedHandler(make_callback(this, &RelationsScenario::PartOpenedOrCreated));
                idPartOpened1 = Session::GetSession()->Parts()->AddPartOpenedHandler(make_callback(this, &RelationsScenario::PartOpenedOrCreated));
                registered = 1;
            }
            else
            {
                Session::GetSession()->LogFile()->WriteLine("Already registered!");
            }
        }
        catch (const NXException & e)
        {
            // Get and open the listing window for this session
            Session::GetSession()->ListingWindow()->Open();
            // Write a line to the listing window
            Session::GetSession()->ListingWindow()->WriteLine(e.Message());
            // Get and close the listing window for this session
            Session::GetSession()->ListingWindow()->Close();
        }
        catch (const std::exception & e)
        {
            // Write a line to the log file
            Session::GetSession()->LogFile()->WriteLine(e.what());
        }
    }
};

// Unload Handler
extern "C" DllExport int ufusr_ask_unload()
{
    delete theRelationsScenario;

    return (int)Session::LibraryUnloadOptionAtTermination;
}

// Called manually from File->Execute->NX Open
extern "C" DllExport void ufusr(char* param, int* retCode, int paramLen)
{
    theRelationsScenario = new RelationsScenario();

    return;
}

// Called when NX starts up
extern "C" DllExport void ufusta(char* param, int* retCode, int paramLen)
{
    theRelationsScenario = new RelationsScenario();

    return;
}
