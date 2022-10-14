#==================================================================================================

#                Copyright (c) 2020 Siemens Product Lifecycle Management Software Inc.
#                                     All Rights Reserved.

#==================================================================================================
#File description:
#    Example User Defined Scenario to show how to create a User Defined Scenario in Simcenter 3D 
#    visible in Scenario Based Data Visualization Navigator. This scenario merges the selection 
#    variables comming from different data sources and overrides the default selection of the data 
#    definition to match the data coming from different data sources.

#==================================================================================================
#

import sys
import os
import traceback
import math
import NXOpen

registered = 0

### Override Callback specific functions ###

# Compares the data sources by the closest position of the head from the preferred data sources list.
def PreferredMatchCompare(preferredDataSources, match):
    # match: NXOpen.CAE.PostScenarioDataMatch
    
    if match.DataSourceName in preferredDataSources:
        return preferredDataSources.index(match.DataSourceName)
    
    return len(preferredDataSources) - 1

# Checks if the subdomains are matching
def IsValidMatch(match, expectedType):
    if len(match.GetMatchedDependentVariables()) != 1:
        return False
            
    if match.GetMatchedDependentVariables()[0].Domain.GetNumberOfComponents() == 0:
        return False
    
    return expectedType == match.GetMatchedDependentVariables()[0].Domain.GetNthComponent(0)
  
# Overrides the default selection of the data definition to match the data coming from different data sources.
def Override(part, input, mc, output):
    # part: NXOpen.BasePart
    # input: NXOpen.CAE.PostScenarioDataMatchesInput
    # mc: NXOpen.CAE.PostScenarioMessageCollector
    # output: NXOpen.CAE.PostScenarioDataMatchOutput
    try:
        excitationSlotMatches = input.GetSlotDataMatches("Excitation Functions")  # NXOpen.CAE.PostScenarioDataMatch
        if not excitationSlotMatches:
            raise Exception('Invalid slot name or no matches for the slot excitation Functions')
        frfSlotMatches = input.GetSlotDataMatches("Frequency Response Functions")
        if not frfSlotMatches:
            raise Exception('Invalid slot name or no matches for the slot Frequency Response Functions')
        responseSlotMatches = input.GetSlotDataMatches("Response Functions")
        if not responseSlotMatches:
            raise Exception('Invalid slot name or no matches for the slot Response Functions')
           
        preferredDataSources = input.GetNamesOfPreferredDataSources() 
        
        if len(preferredDataSources) > 0:
            # Sort the slots in such a way that the preferred data sources are the first ones in the matched list.
            excitationSlotMatches.sort(key=lambda match : PreferredMatchCompare(preferredDataSources, match))
            frfSlotMatches.sort(key=lambda match : PreferredMatchCompare(preferredDataSources, match))
            responseSlotMatches.sort(key=lambda match : PreferredMatchCompare(preferredDataSources, match))

        # Looking for the first valid match for each slot.
        for frfMatch in frfSlotMatches:
            
            if len(frfMatch.GetMatchedDependentVariables()) != 1:
                continue
            
            dependentType = frfMatch.GetMatchedDependentVariables()[0].Domain  # NXOpen.CAE.PostScenarioVariableDomain 
            
            numberOfComponents = dependentType.GetNumberOfComponents()

            if numberOfComponents != 3:
                continue
            
            responseType = dependentType.GetNthComponent(0)            
            excitationType = dependentType.GetNthComponent(numberOfComponents-1)
            
            excitationDataSource = None
            excitationDataDefinition = None
            responseDataSource = None
            responseDataDefinition = None
            
            # Try to find a excitation with matching dependent type.
            for excitationMatch in excitationSlotMatches:
                if not IsValidMatch(excitationMatch, excitationType):
                    continue
                     
                excitationDataSource = excitationMatch.DataSourceName
                excitationDataDefinition = excitationMatch.DataDefinitionName
                
                break
                
            if not excitationDataSource:
                continue
            
            # Try to find a response with matching dependent type.
            for responseMatch in responseSlotMatches:
                if not IsValidMatch(responseMatch, responseType):
                    continue

                responseDataSource = responseMatch.DataSourceName
                responseDataDefinition = responseMatch.DataDefinitionName
                
                break
            
            if not responseDataSource:
                continue  
            
            # If there are 3 data sources selected, but one of the selected data source was a match for both 
            # the response and the excitation, then one of the selected data sources will be left out. 
            # Check if the "unused data source" could be used as a excitation or as a response.   
            if len(preferredDataSources) == 3 and excitationDataSource == responseDataSource:
                
                leftOutDataSource = None
                
                for preferred in preferredDataSources:
                    if frfMatch.DataSourceName != preferred and excitationDataSource != preferred and responseDataSource != preferred:
                        leftOutDataSource = preferred
                        
                        break
                    
                if leftOutDataSource:
                
                    # Check if you have a valid excitation on that data source.
                    for excitationMatch in excitationSlotMatches:
                        if excitationMatch.DataSourceName != leftOutDataSource:
                            continue
    
                        if not IsValidMatch(excitationMatch, excitationType):
                            continue

                        excitationDataSource = excitationMatch.DataSourceName
                        excitationDataDefinition = excitationMatch.DataDefinitionName
                        
                        break

                    # If you didn't find an excitation, try a response.
                    if excitationDataSource == responseDataSource:
                        for responseMatch in responseSlotMatches:
                            if responseMatch.GetDataSourceName != leftOutDataSource:
                                continue

                            if not IsValidMatch(responseMatch, responseType):
                                continue

                            responseDataSource = responseMatch.DataSourceName
                            responseDataDefinition = responseMatch.DataDefinitionName
                        
                            break

            output.SetSlotDataSourceName("Excitation Functions", excitationDataSource, excitationDataDefinition)
            output.SetSlotDataSourceName("Frequency Response Functions", frfMatch.DataSourceName, frfMatch.DataDefinitionName)   
            output.SetSlotDataSourceName("Response Functions", responseDataSource, responseDataDefinition)
            
            # Cleanup
            for var in excitationSlotMatches + frfSlotMatches + responseSlotMatches:
                var.Dispose()
            
            return NXOpen.CAE.DataMatchOverrideResult.Override

        # Cleanup
        for var in excitationSlotMatches + frfSlotMatches + responseSlotMatches:
            var.Dispose()
    except AttributeError as err:
        mc.AddInformationLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        mc.AddInformationLine(tb)
    except TypeError as err:
        mc.AddInformationLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        mc.AddInformationLine(tb)
    except Exception as err:
        mc.AddInformationLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        mc.AddInformationLine(tb)
    return  NXOpen.CAE.DataMatchOverrideResult.UseDefault
    
### Aggregated Callback specific functions  ###

# Checks if there is a default value for the pair (node, dof)
def IsDefaultValue(defaultCandidates, nodeAndDof):
    # node, dof: NXOpen.CAE.PostScenarioVariant
    
    defaultNodes = [pair[0] for pair in defaultCandidates]
        
    defaultDofs = [pair[1] for pair in defaultCandidates]  
    
    for node, dof in zip(defaultNodes, defaultDofs):
        if node == nodeAndDof[0].GetValueAsInteger() and dof == nodeAndDof[1].GetValueAsComponent():
            return True
        
    return False

# Aggregates the nodes with dofs for multiple selection variables of type node and dof 
def RelationFRFNodeDofAggregation(part, input, mc, output, relationVariables):
    # part: NXOpen.BasePart
    # input: NXOpen.CAE.PostScenarioAggregationInput
    # mc: NXOpen.CAE.PostScenarioMessageCollector
    # output: NXOpen.CAE.PostScenarioAggregationOutput
    try:
        # Create the merged variable
        outputDomain = part.PostScenarioMgr.NewVariableDomain() 
        outputDomain.AddComponent(relationVariables["variableDomain"], [relationVariables["variableSubDomain"]]) # NXOpen.CAE.PostScenarioVariableDomain 
        output.CreateAggregatedVariable(relationVariables["variableName"], 
                                        NXOpen.CAE.PostScenarioVariantType.UnicodeString,
                                        outputDomain) # NXOpen.CAE.PostScenarioResultGroupVariable
        outputDomain.Dispose()
    
        nodes, defaultNode = input.GetVariableValues(relationVariables["nodeVariableName"]) # NXOpen.CAE.PostScenarioVariant 
        dofs, defaultDof = input.GetVariableValues(relationVariables["dofVariableName"])
        nodesFRF, defaultNodeFRF = input.GetVariableValues(relationVariables["nodeFRFVariableName"])
        dofsFRF, defaultDofFRF = input.GetVariableValues(relationVariables["dofFRFVariableName"])
  
        # Sort nodes 
        nodes.sort(key=lambda value: value.ToStringRepr())
        nodesFRF.sort(key=lambda value: value.ToStringRepr())
    
        # Get the common nodes in order
        nodesNames = [node.ToStringRepr() for node in nodes]
        commonNodes = [commonNode for commonNode in nodesFRF if commonNode.ToStringRepr() in nodesNames]

        # Sort dofs
        dofs.sort(key=lambda value: value.ToStringRepr())
        dofsFRF.sort(key=lambda value: value.ToStringRepr())
    
        # Get the common dofs in order
        dofsNames = [dof.ToStringRepr() for dof in dofs]
        commonDofs = [commonDof for commonDof in dofsFRF if commonDof.ToStringRepr() in dofsNames]
  
        # Build default value candidates
        defaultCandidates = []
    
        if defaultNode and defaultDof:
            defaultCandidates.append((defaultNode.GetValueAsInteger(), defaultDof.GetValueAsComponent())) 
        if defaultNodeFRF and defaultDofFRF:
            defaultCandidates.append((defaultNodeFRF.GetValueAsInteger(), defaultDofFRF.GetValueAsComponent()))   
        if commonNodes and commonDofs:
            defaultCandidates.append((commonNodes[0].GetValueAsInteger(), commonDofs[0].GetValueAsComponent()))       
    
        # Iterate over common nodes
        for node in commonNodes:
            # Skip unidentified nodes
            if node.GetDataType() == NXOpen.CAE.PostScenarioVariantType.Wildcard: 
                continue

            # Iterate over common dofs
            for dof in commonDofs:
                # Skip unidentified dofs
                if dof.GetDataType() == NXOpen.CAE.PostScenarioVariantType.Wildcard: 
                    continue

                # Create the aggregated value
                mergedStr = '[{node}]:+{dof}'.format(node=node.ToStringRepr(), dof=dof.ToStringRepr())
                mergedVariant = part.PostScenarioMgr.NewVariant() # NXOpen.CAE.PostScenarioVariant
                mergedVariant.SetValueAsUnicodeString(mergedStr)
                aggregateBuilder = output.NewAggregateValue(mergedVariant) # NXOpen.CAE.PostScenarioAggregateValueBuilder

                # Set the deaggregated values
                aggregateBuilder.SetDeaggregates(relationVariables["nodeVariableName"], [node])
                aggregateBuilder.SetDeaggregates(relationVariables["dofVariableName"], [dof])
                aggregateBuilder.SetDeaggregates(relationVariables["nodeFRFVariableName"], [node])
                aggregateBuilder.SetDeaggregates(relationVariables["dofFRFVariableName"], [dof])
                aggregateBuilder.Commit()
                aggregateBuilder.Dispose()

                # Try settting the default value. Default values might be missing
                if IsDefaultValue(defaultCandidates,(node, dof)): 
                    output.SetDefaultValue(mergedVariant)
            
                mergedVariant.Dispose()

        # Cleanup
        for var in nodes + nodesFRF + dofs + dofsFRF  + [defaultNode, defaultDof, defaultNodeFRF, defaultDofFRF]:
            var.Dispose()
        
    except AttributeError as err:
        mc.AddInformationLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        mc.AddInformationLine(tb)
    except TypeError as err:
        mc.AddInformationLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        mc.AddInformationLine(tb)
    except Exception as err:
        mc.AddInformationLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        mc.AddInformationLine(tb)
      
# Aggregates the excitation nodes and dofs with the frf excitation nodes and dofs
def RelationExcitationFRFNodeDofAggregation(part, input, mc, output):
    relationVariables = {
        "variableDomain": "node", 
        "variableSubDomain": "excitation",
        "variableName": "Node Excitation",
        "nodeVariableName": "Excitation Node",
        "dofVariableName": "Excitation DOF",
        "nodeFRFVariableName": "FRF Excitation Node",
        "dofFRFVariableName": "FRF Excitation DOF"
    }
        
    # Call your implementation
    RelationFRFNodeDofAggregation(part, input, mc, output, relationVariables)

# Aggregates the response nodes and dofs with the frf response nodes and dofs
def RelationResponseFRFNodeDofAggregation(part, input, mc, output):
    # Call your implementation
    relationVariables = {
        "variableDomain": "node", 
        "variableSubDomain": "response",
        "variableName": "Node Response",
        "nodeVariableName": "Response Node",
        "dofVariableName": "Response DOF",
        "nodeFRFVariableName": "FRF Response Node",
        "dofFRFVariableName": "FRF Response DOF"
    }
        
    RelationFRFNodeDofAggregation(part, input, mc, output, relationVariables)
 
# Aggregates the excitation subcases with the frf response subcases
def RelationExcitationResponseSubcaseAggregation(part, input, mc, output):
    # part: NXOpen.BasePart
    # input: NXOpen.CAE.PostScenarioAggregationInput
    # mc: NXOpen.CAE.PostScenarioMessageCollector
    # output: NXOpen.CAE.PostScenarioAggregationOutput
    try:
        # Create the merged variable
        outputDomain = part.PostScenarioMgr.NewVariableDomain()
        outputDomain.AddComponent("subcase_name", [])
        output.CreateAggregatedVariable("Subcase", 
                                        NXOpen.CAE.PostScenarioVariantType.UnicodeString,
                                        outputDomain)
        outputDomain.Dispose()
        
        excitationSubcases, defaultExcitationSubcase = input.GetVariableValues("Excitation Subcase")
        responseSubcases, defaultResponseSubcase = input.GetVariableValues("Response Subcase")
       
       # Sort subcases 
        excitationSubcases.sort(key=lambda value: value.ToStringRepr())
        responseSubcases.sort(key=lambda value: value.ToStringRepr())
    
        # Get the common subcases in order
        subcasesNames = [subcase.ToStringRepr() for subcase in excitationSubcases]
        commonSubcases = [commonSubcase for commonSubcase in responseSubcases if commonSubcase.ToStringRepr() in subcasesNames]

        # Iterate over subcases
        for commonSubcase in commonSubcases:
            # Skip undentified subcases
            if commonSubcase.GetDataType() == NXOpen.CAE.PostScenarioVariantType.Wildcard: 
                continue
                
            # Create the aggregated value
            mergedStr = '{subcase}'.format(subcase=commonSubcase.ToStringRepr())
            mergedVariant = part.PostScenarioMgr.NewVariant()
            mergedVariant.SetValueAsUnicodeString(mergedStr)
            aggregateBuilder = output.NewAggregateValue(mergedVariant)

            # Set the deaggregated values
            aggregateBuilder.SetDeaggregates("Excitation Subcase", [commonSubcase])
            aggregateBuilder.SetDeaggregates("Response Subcase", [commonSubcase])
            aggregateBuilder.Commit()
            aggregateBuilder.Dispose()

            # Try settting the default value. Default values might be missing
            if commonSubcase.GetValueAsUnicodeString() == defaultExcitationSubcase.GetValueAsUnicodeString() \
               or commonSubcase.GetValueAsUnicodeString() == defaultResponseSubcase.GetValueAsUnicodeString():
                output.SetDefaultValue(mergedVariant)

            mergedVariant.Dispose()
        
        # Cleanup
        for var in excitationSubcases + responseSubcases + [defaultExcitationSubcase, defaultResponseSubcase]:
            var.Dispose()

    except AttributeError as err:
        mc.AddInformationLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        mc.AddInformationLine(tb)
    except TypeError as err:
        mc.AddInformationLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        mc.AddInformationLine(tb)
    except Exception as err:
        mc.AddInformationLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        mc.AddInformationLine(tb)

# Scenario specific functions
def Description():
    return "This scenario illustrates the usage of multiple data sets, stacked plots, the data set override callback and the aggregation callback."
   
# Creates the scenario
def PartOpenedOrCreated(part):
    theSession  = NXOpen.Session.GetSession()
    theSession.LogFile.WriteLine("Inserting Relations Scenario")
    
    try:
        builder = part.PostScenarioMgr.PostScenarioDescriptors.NewPostScenarioDescriptorBuilder()
        try:
            
            # Add the scenario descriptor 

            builder.XmlPath = "./RelationsScenario.xml"   
            
            ### Attach callbacks ###

            # Add Description
            # Check Programmers's Guide / Callbacks / Description Callback
            builder.AddDescriptionCallback(Description)
            # When data is matched with the scenario
            # Check Programmers's Guide / Callbacks / Override Default Data Set Match
            builder.AddDefaultMatchOverrideCallback(Override)
            # When selection is changed
            # Check Programmers's Guide / Callbacks / Override Default Data Set Match
            builder.AddDataDefinitionChangedOverrideCallback(Override)
            # Relationship between nodes and dofs (Excitation/Excitation FRF Node - Excitation/Excitation FRF Dof)
            # Check Programmers's Guide/ Callbacks / Data Aggregation
            builder.AddAggregationCallback("RelationExcitationFRFNodeDofAggregation", RelationExcitationFRFNodeDofAggregation)
            # Relationship between nodes and dofs (Response/Response FRF Node - Response/Response FRF Dof)
            builder.AddAggregationCallback("RelationResponseFRFNodeDofAggregation", RelationResponseFRFNodeDofAggregation)
            # Relationship between subcases (Excitation Subcase - Response FRF Dof)
            builder.AddAggregationCallback("RelationExcitationResponseSubcaseAggregation", RelationExcitationResponseSubcaseAggregation)
            
            builder.Commit()
            
        finally:
            builder.Destroy()
    except AttributeError as err:
        lw = theSession.ListingWindow
        lw.Open()
        lw.WriteLine(str(err))
        lw.Close()
    except NXOpen.NXException as err:
        lw = theSession.ListingWindow
        lw.Open()
        lw.WriteLine("The user defined scenario could not be added.")
        lw.WriteLine("The following error was raised: {}".format(err.GetMessage()))
        lw.Close()

# The main function
def startup(argc, args):
    # Get the NXOpen Session
    theSession  = NXOpen.Session.GetSession()

    global registered
    try:
        if registered == 0:
            registered = 1
            idPartCreated1 = theSession.Parts.AddPartCreatedHandler(PartOpenedOrCreated)
            idPartOpened1 = theSession.Parts.AddPartOpenedHandler(PartOpenedOrCreated)
        else:
            theSession.LogFile.WriteLine("Already registered!")
    except AttributeError as err:
        # Get the listing window for this session
        lw = theSession.ListingWindow
	
        # Open the listing window
        lw.Open()

        # Add a line in the listing window
        lw.WriteLine(str(err))

        # Close the listing window
        lw.Close()
       
    return 0

def main(): 
    return startup(0, [])
    
if __name__ == '__main__':
    main()
