# Shortcuts Manager

## Overview
The Shortcuts Manager is a desktop application built using PyQt5 that allows users to efficiently manage custom shortcuts. This includes searching, adding, updating, and deleting shortcuts through a user-friendly graphical interface. The project leverages a local SQLite database (managed via `db_connect`) to store shortcut information, such as names and file paths. 

## Features
- **Search Shortcuts**: Quickly search for shortcuts by name or path, and open matching files directly.
- **Add Shortcuts**: Easily add new shortcuts with a specified name and file path.
- **Update Shortcuts**: Modify existing shortcuts to reflect updated file paths or names.
- **Delete Shortcuts**: Remove outdated or unused shortcuts from the database.
- **Edit Shortcuts Window**: View and manage all shortcuts in a table with the ability to reload data.

## Structure
- **Main Window**: 
  - Provides options to search for shortcuts and access the editing interface.
  - Search functionality allows users to input the desired file name and path to locate shortcuts.
- **Edit Shortcuts Window**:
  - Displays a table listing all shortcuts stored in the database.
  - Buttons to add, update, delete, and reload shortcut data.
- **Add, Update, and Delete Windows**:
  - Individual forms to manage shortcut data.

## How It Works
1. **Database Management**: The `db_connect` module handles SQLite database operations, including creating the table, inserting, updating, reading, and deleting records.
2. **UI Design**: The graphical interface is designed using Qt Designer and loaded dynamically using PyQt5's `uic` module.
3. **File Handling**: The application verifies the existence of directories and files to ensure shortcuts are valid.
4. **Keyboard Shortcuts**: The application supports `Enter` to trigger search and `Escape` to close windows for improved usability.

## File Structure
- **`main_window.ui`**: Defines the layout of the main application window.
- **`edit.ui`**: Defines the layout for the Edit Shortcuts window.
- **`add_short.ui`**: UI for adding new shortcuts.
- **`del_short.ui`**: UI for deleting shortcuts.
- **`updt_short.ui`**: UI for updating existing shortcuts.
- **`db_connect.py`**: Handles database operations (create, read, update, delete).
- **`main.py`**: Main application logic and entry point.

## Prerequisites
No additional libraries or dependencies are required to use this application.

## Setup Instructions
1. Download the project to your computer.
2. Navigate to the `dist` folder.
3. Execute the `app.exe` file to run the application.

## Usage
1. Launch the application.
2. Use the main window to:
   - Search for shortcuts by entering a file name and path.
   - Open the Edit Shortcuts window.
3. In the Edit Shortcuts window:
   - View and manage shortcuts through the table.
   - Add, update, or delete shortcuts using the corresponding buttons.

## Key Bindings
- **Enter**: Trigger search functionality.
- **Escape**: Close the current window.

## Future Improvements
- Add drag-and-drop functionality for easier path selection.
- Implement sorting and filtering in the table view.
- Add a feature to export/import shortcuts.

## License
This project is open-source and available under the [MIT License](LICENSE).

