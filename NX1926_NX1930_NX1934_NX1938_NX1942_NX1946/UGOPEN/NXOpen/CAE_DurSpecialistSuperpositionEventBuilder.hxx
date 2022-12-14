#ifndef NXOpen_CAE_DURSPECIALISTSUPERPOSITIONEVENTBUILDER_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTSUPERPOSITIONEVENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistSuperpositionEventBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/CAE_DurSpecialistDataSources.hxx>
#include <NXOpen/CAE_DurSpecialistEvent.hxx>
#include <NXOpen/CAE_DurSpecialistLoadLengthBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class DurSpecialistSuperpositionEventBuilder;
    }
    class Builder;
    namespace CAE
    {
        class DurSpecialistDataSources;
    }
    namespace CAE
    {
        class DurSpecialistLoadLengthBuilder;
    }
    class Expression;
    namespace CAE
    {
        class _DurSpecialistSuperpositionEventBuilderBuilder;
        class DurSpecialistSuperpositionEventBuilderImpl;
        /**  @brief 
                Represents a builder class for creating and editing an @link NXOpen::CAE::DurSpecialistSuperpositionEvent NXOpen::CAE::DurSpecialistSuperpositionEvent@endlink .
                 

         
             <br> To create a new instance of this class, use @link NXOpen::CAE::DurSpecialistEventCollection::CreateSuperpositionEventBuilder  NXOpen::CAE::DurSpecialistEventCollection::CreateSuperpositionEventBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        HistoryEndTreatment </term> <description> 
         
        Truncate </description> </item> 

        <item><term> 
         
        MatchUsing </term> <description> 
         
        CompleteSubstring </description> </item> 

        <item><term> 
         
        Range </term> <description> 
         
        FullHistory </description> </item> 

        </list> 

         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistSuperpositionEventBuilder : public NXOpen::Builder
        {
            /** Represents the interval range type */
            public: enum RangeType
            {
                RangeTypeFullHistory/** All the points of the load history are taken */,
                RangeTypeSubRange/** The load history is restricted to a range */
            };

            /** Represents the matching type */
            public: enum MatchingType
            {
                MatchingTypeAutomatic/** The connections are done automatically */,
                MatchingTypeManual/** The connections are done manually */
            };

            /** Represents the match by type for automatic matching */
            public: enum MatchByType
            {
                MatchByTypeName/** Name matching */,
                MatchByTypeIndex/** Index matching */
            };

            /** Represents the match by type for manual matching */
            public: enum ManualMatchByType
            {
                ManualMatchByTypeName/** Name matching */,
                ManualMatchByTypeOrder/** Order matching */
            };

            /** Represents the name matching algorithm */
            public: enum MatchUsingType
            {
                MatchUsingTypeCompleteSubstring/** Compare complete string */,
                MatchUsingTypeField/** Compare substrings splitted by tokens */,
                MatchUsingTypePattern/** Match using a regular expression */,
                MatchUsingTypeSubstringOfSpecifiedLength/** find shorter substrings */
            };

            /** Represents the find in type */
            public: enum FindInType
            {
                FindInTypeLoadHistories/** Search in load histories */,
                FindInTypeSubcases/** Search in subcases */
            };

            /**  @brief  treatment of load histories with different channel length  

             */
            public: enum HistoryEndTreatmentType
            {
                HistoryEndTreatmentTypeTruncate/** Stop at the first ending load history */,
                HistoryEndTreatmentTypeFillWithLastValue/** Stay at the last value */,
                HistoryEndTreatmentTypeRepeat/** Restart from the first value until the longest channel has ended */
            };

            private: DurSpecialistSuperpositionEventBuilderImpl * m_durspecialistsuperpositioneventbuilder_impl;
            private: friend class  _DurSpecialistSuperpositionEventBuilderBuilder;
            protected: DurSpecialistSuperpositionEventBuilder();
            public: ~DurSpecialistSuperpositionEventBuilder();
            /**Returns  the interval range. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::RangeType Range
            (
            );
            /**Sets  the interval range. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetRange
            (
                NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::RangeType type /** type */ 
            );
            /**Returns  the static load update method. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistEvent::UpdateCriterionType StaticLoadUpdate
            (
            );
            /**Sets  the static load update method. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetStaticLoadUpdate
            (
                NXOpen::CAE::DurSpecialistEvent::UpdateCriterionType type /** type */ 
            );
            /**Returns  the pre-stress update method. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistEvent::UpdateCriterionType PreStressUpdate
            (
            );
            /**Sets  the pre-stress update method. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetPreStressUpdate
            (
                NXOpen::CAE::DurSpecialistEvent::UpdateCriterionType type /** type */ 
            );
            /**Returns  the update method for manual matchings. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistEvent::UpdateCriterionType MatchingUpdate
            (
            );
            /**Sets  the update method for manual matchings. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetMatchingUpdate
            (
                NXOpen::CAE::DurSpecialistEvent::UpdateCriterionType type /** type */ 
            );
            /**Returns  the matching. Setting matching to Automatic will remove the manual connections. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::MatchingType Matching
            (
            );
            /**Sets  the matching. Setting matching to Automatic will remove the manual connections. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetMatching
            (
                NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::MatchingType type /** type */ 
            );
            /**Returns  the match by for automatic matching. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::MatchByType MatchBy
            (
            );
            /**Sets  the match by for automatic matching. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetMatchBy
            (
                NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::MatchByType type /** type */ 
            );
            /**Returns  the match by for manual matching. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::ManualMatchByType ManualMatchBy
            (
            );
            /**Sets  the match by for manual matching. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetManualMatchBy
            (
                NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::ManualMatchByType type /** type */ 
            );
            /**Returns  the match using. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::MatchUsingType MatchUsing
            (
            );
            /**Sets  the match using. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetMatchUsing
            (
                NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::MatchUsingType type /** type */ 
            );
            /**Returns  the case sensitive comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool CaseSensitive
            (
            );
            /**Sets  the case sensitive comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetCaseSensitive
            (
                bool caseSensitive /** casesensitive */ 
            );
            /**Returns  the flag to ignore non-alphanumeric characters in comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool IgnoreSpecialCharacters
            (
            );
            /**Sets  the flag to ignore non-alphanumeric characters in comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetIgnoreSpecialCharacters
            (
                bool ignore /** ignore */ 
            );
            /**Returns  the search pattern. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Find
            (
            );
            /**Sets  the search pattern. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetFind
            (
                const NXString & pattern /** pattern */ 
            );
            /**Sets  the search pattern. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            void SetFind
            (
                const char * pattern /** pattern */ 
            );
            /**Returns  the source of search pattern. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::FindInType FindIn
            (
            );
            /**Sets  the source of search pattern. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetFindIn
            (
                NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::FindInType findIn /** findin */ 
            );
            /**Returns  the comparison pattern. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString MatchWith
            (
            );
            /**Sets  the comparison pattern. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetMatchWith
            (
                const NXString & pattern /** pattern */ 
            );
            /**Sets  the comparison pattern. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            void SetMatchWith
            (
                const char * pattern /** pattern */ 
            );
            /**Returns  the source field index. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int FieldFind
            (
            );
            /**Sets  the source field index. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetFieldFind
            (
                int fieldIndex /** fieldindex */ 
            );
            /**Returns  the source field delimiter. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString FieldFindUsing
            (
            );
            /**Sets  the source field delimiter. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetFieldFindUsing
            (
                const NXString & delimiter /** delimiter */ 
            );
            /**Sets  the source field delimiter. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            void SetFieldFindUsing
            (
                const char * delimiter /** delimiter */ 
            );
            /**Returns  the target field index. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int FieldMatchWith
            (
            );
            /**Sets  the target field index. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetFieldMatchWith
            (
                int fieldIndex /** fieldindex */ 
            );
            /**Returns  the target field delimiter. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString FieldMatchUsing
            (
            );
            /**Sets  the target field delimiter. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetFieldMatchUsing
            (
                const NXString & delimiter /** delimiter */ 
            );
            /**Sets  the target field delimiter. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            void SetFieldMatchUsing
            (
                const char * delimiter /** delimiter */ 
            );
            /**Returns  the flag to use min length in substring comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseMinLength
            (
            );
            /**Sets  the flag to use min length in substring comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetUseMinLength
            (
                bool use /** use */ 
            );
            /**Returns  the min length in substring comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int MinLength
            (
            );
            /**Sets  the min length in substring comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetMinLength
            (
                int length /** length */ 
            );
            /**Returns  the flag to use max length in substring comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseMaxLength
            (
            );
            /**Sets  the flag to use max length in substring comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetUseMaxLength
            (
                bool use /** use */ 
            );
            /**Returns  the max length in substring comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int MaxLength
            (
            );
            /**Sets  the max length in substring comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetMaxLength
            (
                int length /** length */ 
            );
            /**Returns  the load histories. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistDataSources * LoadHistories
            (
            );
            /**Returns  the load length. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistLoadLengthBuilder * LoadLength
            (
            );
            /**Returns  the FE results. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistDataSources * FeResults
            (
            );
            /**Returns  the flag if pre-stress is included in all other subcases. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool PreStressIncluded
            (
            );
            /**Sets  the flag if pre-stress is included in all other subcases. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetPreStressIncluded
            (
                bool included /** included */ 
            );
            /**Returns  the pre-stress scale factor 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * PreStressScale
            (
            );
            /**Returns  the unit load force 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Force
            (
            );
            /**Returns  the unit load moment 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Moment
            (
            );
            /**Returns  the unit load pressure 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Pressure
            (
            );
            /**Returns  the unit load length 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Length
            (
            );
            /**Returns  the unit load angle 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Angle
            (
            );
            /**Returns  the unit load velocity 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Velocity
            (
            );
            /**Returns  the unit load angular velocity 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * AngularVelocity
            (
            );
            /**Returns  the unit load acceleration 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Acceleration
            (
            );
            /**Returns  the unit load angular acceleration 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * AngularAcceleration
            (
            );
            /**Returns  the range start 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RangeStart
            (
            );
            /**Returns  the range end 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RangeEnd
            (
            );
            /**Returns  the pre-stress case 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int PreStressCase
            (
            );
            /**Sets  the pre-stress case 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetPreStressCase
            (
                int modeIndex /** The index in list of available subcases, 0 for deselecting pre-stress */
            );
            /** Get the static loads with their scale factors 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void GetStaticLoad
            (
                std::vector<int> & modeIndex /** modeindex */ ,
                std::vector<double> & scaleFactor /** scalefactor */ 
            );
            /** Set the static loads and their scale factors 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetStaticLoad
            (
                const std::vector<int> & modeIndex /** modeindex */ ,
                const std::vector<double> & scaleFactor /** scalefactor */ 
            );
            /** Add manual connection  @return  -1 if  duplicate load/mode combination 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: int AddConnection
            (
                int loadIndex /** loadindex */ ,
                int modeIndex /** modeindex */ ,
                bool active /** active */ ,
                double scaleFactor /** scalefactor */ 
            );
            /** Delete manual connection 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void DeleteConnection
            (
                int connectionIndex /** connectionindex */ 
            );
            /** Update manual connection 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void UpdateConnection
            (
                int connectionIndex /** connectionindex */ ,
                bool active /** active */ ,
                double scaleFactor /** scalefactor */ 
            );
            /** Update manual connection 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void UpdateUnitLoad
            (
                int connectionIndex /** connectionindex */ ,
                const NXString & unitLoad /** unitload */ 
            );
            /** Update manual connection 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            void UpdateUnitLoad
            (
                int connectionIndex /** connectionindex */ ,
                const char * unitLoad /** unitload */ 
            );
            /**Returns  the name. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            void SetName
            (
                const char * name /** name */ 
            );
            /**Returns  the description. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Description
            (
            );
            /**Sets  the description. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetDescription
            (
                const NXString & description /** description */ 
            );
            /**Sets  the description. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            void SetDescription
            (
                const char * description /** description */ 
            );
            /**Returns  the history treatment 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::HistoryEndTreatmentType HistoryEndTreatment
            (
            );
            /**Sets  the history treatment 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetHistoryEndTreatment
            (
                NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::HistoryEndTreatmentType historyTreatment /** historytreatment */ 
            );
            /**Returns  the name. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: int NumStaticLoadScales
            (
            );
            /**Sets  the name. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetNumStaticLoadScales
            (
                int numModes /** nummodes */ 
            );
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif
