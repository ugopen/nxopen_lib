#ifndef NXOpen_CAE_XYPLOT_BASICMODEL_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_BASICMODEL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_BasicModel.ja
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
#include <NXOpen/CAE_Xyplot_BasicModel.hxx>
#include <NXOpen/CAE_Xyplot_IDisplayableModel.hxx>
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
            class BasicModel;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class IDisplayStyle;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class IDisplayableModel;
        }
    }
    class TaggedObject;
    namespace CAE
    {
        namespace Xyplot
        {
            class _BasicModelBuilder;
            class BasicModelImpl;
            /** Represents a abstract component object on a XY graphing.  <br> Not support KF.  <br> 
             <br>  Created in NX10.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  BasicModel : public NXOpen::TaggedObject, public virtual NXOpen::CAE::Xyplot::IDisplayableModel
            {
                private: BasicModelImpl * m_basicmodel_impl;
                private: friend class  _BasicModelBuilder;
                protected: BasicModel();
                public: ~BasicModel();
                /**Returns  the model display style 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::Xyplot::IDisplayStyle * DisplayStyle
                (
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
                /** Updates model display 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: virtual void UpdateDisplay
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
