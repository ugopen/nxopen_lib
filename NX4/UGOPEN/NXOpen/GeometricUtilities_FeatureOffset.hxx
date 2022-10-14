#ifndef NXOpen_GEOMETRICUTILITIES_FEATUREOFFSET_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_FEATUREOFFSET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_FeatureOffset.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/GeometricUtilities_Limits.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricUtilities
    {
        class FeatureOffset;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        /** This enum represents the kind of offset */
        enum Type
        {
            TypeNoOffset/** No offset */,
            TypeNonsymmetricOffset/** Offset with two different distances */,
            TypeSymmetricOffset/** Offset with same distance in both directions */,
            TypeSingleOffset/** Offset with single distance in one direction */
        };

    }
    namespace GeometricUtilities
    {
        class _FeatureOffsetBuilder;
        /** Represents a Offset . 
            */
        class NXOPENCPPEXPORT FeatureOffset : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: friend class  _FeatureOffsetBuilder;
            protected: FeatureOffset();
            /** The Start Offset
            		 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetStartOffset
            (
                const NXString & value_expression /** value of start offset expression   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** The End Offset
            		 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetEndOffset
            (
                const NXString & value_expression /** value of end offset expression   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the Start Offset
            		 <br> License requirements : None */
            public: NXOpen::Expression * StartOffset
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link StartOffset() StartOffset@endlink instead.
            @deprecated
            */
            public: NXOpen::Expression * GetStartOffset
            (
            ) { return this->StartOffset(); }
            /**Returns  the End Offset
            		 <br> License requirements : None */
            public: NXOpen::Expression * EndOffset
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link EndOffset() EndOffset@endlink instead.
            @deprecated
            */
            public: NXOpen::Expression * GetEndOffset
            (
            ) { return this->EndOffset(); }
            /**Sets  the Offset Option. 
                         <br> 
                        This is deprecated. Please use @link FeatureOffset::OffsetTypeFeatureOffset::OffsetType @endlink and @link FeatureOffset::SetOffsetTypeFeatureOffset::SetOffsetType @endlink  instead.	
                         <br> 
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetOffsetOption
            (
                NXOpen::GeometricUtilities::Limits::LimitOption limit_opt /**  offset option */
            );
            /**Returns  the Offset Option. 
                         <br> 
                        This is deprecated. Please use @link FeatureOffset::OffsetTypeFeatureOffset::OffsetType @endlink and @link FeatureOffset::SetOffsetTypeFeatureOffset::SetOffsetType @endlink  instead.	
                         <br> 
                     <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Limits::LimitOption OffsetOption
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link OffsetOption() OffsetOption@endlink instead.
            @deprecated
            */
            public: NXOpen::GeometricUtilities::Limits::LimitOption GetOffsetOption
            (
            ) { return this->OffsetOption(); }
            /**Sets  the Offset type
            		 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetOffsetType
            (
                NXOpen::GeometricUtilities::Type offset_type /** offset type */
            );
            /**Returns  the Offset type
            		 <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Type OffsetType
            (
            );
            /** Validate Self
                 @return  Was self validation successful  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif