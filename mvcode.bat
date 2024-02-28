@echo off

if "%~2" neq "" goto error
if "%~1"=="" goto error

mkdir %1
move "%1*.py" ".\%1\."
git add %1

: git commit -m ":hammer: practice"

goto end

:error
echo Error: Please provide exactly one argument.
exit /b 1

:end
