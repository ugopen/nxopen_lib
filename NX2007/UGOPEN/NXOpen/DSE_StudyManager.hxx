#ifndef NXOpen_DSE_STUDYMANAGER_HXX_INCLUDED
#define NXOpen_DSE_STUDYMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     DSE_StudyManager.ja
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
#include <NXOpen/BasePart.hxx>
#include <NXOpen/DSE_DesignConstraint.hxx>
#include <NXOpen/DSE_DesignConstraintBuilder.hxx>
#include <NXOpen/DSE_DesignObjective.hxx>
#include <NXOpen/DSE_DesignObjectiveBuilder.hxx>
#include <NXOpen/DSE_DesignVariable.hxx>
#include <NXOpen/DSE_DesignVariableBuilder.hxx>
#include <NXOpen/DSE_DiscreteVariableValueBuilder.hxx>
#include <NXOpen/DSE_OptimizationStudy.hxx>
#include <NXOpen/DSE_OptimizationStudyBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libdseopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace DSE
    {
        class StudyManager;
    }
    class Session;
    namespace DSE
    {
        class DesignConstraint;
    }
    namespace DSE
    {
        class DesignConstraintBuilder;
    }
    namespace DSE
    {
        class DesignObjective;
    }
    namespace DSE
    {
        class DesignObjectiveBuilder;
    }
    namespace DSE
    {
        class DesignVariable;
    }
    namespace DSE
    {
        class DesignVariableBuilder;
    }
    namespace DSE
    {
        class DiscreteVariableValueBuilder;
    }
    namespace DSE
    {
        class OptimizationStudy;
    }
    namespace DSE
    {
        class OptimizationStudyBuilder;
    }
    class Part;
    namespace DSE
    {
        class StudyManagerImpl;
        /** Represents the Design Space Explorer Study Manager class. <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class DSEOPENCPPEXPORT  StudyManager
        {
            private: StudyManagerImpl * m_studymanager_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit StudyManager(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            private: static StudyManager* theStudyManager;
            /** Returns the StudyManager object for the running session which serves as the 'gateway' class for the application API.  
                References to all other objects in this API are obtained either directly or indirectly via methods and properties on this class.  
                Platform Session should be initialized using 'GetSession' method from NXOpen API prior to this call.  
            */
            public: static StudyManager* GetStudyManager(NXOpen::Session *owner);
            public: ~StudyManager();
            /** Creates a @link DSE::OptimizationStudyBuilder DSE::OptimizationStudyBuilder@endlink  
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_design_explorer (" NX Design Space Exploration") */
            public: NXOpen::DSE::OptimizationStudyBuilder * CreateOptimizationStudyBuilder
            (
                NXOpen::Part * part /** part */ ,
                NXOpen::DSE::OptimizationStudy * studyObj /** studyobj */ 
            );
            /** Creates a @link DSE::DesignVariableBuilder DSE::DesignVariableBuilder@endlink  
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_design_explorer (" NX Design Space Exploration") */
            public: NXOpen::DSE::DesignVariableBuilder * CreateDesignVariableBuilder
            (
                NXOpen::Part * part /** part */ ,
                NXOpen::DSE::DesignVariable * dvObj /** dvobj */ 
            );
            /** Creates a @link DSE::DiscreteVariableValueBuilder DSE::DiscreteVariableValueBuilder@endlink  
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_design_explorer (" NX Design Space Exploration") */
            public: NXOpen::DSE::DiscreteVariableValueBuilder * CreateDiscreteVariableValueBuilder
            (
                NXOpen::Part * part /** part */ 
            );
            /** Creates a @link DSE::DesignConstraintBuilder DSE::DesignConstraintBuilder@endlink  
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_design_explorer (" NX Design Space Exploration") */
            public: NXOpen::DSE::DesignConstraintBuilder * CreateDesignConstraintBuilder
            (
                NXOpen::Part * part /** part */ ,
                NXOpen::DSE::DesignConstraint * desConstraint /** desconstraint */ 
            );
            /** Creates a @link DSE::DesignObjectiveBuilder DSE::DesignObjectiveBuilder@endlink  
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_design_explorer (" NX Design Space Exploration") */
            public: NXOpen::DSE::DesignObjectiveBuilder * CreateDesignObjectiveBuilder
            (
                NXOpen::Part * part /** part */ ,
                NXOpen::DSE::DesignObjective * designObjectiveObj /** designobjectiveobj */ 
            );
        }; //lint !e1712 default constructor not defined for class  

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
