#ifndef NXOpen_ANNOTATIONS_ASSOCIATIVITY_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_ASSOCIATIVITY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_Associativity.ja
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
#include <NXOpen/Annotations.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class Associativity;
    }
    class NXObject;
    class View;
    namespace Annotations
    {
    }
    namespace Annotations
    {
        class AssociativityImpl;
        /** Represents an associativity object. The associativity object describes
                how an annotation is attached to geometry. The associativities are specified 
                at indices starting with 1. In most cases, the index corresponds to the order in
                which objects are selected to create an annotation. So, the associativity at 
                index 1 specifies first object selectd, the associativity at index 2 specifies second 
                object selected and so on...
                 <br> 
                Dimensions can only have associativities at indices {1, 2, 3}. Please note the following
                special cases for the dimension associativities - <br>         
                 <br> 1. For ordinate dimensions @link Annotations::OrdinateDimension Annotations::OrdinateDimension@endlink , the 
                   associativity at index 1 stores the ordinate origin data. <br> 
                 <br> 2. The associativity at index 3 stores the following - <br> 
                 <br>    A. Fold location for the folded radius dimension <br> 
                 <br>    B. Margin data for the ordinate dimensions <br> 
                 <br> 3. Set the associativities at index 1 when creating chain and baseline dimensions.
                   The associativity at index 2 and 3 are ignored.  <br>  <br> To create a new instance of this class, use @link Annotations::AnnotationManager::NewAssociativity Annotations::AnnotationManager::NewAssociativity@endlink  <br> */
        class NXOPENCPPEXPORT  Associativity : public TransientObject
        {
            private: AssociativityImpl * m_associativity_impl;
            public: explicit Associativity(void *ptr);
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~Associativity();
            /**Returns  the first associativity object  <br> License requirements : None */
            public: NXOpen::NXObject * FirstObject
            (
            );
            /**Sets  the first associativity object  <br> License requirements : None */
            public: void SetFirstObject
            (
                NXOpen::NXObject * object /** New first associativity object */
            );
            /**Returns  the second associativity object, if the annotation is associated to
                        an intersection point.  <br> License requirements : None */
            public: NXOpen::NXObject * SecondObject
            (
            );
            /**Sets  the second associativity object, if the annotation is associated to
                        an intersection point.  <br> License requirements : None */
            public: void SetSecondObject
            (
                NXOpen::NXObject * object2 /** New second associativity object */
            );
            /**Returns  the object view. Both the associativity objects must have the same view.  <br> License requirements : None */
            public: NXOpen::View * ObjectView
            (
            );
            /**Sets  the object view. Both the associativity objects must have the same view.  <br> License requirements : None */
            public: void SetObjectView
            (
                NXOpen::View * objectView /** New object view */
            );
            /**Returns  the pick point  <br> License requirements : None */
            public: NXOpen::Point3d PickPoint
            (
            );
            /**Sets  the pick point  <br> License requirements : None */
            public: void SetPickPoint
            (
                const NXOpen::Point3d & pickPoint /** New pick point in absolute coordinates */
            );
            /**Returns  the point option  <br> License requirements : None */
            public: NXOpen::Annotations::AssociativityPointOption PointOption
            (
            );
            /**Sets  the point option  <br> License requirements : None */
            public: void SetPointOption
            (
                NXOpen::Annotations::AssociativityPointOption pointOption /** New point option */
            );
            /**Returns  the line option  <br> License requirements : None */
            public: NXOpen::Annotations::AssociativityLineOption LineOption
            (
            );
            /**Sets  the line option  <br> License requirements : None */
            public: void SetLineOption
            (
                NXOpen::Annotations::AssociativityLineOption lineOption /** New line option */
            );
            /**Returns  the first definition point. Required for following line options -
                        @link Annotations::AssociativityLineOptionPointVector Annotations::AssociativityLineOptionPointVector@endlink   <br> License requirements : None */
            public: NXOpen::Point3d FirstDefinitionPoint
            (
            );
            /**Sets  the first definition point. Required for following line options -
                        @link Annotations::AssociativityLineOptionPointVector Annotations::AssociativityLineOptionPointVector@endlink   <br> License requirements : None */
            public: void SetFirstDefinitionPoint
            (
                const NXOpen::Point3d & firstDefinitionPoint /** New first definition point in absolute coordinates */
            );
            /**Returns  the second definition point. Required for following line options -
                        @link Annotations::AssociativityLineOptionPointVector Annotations::AssociativityLineOptionPointVector@endlink   <br> License requirements : None */
            public: NXOpen::Point3d SecondDefinitionPoint
            (
            );
            /**Sets  the second definition point. Required for following line options -
                        @link Annotations::AssociativityLineOptionPointVector Annotations::AssociativityLineOptionPointVector@endlink   <br> License requirements : None */
            public: void SetSecondDefinitionPoint
            (
                const NXOpen::Point3d & secondDefinitionPoint /** New second definition point in absolute coordinates */
            );
            /**Returns  the angle. Required for following line option -
                        @link Annotations::AssociativityLineOptionAngle Annotations::AssociativityLineOptionAngle@endlink   <br> License requirements : None */
            public: double Angle
            (
            );
            /**Sets  the angle. Required for following line option -
                        @link Annotations::AssociativityLineOptionAngle Annotations::AssociativityLineOptionAngle@endlink   <br> License requirements : None */
            public: void SetAngle
            (
                double angle /** New angle in radians */
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
