document.addEventListener("DOMContentLoaded", function () {
    const glow = document.getElementById('glow');

    document.addEventListener('mousemove', (e) => {
        // Update the position of the glow to follow the mouse
        glow.style.left = `${e.pageX}px`;
        glow.style.top = `${e.pageY}px`;
    });
});