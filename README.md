# Восстановление трехмерного макета помещения по панорамному изображению

Данный проект предназначен для автоматического восстановления трехмерного макета помещения по одному панорамному изображению с использованием архитектуры **AtlantaNet**.

## 1. Ресурсы

Для корректного запуска проекта необходимо:
* **Операционная система**: Windows 10/11 с поддержкой WSL2 (Windows Subsystem for Linux).
* **Свободное место**: не менее **60 ГБ** на диске
* **Программное обеспечение**: 
    * Docker Desktop (используемая версия 4.67.0) https://www.docker.com/products/docker-desktop/
    * WSL2 Backend (рекомендуется дистрибутив Ubuntu)

## 2. Инструкция по запуску
* Склонировать данный репозиторий с использованием команды
  ```powershell
  git clone https://github.com/ShLera04/developmentOfDeepLearningSystems.git
* Перейти в папку
  ```powershell
  cd developmentOfDeepLearningSystems
* Создать папку **ckpt**
  ```powershell
  mkdir ckpt
* Скачать веса модели **resnet101_atlantalayout.pth** https://vicserver.crs4.it/atlantanet/, переместить их в папку **ckpt**.
* Запустить приложение **Docker Desktop**
* Место для хранения образов Docker можно изменить следующим образом. В приложении **Docker Desktop** перейти по вкладкам **Settings -> Resources -> Advanced -> Disk image location**, затем выбрать нужное место для хранения образов Docker.
* Выполнить сборку образа с использование команды
    ```powershell
    docker-compose build
* Для запуска инференса необходимо выполнить следующую команду
  ```powershell
  docker-compose up
## 3. Результаты инференса
После завершения инференса в консоли отобразится статус "Инференс завершен успешно", в папке проекта обновится файл в директории results/, содержащий предсказанные параметры помещения, автоматически запустится тест сравнения полученных результатов с эталонными.

```text
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
```
## 4. Дополнительные команды
* запуск временного контейнера
  ``` powershell
  docker-compose run --rm atlanta-net bash
* извлечение файлов
  ``` powershell
  docker cp atlanta-net-inference:/app/results/. ./results_from_docker