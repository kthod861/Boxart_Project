pyinstaller -y -F -w ^
--clean ^
--icon "F:\Boxart_Project\Pyinstaller_MakeGrid/Lib/MCL.ico" ^
--distpath "F:\Boxart_Project\Pyinstaller_MakeGrid/" ^
--add-data "F:\Boxart_Project\Pyinstaller_MakeGrid/Lib/MCL.ico";"Lib/" ^
--add-data "F:\Boxart_Project\Pyinstaller_MakeGrid/Lib/Demo.ui";"Lib/" ^
--add-data "F:\Boxart_Project\Pyinstaller_MakeGrid/Lib/Demo_Lib.py";"Lib/" ^
"F:\Boxart_Project\Pyinstaller_MakeGrid/Make_Grid.py"