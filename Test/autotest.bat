@echo off
ECHO SimPi auto test for GPIO, Please check the light on the device
ECHO.
ECHO ---------- Test Case 1 ------------
ECHO In this test case, you should see GPIO 15 light off, which means connection is stable.
ECHO Press ENTER to start test case
pause >nul
start "" D:\SimPi\Test\GPIOtest1.html
ECHO.
ECHO ---------- Test Case 2 ------------
ECHO In this test case, you should see GPIO 5 flash, which means SimPi Queue and GPIO perform normally.
ECHO Press ENTER to start test case
pause >nul
start "" D:\SimPi\Test\GPIOtest2.html
ECHO.
ECHO Testing is finished. Press ENTER to close tabs
pause >nul