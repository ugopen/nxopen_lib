#ifndef NXOpen_CAE_FEATUREEDGENODEMETHODOPTIONS_HXX_INCLUDED
#define NXOpen_CAE_FEATUREEDGENODEMETHODOPTIONS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FeatureEdgeNodeMethodOptions.ja
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
#include <NXOpen/CAE_FeatureElementEdgeType.hxx>
#include <NXOpen/TransientObject.hxx>
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
        class FeatureEdgeNodeMethodOptions;
    }
    namespace CAE
    {
        class FeatureEdgeNodeMethodOptionsImpl;
        /**  @brief  Represents the FEM creation options to be used when a FEM part is created  

          <br> To obtain an instance of this class use CAE::SmartSelectionManager  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  FeatureEdgeNodeMethodOptions : public NXOpen::TransientObject
        {
            private: FeatureEdgeNodeMethodOptionsImpl * m_featureedgenodemethodoptions_impl;
            /// \cond NX_NO_DOC 
            public: explicit FeatureEdgeNodeMethodOptions(void *ptr);
            /// \endcond 
            /** Destroys the object 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~FeatureEdgeNodeMethodOptions();
            /** Set flag for entity visibility check 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDoEntityVisibilityCheck
            (
                bool doEntityVisibilityCheck /** If true, visible entities will be returned */
            );
            /** Set flag for compute free edges on visible model 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetComputeFreeEdgesOnVisibleModel
            (
                bool computeFreeEdgesOnVisibleModel /** If true, free edges are computed with respect to the visible elements in the model */
            );
            /** Set flag for stop at non-manifold junctions 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStopAtNonmanifoldJunctions
            (
                bool stopAtNonManifoldJunctions /** If true, the method's output will not span non-manifold junctions */
            );
            /** Set compute element edge type 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetComputeElementEdgeType
            (
                NXOpen::CAE::Type edgeType /** edgetype */ 
            );
            /** Set feature angle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFeatureAngle
            (
                double featureAngle /** featureangle */ 
            );
            /** Set flag for corner nodes 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOnlyCornerNodes
            (
                bool onlyCornerNodes /** If true, only corner nodes will be returned */
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
