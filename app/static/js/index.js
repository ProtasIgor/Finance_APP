(function () {
    document.addEventListener('DOMContentLoaded', () => {
      // Получаем значение cookie 'darkMode'
      theme_btn = document.querySelector('.theme-button')
      menu_btn_open = document.querySelector('.menu-button')
      menu_btn_close = document.querySelector('.menu-close-button')
      rootElement = document.querySelector(':root')
      headerElement = document.querySelector('.header')


      function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
      }

      const darkMode = getCookie('darkMode');
      if (darkMode == 1) rootElement.classList.add('dark__mode')

      menu_btn_open.addEventListener('click', () => {
        headerElement.classList.toggle('visit');
        rootElement.classList.toggle('overflow-hidden');
      });

      menu_btn_close.addEventListener('click', () => {
        headerElement.classList.toggle('visit');
        rootElement.classList.toggle('overflow-hidden');
      });

      // header theme button
      theme_btn.addEventListener('click', () => {
        rootElement.classList.toggle('dark__mode');
        // Пример использования:
        setCookie('darkMode', `${rootElement.classList.contains('dark__mode') ? 1 : 0 }`, {'max-age': 3600});
      });

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



    });
}());