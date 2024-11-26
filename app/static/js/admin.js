(function () {

    document.addEventListener('DOMContentLoaded', () => {
        const apiUrl = "http://192.168.1.104:5000/api/system_info.get";
        // Функция для загрузки данных и обновления разметки
        async function fetchAndUpdate() {
            try {
                // Отправка запроса
                const response = await fetch(apiUrl);
                if (!response.ok) {
                    throw new Error(`Ошибка HTTP: ${response.status}`);
                }
                const data = await response.json();

                // Очистка предыдущих данных
                const tableBody = document.getElementById("system-info");
                tableBody.innerHTML = "";

                // Функция добавления строки в таблицу
                const addRow = (key, value) => {
                    const row = document.createElement("tr");
                    const keyCell = document.createElement("td");
                    const valueCell = document.createElement("td");

                    keyCell.textContent = key.replace(/_/g, ' ');
                    valueCell.textContent = typeof value === "object" ? JSON.stringify(value, null, 2) : value;

                    row.appendChild(keyCell);
                    row.appendChild(valueCell);
                    tableBody.appendChild(row);
                };

                // Рекурсивный вывод JSON-объектов
                const parseObject = (obj, parentKey = "") => {
                    for (const key in obj) {
                        const fullKey = parentKey ? `${parentKey} -> ${key}` : key;
                        if (typeof obj[key] === "object" && obj[key] !== null) {
                            parseObject(obj[key], fullKey);
                        } else {
                            addRow(fullKey, obj[key]);
                        }
                    }
                };

                // Парсинг данных
                parseObject(data);
            } catch (error) {
                console.error("Ошибка при обновлении данных:", error);
            }
        }

        // Установить интервал обновления
        setInterval(fetchAndUpdate, 1000);

        // Первоначальная загрузка
        fetchAndUpdate();
    });

}())