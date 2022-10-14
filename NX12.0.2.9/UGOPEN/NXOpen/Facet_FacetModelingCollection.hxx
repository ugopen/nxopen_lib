#ifndef NXOpen_FACET_FACETMODELINGCOLLECTION_HXX_INCLUDED
#define NXOpen_FACET_FACETMODELINGCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Facet_FacetModelingCollection.ja
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
#include <NXOpen/Facet_AdjustMinimumRadiusBuilder.hxx>
#include <NXOpen/Facet_CleanupFacetBodyBuilder.hxx>
#include <NXOpen/Facet_CombineFacetBodyBuilder.hxx>
#include <NXOpen/Facet_ConvertFacetBodyBuilder.hxx>
#include <NXOpen/Facet_CreateTransitionBuilder.hxx>
#include <NXOpen/Facet_DetectPrimitivesBuilder.hxx>
#include <NXOpen/Facet_DivideFacetFaceBuilder.hxx>
#include <NXOpen/Facet_FacetBodyFromBodyBuilder.hxx>
#include <NXOpen/Facet_LocalOffsetBuilder.hxx>
#include <NXOpen/Facet_MergeFacetFacesBuilder.hxx>
#include <NXOpen/Facet_PaintBrushBuilder.hxx>
#include <NXOpen/Facet_PaintFacetBodyBuilder.hxx>
#include <NXOpen/Facet_PolygonModelingBuilder.hxx>
#include <NXOpen/Facet_RemoveUndercutsBuilder.hxx>
#include <NXOpen/Facet_SplitCurveMethodBuilder.hxx>
#include <NXOpen/Facet_SplitCurveMethodListDataManager.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_facet_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Facet
    {
        class FacetModelingCollection;
    }
    namespace Facet
    {
        class FacetedBodyCollection;
    }
    namespace Facet
    {
        class AdjustMinimumRadiusBuilder;
    }
    namespace Facet
    {
        class CleanupFacetBodyBuilder;
    }
    namespace Facet
    {
        class CombineFacetBodyBuilder;
    }
    namespace Facet
    {
        class ConvertFacetBodyBuilder;
    }
    namespace Facet
    {
        class CreateTransitionBuilder;
    }
    namespace Facet
    {
        class DetectPrimitivesBuilder;
    }
    namespace Facet
    {
        class DivideFacetFaceBuilder;
    }
    namespace Facet
    {
        class FacetBodyFromBodyBuilder;
    }
    namespace Facet
    {
        class LocalOffsetBuilder;
    }
    namespace Facet
    {
        class MergeFacetFacesBuilder;
    }
    namespace Facet
    {
        class PaintBrushBuilder;
    }
    namespace Facet
    {
        class PaintFacetBodyBuilder;
    }
    namespace Facet
    {
        class PolygonModelingBuilder;
    }
    namespace Facet
    {
        class RemoveUndercutsBuilder;
    }
    namespace Facet
    {
        class SplitCurveMethodBuilder;
    }
    namespace Facet
    {
        class SplitCurveMethodListDataManager;
    }
    namespace Facet
    {
        class FacetModelingCollectionImpl;
        /** Collection of freeform facet operations.  <br> To obtain an instance of this class, refer to @link NXOpen::Facet::FacetedBodyCollection  NXOpen::Facet::FacetedBodyCollection @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_FACETEXPORT  FacetModelingCollection
        {
            private: FacetModelingCollectionImpl * m_facetmodelingcollection_impl;
            private: NXOpen::Facet::FacetedBodyCollection* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit FacetModelingCollection(NXOpen::Facet::FacetedBodyCollection *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~FacetModelingCollection();
            /** Creates a @link NXOpen::Facet::ConvertFacetBodyBuilder NXOpen::Facet::ConvertFacetBodyBuilder@endlink   @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::Facet::ConvertFacetBodyBuilder * CreateConvertFacetBodyBuilder
            (
            );
            /** Creates a @link NXOpen::Facet::CleanupFacetBodyBuilder NXOpen::Facet::CleanupFacetBodyBuilder@endlink   @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::Facet::CleanupFacetBodyBuilder * CreateCleanupFacetBodyBuilder
            (
            );
            /** Creates a @link NXOpen::Facet::CombineFacetBodyBuilder NXOpen::Facet::CombineFacetBodyBuilder@endlink   @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::Facet::CombineFacetBodyBuilder * CreateCombineFacetBodyBuilder
            (
            );
            /** Creates a @link NXOpen::Facet::FacetBodyFromBodyBuilder NXOpen::Facet::FacetBodyFromBodyBuilder@endlink   @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::Facet::FacetBodyFromBodyBuilder * CreateFacetBodyFromBodyBuilder
            (
            );
            /** Creates a @link NXOpen::Facet::DetectPrimitivesBuilder NXOpen::Facet::DetectPrimitivesBuilder@endlink  object.  @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::DetectPrimitivesBuilder * CreateDetectPrimitivesBuilder
            (
            );
            /** Creates a @link NXOpen::Facet::PaintFacetBodyBuilder NXOpen::Facet::PaintFacetBodyBuilder@endlink  object.  @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::PaintFacetBodyBuilder * CreatePaintFacetBodyBuilder
            (
            );
            /** Creates a @link NXOpen::Facet::PaintBrushBuilder NXOpen::Facet::PaintBrushBuilder@endlink  object.  @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::PaintBrushBuilder * CreatePaintBrushBuilder
            (
            );
            /** Creates a @link NXOpen::Facet::RemoveUndercutsBuilder NXOpen::Facet::RemoveUndercutsBuilder@endlink  object  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: NXOpen::Facet::RemoveUndercutsBuilder * CreateRemoveUndercutsBuilder
            (
            );
            /** Creates a @link NXOpen::Facet::CreateTransitionBuilder NXOpen::Facet::CreateTransitionBuilder@endlink  object  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: NXOpen::Facet::CreateTransitionBuilder * CreateCreateTransitionBuilder
            (
            );
            /** Creates a @link Facet::LocalOffsetBuilder Facet::LocalOffsetBuilder@endlink   @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: NXOpen::Facet::LocalOffsetBuilder * CreateLocalOffsetBuilder
            (
            );
            /** Creates a @link NXOpen::Facet::MergeFacetFacesBuilder NXOpen::Facet::MergeFacetFacesBuilder@endlink   @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: NXOpen::Facet::MergeFacetFacesBuilder * CreateMergeFacetFacesBuilder
            (
            );
            /** Create a @link NXOpen::Facet::AdjustMinimumRadiusBuilder NXOpen::Facet::AdjustMinimumRadiusBuilder@endlink  object.  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::AdjustMinimumRadiusBuilder * CreateFacetAdjustMinimumRadiusBuilder
            (
            );
            /** Creates a @link NXOpen::Facet::DivideFacetFaceBuilder NXOpen::Facet::DivideFacetFaceBuilder@endlink   @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: NXOpen::Facet::DivideFacetFaceBuilder * CreateDivideFacetFaceBuilder
            (
            );
            /** Creates a @link NXOpen::Facet::PolygonModelingBuilder NXOpen::Facet::PolygonModelingBuilder@endlink   @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: NXOpen::Facet::PolygonModelingBuilder * CreatePolygonModelingBuilder
            (
            );
            /** Creates a @link NXOpen::Facet::SplitCurveMethodBuilder NXOpen::Facet::SplitCurveMethodBuilder@endlink   @return  
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: NXOpen::Facet::SplitCurveMethodBuilder * CreateSplitCurveMethodBuilder
            (
            );
            /** Creates a @link NXOpen::Facet::SplitCurveMethodListDataManager NXOpen::Facet::SplitCurveMethodListDataManager@endlink   @return  
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: NXOpen::Facet::SplitCurveMethodListDataManager * CreateSplitCurveMethodListDataManager
            (
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