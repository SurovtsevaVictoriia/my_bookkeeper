# Программа для управления личными финансами
#### (учебный проект для курса по практике программирования на Python)

Структура проекта:

📁 bookkeeper — корневая директория проекта 
    📁 bookkeeper — исполняемый код 
        - 📁dirs
            - 📁 models_dir — модели данных
                - 📄 base.py — создает базу данных
                - 📄 category.py — категория расходов
                - 📄 expense.py — расходная операция
                - 📄 model.py — описывает взаимодействия категорий и расходов, в т.ч. расчет бюджета
                - 📄 settings.py — настройки прдеставления, пути к файлам хранения данных
            - 📁 presenter_dir — директория взаимодействия модели и интерфейса, + файлы данных
                - 📄 bookkeeper.sqlite — хранение данных о расходах и категориях
                - 📄 budget.json — хранит данные о лимитах бюджета (отдельным файлом для разнообразия)
                - 📄 presenter.py - обеспчивает взаимодействие модели и интерфейса
                    работает напрямую исключительно с model.py и view.py
            - 📁 view_dir — графический интерфейс (пока не написан)
                - 📄 view.py - запуск QT-приложения, предоставление данных      презентеру
                - 📄 basic_layout.py - главный виджет
                - 📄 view_expense.py - виджет отображения, удаления, редактирования расходов
                - 📄 view_budget.py - виджет отображения бюджета
                - 📄 add_expense.py - виджет добавления расхода
                - 📄 redact_category.py - диалог добавления, раедактирования, удаления категорий
                - 📄 edit_expense_category.py - диалог изменения категории расхода
                - 📄 category_tree.py - дерево категорий расходов
                - 📄 utils.py - дополнительные операции с интерфейсом
            - 📄 main.py — файл запуска приложения
            - 📄 create_base.py - создание базы данных с нуля в случае необходимости

    📁 tests — тесты, к сожалению, реализовать не удалось из-за проблем с импортами

В проекте предусмотрена установка зависимостей с помощью poetry. Все необходимые модули описаны в poetry.lock

Для запуска приложения необходимо:
    1. Открыть командную строку в главной директории проекта
    2. Ввести команду >>poetry shell, чтобы войти в виртуальное окружение
    3. Ввести команду >>poetry install, чтобы установить необходимые модули
    4. Запустить файл main.py, введя команду >>poetry run python bookkeeper\main.py

Если на устройстве необходимые библиотеки, достаточно запустить main.py.

Функционал приложения показан в видеодемонстрации по ссылке :
https://drive.google.com/drive/folders/1z1gyxaUyEIts-RbdSIYs3gsN8EGpPhzC?usp=sharing



