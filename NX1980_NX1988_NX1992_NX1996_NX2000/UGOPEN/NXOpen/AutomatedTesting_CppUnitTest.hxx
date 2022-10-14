#ifndef NXOpen_AUTOMATEDTESTING_CPPUNITTEST_HXX
#define NXOpen_AUTOMATEDTESTING_CPPUNITTEST_HXX

#ifdef _MSC_VER
#pragma once
#endif

#include <vector>

#include <NXOpen/NXString.hxx>

namespace NXOpen
{
    namespace  AutomatedTesting
    {
      /* A TestFixture is used to provide a common environment for a set of test methods.
       *
       * To define a test method
       *
       *    class HelloWorld: public NXOpen::AutomatedTesting::TestFixture
       *    {
       *        ATSUNIT_TEST_SUITE(HelloWorld);
       *        ATSUNIT_TEST(Test_case1); // Test_case1 will be register into ATS.
       *        ATSUNIT_TEST(Test_case2); // Test_case2 will be register into ATS.
       *        ATSUNIT_TEST_SUITE_END();
       *     public:
       *        HelloWorld()
       *        {
       *            classId = "HelloWorld_CPP"; //required
       *            category = "UnitTest";  // optional
       *            displayName = "HelloWorld(CPP)"; // optional
       *            interactive = false; // optional
       *            resourceFiles = { "ATS_TestFile.txt" };// optional
       *            isManagedMode = "undefine";// optional
       *        }
       *        void Test_case1(){}
       *        void Test_case2(){}}
       *    };
       *    ATSUNIT_TEST_SUITE_REGISTRATION()
       *
       */
      class TestFixture
      {
      public:
          virtual ~TestFixture();
          
          virtual void SetUpClass();
          virtual void TearDownClass();
          virtual void SetUp();
          virtual void TearDown();
          
          NXString classId = "";  // Required and its value must be unique.
          NXString category = "UnitTest"; // Optional.
          NXString displayName = "";
          NXString description = "";
          NXString nxVersion = "1980";
          bool interactive = false;
          std::vector< NXString > resourceFiles = {};
          bool isManagedMode = false;
          bool closeAllParts = true;
          NXString stopOnOption = "StopOnNone";
      };

      /* 
       * Inner class, each method deine in TestFixture will be wrapped in a TestCase.
       * This class will be used in Macro.
       */
      class TestCase
      {
      public:
          TestCase(NXOpen::NXString funcName = "testCase");
          ~TestCase();
          virtual void Run() = 0;

          NXOpen::NXString GetName();
          TestFixture* GetWrappedFixture();
          void SetWrappedFixture(TestFixture* fixture);

          virtual void SetUp();
          virtual void TearDown();
          virtual void SetUpClass();
          virtual void TearDownClass();

      private:
          TestFixture*  m_wrappedFixture;
          NXOpen::NXString m_functioName;
      };

      /*
      * Inner class, each TestCase will be grouped in test suite.
      * This class will be used in Macro.
      */
      class TestSuite
      {
      public:
          TestSuite();
          ~TestSuite();

          void Run();
          void AddTest(TestCase* test);
      private:
          std::vector<TestCase*> m_tests;
      };

      /*
      * Inner class, TestCaller is used to created a TestCase.
      * This class will be used in Macro.
      */
      template <class Fixture>
      class TestCaller : public TestCase
      {
          typedef void (Fixture::* TestMethod)();

      public:

          TestCaller(NXOpen::NXString funcName, TestMethod test) :
              TestCase(funcName),
              m_fixture(new Fixture()),
              m_test(test)
          {
              SetWrappedFixture(m_fixture);
          }

          ~TestCaller()
          {
              if (m_fixture != nullptr)
                  delete m_fixture;
          }

          void Run() override
          {
              (m_fixture->*m_test)();
          }

          void SetUp() override
          {
              m_fixture->SetUp();
          }

          void TearDown()override
          {
              m_fixture->TearDown();
          }

          void SetUpClass() override
          {
              m_fixture->SetUpClass();
          }

          void TearDownClass()override
          {
              m_fixture->TearDownClass();
          }

      private:
          TestCaller(const TestCaller& other);
          TestCaller& operator =(const TestCaller& other);
          TestMethod m_test;
          Fixture* m_fixture;
      };

      /*
      * Inner class, AutoRegisterSuite is used to register a group of test methods 
      * into Automated Testing Studio.
      *
      * This class will be used in Macro.
      */
      template<class TestCaseType>
      class AutoRegisterSuite
      {
      public:
          /** Auto-register the suite into Automated Testing Studio.
          */
          AutoRegisterSuite()
          {
              TestCaseType::suite()->Run();
          }

          ~AutoRegisterSuite()
          {
          }
      };

// This macro starts the declaration of a new test suite.
#define ATSUNIT_TEST_SUITE( ATestFixtureType )         \
  public:                                              \
    typedef ATestFixtureType TestFixtureType;          \
                                                       \
    static void AddTestsToSuite( NXOpen::AutomatedTesting::TestSuite* testSuite )\
    { 

// Add a method to the suite
#define ATSUNIT_TEST( testMethod )                     \
    testSuite->AddTest(                                \
        ( new NXOpen::AutomatedTesting::TestCaller<TestFixtureType>(#testMethod, \
                  &TestFixtureType::testMethod )));

// End declaration of the test suite.
#define ATSUNIT_TEST_SUITE_END()                                                             \
    }                                                                                        \
                                                                                             \
    static NXOpen::AutomatedTesting::TestSuite* suite()                                      \
    {                                                                                        \
      NXOpen::AutomatedTesting::TestSuite* suite = new NXOpen::AutomatedTesting::TestSuite();\
      TestFixtureType::AddTestsToSuite(suite);                                               \
      return suite;                                                                          \
    }                                                   

// Generate an unique name
#define ATSUNIT_MAKE_UNIQUE_NAME( prefix ) ATSUNIT_JOIN( prefix, __LINE__ )
#define ATSUNIT_JOIN( symbol1, symbol2 ) symbol1##symbol2

// Register a defiend class into ATS
#define ATSUNIT_TEST_SUITE_REGISTRATION( ATestFixtureType )                                  \
static NXOpen::AutomatedTesting::AutoRegisterSuite< ATestFixtureType >                       \
             ATSUNIT_MAKE_UNIQUE_NAME(autoRegisterRegistry__ )
    }
}

#endif