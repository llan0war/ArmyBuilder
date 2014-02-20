@FOR %%G IN (*.ui) DO @CALL :GenInt %%G
@GOTO :EOF

:GenInt
@SET name=%~n1%
call C:\Python27\Lib\site-packages\PyQt4\pyuic4.bat %name%.ui -o %name%.py
