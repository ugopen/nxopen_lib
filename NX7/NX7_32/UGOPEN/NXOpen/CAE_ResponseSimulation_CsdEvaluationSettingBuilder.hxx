#ifndef NXOpen_CAE_RESPONSESIMULATION_CSDEVALUATIONSETTINGBUILDER_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_CSDEVALUATIONSETTINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_CsdEvaluationSettingBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/CAE_ResponseSimulation.hxx>
#include <NXOpen/CAE_ResponseSimulation_FunctionEvaluationSettingBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class CsdEvaluationSettingBuilder;
        }
    }
    namespace CAE
    {
        class FEElement;
    }
    namespace CAE
    {
        class FENode;
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class DataLocation;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class FunctionEvaluationSettingBuilder;
        }
    }
    class Direction;
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _CsdEvaluationSettingBuilderBuilder;
            /** Represents the CSD build  <br> To create a new instance of this class, use @link CAE::ResponseSimulation::EvaluationSettingManager::CreateCsdEvaluationSettingBuilder CAE::ResponseSimulation::EvaluationSettingManager::CreateCsdEvaluationSettingBuilder@endlink  <br> */
            class NXOPENCPPEXPORT CsdEvaluationSettingBuilder : public CAE::ResponseSimulation::FunctionEvaluationSettingBuilder
            {
                private: friend class  _CsdEvaluationSettingBuilderBuilder;
                protected: CsdEvaluationSettingBuilder();
                /**Returns  the reference node. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::FENode * ReferenceNode
                (
                );
                /**Sets  the reference node. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetReferenceNode
                (
                    NXOpen::CAE::FENode * referenceNode /** reference node */ 
                );
                /**Returns  the reference element. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::FEElement * ReferenceElement
                (
                );
                /**Sets  the reference element. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetReferenceElement
                (
                    NXOpen::CAE::FEElement * referenceElement /** reference element */ 
                );
                /**Returns  the option of using user defined direction of the reference node. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::NodalFunctionEvalRequest ReferenceUsingUserDefinedDirection
                (
                );
                /**Sets  the option of using user defined direction of the reference node. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetReferenceUsingUserDefinedDirection
                (
                    NXOpen::CAE::ResponseSimulation::NodalFunctionEvalRequest referenceUsingUserDefinedDirection /** reference using user defined direction */ 
                );
                /**Returns   the user defined direction of reference node.          
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::Direction * ReferenceUserDefinedDirection
                (
                );
                /**Sets   the user defined direction of reference node.          
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetReferenceUserDefinedDirection
                (
                    NXOpen::Direction * referenceUserDefinedDirection /** reference user defined direction */ 
                );
                /**Returns  the direction data component of reference node. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::DirectionDataComponent ReferenceNodeDataComponent
                (
                );
                /**Sets  the direction data component of reference node. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetReferenceNodeDataComponent
                (
                    NXOpen::CAE::ResponseSimulation::DirectionDataComponent referenceNodeDataComponent /** reference node data component */ 
                );
                /**Returns  the coordinate system of reference element. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::CoordinateSystem ReferenceCoordinateSystem
                (
                );
                /**Sets  the coordinate system of reference element. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetReferenceCoordinateSystem
                (
                    NXOpen::CAE::ResponseSimulation::CoordinateSystem referenceCoordinateSystem /** reference coordinate system */ 
                );
                /**Returns  the direction data component of reference element. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::DirectionDataComponent ReferenceElementDataComponent
                (
                );
                /**Sets  the direction data component of reference element. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetReferenceElementDataComponent
                (
                    NXOpen::CAE::ResponseSimulation::DirectionDataComponent referenceElementDataComponent /** reference element data component */ 
                );
                /**Returns  the reference element location of reference element. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::DataLocation * ReferenceDataLocation
                (
                );
                /** Get the response nodes. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                         @return   <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: std::vector<NXOpen::CAE::FENode *> GetResponseNodes
                (
                );
                /** Set the response nodes. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetResponseNodes
                (
                    const std::vector<NXOpen::CAE::FENode *> & responseNode /** response node */ 
                );
                /** Get the response elments. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                         @return   <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: std::vector<NXOpen::CAE::FEElement *> GetResponseElements
                (
                );
                /** Set the response elments. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetResponseElements
                (
                    const std::vector<NXOpen::CAE::FEElement *> & responseElements /** response elements */ 
                );
                /**Returns  the option of using user defined direction of response nodes. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::NodalFunctionEvalRequest ResponseUsingUserDefinedDirection
                (
                );
                /**Sets  the option of using user defined direction of response nodes. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetResponseUsingUserDefinedDirection
                (
                    NXOpen::CAE::ResponseSimulation::NodalFunctionEvalRequest responseUsingUserDefinedDirection /** response using user defined direction */ 
                );
                /**Returns   the user defined direction of response nodes. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::Direction * ResponseUserDefinedDirection
                (
                );
                /**Sets   the user defined direction of response nodes. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetResponseUserDefinedDirection
                (
                    NXOpen::Direction * responseUserDefinedDirection /** response user defined direction */ 
                );
                /**Returns  the direction data component of response node. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::DirectionDataComponent ResponseNodeDataComponent
                (
                );
                /**Sets  the direction data component of response node. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetResponseNodeDataComponent
                (
                    NXOpen::CAE::ResponseSimulation::DirectionDataComponent responseNodeDataComponent /** response node data component */ 
                );
                /**Returns  the coordinate system of response elements. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::CoordinateSystem ResponseCoordinateSystem
                (
                );
                /**Sets  the coordinate system of response elements. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetResponseCoordinateSystem
                (
                    NXOpen::CAE::ResponseSimulation::CoordinateSystem responseCoordinateSystem /** response coordinate system */ 
                );
                /**Returns  the direction data component of response elements. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::DirectionDataComponent ResponseElementDataComponent
                (
                );
                /**Sets  the direction data component of response elements. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetResponseElementDataComponent
                (
                    NXOpen::CAE::ResponseSimulation::DirectionDataComponent responseElementDataComponent /** response element data component */ 
                );
                /**Returns  the response element location. 
                         Available if the result type is 
                         @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                         @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                         <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::DataLocation * ResponseDataLocation
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
