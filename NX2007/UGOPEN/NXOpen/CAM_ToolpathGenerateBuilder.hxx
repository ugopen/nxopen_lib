#ifndef NXOpen_CAM_TOOLPATHGENERATEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TOOLPATHGENERATEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ToolpathGenerateBuilder.ja
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
#include <NXOpen/CAM_ToolpathGenerateResult.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class ToolpathGenerateBuilder;
    }
    namespace CAM
    {
        class ToolpathGenerateResult;
    }
    namespace CAM
    {
        class ToolpathGenerateBuilderImpl;
        /** Represents a context for toolpath generate action
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ToolpathGenerateBuilder : public NXOpen::TransientObject
        {
            /** Generation type */
            public: enum Types
            {
                TypesForeground/** foreground */ ,
                TypesBackground/** background */ ,
                TypesParallel/** parallel */ 
            };

            private: ToolpathGenerateBuilderImpl * m_toolpathgeneratebuilder_impl;
            /// \cond NX_NO_DOC 
            public: explicit ToolpathGenerateBuilder(void *ptr);
            /// \endcond 
            /** Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage
                    collector. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~ToolpathGenerateBuilder();
            /**Returns  the generation type 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ToolpathGenerateBuilder::Types GenerationType
            (
            );
            /**Sets  the generation type 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetGenerationType
            (
                NXOpen::CAM::ToolpathGenerateBuilder::Types generationType /** generationtype */ 
            );
            /** Generate 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void Generate
            (
                std::vector<NXOpen::CAM::ToolpathGenerateResult *> & reuslts /** reuslts */ 
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
