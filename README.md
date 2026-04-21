# Восстановление трехмерного макета помещения по панорамному изображению

Данный проект предназначен для автоматического восстановления трехмерного макета помещения по одному панорамному изображению с использованием архитектуры **AtlantaNet**.

## 1. Ресурсы

Для корректного запуска проекта необходимо:
* **Операционная система**: Windows 10/11 с поддержкой WSL2 (Windows Subsystem for Linux).
* **Свободное место**: не менее **60 ГБ** на диске (рекомендуется использовать диск `D:` для хранения образов Docker).
* **Программное обеспечение**: 
    * Docker Desktop (используемая версия 4.67.0) https://www.docker.com/products/docker-desktop/
    * WSL2 Backend (рекомендуется дистрибутив Ubuntu)

## 2. Инструкция по запуску
* Склонировать данный репозиторий с использованием команды ```git clone <ссылка на репозиторий>```
* Перейти в папку ```cd developmentOfDeepLearningSystems```
* Создать папку **ckpt/** ```mkdir ckpt```
* Скачать веса модели resnet101_atlantalayout.pth https://vicserver.crs4.it/atlantanet/, переместить их в папку **ckpt/**
* Запустить приложение **Docker Desktop**
* В случае, если места на диске `С:` мало, необходимо использовать диск `D:` для хранения образов Docker. Это можно сделать следующим образом. В приложении **Docker Desktop** перейти по вкладкам Settings -> Resources -> Advanced -> Disk image location, затем выбрать нужное место для хранения образов Docker.
* Выполнить сборку образа с использование команды **docker-compose build**
* Для запуска инференса необходимо выполнить следующую команду **docker-compose up**
  
## 3. Результаты инференса
После завершения инференса в консоли отобразится статус "Инференс завершен успешно", в папке проекта обновится файл в директории results/, содержащий предсказанные параметры помещения, автоматически запустится тест сравнения полученных результатов с эталонными.

```

atlanta-net-inference  | Инференс завершен успешно

atlanta-net-inference  | 

atlanta-net-inference  | Запуск теста сравнения JSON файлов...

atlanta-net-inference  | -----------------------------------------

atlanta-net-inference  | Сравнение JSON файлов...

atlanta-net-inference  | Файл 1: results/demo.json

atlanta-net-inference  | Файл 2: results/test.json

atlanta-net-inference  | 

atlanta-net-inference  | Структура JSON совпадает

atlanta-net-inference  | Ошибок не найдено

atlanta-net-inference  | JSON файлы полностью совпадают

atlanta-net-inference  | 

atlanta-net-inference  | =========================================

atlanta-net-inference  | Все задачи выполнены успешно!

atlanta-net-inference  | =========================================

atlanta-net-inference  | 

atlanta-net-inference  | Результаты инференса сохранены в папку results/

atlanta-net-inference  | Файлы: demo.json и test.json

