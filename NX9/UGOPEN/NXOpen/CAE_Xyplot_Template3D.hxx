#ifndef NXOpen_CAE_XYPLOT_TEMPLATE3D_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_TEMPLATE3D_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_Template3D.ja
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
#include <NXOpen/CAE_Xyplot_BaseTemplate.hxx>
#include <NXOpen/CAE_XyplotDataTypes.hxx>
#include <NXOpen/CAE_Xyplot_SurfaceStyleSetting.hxx>
#include <NXOpen/CAE_Xyplot_Template3D.hxx>
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
            class Template3D;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class BaseTemplate;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class SurfaceStyleSetting;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class _Template3DBuilder;
            class Template3DImpl;

            /// \cond NX_NO_DOC 
            /** Manages the 3D display style  <br> Not support KF.  <br> 
             <br>  Created in NX7.5.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  Template3D : public CAE::Xyplot::BaseTemplate
            {
                private: Template3DImpl * m_template3d_impl;
                private: friend class  _Template3DBuilder;
                protected: Template3D();
                public: ~Template3D();
                /**Returns  the complex option 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::Xyplot::ComplexOption3D ComplexOption
                (
                );
                /**Sets  the complex option 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetComplexOption
                (
                    NXOpen::CAE::Xyplot::ComplexOption3D complexOption /** Complex option */
                );
                /**Returns  the grid layout style 
                 <br>  @deprecated Deprecated in NX9.0.0.  Use @link CAE::Xyplot::BaseTemplate::GridLayoutStyleSetting CAE::Xyplot::BaseTemplate::GridLayoutStyleSetting@endlink  instead. <br>  

                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use CAE::Xyplot::BaseTemplate::GridLayoutStyleSetting instead.") NXOpen::CAE::Xyplot::GridLayout3D GridLayout
                (
                );
                /**Sets  the grid layout style 
                 <br>  @deprecated Deprecated in NX9.0.0.  Use @link CAE::Xyplot::IDisplayStyle::CommitChange CAE::Xyplot::IDisplayStyle::CommitChange@endlink  instead. <br>  

                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use CAE::Xyplot::IDisplayStyle::CommitChange instead.") void SetGridLayout
                (
                    const NXOpen::CAE::Xyplot::GridLayout3D & gridLayout /** Grid layout style */
                );
                /** Gets line style option  @return  Line style option 
                 <br>  @deprecated Deprecated in NX9.0.0.  Use @link CAE::Xyplot::BaseTemplate::GetLineStyleSetting CAE::Xyplot::BaseTemplate::GetLineStyleSetting@endlink  instead. <br>  

                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use CAE::Xyplot::BaseTemplate::GetLineStyleSetting instead.") NXOpen::CAE::Xyplot::LineOption3D GetLineOption
                (
                    int styleIndex /** Style index */
                );
                /** Sets line style option 
                 <br>  @deprecated Deprecated in NX9.0.0.  Use @link CAE::Xyplot::IDisplayStyle::CommitChange CAE::Xyplot::IDisplayStyle::CommitChange@endlink  instead. <br>  

                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use CAE::Xyplot::IDisplayStyle::CommitChange instead.") void SetLineOption
                (
                    int styleIndex /** Style index */,
                    const NXOpen::CAE::Xyplot::LineOption3D & lineOption /** Line style option */
                );
                /** Gets bar style option  @return  Bar style option 
                 <br>  @deprecated Deprecated in NX9.0.0.  Use @link CAE::Xyplot::BaseTemplate::GetBarStyleSetting CAE::Xyplot::BaseTemplate::GetBarStyleSetting@endlink  instead. <br>  

                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use CAE::Xyplot::BaseTemplate::GetBarStyleSetting instead.") NXOpen::CAE::Xyplot::BarOption3D GetBarOption
                (
                    int styleIndex /** Style index */
                );
                /** Sets bar style option 
                 <br>  @deprecated Deprecated in NX9.0.0.  Use @link CAE::Xyplot::IDisplayStyle::CommitChange CAE::Xyplot::IDisplayStyle::CommitChange@endlink  instead. <br>  

                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use CAE::Xyplot::IDisplayStyle::CommitChange instead.") void SetBarOption
                (
                    int styleIndex /** Style index */,
                    const NXOpen::CAE::Xyplot::BarOption3D & barOption /** Bar style option */
                );
                /** Gets plate style option  @return  Plate style option 
                 <br>  @deprecated Deprecated in NX9.0.0.  Use @link CAE::Xyplot::BaseTemplate::GetPlateStyleSetting CAE::Xyplot::BaseTemplate::GetPlateStyleSetting@endlink  instead. <br>  

                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use CAE::Xyplot::BaseTemplate::GetPlateStyleSetting instead.") NXOpen::CAE::Xyplot::PlateOption3D GetPlateOption
                (
                    int styleIndex /** Style index */
                );
                /** Sets plate style option 
                 <br>  @deprecated Deprecated in NX9.0.0.  Use @link CAE::Xyplot::IDisplayStyle::CommitChange CAE::Xyplot::IDisplayStyle::CommitChange@endlink  instead. <br>  

                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use CAE::Xyplot::IDisplayStyle::CommitChange instead.") void SetPlateOption
                (
                    int styleIndex /** Style index */,
                    const NXOpen::CAE::Xyplot::PlateOption3D & plateOption /** Plate style option */
                );
                /** Gets surface style option  @return  Surface style option 
                 <br>  @deprecated Deprecated in NX9.0.0.  Use @link CAE::Xyplot::Template3D::GetSurfaceStyleSetting CAE::Xyplot::Template3D::GetSurfaceStyleSetting@endlink  instead. <br>  

                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use CAE::Xyplot::Template3D::GetSurfaceStyleSetting instead.") NXOpen::CAE::Xyplot::SurfaceOption3D GetSurfaceOption
                (
                    int styleIndex /** Style index */
                );
                /** Sets surface style option 
                 <br>  @deprecated Deprecated in NX9.0.0.  Use @link CAE::Xyplot::IDisplayStyle::CommitChange CAE::Xyplot::IDisplayStyle::CommitChange@endlink  instead. <br>  

                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use CAE::Xyplot::IDisplayStyle::CommitChange instead.") void SetSurfaceOption
                (
                    int styleIndex /** Style index */,
                    const NXOpen::CAE::Xyplot::SurfaceOption3D & surfaceOption /** Surface style option */
                );
                /** Gets the sureface display style setting of a specified index in a 3D graph template  @return  Surface style 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::Xyplot::SurfaceStyleSetting * GetSurfaceStyleSetting
                (
                    int styleIndex /** Style index, from 0 to 19 */
                );
            };

            /// \endcond 
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
