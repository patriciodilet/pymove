@echo off
:loop
set /a "x=%random% %% 601 + 900"
set /a "y=%random% %% 401 + 400"
echo Working... X=%x%, Y=%y%
powershell.exe -command "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point(%x%, %y%)"
timeout /t 10 >nul

:: Presionar la tecla "Win"
powershell.exe -command "[System.Windows.Forms.SendKeys]::SendWait('^{ESC}')"

goto loop
