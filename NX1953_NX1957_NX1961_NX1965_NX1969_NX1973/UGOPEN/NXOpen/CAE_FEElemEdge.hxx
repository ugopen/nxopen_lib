#ifndef NXOpen_CAE_FEELEMEDGE_HXX_INCLUDED
#define NXOpen_CAE_FEELEMEDGE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FEElemEdge.ja
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
        class FEElemEdge;
    }
    namespace CAE
    {
        class FEElement;
    }
    namespace CAE
    {
        class _FEElemEdgeBuilder;
        class FEElemEdgeImpl;
        /** Represents a Finite Element Edge which can be shared by more that one element. 
         <br>  Created in NX7.5.2.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  FEElemEdge : public NXOpen::TaggedObject
        {
            private: FEElemEdgeImpl * m_feelemedge_impl;
            private: friend class  _FEElemEdgeBuilder;
            protected: FEElemEdge();
            public: ~FEElemEdge();
            /** Returns the elements for this element edge and the corresponding element edge ids. 
                      More information can be queried for these element edges by using the method 
                      on @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink  class 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::CAE::FEElement *> GetElementsAndEdgeIds
            (
                std::vector<int> & edgeIds /** edge ids */ 
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
