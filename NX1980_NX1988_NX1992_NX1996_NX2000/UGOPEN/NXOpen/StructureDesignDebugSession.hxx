#ifndef NXOpen_STRUCTUREDESIGNDEBUGSESSION_HXX_INCLUDED
#define NXOpen_STRUCTUREDESIGNDEBUGSESSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     StructureDesignDebugSession.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class StructureDesignDebugSession;
    class DebugSession;
    class BasePart;
    namespace Features
    {
        namespace StructureDesign
        {
            class Corner;
        }
    }
    class StructureDesignBaseValidator;
    class StructureDesignDebugSessionImpl;

    /// \cond NX_NO_DOC 
    /** Represents a class that is used for NX STRUCTUREDESIGN Autotest.  This class should not
    be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::DebugSession  NXOpen::DebugSession @endlink  <br> 
     <br>  Created in NX1926.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  StructureDesignDebugSession
    {
        private: StructureDesignDebugSessionImpl * m_structuredesigndebugsession_impl;
        private: NXOpen::DebugSession* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit StructureDesignDebugSession(NXOpen::DebugSession *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~StructureDesignDebugSession();

        /// \cond NX_NO_DOC 
        /** Create a structuredesign member validator collection object.  @return  created validator 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::StructureDesignBaseValidator * CreateStructuredesignMembercollectionvalidator
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create the validators for each structuredesign member found. 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateMembervalidators
        (
            NXOpen::StructureDesignBaseValidator * mainValidator /** main structuredesign validator */,
            std::vector<NXOpen::StructureDesignBaseValidator *> & validators /** created validators */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create a structure design corner validation object.  @return  created structure design corner validator 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::StructureDesignBaseValidator * CreateStructureDesignCornerValidator
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Populate the validator with data for each corner found. 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateAndPrintCornerValidator
        (
            NXOpen::StructureDesignBaseValidator * validator /** corner validator */,
            NXOpen::Features::StructureDesign::Corner * cornerTag /** CornerObj being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create a structuredesign gusset validator collection object.  @return  created validator 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::StructureDesignBaseValidator * CreateStructuredesignGussetcollectionvalidator
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create the validators for each structuredesign gusset found. 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateGussetvalidators
        (
            NXOpen::StructureDesignBaseValidator * mainValidator /** main structuredesign validator */,
            std::vector<NXOpen::StructureDesignBaseValidator *> & validators /** created validators */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create a structuredesign endcap validator collection object.  @return  created validator 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::StructureDesignBaseValidator * CreateStructuredesignEndcapcollectionvalidator
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create the validators for each structuredesign endcap found. 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateEndcapvalidators
        (
            NXOpen::StructureDesignBaseValidator * mainValidator /** main structuredesign validator */,
            std::vector<NXOpen::StructureDesignBaseValidator *> & validators /** created validators */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create a structuredesign mountingfeet validator collection object.  @return  created validator 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::StructureDesignBaseValidator * CreateStructuredesignMountingfeetcollectionvalidator
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create the validators for each structuredesign mountingfeet found. 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateMountingfeetvalidators
        (
            NXOpen::StructureDesignBaseValidator * mainValidator /** main structuredesign validator */,
            std::vector<NXOpen::StructureDesignBaseValidator *> & validators /** created validators */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create a structuredesign Grab Tab validator collection object.  @return  created validator 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::StructureDesignBaseValidator * CreateStructuredesignGrabtabcollectionvalidator
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create the validators for each structuredesign Grab Tab found. 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateGrabtabvalidators
        (
            NXOpen::StructureDesignBaseValidator * mainValidator /** main structuredesign validator */,
            std::vector<NXOpen::StructureDesignBaseValidator *> & validators /** created validators */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create a structuredesign Beam Preparation validator object.  @return  created validator 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::StructureDesignBaseValidator * CreateStructuredesignBeamPreparationValidator
        (
            NXOpen::BasePart * displayPart /** beam preparation part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create a structuredesign consolidate validator object.  @return  created validator 
         <br>  Created in NX1980.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::StructureDesignBaseValidator * CreateStructuredesignConsolidateValidator
        (
            NXOpen::BasePart * displayPart /** consolidated structure being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create the validators for each structuredesign consolidated structure found. 
         <br>  Created in NX1980.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateConsolidatevalidators
        (
            NXOpen::StructureDesignBaseValidator * mainValidator /** main structuredesign validator */,
            std::vector<NXOpen::StructureDesignBaseValidator *> & validators /** created validators */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create a structuredesign Manufacture Preparation validator object.  @return  created validator 
         <br>  Created in NX1980.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::StructureDesignBaseValidator * CreateStructuredesignManufacturePreparationValidator
        (
            NXOpen::BasePart * displayPart /** manufacture preparation part being validated */
        );

        /// \endcond 
    }; //lint !e1712 default constructor not defined for class  


    /// \endcond 
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