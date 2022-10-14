#ifndef NXOpen_FEATURES_EXTRUDELIMITDATA_HXX_INCLUDED
#define NXOpen_FEATURES_EXTRUDELIMITDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ExtrudeLimitData.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class ExtrudeLimitData;
    }
    class NXObject;
    namespace Features
    {
    }
    namespace Features
    {
        /** Represents limit data of an extrude feature */
        class NXOPENCPPEXPORT ExtrudeLimitData : public TransientObject
        {
            /** This enum represents the type of limit */
            public: enum LimitType
            {
                LimitTypeDistance/** */,
                LimitTypeUntilNext/** */,
                LimitTypeUntilSelected/** */,
                LimitTypeUntilSelectedExtendFace/** */,
                LimitTypeThroughAll/** */
            };

            public: explicit ExtrudeLimitData(void *ptr);
            /** Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: virtual ~ExtrudeLimitData();
            /**Returns  the extrude symmetricity
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: bool IsSymmetric
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link IsSymmetric() IsSymmetric@endlink instead.
            @deprecated
            */
            public: bool GetIsSymmetric
            (
            ) { return this->IsSymmetric(); }
            /**Returns  the extrude start limit type
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::ExtrudeLimitData::LimitType StartLimitType
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link StartLimitType() StartLimitType@endlink instead.
            @deprecated
            */
            public: NXOpen::Features::ExtrudeLimitData::LimitType GetStartLimitType
            (
            ) { return this->StartLimitType(); }
            /**Returns  the extrude end limit type
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::ExtrudeLimitData::LimitType EndLimitType
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link EndLimitType() EndLimitType@endlink instead.
            @deprecated
            */
            public: NXOpen::Features::ExtrudeLimitData::LimitType GetEndLimitType
            (
            ) { return this->EndLimitType(); }
            /** Gets start limit distance if @link  ExtrudeLimitData::StartLimitType   ExtrudeLimitData::StartLimitType @endlink  is @link ExtrudeLimitData::LimitTypeDistance ExtrudeLimitData::LimitTypeDistance@endlink .
                 @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXString GetStartLimit
            (
            );
            /** Gets start limit data if @link  ExtrudeLimitData::StartLimitType   ExtrudeLimitData::StartLimitType @endlink  is any of following:
                   @link ExtrudeLimitData::LimitTypeUntilNext ExtrudeLimitData::LimitTypeUntilNext@endlink ,
                   @link ExtrudeLimitData::LimitTypeUntilSelectedExtendFace ExtrudeLimitData::LimitTypeUntilSelectedExtendFace@endlink ,
                   @link ExtrudeLimitData::LimitTypeUntilSelected ExtrudeLimitData::LimitTypeUntilSelected@endlink  and
                   @link ExtrudeLimitData::LimitTypeThroughAll ExtrudeLimitData::LimitTypeThroughAll@endlink .
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void GetStartLimit
            (
                NXOpen::NXObject ** selected_object /** */
            );
            /** Gets end limit distance if @link  ExtrudeLimitData::EndLimitType   ExtrudeLimitData::EndLimitType @endlink  is @link ExtrudeLimitData::LimitTypeDistance ExtrudeLimitData::LimitTypeDistance@endlink .
                 @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXString GetEndLimit
            (
            );
            /** Gets end limit data if @link  ExtrudeLimitData::EndLimitType   ExtrudeLimitData::EndLimitType @endlink  is any of following
                   @link ExtrudeLimitData::LimitTypeUntilNext ExtrudeLimitData::LimitTypeUntilNext@endlink ,
                   @link ExtrudeLimitData::LimitTypeUntilSelectedExtendFace ExtrudeLimitData::LimitTypeUntilSelectedExtendFace@endlink ,
                   @link ExtrudeLimitData::LimitTypeUntilSelected ExtrudeLimitData::LimitTypeUntilSelected@endlink  and
                   @link ExtrudeLimitData::LimitTypeThroughAll ExtrudeLimitData::LimitTypeThroughAll@endlink .
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void GetEndLimit
            (
                NXOpen::NXObject ** selected_object /** */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif