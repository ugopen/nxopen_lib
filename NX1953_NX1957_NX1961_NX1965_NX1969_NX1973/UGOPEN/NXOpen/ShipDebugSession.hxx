#ifndef NXOpen_SHIPDEBUGSESSION_HXX_INCLUDED
#define NXOpen_SHIPDEBUGSESSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ShipDebugSession.ja
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
    class ShipDebugSession;
    class DebugSession;
    class BasePart;
    class ShipBaseDrawingValidator;
    class ShipBaseValidator;
    class ShipDebugSessionImpl;

    /// \cond NX_NO_DOC 
    /** Represents a class that is used for NX SHIP Autotest.  This class should not
    be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::DebugSession  NXOpen::DebugSession @endlink  <br> 
     <br>  Created in NX10.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  ShipDebugSession
    {
        private: ShipDebugSessionImpl * m_shipdebugsession_impl;
        private: NXOpen::DebugSession* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit ShipDebugSession(NXOpen::DebugSession *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~ShipDebugSession();

        /// \cond NX_NO_DOC 
        /** Create a ship validation object.  @return  created validator 
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ShipBaseValidator * CreateShipValidator
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create the validators for each ship feature found. 
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateValidators
        (
            NXOpen::ShipBaseValidator * mainValidator /** main ship validator */,
            std::vector<NXOpen::ShipBaseValidator *> & validators /** created validators */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create a ship drawing validation object.  @return  created drawing validator 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ShipBaseDrawingValidator * CreateShipDrawingValidator
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create the validators for each ship feature found. 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateDrawingValidators
        (
            NXOpen::ShipBaseDrawingValidator * mainDrawingValidator /** main ship drawing validator */,
            std::vector<NXOpen::ShipBaseDrawingValidator *> & drawingValidators /** created drawing validators */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Change the style of all Ship Section Views to make it show stable result. 
         <br>  Created in NX11.0.2.  <br>  
         <br> License requirements : None */
        public: void ChangeSectionViewStyle
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Print expression in master xml. 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void PrintExpression
        (
            NXOpen::BasePart * workPart /** part the expression in */,
            const NXString & expressionName /** expression name */
        );
        /** Print expression in master xml. 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        void PrintExpression
        (
            NXOpen::BasePart * workPart /** part the expression in */,
            const char * expressionName /** expression name */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create a ship standard part validation object.  @return  created ship standard part validator 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ShipBaseValidator * CreateShipStandardPartValidator
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Populate the validator with data for each standard part found. 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateAndPrintStandardPartValidator
        (
            NXOpen::ShipBaseValidator * validator /** standard ship part validator */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Print CAE Preparation objects in master xml. 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateAndPrintCaePreparationObjects
        (
            NXOpen::BasePart * workPart /** part the objects in */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Print weight and cg objects in master xml. 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void WeightAndCg
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Print Hydrostatic Stability Analysis in master xml. 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: void HydrostaticStabilityAnalysis
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Print structure in master xml. 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: void StructureXmloutput
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create a shipga room validator collection object.  @return  created validator 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ShipBaseValidator * CreateShipgaRoomcollectionvalidator
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create the validators for each shipga room found. 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateGaroomvalidators
        (
            NXOpen::ShipBaseValidator * mainValidator /** main ship validator */,
            std::vector<NXOpen::ShipBaseValidator *> & validators /** created validators */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create a manufacturing xml output validator collection object  @return  created validator 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ShipBaseValidator * CreateMfgxmloutputCollectionvalidator
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create validators for manufacturing xml output, one validator per each manufacturing part. 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateMfgxmlValidators
        (
            NXOpen::ShipBaseValidator * mainValidator /** main ship validator */,
            std::vector<NXOpen::ShipBaseValidator *> & validators /** created validators */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create the validators for each ship drawing curve cfw.  @return  created ship drawing curves cfw validator 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ShipBaseDrawingValidator * CreateShipDrawingCurvesCfwValidator
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Populate the validator with data for each standard part found. 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateAndPrintShipDrawingCurvesCfwValidator
        (
            NXOpen::ShipBaseDrawingValidator * validator /** standard ship  drawing curves cfw  validator */,
            std::vector<NXString> & names /** curve information name */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create a ship drawing profile sketch xml output validator collection object  @return  created ship drawing profile sketch validator 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ShipBaseDrawingValidator * CreateShipDrawingProfileSketchValidator
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Populates and outputs the validation to the xml file for profile sketch drawings. 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateAndPrintShipDrawingProfileSketchValidator
        (
            NXOpen::ShipBaseDrawingValidator * validator /** standard ship  drawing profile sketch validator */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Creates a manufacturing profile xml output validator collection object  @return  created validator 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ShipBaseValidator * CreateMfgProfileXmlOutputCollectionValidator
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Creates validators for manufacturing profile xml output, one validator per each manufacturing part. 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateMfgProfileXmlValidators
        (
            NXOpen::ShipBaseValidator * mainValidator /** main ship validator */,
            std::vector<NXOpen::ShipBaseValidator *> & validators /** created validators */
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
