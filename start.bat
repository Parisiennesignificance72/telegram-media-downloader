@echo off
setlocal
chcp 65001 >nul
cd /d "%~dp0"
title Telegram Media Downloader

where python >nul 2>&1
if errorlevel 1 (
    echo [错误] 未找到 Python。请先安装 Python 3.10 或更高版本。
    echo https://www.python.org/downloads/
    pause
    exit /b 1
)

python -c "import telethon, cryptg" >nul 2>&1
if errorlevel 1 (
    echo 正在安装运行依赖，请稍候...
    python -m pip install -r requirements.txt
    if errorlevel 1 (
        echo [错误] 依赖安装失败，请检查网络后重试。
        pause
        exit /b 1
    )
)

python telegram_media_downloader.py
echo.
pause
