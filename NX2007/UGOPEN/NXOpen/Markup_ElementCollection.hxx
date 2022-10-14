#ifndef NXOpen_MARKUP_ELEMENTCOLLECTION_HXX_INCLUDED
#define NXOpen_MARKUP_ELEMENTCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Markup_ElementCollection.ja
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
#include <iterator>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Markup_Circle.hxx>
#include <NXOpen/Markup_EditElementDisplayBuilder.hxx>
#include <NXOpen/Markup_Element.hxx>
#include <NXOpen/Markup_ElementBuilder.hxx>
#include <NXOpen/Markup_Ellipse.hxx>
#include <NXOpen/Markup_Freehand.hxx>
#include <NXOpen/Markup_Icon.hxx>
#include <NXOpen/Markup_InsetImage.hxx>
#include <NXOpen/Markup_Line.hxx>
#include <NXOpen/Markup_Polygon.hxx>
#include <NXOpen/Markup_Polyline.hxx>
#include <NXOpen/Markup_Rectangle.hxx>
#include <NXOpen/Markup_Text.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_markup_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Markup
    {
        class ElementCollection;
    }
    namespace Markup
    {
        class Markup;
    }
    namespace Markup
    {
        class Element;
    }
    namespace Markup
    {
        class Circle;
    }
    namespace Markup
    {
        class EditElementDisplayBuilder;
    }
    namespace Markup
    {
        class ElementBuilder;
    }
    namespace Markup
    {
        class Ellipse;
    }
    namespace Markup
    {
        class Freehand;
    }
    namespace Markup
    {
        class Icon;
    }
    namespace Markup
    {
        class InsetImage;
    }
    namespace Markup
    {
        class Line;
    }
    namespace Markup
    {
        class Polygon;
    }
    namespace Markup
    {
        class Polyline;
    }
    namespace Markup
    {
        class Rectangle;
    }
    namespace Markup
    {
        class Text;
    }
    namespace Markup
    {
        class ElementCollectionImpl;
        /** This collects all the markups in the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink   <br> To obtain an instance of this class, refer to @link NXOpen::Markup::Markup  NXOpen::Markup::Markup @endlink  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_MARKUPEXPORT  ElementCollection : public NXOpen::TaggedObjectCollection
        {
            private: ElementCollectionImpl * m_elementcollection_impl;
            private: NXOpen::Markup::Markup* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit ElementCollection(NXOpen::Markup::Markup *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~ElementCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Markup::ElementCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::Markup::Element *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(nullptr), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Markup::ElementCollection *context) : m_context(context), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                }//lint !e1401 m_state is not initialized
                /// \endcond
                /** Copy constructor */
                iterator(const iterator &other): m_context(nullptr), m_current(NULL_TAG)
                {
                    copy(other);
                }
                /** Copy constructor */
                iterator &operator =(const iterator &other)
                {
                    if (&other != this)
                        copy(other);
                    return *this;
                }
                /** Tests if the iterator objects on the left side and the right side of the operator are equal. */
                bool operator ==(const iterator &other) const
                {
                    return m_current == other.m_current && m_context == other.m_context;
                }
                /** Tests if the iterator objects on the left side and the right side of the operator are not equal. */
                bool operator !=(const iterator &other) const
                {
                    return !operator == (other);
                }
                /** Return the element currently pointed to by the iterator. */
                NXOPENCPP_MARKUPEXPORT  value_type operator * () const;
                /** Points the iterator to next element. */
                iterator & operator ++()
                {
                    next();
                    return *this;
                }
                /** Points the iterator to next element. */
                iterator operator ++(int)
                {
                    iterator tmp(*this);
                    ++*this;
                    return tmp;
                }
            private:
                void copy(const iterator &other)
                {
                    m_context = other.m_context;
                    m_current = other.m_current;
                    for (int i = 0; i < sizeof(m_state)/sizeof(m_state[0]); i++)
                         m_state[i] = other.m_state[i];
                }
                NXOPENCPP_MARKUPEXPORT  void next();
                NXOpen::Markup::ElementCollection *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            /** Returns an iterator addressing the first element. */
            iterator begin();
            /** Returns an iterator addressing one past the last element. */
            iterator end()
            {
                return iterator(this);
            }
            /** Finds the @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  with the given id in current markup.
                        An exception will be thrown if no object can be found with given name.  @return  @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  with this id 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Element * FindObject
            (
                const NXString & id /** The id of the @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  */
            );
            /** Finds the @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  with the given id in current markup.
                        An exception will be thrown if no object can be found with given name.  @return  @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  with this id 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            NXOpen::Markup::Element * FindObject
            (
                const char * id /** The id of the @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  */
            );
            /** Creates a pin to screen @link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Circle * CreateCircle
            (
                const NXOpen::Point3d & center /** Point in absolute coordinate */,
                double radius /** radius */ 
            );

            /// \cond NX_NO_DOC 
            /** Creates a pin to screen @link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Circle * CreateCircle
            (
                const NXOpen::Point2d & center /** Point in normalized coordinate */,
                double radius /** radius */ 
            );

            /// \endcond 
            /** Creates a @link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink  with anchor point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Circle * CreateCircle
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const NXOpen::Point3d & center /** Point in absolute coordinate */,
                double radius /** radius */ 
            );

            /// \cond NX_NO_DOC 
            /** Creates a @link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink  with anchor point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Circle * CreateCircle
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const NXOpen::Point2d & center /** Point in normalized coordinate */,
                double radius /** radius */ 
            );

            /// \endcond 
            /** Creates a pin to screen @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Ellipse * CreateEllipse
            (
                const NXOpen::Point3d & center /** Point in absolute coordinate */,
                double major /** major */ ,
                double minor /** minor */ 
            );

            /// \cond NX_NO_DOC 
            /** Creates a pin to screen @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Ellipse * CreateEllipse
            (
                const NXOpen::Point2d & center /** Point in normalized coordinate */,
                double major /** major */ ,
                double minor /** minor */ 
            );

            /// \endcond 
            /** Creates a @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink  with anchor point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Ellipse * CreateEllipse
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const NXOpen::Point3d & center /** Point in absolute coordinate */,
                double major /** major */ ,
                double minor /** minor */ 
            );

            /// \cond NX_NO_DOC 
            /** Creates a @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink  with anchor point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Ellipse * CreateEllipse
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const NXOpen::Point2d & center /** Point in normalized coordinate */,
                double major /** major */ ,
                double minor /** minor */ 
            );

            /// \endcond 
            /** Creates a pin to screen @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Rectangle * CreateRectangle
            (
                const NXOpen::Point3d & center /** Point in absolute coordinate */,
                double length /** length */ ,
                double width /** width */ 
            );

            /// \cond NX_NO_DOC 
            /** Creates a pin to screen @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Rectangle * CreateRectangle
            (
                const NXOpen::Point2d & center /** Point in normalized coordinate */,
                double length /** length */ ,
                double width /** width */ 
            );

            /// \endcond 
            /** Creates a @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink  with anchor point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Rectangle * CreateRectangle
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const NXOpen::Point3d & center /** Point in absolute coordinate */,
                double length /** length */ ,
                double width /** width */ 
            );

            /// \cond NX_NO_DOC 
            /** Creates a @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink  with anchor point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Rectangle * CreateRectangle
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const NXOpen::Point2d & center /** Point in normalized coordinate */,
                double length /** length */ ,
                double width /** width */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a pin to screen @link NXOpen::Markup::Polyline NXOpen::Markup::Polyline@endlink  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Polyline * CreatePolyline
            (
                const std::vector<NXOpen::Point3d> & points /** Points in absolute coordinate */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a pin to screen @link NXOpen::Markup::Polyline NXOpen::Markup::Polyline@endlink  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Polyline * CreatePolyline
            (
                const std::vector<NXOpen::Point2d> & points /** Points in normalized coordinate */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a @link NXOpen::Markup::Polyline NXOpen::Markup::Polyline@endlink  with anchor point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Polyline * CreatePolyline
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const std::vector<NXOpen::Point3d> & points /** Points in absolute coordinate */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a @link NXOpen::Markup::Polyline NXOpen::Markup::Polyline@endlink  with anchor point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Polyline * CreatePolyline
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const std::vector<NXOpen::Point2d> & points /** Points in normalized coordinate */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a pin to screen @link NXOpen::Markup::Polygon NXOpen::Markup::Polygon@endlink  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Polygon * CreatePolygon
            (
                const std::vector<NXOpen::Point3d> & points /** Points in absolute coordinate */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a pin to screen @link NXOpen::Markup::Polygon NXOpen::Markup::Polygon@endlink  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Polygon * CreatePolygon
            (
                const std::vector<NXOpen::Point2d> & points /** Points in normalized coordinate */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a @link NXOpen::Markup::Polygon NXOpen::Markup::Polygon@endlink  with anchor point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Polygon * CreatePolygon
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const std::vector<NXOpen::Point3d> & points /** Points in absolute coordinate */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a @link NXOpen::Markup::Polygon NXOpen::Markup::Polygon@endlink  with anchor point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Polygon * CreatePolygon
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const std::vector<NXOpen::Point2d> & points /** Points in normalized coordinate */
            );

            /// \endcond 
            /** Creates a pin to screen @link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Freehand * CreateFreehand
            (
                const std::vector<NXOpen::Point3d> & points /** Points in absolute coordinate */
            );

            /// \cond NX_NO_DOC 
            /** Creates a pin to screen @link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Freehand * CreateFreehand
            (
                const std::vector<NXOpen::Point2d> & points /** Points in normalized coordinate */
            );

            /// \endcond 
            /** Creates a @link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink  with anchor point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Freehand * CreateFreehand
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const std::vector<NXOpen::Point3d> & points /** Points in absolute coordinate */
            );

            /// \cond NX_NO_DOC 
            /** Creates a @link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink  with anchor point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Freehand * CreateFreehand
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const std::vector<NXOpen::Point2d> & points /** Points in normalized coordinate */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a pin to screen @link NXOpen::Markup::Line NXOpen::Markup::Line@endlink  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Line * CreateFloatLine
            (
                const NXOpen::Point3d & startPoint /** the start point */,
                const NXOpen::Point3d & endPoint /** the end point */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a @link NXOpen::Markup::Line NXOpen::Markup::Line@endlink  with anchor point 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Line * CreateAnchoredLine
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const NXOpen::Point3d & startPoint /** the start point */,
                const NXOpen::Point3d & endPoint /** the end point */
            );

            /// \endcond 
            /** Creates a @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Text * CreateText
            (
                const NXOpen::Point3d & position /** Point in absolute coordinate */,
                const NXString & textContent /** textcontent */ 
            );
            /** Creates a @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            NXOpen::Markup::Text * CreateText
            (
                const NXOpen::Point3d & position /** Point in absolute coordinate */,
                const char * textContent /** textcontent */ 
            );

            /// \cond NX_NO_DOC 
            /** Creates a @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Text * CreateText
            (
                const NXOpen::Point2d & position /** Point in normalized coordinate */,
                const NXString & textContent /** textcontent */ 
            );
            /** Creates a @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            NXOpen::Markup::Text * CreateText
            (
                const NXOpen::Point2d & position /** Point in normalized coordinate */,
                const char * textContent /** textcontent */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a pin to screen @link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Icon * CreateIcon
            (
                const NXOpen::Point3d & position /** Point in absolute coordinate */,
                const NXString & iconName /** iconname */ ,
                NXOpen::Markup::Icon::Size size /** size */ 
            );
            /** Creates a pin to screen @link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            NXOpen::Markup::Icon * CreateIcon
            (
                const NXOpen::Point3d & position /** Point in absolute coordinate */,
                const char * iconName /** iconname */ ,
                NXOpen::Markup::Icon::Size size /** size */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a pin to screen @link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Icon * CreateIcon
            (
                const NXOpen::Point2d & position /** Point in normalized coordinate */,
                const NXString & iconName /** iconname */ ,
                NXOpen::Markup::Icon::Size size /** size */ 
            );
            /** Creates a pin to screen @link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            NXOpen::Markup::Icon * CreateIcon
            (
                const NXOpen::Point2d & position /** Point in normalized coordinate */,
                const char * iconName /** iconname */ ,
                NXOpen::Markup::Icon::Size size /** size */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a @link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink  with anchor point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Icon * CreateIcon
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const NXOpen::Point3d & position /** Point in absolute coordinate */,
                const NXString & iconName /** iconname */ ,
                NXOpen::Markup::Icon::Size size /** size */ 
            );
            /** Creates a @link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink  with anchor point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            NXOpen::Markup::Icon * CreateIcon
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const NXOpen::Point3d & position /** Point in absolute coordinate */,
                const char * iconName /** iconname */ ,
                NXOpen::Markup::Icon::Size size /** size */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a @link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink  with anchor point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::Icon * CreateIcon
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const NXOpen::Point2d & position /** Point in normalized coordinate */,
                const NXString & iconName /** iconname */ ,
                NXOpen::Markup::Icon::Size size /** size */ 
            );
            /** Creates a @link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink  with anchor point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            NXOpen::Markup::Icon * CreateIcon
            (
                const NXOpen::Point3d & anchorPoint /** anchorpoint */ ,
                const NXOpen::Point2d & position /** Point in normalized coordinate */,
                const char * iconName /** iconname */ ,
                NXOpen::Markup::Icon::Size size /** size */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a pin to screen @link NXOpen::Markup::InsetImage NXOpen::Markup::InsetImage@endlink  
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::InsetImage * CreateInsetImage
            (
                const NXOpen::Point3d & position /** Point in absolute coordinate */,
                const NXString & filename /** the image file */
            );
            /** Creates a pin to screen @link NXOpen::Markup::InsetImage NXOpen::Markup::InsetImage@endlink  
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            NXOpen::Markup::InsetImage * CreateInsetImage
            (
                const NXOpen::Point3d & position /** Point in absolute coordinate */,
                const char * filename /** the image file */
            );

            /// \endcond 
            /** Creates a @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink   @return  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::ElementBuilder * CreateElementBuilder
            (
                NXOpen::Markup::Element * annotation /** annotation */ 
            );
            /** Creates a @link NXOpen::Markup::EditElementDisplayBuilder NXOpen::Markup::EditElementDisplayBuilder@endlink   @return  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: NXOpen::Markup::EditElementDisplayBuilder * CreateEditElementDisplayBuilder
            (
                const std::vector<NXOpen::Markup::Element *> & objects /** objects */ 
            );
        }; //lint !e1712 default constructor not defined for class  

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