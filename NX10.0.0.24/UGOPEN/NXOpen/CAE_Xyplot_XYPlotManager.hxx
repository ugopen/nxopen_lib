#ifndef NXOpen_CAE_XYPLOT_XYPLOTMANAGER_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_XYPLOTMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_XYPlotManager.ja
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
#include <NXOpen/CAE_Xyplot_BaseTemplateManager.hxx>
#include <NXOpen/CAE_Xyplot_OverlayParameters.hxx>
#include <NXOpen/CAE_Xyplot_Plot.hxx>
#include <NXOpen/CAE_Xyplot_PlotParameters.hxx>
#include <NXOpen/CAE_Xyplot_Preference.hxx>
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
            class XYPlotManager;
        }
    }
    class Session;
    namespace CAE
    {
        namespace Xyplot
        {
            class BaseTemplateManager;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class OverlayParameters;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class Plot;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class PlotParameters;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class Preference;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class WindowManager;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class XYPlotManagerImpl;
            /** XYPlot function manager  <br> To obtain an instance of this class use @link NXOpen::Session::XYPlotManager NXOpen::Session::XYPlotManager@endlink .  <br> 
             <br>  Created in NX7.5.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  XYPlotManager
            {
                private: XYPlotManagerImpl * m_xyplotmanager_impl;
                private: NXOpen::Session* m_owner;
                /// \cond NX_NO_DOC 
                public: explicit XYPlotManager(NXOpen::Session *owner);


                /// \endcond 
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 
                public: ~XYPlotManager();
                /** Creates plot with given parameters  @return  Created plot 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::Xyplot::Plot * PlotRecords
                (
                    NXOpen::CAE::Xyplot::PlotParameters * plotParameters /** the plot parameters */
                );
                /** Overlay records with given parameters  @return  Overlayed plot 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::Xyplot::Plot * OverlayRecords
                (
                    NXOpen::CAE::Xyplot::OverlayParameters * overlayParameters /** the overlay parameters */
                );
                /** Gets the current plot on the view port of specific device  @return  Current plot 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::Xyplot::Plot * GetCurrentPlot
                (
                    int deviceIndex /** Device index */,
                    int viewIndex /** View index */
                );
                /** Shows the next plot on the view port of specific device 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void ShowNextPlot
                (
                    int deviceIndex /** Device index */,
                    int viewIndex /** View index */
                );
                /** Shows the previous plot on the view port of specific device 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void ShowPreviousPlot
                (
                    int deviceIndex /** Device index */,
                    int viewIndex /** View index */
                );
                /** Gets the 2D template manager  @return  2D template manager 
                 <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::CAE::Xyplot::XYPlotManager::TemplateManager NXOpen::CAE::Xyplot::XYPlotManager::TemplateManager@endlink  instead. <br>  

                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use NXOpen::CAE::Xyplot::XYPlotManager::TemplateManager instead.") NXOpen::CAE::Xyplot::BaseTemplateManager * GetTemplateManager2d
                (
                );
                /** Gets the 3D template manager  @return  3D template manager 
                 <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::CAE::Xyplot::XYPlotManager::TemplateManager NXOpen::CAE::Xyplot::XYPlotManager::TemplateManager@endlink  instead. <br>  

                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use NXOpen::CAE::Xyplot::XYPlotManager::TemplateManager instead.") NXOpen::CAE::Xyplot::BaseTemplateManager * GetTemplateManager3d
                (
                );
                /**Returns  the preference 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::Xyplot::Preference * Preference
                (
                );
                /** Creates an transient object @link  NXOpen::CAE::Xyplot::PlotParameters   NXOpen::CAE::Xyplot::PlotParameters @endlink  to contain the
                                settings required by creating a plot. The object should be destroyed after plot is created.  @return  the plot parameters object created 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::Xyplot::PlotParameters * NewPlotParameters
                (
                );
                /** Creates an transient object @link  NXOpen::CAE::Xyplot::PlotParameters   NXOpen::CAE::Xyplot::PlotParameters @endlink  to contain the settings
                                required by overlaying new records on a plot. The object should be destroyed after overlaying plot is created.  @return  the overlay parameters object created 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::Xyplot::OverlayParameters * NewOverlayParameters
                (
                );
                /** Gets all window devices on which XY graph could be plotted  @return  Available Plot Winodw Devices 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: std::vector<int> GetAvailableWindowDevices
                (
                );
                /** Gets view count and views for specified window device  @return  the views on window device
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: std::vector<int> GetWindowDevicesViews
                (
                    int windowDevice /**  window index  */
                );
                /** Gets all plots on a view of specified window device  @return  Plots      
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: std::vector<NXOpen::CAE::Xyplot::Plot *> GetPlots
                (
                    int windowDevice /**  Plot index */,
                    int view /**  View index */
                );
                /**Returns  the template manager. 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::Xyplot::BaseTemplateManager * TemplateManager
                (
                );


                /** Returns the @link NXOpen::CAE::Xyplot::WindowManager NXOpen::CAE::Xyplot::WindowManager@endlink  belonging.
                                This class is restricted to being called from a program running during an interactive NX session.
                                If run from a non-interactive session it will return NULL. 
                 <br>  Created in NX9.0.0.  <br>  
                */
                public: NXOpen::CAE::Xyplot::WindowManager *WindowManager();
            }; //lint !e1712 default constructor not defined for class  

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