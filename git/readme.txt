PowerShell or 

C:\Users\Iziaslaw>git config --global user.name "Iziaslaw"

C:\Users\Iziaslaw>git config --global user.email "ili--ya@ya.ru"

C:\Users\Iziaslaw>git config --global init.defaultBranch main

C:\Users\Iziaslaw>git config --global color.ui auto

C:\Users\Iziaslaw>git config --list

C:\Users\Iziaslaw>ssh-keygen -t ed25519 -C "ili--ya@ya.ru"

C:\Users\Iziaslaw>cat ~/.ssh/id_ed25519.pub | clip 

C:\Users\Iziaslaw>ssh -T git@github.com

:: 1. Инициализируем Git в папке с вашим проектом на ПК (сначала перейдите в неё через cd)
git init

:: 2. Добавляем файлы проекта в индекс
git add .

:: 3. Делаем первый коммит
git commit -m "first commit"

:: 4. Переименовываем главную ветку в main
git branch -M main

:: 5. Связываем локальную папку с созданным репозиторием на GitHub (копируйте строку с сайта!)
git remote add origin git@github.com:ВАШ_НИК/НАЗВАНИЕ_РЕПОЗИТОРИЯ.git

:: 6. Отправляем код на GitHub
git push -u origin main
