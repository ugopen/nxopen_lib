#ifndef NXOpen_TOOLING_QUICKDATUMCSYSBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_QUICKDATUMCSYSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_QuickDatumCsysBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class QuickDatumCsysBuilder;
    }
    class Builder;
    class CoordinateSystem;
    class Edge;
    namespace Tooling
    {
        class _QuickDatumCsysBuilderBuilder;
        class QuickDatumCsysBuilderImpl;
        /** 
            Represents a @link NXOpen::Tooling::QuickDatumCsysBuilder NXOpen::Tooling::QuickDatumCsysBuilder@endlink  builder.
             <br> Use the @link NXOpen::Tooling::ReusableObjectManager NXOpen::Tooling::ReusableObjectManager@endlink  class to create a QuickDatumCsysBuilder.  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  QuickDatumCsysBuilder : public NXOpen::Builder
        {
            /** Represents an index to components list type. */
            public: enum AlignVectors
            {
                AlignVectorsX/** A list includes X vector */,
                AlignVectorsNegativeX/** A list includes negative X vector */,
                AlignVectorsY/** A list includes Y vector */,
                AlignVectorsNegativeY/** A list includes negative Y vector */,
                AlignVectorsZ/** A list includes Z vector */,
                AlignVectorsNegativeZ/** A list includes negative Z vector */
            };

            private: QuickDatumCsysBuilderImpl * m_quickdatumcsysbuilder_impl;
            private: friend class  _QuickDatumCsysBuilderBuilder;
            protected: QuickDatumCsysBuilder();
            public: ~QuickDatumCsysBuilder();
            /** Gets the align vector type.  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::QuickDatumCsysBuilder::AlignVectors GetAlignVector
            (
            );
            /** Sets the align vector type. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAlignVector
            (
                NXOpen::Tooling::QuickDatumCsysBuilder::AlignVectors alignVector /** alignvector */ 
            );
            /** Gets the reference diameter.  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: double GetReferenceDiameter
            (
            );
            /** Sets the reference diameter. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void SetReferenceDiameter
            (
                double referenceDiameter /** referencediameter */ 
            );
            /** Gets the offset value.  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: double GetOffset
            (
            );
            /** Sets the reference diameter. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOffset
            (
                double offset /** offset */ 
            );
            /** Gets the seed csys.  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CoordinateSystem * GetSeedCsys
            (
            );
            /** Sets the seed csys. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSeedCsys
            (
                NXOpen::CoordinateSystem * seedCsys /** seedcsys */ 
            );
            /** Gets the offset csys.  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CoordinateSystem * GetOffsetCsys
            (
            );
            /** Sets the offset csys. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOffsetCsys
            (
                NXOpen::CoordinateSystem * offsetCsys /** offsetcsys */ 
            );
            /** Gets the csys.  @return  The csys. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::CoordinateSystem *> GetCsys
            (
            );
            /** Romoves the selected edges. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void RemoveEdges
            (
                const std::vector<NXOpen::Edge *> & edges /** The Edges. */
            );
            /** Sets the selected edges. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void SetEdges
            (
                const std::vector<NXOpen::Edge *> & edges /** The Edges. */
            );
            /** Sets the csys. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCsys
            (
                const std::vector<NXOpen::CoordinateSystem *> & csys /** The Csys. */
            );
            /** Update the offset csys. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void UpdateOffsetCsys
            (
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
