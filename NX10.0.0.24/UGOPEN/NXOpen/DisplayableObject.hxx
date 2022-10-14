#ifndef NXOpen_DISPLAYABLEOBJECT_HXX_INCLUDED
#define NXOpen_DISPLAYABLEOBJECT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     DisplayableObject.ja
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
#include <NXOpen/IFitTo.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class DisplayableObject;
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class IFitTo;
    class INXObject;
    class NXObject;
    class _DisplayableObjectBuilder;
    class DisplayableObjectImpl;
    /** Base class for all objects that are displayable.  <br> This is an abstract class, and cannot be instantiated.  <br> 
     <br>  Created in NX3.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  DisplayableObject : public NXOpen::NXObject, public virtual NXOpen::IFitTo
    {
        /** specifies object width for objects such as lines and text 
         <br>  Created in NX3.0.0.  <br>  
        */
        public: enum ObjectWidth
        {
            ObjectWidthNormal/** normal */ ,
            ObjectWidthThick/** thick */ ,
            ObjectWidthThin/** thin */ ,
            ObjectWidthOne = 5/** one */ ,
            ObjectWidthTwo/** two */ ,
            ObjectWidthThree/** three */ ,
            ObjectWidthFour/** four */ ,
            ObjectWidthFive/** five */ ,
            ObjectWidthSix/** six */ ,
            ObjectWidthSeven/** seven */ ,
            ObjectWidthEight/** eight */ ,
            ObjectWidthNine/** nine */ 
        };

        /** specifies the object font for objects such as lines 
         <br>  Created in NX3.0.0.  <br>  
        */
        public: enum ObjectFont
        {
            ObjectFontSolid = 1/** solid */ ,
            ObjectFontDashed/** dashed */ ,
            ObjectFontPhantom/** phantom */ ,
            ObjectFontCenterline/** centerline */ ,
            ObjectFontDotted/** dotted */ ,
            ObjectFontLongDashed/** long dashed */ ,
            ObjectFontDottedDashed/** dotted dashed */ 
        };

        private: DisplayableObjectImpl * m_displayableobject_impl;
        private: friend class  _DisplayableObjectBuilder;
        protected: DisplayableObject();
        public: ~DisplayableObject();
        /** Blanks the object. 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void Blank
        (
        );
        /** Unblanks the object. 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void Unblank
        (
        );
        /**Returns  the blank status of this object. 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: bool IsBlanked
        (
        );
        /** Highlights the object. 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void Highlight
        (
        );
        /** Unhighlights the object. 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void Unhighlight
        (
        );
        /**Returns  the color of the object. After setting the color, you must call
                @link RedisplayObject RedisplayObject@endlink  in order for the change to take effect.
                There is a more efficient way to change the color, layer, line font or
                line width of a object. First call
                @link NXOpen::DisplayManager::NewDisplayModification NXOpen::DisplayManager::NewDisplayModification@endlink  and
                then call any combination of set methods for the properties
                @link NXOpen::DisplayModification::NewColor NXOpen::DisplayModification::NewColor @endlink and @link NXOpen::DisplayModification::SetNewColor NXOpen::DisplayModification::SetNewColor @endlink ,
                @link NXOpen::DisplayModification::NewWidth NXOpen::DisplayModification::NewWidth @endlink and @link NXOpen::DisplayModification::SetNewWidth NXOpen::DisplayModification::SetNewWidth @endlink ,
                @link NXOpen::DisplayModification::NewFont NXOpen::DisplayModification::NewFont @endlink and @link NXOpen::DisplayModification::SetNewFont NXOpen::DisplayModification::SetNewFont @endlink 
                and @link NXOpen::DisplayModification::NewLayer NXOpen::DisplayModification::NewLayer @endlink and @link NXOpen::DisplayModification::SetNewLayer NXOpen::DisplayModification::SetNewLayer @endlink . Finally call
                @link NXOpen::DisplayModification::Apply NXOpen::DisplayModification::Apply@endlink  and
                @link TransientObject::Dispose TransientObject::Dispose@endlink .
                This eliminates the need to call @link RedisplayObject RedisplayObject@endlink .

                NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                      If it is, the changes will be overridden when the part is updated. 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: int Color
        (
        );
        /**Returns  the layer that the object is in.  After setting the layer, you must call
                @link RedisplayObject RedisplayObject@endlink  in order for the change to take effect,
                except see the comments for @link NXOpen::DisplayableObject::Color NXOpen::DisplayableObject::Color @endlink and @link NXOpen::DisplayableObject::SetColor NXOpen::DisplayableObject::SetColor @endlink .

                NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                      If it is, the changes will be overridden when the part is updated. 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: int Layer
        (
        );
        /**Returns  the line font of the object. After setting the line font, you must call
                @link RedisplayObject RedisplayObject@endlink  in order for the change to take effect,
                except see the comments for @link NXOpen::DisplayableObject::Color NXOpen::DisplayableObject::Color @endlink and @link NXOpen::DisplayableObject::SetColor NXOpen::DisplayableObject::SetColor @endlink .

                NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                      If it is, the changes will be overridden when the part is updated. 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::DisplayableObject::ObjectFont LineFont
        (
        );
        /**Returns  the line width of the object.  After setting the line width, you must call
                @link RedisplayObject RedisplayObject@endlink  in order for the change to take effect,
                except see the comments for @link NXOpen::DisplayableObject::Color NXOpen::DisplayableObject::Color @endlink and @link NXOpen::DisplayableObject::SetColor NXOpen::DisplayableObject::SetColor @endlink .

                NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                      If it is, the changes will be overridden when the part is updated. 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::DisplayableObject::ObjectWidth LineWidth
        (
        );
        /** Sets the location of the object's name.
                NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
                      If it is, the changes will be overridden when the part is updated. 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void SetNameLocation
        (
            const NXOpen::Point3d & location /** location */ 
        );
        /**Returns  the location of the object's name. 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Point3d NameLocation
        (
        );
        /**Sets  the color of the object. After setting the color, you must call
                @link RedisplayObject RedisplayObject@endlink  in order for the change to take effect.
                There is a more efficient way to change the color, layer, line font or
                line width of a object. First call
                @link NXOpen::DisplayManager::NewDisplayModification NXOpen::DisplayManager::NewDisplayModification@endlink  and
                then call any combination of set methods for the properties
                @link NXOpen::DisplayModification::NewColor NXOpen::DisplayModification::NewColor @endlink and @link NXOpen::DisplayModification::SetNewColor NXOpen::DisplayModification::SetNewColor @endlink ,
                @link NXOpen::DisplayModification::NewWidth NXOpen::DisplayModification::NewWidth @endlink and @link NXOpen::DisplayModification::SetNewWidth NXOpen::DisplayModification::SetNewWidth @endlink ,
                @link NXOpen::DisplayModification::NewFont NXOpen::DisplayModification::NewFont @endlink and @link NXOpen::DisplayModification::SetNewFont NXOpen::DisplayModification::SetNewFont @endlink 
                and @link NXOpen::DisplayModification::NewLayer NXOpen::DisplayModification::NewLayer @endlink and @link NXOpen::DisplayModification::SetNewLayer NXOpen::DisplayModification::SetNewLayer @endlink . Finally call
                @link NXOpen::DisplayModification::Apply NXOpen::DisplayModification::Apply@endlink  and
                @link TransientObject::Dispose TransientObject::Dispose@endlink .
                This eliminates the need to call @link RedisplayObject RedisplayObject@endlink .

                NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                      If it is, the changes will be overridden when the part is updated. 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: void SetColor
        (
            int color /** color */ 
        );
        /**Sets  the layer that the object is in.  After setting the layer, you must call
                @link RedisplayObject RedisplayObject@endlink  in order for the change to take effect,
                except see the comments for @link NXOpen::DisplayableObject::Color NXOpen::DisplayableObject::Color @endlink and @link NXOpen::DisplayableObject::SetColor NXOpen::DisplayableObject::SetColor @endlink .

                NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                      If it is, the changes will be overridden when the part is updated. 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: void SetLayer
        (
            int layer /** layer */ 
        );
        /**Sets  the line font of the object. After setting the line font, you must call
                @link RedisplayObject RedisplayObject@endlink  in order for the change to take effect,
                except see the comments for @link NXOpen::DisplayableObject::Color NXOpen::DisplayableObject::Color @endlink and @link NXOpen::DisplayableObject::SetColor NXOpen::DisplayableObject::SetColor @endlink .

                NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                      If it is, the changes will be overridden when the part is updated. 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: void SetLineFont
        (
            NXOpen::DisplayableObject::ObjectFont font /** font */ 
        );
        /**Sets  the line width of the object.  After setting the line width, you must call
                @link RedisplayObject RedisplayObject@endlink  in order for the change to take effect,
                except see the comments for @link NXOpen::DisplayableObject::Color NXOpen::DisplayableObject::Color @endlink and @link NXOpen::DisplayableObject::SetColor NXOpen::DisplayableObject::SetColor @endlink .

                NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                      If it is, the changes will be overridden when the part is updated. 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: void SetLineWidth
        (
            NXOpen::DisplayableObject::ObjectWidth width /** width */ 
        );
        /** Redisplays the object in all views. Typically this is used to display
            an object after its creation. 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: void RedisplayObject
        (
        );
        /** Remove dependency on all views from an object. 
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveViewDependency
        (
        );
    };
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