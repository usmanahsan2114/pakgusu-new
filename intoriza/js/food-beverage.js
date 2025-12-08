/* Food & Beverage Industry - Interactive Components */

document.addEventListener('DOMContentLoaded', () => {
    try { initRadar(); } catch (e) { console.error("Radar Init Error:", e); }
    try { initBlueprint(); } catch (e) { console.error("Blueprint Init Error:", e); }
    try { initClasses(); } catch (e) { console.error("Classes Init Error:", e); }
    try { initCarousel(); } catch (e) { console.error("Carousel Init Error:", e); }
    try { initProductFilters(); } catch (e) { console.error("Product Filter Init Error:", e); }

    // Safety fallback: Force hide preloader if window.load hangs
    setTimeout(() => {
        const loader = document.querySelector('.loading-area');
        if (loader) {
            loader.style.transition = 'opacity 0.5s ease';
            loader.style.opacity = '0';
            setTimeout(() => loader.style.display = 'none', 500);
        }
    }, 2000); // 2 seconds max wait
});

// --- SECTION 1: RADAR (Food Safety Risks) ---
const radarData = {
    'particles': {
        title: 'Microbial Control',
        tag: 'GMP / HACCP',
        desc: 'Preventing growth of bacteria, mold, and yeast in critical filling areas.',
        stat1: '< 10 CFU', label1: 'Bioburden',
        stat2: 'Grade A', label2: 'Zone Std'
    },
    'esd': {
        title: 'Cross-Contamination',
        tag: 'Allergen Control',
        desc: 'Segregation of production lines to prevent allergen traces in non-allergen products.',
        stat1: '0%', label1: 'Tolerance',
        stat2: 'Separate', label2: 'Air Handling'
    },
    'chemicals': {
        title: 'Washdown & Sterilization',
        tag: 'Chemical Resistance',
        desc: 'Surfaces must withstand frequent high-pressure cleaning and harsh disinfectants.',
        stat1: 'IP65/69K', label1: 'Rating',
        stat2: 'SS 304', label2: 'Material'
    },
    'audits': {
        title: 'Regulatory Compliance',
        tag: 'FDA / ISO 22000',
        desc: 'Ensuring facility passes strict food safety audits for export markets.',
        stat1: '100%', label1: 'Audit Pass',
        stat2: 'Traceable', label2: 'Records'
    },
    'vibration': {
        title: 'Temp & Humidity',
        tag: 'Shelf Life',
        desc: 'Strict control of T/RH to prevent spoilage and clumping of powders.',
        stat1: 'Low RH', label1: 'Dry Process',
        stat2: '< 4°C', label2: 'Cold Chain'
    },
    'humidity': {
        title: 'Mold Prevention',
        tag: 'Moisture Control',
        desc: 'Keeping humidity low to inhibit mold growth in storage and packaging.',
        stat1: '40-50%', label1: 'RH Target',
        stat2: 'HVAC', label2: 'Dehumidify'
    },
    'temp': {
        title: 'Foreign Matter',
        tag: 'Physical Risks',
        desc: 'Preventing glass, metal, or plastic fragments from entering the food chain.',
        stat1: 'Zero', label1: 'Tolerance',
        stat2: 'Laminar', label2: 'Protection'
    }
};

function initRadar() {
    const nodes = document.querySelectorAll('.new-elec-radar-node');
    if (!nodes.length) return;

    // Elements
    const pTitle = document.getElementById('radar-panel-title');
    const pTag = document.getElementById('radar-panel-tag');
    const pDesc = document.getElementById('radar-panel-desc');
    const pS1Val = document.getElementById('radar-stat1-val');
    const pS1Lab = document.getElementById('radar-stat1-label');
    const pS2Val = document.getElementById('radar-stat2-val');
    const pS2Lab = document.getElementById('radar-stat2-label');
    const panel = document.querySelector('.new-elec-context-panel');

    // Initial state set to match first active node 'particles'
    if (pTitle) {
        pTitle.textContent = radarData['particles'].title;
        pTag.textContent = radarData['particles'].tag;
        pDesc.textContent = radarData['particles'].desc;
        pS1Val.textContent = radarData['particles'].stat1;
        pS1Lab.textContent = radarData['particles'].label1;
        pS2Val.textContent = radarData['particles'].stat2;
        pS2Lab.textContent = radarData['particles'].label2;
    }

    nodes.forEach(node => {
        node.addEventListener('mouseenter', () => {
            nodes.forEach(n => n.classList.remove('active'));
            node.classList.add('active');

            const key = node.dataset.key;
            const data = radarData[key];
            if (data && panel) {
                panel.style.opacity = '0.5';
                setTimeout(() => {
                    if (pTitle) pTitle.textContent = data.title;
                    if (pTag) pTag.textContent = data.tag;
                    if (pDesc) pDesc.textContent = data.desc;
                    if (pS1Val) pS1Val.textContent = data.stat1;
                    if (pS1Lab) pS1Lab.textContent = data.label1;
                    if (pS2Val) pS2Val.textContent = data.stat2;
                    if (pS2Lab) pS2Lab.textContent = data.label2;
                    panel.style.opacity = '1';
                }, 150);
            }
        });
    });
}

// --- SECTION 2: BLUEPRINT ---
function initBlueprint() {
    const steps = document.querySelectorAll('.new-elec-step-card');
    if (!steps.length) return;

    steps.forEach((step, index) => {
        step.addEventListener('click', () => {
            steps.forEach(s => s.classList.remove('active'));
            step.classList.add('active');
        });
    });
}

// --- SECTION 3: CLASSES (Hygiene Standards) ---
const classData = {
    'iso5': {
        name: 'High Care (ISO 5)',
        desc: 'Aseptic filling zones and open product handling.',
        part: '< 1 CFU/m³',
        ach: '240 - 480 /hr',
        cover: '60 - 100%'
    },
    'iso6': {
        name: 'High Hygiene (ISO 6)',
        desc: 'Primary packaging and sensitive blending areas.',
        part: '< 10 CFU/m³',
        ach: '150 - 240 /hr',
        cover: '25 - 40%'
    },
    'iso7': {
        name: 'Medium Care (ISO 7)',
        desc: 'Secondary packaging and controlled storage.',
        part: '< 100 CFU/m³',
        ach: '60 - 90 /hr',
        cover: '15 - 20%'
    },
    'iso8': {
        name: 'Low Care (ISO 8)',
        desc: 'General production, corridors, and warehousing.',
        part: '< 200 CFU/m³',
        ach: '10 - 25 /hr',
        cover: '5 - 15%'
    }
};

function initClasses() {
    const btns = document.querySelectorAll('.new-elec-class-btn');
    const title = document.getElementById('class-display-title');
    const desc = document.getElementById('class-display-desc');
    // Specs
    const sPart = document.getElementById('spec-part');
    const sAch = document.getElementById('spec-ach');
    const sCover = document.getElementById('spec-cover');
    const sPartLabel = document.querySelector('#spec-part')?.parentElement?.querySelector('.new-elec-spec-label');


    const chamber = document.getElementById('particle-chamber');

    if (!btns.length) return;

    // Set initial state (ISO 5)
    if (chamber) chamber.classList.add('chamber-density-iso5');
    // Change label for Food
    if (sPartLabel) sPartLabel.textContent = 'Bioburden Limit';

    btns.forEach(btn => {
        btn.addEventListener('click', () => {
            btns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const key = btn.dataset.class;
            const data = classData[key];
            if (data) {
                if (title) title.textContent = data.name;
                if (desc) desc.textContent = data.desc;

                // Update Particle Chamber Density
                if (chamber) {
                    chamber.classList.remove('chamber-density-iso5', 'chamber-density-iso6', 'chamber-density-iso7', 'chamber-density-iso8');
                    chamber.classList.add(`chamber-density-${key}`);
                }

                // Animate specs update
                if (sPart && sAch && sCover) {
                    sPart.style.opacity = 0;
                    sAch.style.opacity = 0;
                    sCover.style.opacity = 0;
                    setTimeout(() => {
                        sPart.textContent = data.part;
                        sAch.textContent = data.ach;
                        sCover.textContent = data.cover;
                        sPart.style.opacity = 1;
                        sAch.style.opacity = 1;
                        sCover.style.opacity = 1;
                    }, 150);
                }
            }
        });
    });
}

// --- SECTION 4: CAROUSEL ---
function initCarousel() {
    const track = document.getElementById('elec-slider-track');
    const prevBtn = document.querySelector('.elec-slider-btn.prev');
    const nextBtn = document.querySelector('.elec-slider-btn.next');
    if (!track || !prevBtn || !nextBtn) return;

    let scrollAmount = 0;
    const scrollStep = 320;
    const maxScroll = track.scrollWidth - track.clientWidth;

    // Auto play
    let autoPlayInterval = setInterval(() => {
        moveRight();
    }, 3000);

    const resetTimer = () => {
        clearInterval(autoPlayInterval);
        autoPlayInterval = setInterval(moveRight, 3000);
    };

    const moveRight = () => {
        const currentMaxScroll = track.scrollWidth - track.clientWidth;
        if (track.scrollLeft >= currentMaxScroll - 10) {
            scrollAmount = 0;
        } else {
            scrollAmount = Math.min(track.scrollLeft + scrollStep, currentMaxScroll);
        }
        track.scrollTo({ left: scrollAmount, behavior: 'smooth' });
    };

    const moveLeft = () => {
        const currentMaxScroll = track.scrollWidth - track.clientWidth;
        if (track.scrollLeft <= 10) {
            scrollAmount = currentMaxScroll;
        } else {
            scrollAmount = Math.max(track.scrollLeft - scrollStep, 0);
        }
        track.scrollTo({ left: scrollAmount, behavior: 'smooth' });
    };

    nextBtn.addEventListener('click', () => {
        moveRight();
        resetTimer();
    });

    prevBtn.addEventListener('click', () => {
        moveLeft();
        resetTimer();
    });

    // Pause on hover
    track.parentElement.addEventListener('mouseenter', () => clearInterval(autoPlayInterval));
    track.parentElement.addEventListener('mouseleave', resetTimer);
}

// --- SECTION 5: PRODUCTS ---
function initProductFilters() {
    const btns = document.querySelectorAll('.new-elec-filter-btn');
    const cards = document.querySelectorAll('.new-elec-prod-card');

    if (!btns.length) return;

    btns.forEach(btn => {
        btn.addEventListener('click', () => {
            btns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.dataset.filter;
            cards.forEach(card => {
                const type = card.dataset.type;
                if (filter === 'all' || type === filter) {
                    card.style.display = 'block';
                    setTimeout(() => card.style.opacity = '1', 10);
                } else {
                    card.style.display = 'none';
                    card.style.opacity = '0';
                }
            });
        });
    });
}
