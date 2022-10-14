/*
===============================================================================

			Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
					  Unpublished - All rights reserved
===============================================================================

File Description:
	This file declares the interface for UIStyler action buttons.

Classes Declared:
	UgUIActionButton

================================================================================



*/

#ifndef UG_UI_ACTION_BUTTON_INCLUDED
#define UG_UI_ACTION_BUTTON_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler action button controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIActionButton : public UgUIControl
{
	public:
		// Constructor
		UgUIActionButton
		(
			const std::string  &control_id, // Identifying name of the control
			const UgUIDialog   *dialog	    // Dialog associated with the
										    // control
		);

		// Destructor
		virtual ~UgUIActionButton ( );

		// Sets the button bitmap
		void setBitmap
		(
			const std::string &file	    // <I>
                                        // Name of the bitmap file
		);

		// Sets the default action to this button
		void setDefaultAction ( );

		// Sets the focus to this button
        void setFocus ( );

		// Sets the button label
		void setLabel
		(
			const std::string &label    // <I>
										// Button label
		);
};

#undef EXPORTLIBRARY

#endif // UG_UI_ACTION_BUTTON_INCLUDED
