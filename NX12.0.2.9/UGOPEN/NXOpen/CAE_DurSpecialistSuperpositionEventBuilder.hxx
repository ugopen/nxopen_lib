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

        /// \cond NX_NO_DOC 
        /** Represents a @link NXOpen::CAE::DurSpecialistSuperpositionEvent NXOpen::CAE::DurSpecialistSuperpositionEvent@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::CAE::DurSpecialistLoadProviderCollection::CreateSuperpositionEventBuilder  NXOpen::CAE::DurSpecialistLoadProviderCollection::CreateSuperpositionEventBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        MatchUsing </td> <td> 
         
        CompleteSubstring </td> </tr> 

        <tr><td> 
         
        Range </td> <td> 
         
        FullHistory </td> </tr> 

        </table>  

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

            private: DurSpecialistSuperpositionEventBuilderImpl * m_durspecialistsuperpositioneventbuilder_impl;
            private: friend class  _DurSpecialistSuperpositionEventBuilderBuilder;
            protected: DurSpecialistSuperpositionEventBuilder();
            public: ~DurSpecialistSuperpositionEventBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the interval range. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::RangeType Range
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the interval range. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetRange
            (
                NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::RangeType type /** type */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the static load update method. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistEvent::UpdateCriterionType StaticLoadUpdate
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the static load update method. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetStaticLoadUpdate
            (
                NXOpen::CAE::DurSpecialistEvent::UpdateCriterionType type /** type */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the pre-stress update method. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistEvent::UpdateCriterionType PreStressUpdate
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the pre-stress update method. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetPreStressUpdate
            (
                NXOpen::CAE::DurSpecialistEvent::UpdateCriterionType type /** type */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the update method for manual matchings. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistEvent::UpdateCriterionType MatchingUpdate
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the update method for manual matchings. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetMatchingUpdate
            (
                NXOpen::CAE::DurSpecialistEvent::UpdateCriterionType type /** type */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the matching. Setting matching to Automatic will remove the manual connections. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::MatchingType Matching
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the matching. Setting matching to Automatic will remove the manual connections. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetMatching
            (
                NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::MatchingType type /** type */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the match by. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::MatchByType MatchBy
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the match by. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetMatchBy
            (
                NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::MatchByType type /** type */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the match using. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::MatchUsingType MatchUsing
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the match using. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetMatchUsing
            (
                NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::MatchUsingType type /** type */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the case sensitive comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool CaseSensitive
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the case sensitive comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetCaseSensitive
            (
                bool caseSensitive /** casesensitive */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the flag to ignore non-alphanumeric characters in comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool IgnoreSpecialCharacters
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the flag to ignore non-alphanumeric characters in comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetIgnoreSpecialCharacters
            (
                bool ignore /** ignore */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the search pattern. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Find
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the search pattern. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetFind
            (
                const NXString & pattern /** pattern */ 
            );
            /**Sets  the search pattern. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            void SetFind
            (
                const char * pattern /** pattern */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the source of search pattern. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::FindInType FindIn
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the source of search pattern. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetFindIn
            (
                NXOpen::CAE::DurSpecialistSuperpositionEventBuilder::FindInType findIn /** findin */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the comparison pattern. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString MatchWith
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the comparison pattern. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetMatchWith
            (
                const NXString & pattern /** pattern */ 
            );
            /**Sets  the comparison pattern. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            void SetMatchWith
            (
                const char * pattern /** pattern */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the source field index. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int FieldFind
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the source field index. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetFieldFind
            (
                int fieldIndex /** fieldindex */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the source field delimiter. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString FieldFindUsing
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the source field delimiter. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetFieldFindUsing
            (
                const NXString & delimiter /** delimiter */ 
            );
            /**Sets  the source field delimiter. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            void SetFieldFindUsing
            (
                const char * delimiter /** delimiter */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the target field index. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int FieldMatchWith
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the target field index. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetFieldMatchWith
            (
                int fieldIndex /** fieldindex */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the target field delimiter. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString FieldMatchUsing
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the target field delimiter. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetFieldMatchUsing
            (
                const NXString & delimiter /** delimiter */ 
            );
            /**Sets  the target field delimiter. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            void SetFieldMatchUsing
            (
                const char * delimiter /** delimiter */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the flag to use min length in substring comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseMinLength
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the flag to use min length in substring comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetUseMinLength
            (
                bool use /** use */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the min length in substring comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int MinLength
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the min length in substring comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetMinLength
            (
                int length /** length */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the flag to use max length in substring comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseMaxLength
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the flag to use max length in substring comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetUseMaxLength
            (
                bool use /** use */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the max length in substring comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int MaxLength
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the max length in substring comparison. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetMaxLength
            (
                int length /** length */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the load histories. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistDataSources * LoadHistories
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the load length. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistLoadLengthBuilder * LoadLength
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the FE results. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistDataSources * FeResults
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the flag if pre-stress is included in all other subcases. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool PreStressIncluded
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the flag if pre-stress is included in all other subcases. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetPreStressIncluded
            (
                bool included /** included */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the pre-stress scale factor 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * PreStressScale
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the unit load force 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Force
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the unit load moment 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Moment
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the unit load pressure 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Pressure
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the unit load length 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Length
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the unit load angle 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Angle
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the unit load velocity 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Velocity
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the unit load angular velocity 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * AngularVelocity
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the unit load acceleration 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Acceleration
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the unit load angular acceleration 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * AngularAcceleration
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the range start 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RangeStart
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the range end 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RangeEnd
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the pre-stress case 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int PreStressCase
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the pre-stress case 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetPreStressCase
            (
                int modeIndex /** The index in list of available subcases, 0 for deselecting pre-stress */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get the static loads with their scale factors 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void GetStaticLoad
            (
                std::vector<int> & modeIndex /** modeindex */ ,
                std::vector<double> & scaleFactor /** scalefactor */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Set the static loads and their scale factors 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetStaticLoad
            (
                const std::vector<int> & modeIndex /** modeindex */ ,
                const std::vector<double> & scaleFactor /** scalefactor */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Add manual connection  @return  -1 if  duplicate load/mode combination 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: int AddConnection
            (
                int loadIndex /** loadindex */ ,
                int modeIndex /** modeindex */ ,
                bool active /** active */ ,
                double scaleFactor /** scalefactor */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Delete manual connection 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void DeleteConnection
            (
                int connectionIndex /** connectionindex */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Update manual connection 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void UpdateConnection
            (
                int connectionIndex /** connectionindex */ ,
                bool active /** active */ ,
                double scaleFactor /** scalefactor */ 
            );

            /// \endcond 
        };

        /// \endcond 
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
