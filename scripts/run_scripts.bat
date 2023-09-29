@echo off
setlocal enabledelayedexpansion

set SCRIPTS_DIR=.
set DATA_DIR=..\data
set INPUT_FILE=%DATA_DIR%\resolution_more_6A_4aa.csv
set PROCESSED_FILE=%DATA_DIR%\resolution_more_6A_4aa.csv
set SDF_FILE=%DATA_DIR%\sdf_files\resolution_more_6A_4aa.sdf
set UNCHARGED_SDF_FILE=%DATA_DIR%\sdf_files\resolution_more_6A_4aa.sdf
set CONFIG_FILE=%SCRIPTS_DIR%\config.json

cd %SCRIPTS_DIR%

echo Running MergePDB.py...
python MergePDB.py "%INPUT_FILE%" "%PROCESSED_FILE%"
if errorlevel 1 (
    echo Error occurred while running MergePDB.py!
    pause
    exit /b !errorlevel!
)

echo Running SeqToSDF.py...
python SeqToSDF.py "%CONFIG_FILE%"
if errorlevel 1 (
    echo Error occurred while running SeqToSDF.py!
    pause
    exit /b !errorlevel!
)

echo Running UniquifySDF.py...
python UniquifySDF.py "%SDF_FILE%" "%UNCHARGED_SDF_FILE%"
if errorlevel 1 (
    echo Error occurred while running UniquifySDF.py!
    pause
    exit /b !errorlevel!
)

echo All scripts ran successfully!
pause