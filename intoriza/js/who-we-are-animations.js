/* Scoped JS for 'Who We Are' Section Animations */

document.addEventListener('DOMContentLoaded', function() {
    const section = document.getElementById('who-we-are-section');
    if (!section) return;

    // 3D Tilt Effect for Gallery Images
    const cards = section.querySelectorAll('.wt-box.hover-zoom-card');

    cards.forEach(card => {
        card.addEventListener('mousemove', handleMouseMove);
        card.addEventListener('mouseleave', handleMouseLeave);
    });

    function handleMouseMove(e) {
        const card = this;
        const cardRect = card.getBoundingClientRect();
        const cardWidth = cardRect.width;
        const cardHeight = cardRect.height;
        const centerX = cardRect.left + cardWidth / 2;
        const centerY = cardRect.top + cardHeight / 2;
        const mouseX = e.clientX - centerX;
        const mouseY = e.clientY - centerY;

        // Calculate rotation (max 10 degrees)
        const rotateX = (mouseY / (cardHeight / 2)) * -10;
        const rotateY = (mouseX / (cardWidth / 2)) * 10;

        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.05)`;
    }

    function handleMouseLeave() {
        this.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale(1)';
    }
});
