#ifndef NXOpen_CAE_XYPLOT_AXISSTYLESETTING_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_AXISSTYLESETTING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_AxisStyleSetting.ja
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
#include <NXOpen/CAE_XyplotDataTypes.hxx>
#include <NXOpen/CAE_Xyplot_AxisStyleSetting.hxx>
#include <NXOpen/CAE_Xyplot_IDisplayStyle.hxx>
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
        namespace Xyplot
        {
            class AxisStyleSetting;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class IDisplayStyle;
        }
    }
    class TaggedObject;
    namespace CAE
    {
        namespace Xyplot
        {
            class _AxisStyleSettingBuilder;
            class AxisStyleSettingImpl;
            /** Represents the axis display style. Call @link CAE::Xyplot::IDisplayStyle::CommitChange CAE::Xyplot::IDisplayStyle::CommitChange@endlink 
                        to apply style changes to corresponding plot after it's modified.
                     <br> Not support KF.  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  AxisStyleSetting : public NXOpen::TaggedObject, public virtual NXOpen::CAE::Xyplot::IDisplayStyle
            {
                private: AxisStyleSettingImpl * m_axisstylesetting_impl;
                private: friend class  _AxisStyleSettingBuilder;
                protected: AxisStyleSetting();
                public: ~AxisStyleSetting();
                /**Returns  the axis scale type 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::AxisType AxisType
                (
                );
                /**Sets  the axis scale type 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetAxisType
                (
                    NXOpen::CAE::Xyplot::AxisType axisType /** axistype */ 
                );
                /**Returns  the dB reference value for a dB axis type. Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType @endlink and @link CAE::Xyplot::AxisStyleSetting::SetAxisType CAE::Xyplot::AxisStyleSetting::SetAxisType @endlink 
                                is @link CAE::Xyplot::AxisTypeDb CAE::Xyplot::AxisTypeDb@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: double DbRef
                (
                );
                /**Sets  the dB reference value for a dB axis type. Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType @endlink and @link CAE::Xyplot::AxisStyleSetting::SetAxisType CAE::Xyplot::AxisStyleSetting::SetAxisType @endlink 
                                is @link CAE::Xyplot::AxisTypeDb CAE::Xyplot::AxisTypeDb@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetDbRef
                (
                    double dbRef /** dbref */ 
                );
                /**Returns  the dB scale. Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType @endlink and @link CAE::Xyplot::AxisStyleSetting::SetAxisType CAE::Xyplot::AxisStyleSetting::SetAxisType @endlink 
                                is @link CAE::Xyplot::AxisTypeDb CAE::Xyplot::AxisTypeDb@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::AxisDBScale DbScale
                (
                );
                /**Sets  the dB scale. Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType @endlink and @link CAE::Xyplot::AxisStyleSetting::SetAxisType CAE::Xyplot::AxisStyleSetting::SetAxisType @endlink 
                                is @link CAE::Xyplot::AxisTypeDb CAE::Xyplot::AxisTypeDb@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetDbScale
                (
                    NXOpen::CAE::Xyplot::AxisDBScale dbScale /** dbscale */ 
                );
                /**Returns  the number of Log decades to display. Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType @endlink and @link CAE::Xyplot::AxisStyleSetting::SetAxisType CAE::Xyplot::AxisStyleSetting::SetAxisType @endlink 
                                is @link CAE::Xyplot::AxisTypeLog CAE::Xyplot::AxisTypeLog@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: int LogDecades
                (
                );
                /**Sets  the number of Log decades to display. Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType @endlink and @link CAE::Xyplot::AxisStyleSetting::SetAxisType CAE::Xyplot::AxisStyleSetting::SetAxisType @endlink 
                                is @link CAE::Xyplot::AxisTypeLog CAE::Xyplot::AxisTypeLog@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetLogDecades
                (
                    int logDecades /** logdecades */ 
                );
                /**Returns  the number of dB decades to display. Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType @endlink and @link CAE::Xyplot::AxisStyleSetting::SetAxisType CAE::Xyplot::AxisStyleSetting::SetAxisType @endlink 
                                is @link CAE::Xyplot::AxisTypeDb CAE::Xyplot::AxisTypeDb@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: int DbDecades
                (
                );
                /**Sets  the number of dB decades to display. Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType @endlink and @link CAE::Xyplot::AxisStyleSetting::SetAxisType CAE::Xyplot::AxisStyleSetting::SetAxisType @endlink 
                                is @link CAE::Xyplot::AxisTypeDb CAE::Xyplot::AxisTypeDb@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetDbDecades
                (
                    int dbDecades /** dbdecades */ 
                );
                /**Returns  the round value to display. It is a percent value. Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType @endlink and @link CAE::Xyplot::AxisStyleSetting::SetAxisType CAE::Xyplot::AxisStyleSetting::SetAxisType @endlink 
                                is not @link CAE::Xyplot::AxisTypeAuto CAE::Xyplot::AxisTypeAuto@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: int GraphOverhead
                (
                );
                /**Sets  the round value to display. It is a percent value. Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType @endlink and @link CAE::Xyplot::AxisStyleSetting::SetAxisType CAE::Xyplot::AxisStyleSetting::SetAxisType @endlink 
                                is not @link CAE::Xyplot::AxisTypeAuto CAE::Xyplot::AxisTypeAuto@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetGraphOverhead
                (
                    int graphOverhead /** graphoverhead */ 
                );
                /**Returns  the unit system 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::UnitSystem UnitSystem
                (
                );
                /**Sets  the unit system 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetUnitSystem
                (
                    NXOpen::CAE::Xyplot::UnitSystem unitSystem /** unitsystem */ 
                );
                /** Finds the @link  NXObject   NXObject @endlink  with the given identifier as recorded in a journal. 
                            An object may not return the same value as its JournalIdentifier in different versions of 
                            the software. However newer versions of the software should find the same object when 
                            FindObject is passed older versions of its journal identifier. In general, this method 
                            should not be used in handwritten code and exists to support record and playback of journals.

                            An exception will be thrown if no object can be found with the given journal identifier.  @return  
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::TaggedObject * Find
                (
                    const NXString & journalIdentifier /** Journal identifier of the object */
                );
                /** Finds the @link  NXObject   NXObject @endlink  with the given identifier as recorded in a journal. 
                            An object may not return the same value as its JournalIdentifier in different versions of 
                            the software. However newer versions of the software should find the same object when 
                            FindObject is passed older versions of its journal identifier. In general, this method 
                            should not be used in handwritten code and exists to support record and playback of journals.

                            An exception will be thrown if no object can be found with the given journal identifier.  @return  
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                NXOpen::TaggedObject * Find
                (
                    const char * journalIdentifier /** Journal identifier of the object */
                );
                /** Commits any edits that have been applied to the display style.
                                Triggers the corresponding plot to update graph. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: virtual void CommitChange
                (
                );
                /**Returns  the owner style 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::Xyplot::IDisplayStyle * Owner
                (
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
