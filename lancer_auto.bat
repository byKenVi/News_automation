@echo off
echo ========================================
echo    LANCEMENT NEWS AUTOMATIQUE
echo    %date% %time%
echo ========================================

cd /d "E:\Code python\News_automation"

:: Activer l'environnement virtuel
call venv\Scripts\activate.bat

:: Lancer le script (version simplifiée)
python main.py

echo ========================================
echo    EXECUTION TERMINEE
echo    %date% %time%
echo ========================================
timeout /t 10