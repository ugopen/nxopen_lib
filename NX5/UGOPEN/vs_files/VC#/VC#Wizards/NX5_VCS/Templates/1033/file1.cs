using NXOpen;
using NXOpen.Utilities;
using NXOpen.UF;
using NXOpenUI;

namespace MyProject
{

    // <summary>
    //   Summary description for [!output SAFE_CLASS_NAME].
    // </summary>
    //
    public class [!output SAFE_CLASS_NAME]
    {

        //  Main()
        //    Add description here
        //
        public static void Main()
        {

            //
            // TODO: Add application code here
            //
            
        }

        //  GetUnloadOption()
        //
        //    Used to tell NX when to unload this library
        //
        //    Available options include: 
        //       Session.LibraryUnloadOption.Immediately
        //       Session.LibraryUnloadOption.Explicitly
        //       Session.LibraryUnloadOption.AtTermination
        //
        //    Any programs that register callbacks must use 
        //    AtTermination as the unload option.
        //
        public static int GetUnloadOption(string dummy) 
        {
            return (int)Session.LibraryUnloadOption.Immediately;
        }

    }

}
