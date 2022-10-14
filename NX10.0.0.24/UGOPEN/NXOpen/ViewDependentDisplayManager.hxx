#ifndef NXOpen_VIEWDEPENDENTDISPLAYMANAGER_HXX_INCLUDED
#define NXOpen_VIEWDEPENDENTDISPLAYMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ViewDependentDisplayManager.ja
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
    class ViewDependentDisplayManager;
    class View;
    class DisplayableObject;
    class NXColor;
    class ViewDependentDisplayManagerImpl;
    /** Represents all view dependent display operations  <br> To obtain an instance of this class, refer to @link NXOpen::View  NXOpen::View @endlink  <br> 
     <br>  Created in NX5.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  ViewDependentDisplayManager
    {
        /** specifies the font for wireframe edits 
         <br>  Created in NX5.0.0.  <br>  
        */
        public: enum Font
        {
            FontInvisible/** invisible */ ,
            FontSolid/** solid */ ,
            FontDashed/** dashed */ ,
            FontPhantom/** phantom */ ,
            FontCenterline/** centerline */ ,
            FontDotted/** dotted */ ,
            FontLongDashed/** long dashed */ ,
            FontDottedDashed/** dotted dashed */ ,
            FontObject/** object */ 
        };

        /** specifies the width for wireframe edits 
         <br>  Created in NX5.0.0.  <br>  
        */
        public: enum Width
        {
            WidthNormal/** normal */ ,
            WidthThick/** thick */ ,
            WidthThin/** thin */ ,
            WidthObject/** object */ ,
            WidthOne = 5/** one */ ,
            WidthTwo/** two */ ,
            WidthThree/** three */ ,
            WidthFour/** four */ ,
            WidthFive/** five */ ,
            WidthSix/** six */ ,
            WidthSeven/** seven */ ,
            WidthEight/** eight */ ,
            WidthNine/** nine */ 
        };

        /** specifies the partial shading options for shading edits 
         <br>  Created in NX5.0.0.  <br>  
        */
        public: enum PartialShading
        {
            PartialShadingNoChange/** no change */ ,
            PartialShadingOriginal/** original */ ,
            PartialShadingNo/** no */ ,
            PartialShadingYes/** yes */ 
        };

        /** specifies the translucency options for shading edits 
         <br>  Created in NX5.0.0.  <br>  
        */
        public: enum Translucency
        {
            TranslucencyNoChange/** no change */ ,
            TranslucencyOriginal/** original */ ,
            TranslucencyYes/** yes */ 
        };

        private: ViewDependentDisplayManagerImpl * m_viewdependentdisplaymanager_impl;
        private: NXOpen::View* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit ViewDependentDisplayManager(NXOpen::View *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~ViewDependentDisplayManager();
        /** Applies a shading edit to specified faces and/or bodies in a view. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void ApplyShadeEdit
        (
            NXOpen::NXColor * shadeColor /** shade color */ ,
            NXOpen::ViewDependentDisplayManager::PartialShading partialShading /** partial shading */ ,
            NXOpen::ViewDependentDisplayManager::Translucency translucencyOption /** translucency option */ ,
            int translucencyScale /** new translucency value in the range 0 to 100 */,
            const std::vector<NXOpen::DisplayableObject *> & objects /** objects */ 
        );
        /** Applies a shading edit to specified faces and/or bodies in a view when
                shade color is original color 
         <br>  Created in NX6.0.3.  <br>  
         <br> License requirements : None */
        public: void ApplyShadeEdit
        (
            NXOpen::ViewDependentDisplayManager::PartialShading partialShading /** partial shading */ ,
            NXOpen::ViewDependentDisplayManager::Translucency translucencyOption /** translucency option */ ,
            int translucencyScale /** new translucency value in the range 0 to 100 */,
            const std::vector<NXOpen::DisplayableObject *> & objects /** objects */ 
        );
        /** Applies a wireframe edit to specified objects in a view. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void ApplyWireframeEdit
        (
            NXOpen::NXColor * color /** color */ ,
            NXOpen::ViewDependentDisplayManager::Font font /** font */ ,
            NXOpen::ViewDependentDisplayManager::Width width /** width */ ,
            const std::vector<NXOpen::DisplayableObject *> & objects /** objects */ 
        );
        /** Applies a wireframe edit to specified objects in a view
                when the color is the original color 
         <br>  Created in NX6.0.3.  <br>  
         <br> License requirements : None */
        public: void ApplyWireframeEdit
        (
            NXOpen::ViewDependentDisplayManager::Font font /** font */ ,
            NXOpen::ViewDependentDisplayManager::Width width /** width */ ,
            const std::vector<NXOpen::DisplayableObject *> & objects /** objects */ 
        );
        /** Applies a wireframe edit to specified objects in a view. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void ApplySegmentEdit
        (
            NXOpen::DisplayableObject * object /** object */ ,
            NXOpen::NXColor * color /** color */ ,
            NXOpen::ViewDependentDisplayManager::Font font /** font */ ,
            NXOpen::ViewDependentDisplayManager::Width width /** width */ ,
            const std::vector<double> & segmentStart /** The length of the segment_start and segment_end arrays must match. */,
            const std::vector<double> & segmentEnd /** The length of the segment_start and segment_end arrays must match. */
        );
        /** Applies a wireframe edit to specified objects in a view
                when the color is the original color 
         <br>  Created in NX6.0.3.  <br>  
         <br> License requirements : None */
        public: void ApplySegmentEdit
        (
            NXOpen::DisplayableObject * object /** object */ ,
            NXOpen::ViewDependentDisplayManager::Font font /** font */ ,
            NXOpen::ViewDependentDisplayManager::Width width /** width */ ,
            const std::vector<double> & segmentStart /** The length of the segment_start and segment_end arrays must match. */,
            const std::vector<double> & segmentEnd /** The length of the segment_start and segment_end arrays must match. */
        );
        /** Erases specified objects in a view. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void Erase
        (
            const std::vector<NXOpen::DisplayableObject *> & objects /** objects */ 
        );
        /** Removes erasures from specified objects in a view. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveErasure
        (
            const std::vector<NXOpen::DisplayableObject *> & objects /** objects */ 
        );
        /** Removes edits from specified objects in a view. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveEdit
        (
            const std::vector<NXOpen::DisplayableObject *> & objects /** objects */ 
        );
        /** Removes all edits and erasures from all objects in a view. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveAllEdits
        (
        );
        /** Moves view objects to model. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void MoveToModel
        (
            const std::vector<NXOpen::DisplayableObject *> & objects /** objects */ 
        );
        /** Moves model objects to view. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void MoveToView
        (
            const std::vector<NXOpen::DisplayableObject *> & objects /** objects */ 
        );
        /** Sets visibility of background objects. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetBackground
        (
            const std::vector<NXOpen::DisplayableObject *> & objects /** objects */ 
        );
    }; //lint !e1712 default constructor not defined for class  

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