echo "========================================="
echo "Запуск инференса AtlantaNet"
echo "========================================="

if [ ! -f "ckpt/resnet101_atlantalayout.pth" ]; then
    echo "Ошибка: Модель не найдена в ckpt/resnet101_atlantalayout.pth"
    exit 1
fi

if [ ! -f "images/demo.png" ]; then
    echo "Ошибка: Изображение не найдено в images/demo.png"
    exit 1
fi

echo ""
echo "Запуск инференса..."
echo "-----------------------------------------"
python inference_atlanta_net.py \
    --pth ckpt/resnet101_atlantalayout.pth \
    --img images/demo.png \
    --output_dir results \
    --visualize

if [ $? -ne 0 ]; then
    echo ""
    echo "Ошибка при запуске инференса"
    exit 1
fi

echo ""
echo "Инференс завершен успешно"
echo ""

echo "Запуск теста сравнения JSON файлов..."
echo "-----------------------------------------"
python tests/test_json_comparison.py

if [ $? -ne 0 ]; then
    echo ""
    echo "Ошибка при запуске теста"
    exit 1
fi

echo ""
echo "========================================="
echo "Все задачи выполнены успешно!"
echo "========================================="
echo ""
echo "Результаты инференса сохранены в папку results/"
echo "Файлы: demo.json и test.json"
echo ""
