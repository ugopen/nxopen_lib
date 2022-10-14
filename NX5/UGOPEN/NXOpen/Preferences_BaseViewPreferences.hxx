#ifndef NXOpen_PREFERENCES_BASEVIEWPREFERENCES_HXX_INCLUDED
#define NXOpen_PREFERENCES_BASEVIEWPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_BaseViewPreferences.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Preferences_IBaseViewPreferences.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class BaseViewPreferences;
    }
    namespace Preferences
    {
        class ViewPreferences;
    }
    namespace Preferences
    {
        class IBaseViewPreferences;
    }
    namespace Preferences
    {
        /** Represents set of Base View Preferences applicable to drafting views. 
                These settings apply to any newly created base view.
              <br> To obtain an instance of this class, refer to @link Preferences::ViewPreferences Preferences::ViewPreferences@endlink  <br> */
        class NXOPENCPPEXPORT BaseViewPreferences: public virtual Preferences::IBaseViewPreferences
        {
            private: NXOpen::Preferences::ViewPreferences* m_owner;
            public: explicit BaseViewPreferences(NXOpen::Preferences::ViewPreferences *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** the status of faceted representation. If True the clipping bounds are inherited, else 
            		    the imported model view is placed on the drawing with an Automatic Rectangular Boundary  <br> License requirements : drafting ("DRAFTING") */
            public: void SetFacetedRepresentation
            (
                bool is_faceted_representation /** is faceted representation */ 
            );
            /** the status of inherit clipping boundary. If True the model view's 
            		    clipping boundary are inherited when model view is imported onto the drawing, else 
            		    the imported model view is placed on the drawing with an Automatic Rectangular Boundary.
            		  <br> License requirements : drafting ("DRAFTING") */
            public: void SetInheritClippingBoundary
            (
                bool is_inherit_clipping_boundary /** Inherit XY clipping boundaries of model */
            );
            /** the status of transfer annotation. Controls whether or not annotations created in 
            		    a model view are transferred to the drawing when a view is imported.
            		  <br> License requirements : drafting ("DRAFTING") */
            public: void SetTransferAnnotation
            (
                bool is_transfer_annotation /** is transfer annotation */ 
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif