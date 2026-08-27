@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 exit /b 1
)

call ".venv\Scripts\activate.bat"
python -m pip install -r requirements.txt
if errorlevel 1 exit /b 1

if "%~1"=="" (
    set "INPUT_PDF=BRSR_CBI_2024_2025.pdf"
) else (
    set "INPUT_PDF=%~1"
)

if not exist "%INPUT_PDF%" (
    echo PDF not found: %INPUT_PDF%
    exit /b 1
)

python src\extract_document.py "%INPUT_PDF%" --output-dir data\processed
if errorlevel 1 exit /b 1

echo Extraction complete. Outputs are in data\processed\
endlocal
