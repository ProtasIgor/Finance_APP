(function () {
    document.addEventListener('DOMContentLoaded', () => {
        // header theme button
        btn = document.querySelector('.theme__button')
        rootElement = document.querySelector(':root')
        btn.addEventListener('click', () => {
            rootElement.classList.toggle('dark__mode');
            // Пример использования:
            setCookie('darkMode', `${rootElement.classList.contains('dark__mode') ? 1 : 0 }`, {secure: true, 'max-age': 3600});
        });

        function getCookie(name) {
            const value = `; ${document.cookie}`;
            const parts = value.split(`; ${name}=`);
            if (parts.length === 2) return parts.pop().split(';').shift();
        }

        function setCookie(name, value, options = {}) {

            options = {
              path: '/',
              // при необходимости добавьте другие значения по умолчанию
              ...options
            };

            if (options.expires instanceof Date) {
              options.expires = options.expires.toUTCString();
            }

            let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);

            for (let optionKey in options) {
              updatedCookie += "; " + optionKey;
              let optionValue = options[optionKey];
              if (optionValue !== true) {
                updatedCookie += "=" + optionValue;
              }
            }

            document.cookie = updatedCookie;
          }

        // Получаем значение cookie 'darkMode'
        const darkMode = getCookie('darkMode');

        if (darkMode == 1) rootElement.classList.add('dark__mode')
    });
}());