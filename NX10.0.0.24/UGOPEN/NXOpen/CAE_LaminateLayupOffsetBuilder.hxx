#ifndef NXOpen_CAE_LAMINATELAYUPOFFSETBUILDER_HXX_INCLUDED
#define NXOpen_CAE_LAMINATELAYUPOFFSETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LaminateLayupOffsetBuilder.ja
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
#include <NXOpen/CAE_LaminateLayupOffsetBuilder.hxx>
#include <NXOpen/CAE_LaminateSelectEntitiesBuilder.hxx>
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
        class LaminateLayupOffsetBuilder;
    }
    class Builder;
    namespace CAE
    {
        class LaminateSelectEntitiesBuilder;
    }
    class Expression;
    namespace CAE
    {
        class _LaminateLayupOffsetBuilderBuilder;
        class LaminateLayupOffsetBuilderImpl;
        /** Represents a @link NXOpen::CAE::LaminateLayupOffset NXOpen::CAE::LaminateLayupOffset@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::CAE::LaminateGlobalLayupMgr::CreateLayupOffsetBuilder  NXOpen::CAE::LaminateGlobalLayupMgr::CreateLayupOffsetBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  LaminateLayupOffsetBuilder : public NXOpen::Builder
        {
            private: LaminateLayupOffsetBuilderImpl * m_laminatelayupoffsetbuilder_impl;
            private: friend class  _LaminateLayupOffsetBuilderBuilder;
            protected: LaminateLayupOffsetBuilder();
            public: ~LaminateLayupOffsetBuilder();
            /**Returns  the geometric face(s) and element faces on which to assign the layup offset rule 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::LaminateSelectEntitiesBuilder * Selection
            (
            );
            /**Sets  the fiber distance 
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::CAE::LaminateLayupOffsetBuilder::RefPlanePosition NXOpen::CAE::LaminateLayupOffsetBuilder::RefPlanePosition@endlink  instead. <br>  

             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use NXOpen::CAE::LaminateLayupOffsetBuilder::RefPlanePosition instead.") void SetFiberDistance
            (
                double fiberDistance /** fiber distance */
            );
            /**Returns  the fiber distance 
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::CAE::LaminateLayupOffsetBuilder::RefPlanePosition NXOpen::CAE::LaminateLayupOffsetBuilder::RefPlanePosition@endlink  instead. <br>  

             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use NXOpen::CAE::LaminateLayupOffsetBuilder::RefPlanePosition instead.") double FiberDistance
            (
            );
            /**Returns  the reference plane position expression 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RefPlanePosition
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
