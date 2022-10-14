#ifndef NXOpen_CAE_XYPLOT_WINDOWMANAGER_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_WINDOWMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_WindowManager.ja
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
            class WindowManager;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class XYPlotManager;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class WindowManagerImpl;
            /** Manages the separate graphic windows. The value of device index is greater than 0.
                        This class is restricted to being called from a program running during an interactive NX session.
                        If run from a non-interactive session it will return NULL.  <br> To obtain an instance of this class use @link NXOpen::CAE::Xyplot::XYPlotManager::WindowManager NXOpen::CAE::Xyplot::XYPlotManager::WindowManager@endlink .  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  WindowManager
            {
                private: WindowManagerImpl * m_windowmanager_impl;
                private: NXOpen::CAE::Xyplot::XYPlotManager* m_owner;
                /// \cond NX_NO_DOC 
                public: explicit WindowManager(NXOpen::CAE::Xyplot::XYPlotManager *owner);


                /// \endcond 
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 
                public: ~WindowManager();
                /** Creates a new window and returns the device index.  @return   
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: int NewWindow
                (
                );
                /** Closes the window of specified device index. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: void CloseWindow
                (
                    int deviceIndex /** deviceindex */ 
                );
                /** Gets the device indices of all the graphic windows. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<int> GetWindows
                (
                );
                /** Gets the graphics window title. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString GetWindowTitle
                (
                    int deviceIndex /** deviceindex */ 
                );
                /** Sets the graphics window title. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetWindowTitle
                (
                    int deviceIndex /** deviceindex */ ,
                    const NXString & windowTitle /** windowtitle */ 
                );
                /** Sets the graphics window title. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                void SetWindowTitle
                (
                    int deviceIndex /** deviceindex */ ,
                    const char * windowTitle /** windowtitle */ 
                );
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