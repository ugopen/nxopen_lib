#ifndef NXOpen_FACET_FACETEDBODYCOLLECTION_HXX_INCLUDED
#define NXOpen_FACET_FACETEDBODYCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Facet_FacetedBodyCollection.ja
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
#include <NXOpen/Facet_CurvatureBuilder.hxx>
#include <NXOpen/Facet_FeatureExtractionBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Facet
    {
        class FacetedBodyCollection;
    }
    class Part;
    namespace Facet
    {
        class FacetedBody;
    }
    class Body;
    namespace Facet
    {
        class CurvatureBuilder;
    }
    namespace Facet
    {
        class FeatureExtractionBuilder;
    }
    namespace Facet
    {
         /** The structure of JA faceting parameters */

        struct FacetingParameters
        {
            public: /** The maximum number of edges allowed
                                                           in the facets that are to be generated 
                                                           (this does not apply to JT).
                                                        */int MaximumFacetEdges;
            public: /** If this value is true, then
                                                           values must be specified for
                                                           surfaceDistanceTolerance
                                                           and surfaceAngularTolerance. If
                                                           this value is false then values for
                                                           surfaceDistanceTolerance and
                                                           surfaceAngularTolerance will be
                                                           determined by the system based on the
                                                           body box or face box of the solid entity
                                                           being faceted.
                                                        */bool SpecifySurfaceTolerance;
            public: /** This is the maximum distance from
                                                           the surface to the facet.
                                                        */double SurfaceDistanceTolerance;
            public: /** This is the maximum angular variation
                                                           in radians of the surface normal
                                                           over the facet. A value of zero
                                                           indicates no constraint.
                                                        */double SurfaceAngularTolerance;
            public: /** This indicates that values are to be
                                                           specified for curveDistanceTolerance
                                                           and curveAngularTolerance and
                                                           curve_max_length.  If this value is false
                                                           then values for curveDistanceTolerance
                                                           and curveAngularTolerance will be
                                                           determined by the system based on the
                                                           body box or face box of the solid
                                                           entity being faceted, and no restriction
                                                           will be placed on the maximum length
                                                           of curve that can be represented
                                                           by a single facet edge.
                                                        */bool SpecifyCurveTolerance;
            public: /** This is the maximum distance between
                                                           the facet edge and the curve segment
                                                           represented by the facet edge. This
                                                           applies only to those facet edges lying
                                                           along solid edges.
                                                        */double CurveDistanceTolerance;
            public: /** This is the maximum angular variation
                                                           in radians of the curve tangent along
                                                           the curve segment represented by the
                                                           facet edge. This applies only to those
                                                           facet edges lying along solid edges.
                                                           A value of zero indicates no constraint.
                                                        */double CurveAngularTolerance;
            public: /** The maximum length of a curve, default is 1000.0 */double CurveMaximumLength;
            public: /** This indicates that the facets
                                                           generated by the faceter should all be
                                                           convex (this does not apply to JT).
                                                        */bool SpecifyConvexFacets;
            public: /** This indicates that a maximum width of
                                                           facet is to be specified using
                                                           maximumFacetSize. If this field is false
                                                           then no maximum facet size is imposed.
                                                        */bool SpecifyMaximumFacetSize;
            public: /** This is the maximum width of a facet.
                                                           This is only used if
                                                           specifyMaximumFacetSize is true.
                                                        */double MaximumFacetSize;
            public: /** This indicates that the model will be
                                                           created with the parametric information
                                                           for each vertex.  Should parameters at
                                                           the vertices be obtained for the facets
                                                           of the model (this does not apply to JT).
                                                        */bool SpecifyParameters;
            public: /** This indicates whether the real
                                                           numbers for facet vertices and facet
                                                           normals should be stored as floats
                                                           (UF_FACET_TYPE_FLOAT) or as doubles
                                                           (UF_FACET_TYPE_DOUBLE). Note that this
                                                           option applies only when a faceted model
                                                           is being created, and is ignored when the
                                                           model is updated (this does not apply to JT).
                                                        */int NumberStorageType;
            public: /** Should we use a viewing direction
                                                           for denser faceting around
                                                           silhouettes.  The denser faceting will
                                                           honor the tolerance specified by
                                                           silhouetteChordTolerance in the silhouette
                                                           with respect to the view direction
                                                           specified by silhouetteViewDirection vector.
                                                           If this is false, there is no special
                                                           consideration for any silhouette area
                                                           (this does not apply to JT).
                                                        */bool SpecifyViewDirection;
            public: /** If specifyViewDirection is specified,
                                                           then this is the view direction to use
                                                           (this does not apply to JT).
                                                        */NXOpen::Vector3d SilhouetteViewDirection;
            public: /** If specifyViewDirection is specified
                                                           then this is the tolerance which will be
                                                           used as a tighter surface tolerance
                                                           in the silhouette area specified
                                                           by the view direction (this does not apply to JT).
                                                        */double SilhouetteChordTolerance;
            public: /** Should this FACET body record face tags or not 
                                                           (this does not apply to JT). 
                                                        */bool StoreFaceTag;
            public: /** When creating a JT facet body whether to create LODs or not 
                                                           (this does not apply to NX). 
                                                        */bool WithLODS;
            public: FacetingParameters() :
                MaximumFacetEdges(),
                SpecifySurfaceTolerance(),
                SurfaceDistanceTolerance(),
                SurfaceAngularTolerance(),
                SpecifyCurveTolerance(),
                CurveDistanceTolerance(),
                CurveAngularTolerance(),
                CurveMaximumLength(),
                SpecifyConvexFacets(),
                SpecifyMaximumFacetSize(),
                MaximumFacetSize(),
                SpecifyParameters(),
                NumberStorageType(),
                SpecifyViewDirection(),
                SilhouetteViewDirection(),
                SilhouetteChordTolerance(),
                StoreFaceTag(),
                WithLODS()
            {
            }
            /** Constructor for the FacetingParameters struct. */ 
            public: FacetingParameters(int INIT_maximumFacetEdges /** The maximum number of edges allowed
                                                           in the facets that are to be generated 
                                                           (this does not apply to JT).
                                                        */, bool INIT_specifySurfaceTolerance /** If this value is true, then
                                                           values must be specified for
                                                           surfaceDistanceTolerance
                                                           and surfaceAngularTolerance. If
                                                           this value is false then values for
                                                           surfaceDistanceTolerance and
                                                           surfaceAngularTolerance will be
                                                           determined by the system based on the
                                                           body box or face box of the solid entity
                                                           being faceted.
                                                        */, double INIT_surfaceDistanceTolerance /** This is the maximum distance from
                                                           the surface to the facet.
                                                        */, double INIT_surfaceAngularTolerance /** This is the maximum angular variation
                                                           in radians of the surface normal
                                                           over the facet. A value of zero
                                                           indicates no constraint.
                                                        */, bool INIT_specifyCurveTolerance /** This indicates that values are to be
                                                           specified for curveDistanceTolerance
                                                           and curveAngularTolerance and
                                                           curve_max_length.  If this value is false
                                                           then values for curveDistanceTolerance
                                                           and curveAngularTolerance will be
                                                           determined by the system based on the
                                                           body box or face box of the solid
                                                           entity being faceted, and no restriction
                                                           will be placed on the maximum length
                                                           of curve that can be represented
                                                           by a single facet edge.
                                                        */, double INIT_curveDistanceTolerance /** This is the maximum distance between
                                                           the facet edge and the curve segment
                                                           represented by the facet edge. This
                                                           applies only to those facet edges lying
                                                           along solid edges.
                                                        */, double INIT_curveAngularTolerance /** This is the maximum angular variation
                                                           in radians of the curve tangent along
                                                           the curve segment represented by the
                                                           facet edge. This applies only to those
                                                           facet edges lying along solid edges.
                                                           A value of zero indicates no constraint.
                                                        */, double INIT_curveMaximumLength /** The maximum length of a curve, default is 1000.0 */, bool INIT_specifyConvexFacets /** This indicates that the facets
                                                           generated by the faceter should all be
                                                           convex (this does not apply to JT).
                                                        */, bool INIT_specifyMaximumFacetSize /** This indicates that a maximum width of
                                                           facet is to be specified using
                                                           maximumFacetSize. If this field is false
                                                           then no maximum facet size is imposed.
                                                        */, double INIT_maximumFacetSize /** This is the maximum width of a facet.
                                                           This is only used if
                                                           specifyMaximumFacetSize is true.
                                                        */, bool INIT_specifyParameters /** This indicates that the model will be
                                                           created with the parametric information
                                                           for each vertex.  Should parameters at
                                                           the vertices be obtained for the facets
                                                           of the model (this does not apply to JT).
                                                        */, int INIT_numberStorageType /** This indicates whether the real
                                                           numbers for facet vertices and facet
                                                           normals should be stored as floats
                                                           (UF_FACET_TYPE_FLOAT) or as doubles
                                                           (UF_FACET_TYPE_DOUBLE). Note that this
                                                           option applies only when a faceted model
                                                           is being created, and is ignored when the
                                                           model is updated (this does not apply to JT).
                                                        */, bool INIT_specifyViewDirection /** Should we use a viewing direction
                                                           for denser faceting around
                                                           silhouettes.  The denser faceting will
                                                           honor the tolerance specified by
                                                           silhouetteChordTolerance in the silhouette
                                                           with respect to the view direction
                                                           specified by silhouetteViewDirection vector.
                                                           If this is false, there is no special
                                                           consideration for any silhouette area
                                                           (this does not apply to JT).
                                                        */, NXOpen::Vector3d INIT_silhouetteViewDirection /** If specifyViewDirection is specified,
                                                           then this is the view direction to use
                                                           (this does not apply to JT).
                                                        */, double INIT_silhouetteChordTolerance /** If specifyViewDirection is specified
                                                           then this is the tolerance which will be
                                                           used as a tighter surface tolerance
                                                           in the silhouette area specified
                                                           by the view direction (this does not apply to JT).
                                                        */, bool INIT_storeFaceTag /** Should this FACET body record face tags or not 
                                                           (this does not apply to JT). 
                                                        */, bool INIT_withLODS /** When creating a JT facet body whether to create LODs or not 
                                                           (this does not apply to NX). 
                                                        */) :
                MaximumFacetEdges(INIT_maximumFacetEdges),
                SpecifySurfaceTolerance(INIT_specifySurfaceTolerance),
                SurfaceDistanceTolerance(INIT_surfaceDistanceTolerance),
                SurfaceAngularTolerance(INIT_surfaceAngularTolerance),
                SpecifyCurveTolerance(INIT_specifyCurveTolerance),
                CurveDistanceTolerance(INIT_curveDistanceTolerance),
                CurveAngularTolerance(INIT_curveAngularTolerance),
                CurveMaximumLength(INIT_curveMaximumLength),
                SpecifyConvexFacets(INIT_specifyConvexFacets),
                SpecifyMaximumFacetSize(INIT_specifyMaximumFacetSize),
                MaximumFacetSize(INIT_maximumFacetSize),
                SpecifyParameters(INIT_specifyParameters),
                NumberStorageType(INIT_numberStorageType),
                SpecifyViewDirection(INIT_specifyViewDirection),
                SilhouetteViewDirection(INIT_silhouetteViewDirection),
                SilhouetteChordTolerance(INIT_silhouetteChordTolerance),
                StoreFaceTag(INIT_storeFaceTag),
                WithLODS(INIT_withLODS)
            {
            }
        };

    }
    namespace Facet
    {
        /** Represents a collection of faceted bodies in a part  <br> To obtain an instance of this class, refer to @link Part Part@endlink  <br> */
        class NXOPENCPPEXPORT FacetedBodyCollection : public TaggedObjectCollection
        {
            /** Specifies the type of facets created when copying or converting faceted bodies */
            public: enum Type
            {
                TypeNx/** NX facet */,
                TypeJt/** JT facet */
            };

            private: NXOpen::Part* m_owner;
            public: explicit FacetedBodyCollection(NXOpen::Part *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Facet::FacetedBody * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::Facet::FacetedBodyCollection *context) : m_context(context), m_current(NULL_TAG)
                {
                }
                iterator(const iterator &other)
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
                NXOPENCPPEXPORT  value_type operator * ();
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
                NXOPENCPPEXPORT  void next();
                NXOpen::Facet::FacetedBodyCollection *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            /** Returns an iterator addressing the first element. */
            iterator begin();
            /** Returns an iterator addressing the last element. */
            iterator end()
            {
                return iterator(this);
            }
            /** Finds the @link  Facet::FacetedBody   Facet::FacetedBody @endlink  with the given identifier as recorded in a journal. 
                        An object may not return the same value as its JournalIdentifier in different versions of 
                        the software. However newer versions of the software should find the same object when 
                        FindObject is passed older versions of its journal identifier. In general, this method 
                        should not be used in handwritten code and exists to support record and playback of journals.

                        An exception will be thrown if no object can be found with the given journal identifier.  @return  Faceted body with this identifier  <br> License requirements : None */
            public: NXOpen::Facet::FacetedBody * FindObject
            (
                const NXString & journal_identifier /** Identifier of the faceted body you want   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Create a @link Facet::CurvatureBuilder Facet::CurvatureBuilder@endlink  object.  @return   <br> License requirements : None */
            public: NXOpen::Facet::CurvatureBuilder * CreateFacetCurvatureBuilder
            (
            );
            /** Create a @link Facet::FeatureExtractionBuilder Facet::FeatureExtractionBuilder@endlink  object.  @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Facet::FeatureExtractionBuilder * CreateFacetFeatureExtractionBuilder
            (
            );
            /** Converts the internal representation of this faceted body to the specified type. This does not create a new body  <br> License requirements : None */
            public: void Convert
            (
                NXOpen::Facet::FacetedBody * fromBody /** The faceted body to convert */,
                NXOpen::Facet::FacetedBodyCollection::Type toFacetType /** To facet type */
            );
            /** Copies a faceted body and optionally changes the internal representation to the given type
                         (This is only valid for JT to NX copy) 
                      @return  New body  <br> License requirements : None */
            public: NXOpen::Facet::FacetedBody * Copy
            (
                NXOpen::Facet::FacetedBody * fromBody /** The faceted body to copy */,
                NXOpen::Part * toPart /** Part to create the copy in */,
                NXOpen::Facet::FacetedBodyCollection::Type toFacetType /** To facet type */
            );
            /** Returns the loaded solid bodies associated with the argument faceted body.
                        Also returns the number of unloaded associated faceted bodies.
                     @return  Array of loaded associated faceted bodies  <br> License requirements : None */
            public: std::vector<NXOpen::Facet::FacetedBody *> GetAssociatedFacetedBodies
            (
                NXOpen::Body * solidBody /** The body for which to get associated faceted bodies */,
                int* numberOfUnloadedFacetedBodies /** The number of unloaded associated faceted bodies for this solids body */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif