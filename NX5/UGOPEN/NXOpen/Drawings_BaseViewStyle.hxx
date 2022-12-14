#ifndef NXOpen_DRAWINGS_BASEVIEWSTYLE_HXX_INCLUDED
#define NXOpen_DRAWINGS_BASEVIEWSTYLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_BaseViewStyle.ja
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
    namespace Drawings
    {
        class BaseViewStyle;
    }
    namespace Drawings
    {
        class ViewStyle;
    }
    namespace Preferences
    {
        class IBaseViewPreferences;
    }
    namespace Drawings
    {
        /** Represents set of Base View Style Preferences applicable to drafting views. 
              <br> To obtain an instance of this class, refer to @link Drawings::ViewStyle Drawings::ViewStyle@endlink  <br> */
        class NXOPENCPPEXPORT BaseViewStyle: public virtual Preferences::IBaseViewPreferences
        {
            private: NXOpen::Drawings::ViewStyle* m_owner;
            public: explicit BaseViewStyle(NXOpen::Drawings::ViewStyle *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** the status of faceted representation. If True the clipping bounds are inherited, else 
            		    the imported model view is placed on the drawing with an Automatic Rectangular Boundary.
                      <br> License requirements : drafting ("DRAFTING") */
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
            /** Sets the configuration for the arrangement in assembly after an 
                        arrangement part file is loaded.
                      <br> License requirements : drafting ("DRAFTING") */
            public: void SetAssemblyArrangement
            (
                const NXString & config /** name of the configuration for the arrangement  <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** To load the assemblies arrangement part file. If the logical argument is True, 
                        the part would be loaded.
                      <br> License requirements : drafting ("DRAFTING") */
            public: void LoadModelFromPart
            (
                const NXString & load_part_name /** name of the loaded part  <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                bool load_part_toggle /** True or False status for loading the part.*/
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
