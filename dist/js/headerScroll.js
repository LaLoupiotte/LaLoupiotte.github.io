document.addEventListener("DOMContentLoaded", function () {
    window.addEventListener('scroll', function() {
        const header = document.querySelector('header');
        if (window.scrollY > 10) { 
            header.classList.remove('transparent');
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
            header.classList.add('transparent');
        }
    });
});