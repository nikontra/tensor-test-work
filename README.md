# tensor-test-work
## Третий сценарий
 Третий сценарий реализован двумя способами:
- первый - через библиотеку requests
- второй - нажатием на кнопку "Скачать"

В конце теста происходит удаление загруженного файла. Если удаление не требуется, необходимо закоментить предпоследнюю строку теста.
## Логирование
В тестах подключено логирование.
По умолчанию в терминал выводятся логи начиная от уровня WARNING, в pytest.log пишутся логи от уровня INFO. Настройки можно изменить в файле pytest.ini.