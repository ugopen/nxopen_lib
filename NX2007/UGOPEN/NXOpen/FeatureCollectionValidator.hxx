#ifndef NXOpen_FEATURECOLLECTIONVALIDATOR_HXX_INCLUDED
#define NXOpen_FEATURECOLLECTIONVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     FeatureCollectionValidator.ja
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
#include <NXOpen/IValidator.hxx>
#include <NXOpen/IValidator.hxx>
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
    class FeatureCollectionValidator;
    class IValidator;
    class _FeatureCollectionValidatorBuilder;
    class FeatureCollectionValidatorImpl;

    /// \cond NX_NO_DOC 
    /** validator for FeatureCollection in a part.  <br> This is a test class.  <br> 
     <br>  Created in NX7.5.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  FeatureCollectionValidator : public NXOpen::TaggedObject, public virtual NXOpen::IValidator
    {
        /** Enumeration used for various object validation controls. */

        /// \cond NX_NO_DOC 
        public: enum ValidationOption
        {
            ValidationOptionAll/** Print validation for all live objects of the specified type in the part */,
            ValidationOptionNewAndModified/** Print validation for only new objects and objects modified in the current session in the part */,
            ValidationOptionPreExisting/** Print validation for only pre-existing objects (all live objects except new objects) */,
            ValidationOptionNone/** Do not print validation for any objects of the specified type */
        };


        /// \endcond 
        private: FeatureCollectionValidatorImpl * m_featurecollectionvalidator_impl;
        private: friend class  _FeatureCollectionValidatorBuilder;
        protected: FeatureCollectionValidator();
        public: ~FeatureCollectionValidator();

        /// \cond NX_NO_DOC 
        /** Get the expression validation option  @return  
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: bool GetValidateExpressions
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Set the expression validation option 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void SetValidateExpressions
        (
            bool validateExpressions /** validateexpressions */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Get the option to control validation of faces and edges  @return  
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::FeatureCollectionValidator::ValidationOption GetValidateFacesAndEdges
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Set the option to control validation of faces and edges 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: void SetValidateFacesAndEdges
        (
            NXOpen::FeatureCollectionValidator::ValidationOption validateFacesAndEdges /** validatefacesandedges */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Get the option to control validation of bodies  @return  
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::FeatureCollectionValidator::ValidationOption GetValidateBodies
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Set the option to control validation of bodies 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: void SetValidateBodies
        (
            NXOpen::FeatureCollectionValidator::ValidationOption validateBodies /** validatebodies */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Get the option to control validation of curves and points  @return  
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::FeatureCollectionValidator::ValidationOption GetValidateCurvesAndPoints
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Set the option to control validation of curves and points 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: void SetValidateCurvesAndPoints
        (
            NXOpen::FeatureCollectionValidator::ValidationOption validateCurvesAndPoints /** validatecurvesandpoints */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Get the option to control validation of feature states and parent-child information  @return  
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::FeatureCollectionValidator::ValidationOption GetValidateFeatureInfo
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Set the option to control validation of feature states and parent-child information 
         <br>  Created in NX1926.0.0.  <br>  
         <br> License requirements : None */
        public: void SetValidateFeatureInfo
        (
            NXOpen::FeatureCollectionValidator::ValidationOption validateFeatureInfo /** validatefeatureinfo */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Get the shape validation option  @return  
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: bool GetValidateShape
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Set the shape validation option 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: void SetValidateShape
        (
            bool validateShape /** validateshape */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Get the geometry validation option  @return  
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: bool GetValidateGeometry
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Set the geometry validation option 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void SetValidateGeometry
        (
            bool validateGeometry /** validategeometry */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Get the geometry validation option  @return  
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: bool GetCompareConvergentMinimumRadius
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Set the geometry validation option 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void SetCompareConvergentMinimumRadius
        (
            bool compareConvergentMinimumRadius /** compareconvergentminimumradius */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Get the significant tolerance  @return  
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: double GetSignificantDifference
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Set the significant tolerance difference 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSignificantDifference
        (
            double significantDifference /** significantdifference */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Get the distance tolerance  @return  
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: double GetDistanceTolerance
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Set the distance tolerance 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void SetDistanceTolerance
        (
            double distanceTolerance /** distancetolerance */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Get the angular tolerance  @return  
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: double GetAngularTolerance
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Set the angular tolerance 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void SetAngularTolerance
        (
            double angularTolerance /** angulartolerance */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Get the centroid coordinate tolerance  @return  
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: double GetCentroidTolerance
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Set the centroid coordinate tolerance 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void SetCentroidTolerance
        (
            double centroidTolerance /** centroidtolerance */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Get the use parasolid error bounds option  @return  
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: bool GetUseParasolidErrorBounds
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Set the use parasolid error bounds option 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void SetUseParasolidErrorBounds
        (
            bool useParasolidErrorBounds /** useparasoliderrorbounds */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Get the mass properties percent difference  @return  
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: double GetMassPropPercentDifference
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Set the mass properties percent difference 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void SetMassPropPercentDifference
        (
            double massPropPercentDifference /** massproppercentdifference */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the algorithm to use for validation. 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: virtual NXOpen::ValidatorVersion ValidatorVersion
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the algorithm to use for validation. 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: virtual void SetValidatorVersion
        (
            NXOpen::ValidatorVersion version /** version */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the print level for validation. 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: virtual NXOpen::ValidatorPrintLevel ValidatorPrintLevel
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the print level for validation. 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: virtual void SetValidatorPrintLevel
        (
            NXOpen::ValidatorPrintLevel level /** level */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Deletes the validator. 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: virtual void Destroy
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Set the ood status of features. 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: virtual void SetValidatorPrintOodStatus
        (
            bool status /** status */ 
        );

        /// \endcond 
    };

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
