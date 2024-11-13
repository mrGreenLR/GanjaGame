let clickCount = 0;

// Знаходимо елементи
const clickCounter = document.getElementById('clickCount');
const tapCircle = document.getElementById('tapCircle');

// Отримуємо поточне значення лічильника з сервера
fetch('/get_counter')
    .then(response => response.json())
    .then(data => {
        clickCount = data.click_count;
        clickCounter.textContent = clickCount;
    });

// Обробник події для натискання на кругле зображення
tapCircle.addEventListener('click', () => {
    clickCount++;
    clickCounter.textContent = clickCount;

    // Відправляємо нове значення лічильника на сервер для збереження
    fetch('/update_counter', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ click_count: clickCount })
    });
});
