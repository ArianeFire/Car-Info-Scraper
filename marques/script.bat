@echo off
set src_folder=C:\Users\SEYDOU BERTHE\PROJETS\AUTO_SCRAPPING\marques\backup
set dst_folder=C:\Users\SEYDOU BERTHE\PROJETS\AUTO_SCRAPPING\marques\volvo
for /f "tokens=*" %%i in (volvo.txt) DO (
	echo %src_folder%\%%i
    xcopy /S/E "%src_folder%\%%i" "%dst_folder%"
)