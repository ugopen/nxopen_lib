#ifndef NXOpen_CAE_FEATUREELEMEDGEMETHOD_HXX_INCLUDED
#define NXOpen_CAE_FEATUREELEMEDGEMETHOD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FeatureElemEdgeMethod.ja
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
#include <NXOpen/CAE_SetObject.hxx>
#include <NXOpen/SelectionMethod.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class FeatureElemEdgeMethod;
    }
    class SelectionMethod;
    class TaggedObject;
    namespace CAE
    {
    }
    namespace CAE
    {
        class FeatureElemEdgeMethodImpl;
        /** Represents the output from the feature element edge smart selector method
             <br> To obtain an instance of this class use CAE::SmartSelectionManager <br> */
        class NXOPENCPPEXPORT  FeatureElemEdgeMethod : public SelectionMethod
        {
            private: FeatureElemEdgeMethodImpl * m_featureelemedgemethod_impl;
            public: explicit FeatureElemEdgeMethod(void *ptr);
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~FeatureElemEdgeMethod();
            /** Returns the resultant element edges  @return   <br> License requirements : None */
            public: std::vector<NXOpen::CAE::SetObject> GetElementEdges
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif