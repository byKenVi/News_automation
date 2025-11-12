@echo off
echo LANCEMENT AUTOMATIQUE DU Scripts
echo %date% %time%

cd /d "E:\Code Python\News_automation"
call venv\Scripts\activate.bat

python main.py --auto 

if errorlevel 1 (
    echo Erreur detectée , nouvelle tentative dans 30 secondes...
    timeout /t 30 /nobreak
    python main.py 
)

echo ==
echo TACHE TERMINEE