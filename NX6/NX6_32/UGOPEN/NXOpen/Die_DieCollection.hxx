#ifndef NXOpen_DIE_DIECOLLECTION_HXX_INCLUDED
#define NXOpen_DIE_DIECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_DieCollection.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Die
    {
        class DieCollection;
    }
    namespace Features
    {
        class FeatureCollection;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Die
    {
        class AddSurfBuilder;
    }
    namespace Die
    {
        class CastRelief;
    }
    namespace Die
    {
        class CastReliefBuilder;
    }
    namespace Die
    {
        class ClampingSlot;
    }
    namespace Die
    {
        class ClampingSlotBuilder;
    }
    namespace Die
    {
        class CompensateRoughDataBuilder;
    }
    namespace Die
    {
        class DieAttributesBuilder;
    }
    namespace Die
    {
        class DieBooleanBuilder;
    }
    namespace Die
    {
        class DieDirectionBuilder;
    }
    namespace Die
    {
        class DieLocationBuilder;
    }
    namespace Die
    {
        class DieLocationsBuilder;
    }
    namespace Die
    {
        class DiePlaneBuilder;
    }
    namespace Die
    {
        class DieShoe;
    }
    namespace Die
    {
        class DieShoeBuilder;
    }
    namespace Die
    {
        class DrawDiePunchBuilder;
    }
    namespace Die
    {
        class FaceSheetBuilder;
    }
    namespace Die
    {
        class FillBuilder;
    }
    namespace Die
    {
        class FlangeTaskBuilder;
    }
    namespace Die
    {
        class FormTaskBuilder;
    }
    namespace Die
    {
        class Heelpost;
    }
    namespace Die
    {
        class HeelpostBuilder;
    }
    namespace Die
    {
        class Keyway;
    }
    namespace Die
    {
        class KeywayBuilder;
    }
    namespace Die
    {
        class LineupBuilder;
    }
    namespace Die
    {
        class OutputCurvesBuilder;
    }
    namespace Die
    {
        class PierceTaskBuilder;
    }
    namespace Die
    {
        class QuickBinderWrapBuilder;
    }
    namespace Die
    {
        class RotorBuilder;
    }
    namespace Die
    {
        class SteelInsertBuilder;
    }
    namespace Die
    {
        class TrimFlangeDieAssistantBuilder;
    }
    namespace Die
    {
        class TrimLineDevelopmentBuilder;
    }
    namespace Die
    {
        class TrimTaskBuilder;
    }
    namespace Features
    {
        class CompensateRoughData;
    }
    namespace Die
    {
        /** Represents a Die Engineering/Design feature builder.  <br> To obtain an instance of this class, refer to @link Features::FeatureCollection Features::FeatureCollection@endlink  <br> */
        class NXOPENCPPEXPORT DieCollection : public TaggedObjectCollection
        {
            private: NXOpen::Features::FeatureCollection* m_owner;
            public: explicit DieCollection(NXOpen::Features::FeatureCollection *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Features::Feature * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::Die::DieCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Die::DieCollection *m_context;
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
            /** Creates the draw die punch feature builder.  @return  Draw Die Punch feature builder.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DrawDiePunchBuilder * DrawDiePunch
            (
                NXOpen::Features::Feature * drawDiePunch /** Draw Die Punch to be edited, NULL if create. */
            );
            /** Creates/Edits the form task feature builder.  @return  Form Task feature builder.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Die::FormTaskBuilder * FormTask
            (
                NXOpen::Features::Feature * formTask /** Form Task to be edited, NULL if create. */
            );
            /** Creates the die_rotor feature builder.  @return  Die Rotor feature builder.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::RotorBuilder * Rotor
            (
                NXOpen::Features::Feature * rotor /** Die Rotor to be edited, NULL if create */
            );
            /** Creates/Edits the flange task feature builder.  @return  Flange Task feature builder <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Die::FlangeTaskBuilder * FlangeTask
            (
                NXOpen::Features::Feature * flangeTask /** Flange Task to be edited, NULL if create */
            );
            /** Creates/Edits the trim task feature builder.  @return  Trim Task feature builder <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Die::TrimTaskBuilder * TrimTask
            (
                NXOpen::Features::Feature * trimTask /** Trim Task to be edited, NULL if create */
            );
            /** Creates/Edits the pierce task feature builder.  @return  Pierce Task feature builder <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Die::PierceTaskBuilder * PierceTask
            (
                NXOpen::Features::Feature * pierceTask /** Pierce Task to be edited, NULL if create */
            );
            /** Creates/Edits the die area fill feature builder  @return  area fill feature builder <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Die::FillBuilder * Fill
            (
                NXOpen::Features::Feature * fill /** area fill to be edited, NULL if create */
            );
            /** Creates/Edits the die lineup feature builder  @return  lineup feature builder <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Die::LineupBuilder * Lineup
            (
                NXOpen::Features::Feature * lineup /** lineup to be edited, NULL if create */
            );
            /** Creates/Edits the die output curves feature builder  @return  output curves feature builder <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Die::OutputCurvesBuilder * OutputCurves
            (
                NXOpen::Features::Feature * outcurves /** output curves feature to be edited, NULL if create */
            );
            /** Creates/Edits the steel insert feature builder  @return  Steel Insert feature builder <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::SteelInsertBuilder * Steelinsert
            (
                NXOpen::Features::Feature * steelInsert /** Steel Insert to be edited, NULL if create */
            );
            /** Creates a @link Die::QuickBinderWrapBuilder Die::QuickBinderWrapBuilder@endlink   @return   <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Die::QuickBinderWrapBuilder * CreateQuickBinderWrapBuilder
            (
                NXOpen::Features::Feature * quickBinderWrap /** the QuickBinderWrap feature to be edited, NULL if create */
            );
            /** Creates a @link Die::TrimLineDevelopmentBuilder Die::TrimLineDevelopmentBuilder@endlink   @return   <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Die::TrimLineDevelopmentBuilder * CreateTrimLineDevelopmentBuilder
            (
                NXOpen::Features::Feature * trimLineDevelopment /** the TrimLineDevelopment feature to be edited, NULL if create */
            );
            /** Creates a @link Die::AddSurfBuilder Die::AddSurfBuilder@endlink   @return   <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Die::AddSurfBuilder * CreateAddSurfBuilder
            (
                NXOpen::Features::Feature * addSurf /** the AddSurf feature to be edited, NULL if create */
            );
            /** Creates a @link Die::FaceSheetBuilder Die::FaceSheetBuilder@endlink   @return   <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Die::FaceSheetBuilder * FaceSheet
            (
                NXOpen::Features::Feature * faceSheet /** @link Die::FaceSheetBuilder Die::FaceSheetBuilder@endlink  to be edited */
            );
            /** Creates the trim/flange die assistant builder  @return  Trim/Flange Die Assistant builder <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::TrimFlangeDieAssistantBuilder * TrimFlangeDieAssistant
            (
                NXOpen::Features::Feature * nullFeature /** must be NULL to create trim die */
            );
            /** Creates a die_shoe feature builder (@link Die::DieShoeBuilder Die::DieShoeBuilder@endlink )  @return   <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieShoeBuilder * DieShoe
            (
                NXOpen::Die::DieShoe * dieShoe /** @link Die::DieShoe Die::DieShoe@endlink  to be edited */
            );
            /** Creates a @link Die::DieAttributesBuilder Die::DieAttributesBuilder@endlink   @return   <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieAttributesBuilder * CreateDieAttribute
            (
            );
            /** Creates a @link Die::DieBooleanBuilder Die::DieBooleanBuilder@endlink   @return   <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieBooleanBuilder * CreateDieBoolean
            (
            );
            /** Creates a @link Die::DieDirectionBuilder Die::DieDirectionBuilder@endlink   @return   <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieDirectionBuilder * CreateDieDirection
            (
                NXOpen::Features::Feature * feature /** Parent NX Feature */
            );
            /** Creates a @link Die::DiePlaneBuilder Die::DiePlaneBuilder@endlink   @return   <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DiePlaneBuilder * CreateDiePlane
            (
                NXOpen::Features::Feature * feature /** Parent NX Feature */
            );
            /** Creates a clamping slot feature builder (@link Die::ClampingSlotBuilder Die::ClampingSlotBuilder@endlink )  @return   <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::ClampingSlotBuilder * ClampingSlot
            (
                NXOpen::Die::ClampingSlot * clampingSlot /** @link Die::ClampingSlot Die::ClampingSlot@endlink  to be edited */
            );
            /** Creates a @link Die::CompensateRoughDataBuilder Die::CompensateRoughDataBuilder@endlink   @return   <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Die::CompensateRoughDataBuilder * CompensateRoughData
            (
                NXOpen::Features::CompensateRoughData * compensateRoughData /** @link Features::CompensateRoughData Features::CompensateRoughData@endlink  to be edited */
            );
            /** Creates a keyway feature builder @link Die::KeywayBuilder Die::KeywayBuilder@endlink   @return   <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::KeywayBuilder * Keyway
            (
                NXOpen::Die::Keyway * keyway /** @link Die::Keyway Die::Keyway@endlink  to be edited */
            );
            /** Creates a heelpost feature builder @link Die::HeelpostBuilder Die::HeelpostBuilder@endlink   @return   <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::HeelpostBuilder * Heelpost
            (
                NXOpen::Die::Heelpost * heelpost /** @link Die::Heelpost Die::Heelpost@endlink  to be edited */
            );
            /** Creates a cast relief feature builder @link Die::CastReliefBuilder Die::CastReliefBuilder@endlink   @return   <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::CastReliefBuilder * CastRelief
            (
                NXOpen::Die::CastRelief * castRelief /** @link Die::CastRelief Die::CastRelief@endlink  to be edited */
            );
            /** Creates a @link Die::DieLocationBuilder Die::DieLocationBuilder@endlink   @return   <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieLocationBuilder * CreateDieLocation
            (
            );
            /** Creates a @link Die::DieLocationsBuilder Die::DieLocationsBuilder@endlink   @return   <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieLocationsBuilder * CreateDieLocations
            (
                NXOpen::Features::Feature * feature /** Parent NX Feature */,
                bool allowSelection /** Is selection available */,
                bool allowNewPoint /** Is specify point available */,
                bool allowNewCoordinateSystem /** Is specify coordinate system available */,
                bool allowNewVector /** Is specify vector available */,
                bool allowNewPlane /** Is specify plane available */,
                bool isRequired /** Is it required that something be specified, or is everything optional */,
                bool allowMultipleSelection /** Can builder support multiple locations */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
