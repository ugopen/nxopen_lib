#ifndef NXOpen_FEATURES_SUBDIVISION_SUBDIVISIONSETCONTINUITYBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SUBDIVISION_SUBDIVISIONSETCONTINUITYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Subdivision_SubdivisionSetContinuityBuilder.ja
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
#include <NXOpen/Features_Subdivision_SelectCageObjectData.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace Subdivision
        {
            class SubdivisionSetContinuityBuilder;
        }
    }
    class Builder;
    namespace Features
    {
        namespace Subdivision
        {
            class SelectCageObjectData;
        }
    }
    namespace Features
    {
        namespace Subdivision
        {
            class _SubdivisionSetContinuityBuilderBuilder;
            class SubdivisionSetContinuityBuilderImpl;
            /** Represents a @link NXOpen::Features::Subdivision::SubdivisionSetContinuityBuilder NXOpen::Features::Subdivision::SubdivisionSetContinuityBuilder@endlink  builder.   <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionSetContinuityBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionSetContinuityBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            ContinuityType </td> <td> 
             
            Smooth </td> </tr> 

            </table>  

             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  SubdivisionSetContinuityBuilder : public NXOpen::Builder
            {
                /** Represents the continuity type */
                public: enum ContinuityTypes
                {
                    ContinuityTypesSmooth/** smooth */ ,
                    ContinuityTypesSharp/** sharp */ 
                };

                private: SubdivisionSetContinuityBuilderImpl * m_subdivisionsetcontinuitybuilder_impl;
                private: friend class  _SubdivisionSetContinuityBuilderBuilder;
                protected: SubdivisionSetContinuityBuilder();
                public: ~SubdivisionSetContinuityBuilder();
                /**Returns  the target object. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::Subdivision::SelectCageObjectData * TargetObject
                (
                );
                /**Returns  the continuity. The continuity is used to specify creases in the limit surface. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::Subdivision::SubdivisionSetContinuityBuilder::ContinuityTypes ContinuityType
                (
                );
                /**Sets  the continuity. The continuity is used to specify creases in the limit surface. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetContinuityType
                (
                    NXOpen::Features::Subdivision::SubdivisionSetContinuityBuilder::ContinuityTypes continuityType /** continuitytype */ 
                );
            };
        }
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
