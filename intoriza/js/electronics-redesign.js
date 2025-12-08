/* Electronics Redesign - Interactive Components */

document.addEventListener('DOMContentLoaded', () => {
    try { initRadar(); } catch (e) { console.error("Radar Init Error:", e); }
    try { initBlueprint(); } catch (e) { console.error("Blueprint Init Error:", e); }
    try { initClasses(); } catch (e) { console.error("Classes Init Error:", e); }
    try { initCarousel(); } catch (e) { console.error("Carousel Init Error:", e); }
    try { initProductFilters(); } catch (e) { console.error("Product Filter Init Error:", e); }

    // Safety fallback: Force hide preloader if window.load hangs (e.g. due to Unsplash images)
    setTimeout(() => {
        const loader = document.querySelector('.loading-area');
        if (loader) {
            loader.style.transition = 'opacity 0.5s ease';
            loader.style.opacity = '0';
            setTimeout(() => loader.style.display = 'none', 500);
        }
    }, 2000); // 2 seconds max wait
});

// --- SECTION 1: RADAR ---
const radarData = {
    'particles': {
        title: 'Particle Contamination',
        tag: 'ISO 14644-1',
        desc: 'Airborne particulates can bridge circuits in nanometer-scale geometries.',
        stat1: '< 10 /m³', label1: 'Target (ISO 3)',
        stat2: 'Yield Loss', label2: 'Critical Risk'
    },
    'esd': {
        title: 'ESD Control',
        tag: 'ANSI/ESD S20.20',
        desc: 'Uncontrolled static discharge can instantly destroy sensitive components.',
        stat1: '< 100 V', label1: 'Body Voltage',
        stat2: '10⁹ Ω', label2: 'Surface Res.'
    },
    'chemicals': {
        title: 'Molecular Contamination',
        tag: 'AMC Control',
        desc: 'Volatile organic compounds (VOCs) and dopants affecting wafer purity.',
        stat1: 'PPT', label1: 'Detection Limit',
        stat2: 'Carbon', label2: 'Filtration'
    },
    'audits': {
        title: 'Regulatory Audits',
        tag: 'Compliance',
        desc: 'Strict adherence to international standards is mandatory for export.',
        stat1: 'Q1', label1: 'Audit Cycle',
        stat2: '100%', label2: 'Traceability'
    },
    'vibration': {
        title: 'Micro-Vibration',
        tag: 'VC Curves',
        desc: 'Structural resonance can disrupt photolithography alignment.',
        stat1: 'VC-E', label1: 'Standard',
        stat2: 'Isolators', label2: 'Solution'
    },
    'humidity': {
        title: 'Humidity Control',
        tag: 'RH Stability',
        desc: 'Fluctuations affect photoresist adhesion and static buildup.',
        stat1: '40% ±5%', label1: 'Set Point',
        stat2: 'Desiccant', label2: 'Control'
    },
    'temp': {
        title: 'Thermal Stability',
        tag: 'Temp Control',
        desc: 'Thermal expansion mismatch causes wafer overlay errors.',
        stat1: '±0.1°C', label1: 'Precision',
        stat2: 'Laminar', label2: 'Airflow'
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
    const zones = document.querySelectorAll('.map-zone');
    if (!steps.length) return;

    steps.forEach((step, index) => {
        step.addEventListener('click', () => {
            // UI Update
            steps.forEach(s => s.classList.remove('active'));
            step.classList.add('active');
        });
    });
}

// --- SECTION 3: CLASSES ---
const classData = {
    'iso5': {
        name: 'ISO Class 5',
        desc: 'Critical Core: For photolithography and wafer bonding.',
        part: '3,520 (0.5µm)',
        ach: '240 - 480 /hr',
        cover: '60 - 100%'
    },
    'iso6': {
        name: 'ISO Class 6',
        desc: 'Fine Assembly: Optical assembly and precision etching.',
        part: '35,200 (0.5µm)',
        ach: '150 - 240 /hr',
        cover: '25 - 40%'
    },
    'iso7': {
        name: 'ISO Class 7',
        desc: 'General Assembly: SMT lines and component packaging.',
        part: '352,000 (0.5µm)',
        ach: '60 - 90 /hr',
        cover: '15 - 20%'
    },
    'iso8': {
        name: 'ISO Class 8',
        desc: 'Support Zones: Gowning, corridors, and packaging.',
        part: '3,520,000 (0.5µm)',
        ach: '5 - 48 /hr',
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

    const chamber = document.getElementById('particle-chamber');

    if (!btns.length) return;

    // Set initial state (ISO 5)
    if (chamber) chamber.classList.add('chamber-density-iso5');

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
    const scrollStep = 320; // Approx card width + gap
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
        // Recalculate maxScroll in case of resize
        const currentMaxScroll = track.scrollWidth - track.clientWidth;

        if (track.scrollLeft >= currentMaxScroll - 10) {
            scrollAmount = 0; // Loop back
        } else {
            scrollAmount = Math.min(track.scrollLeft + scrollStep, currentMaxScroll);
        }
        track.scrollTo({ left: scrollAmount, behavior: 'smooth' });
    };

    const moveLeft = () => {
        // Recalculate maxScroll
        const currentMaxScroll = track.scrollWidth - track.clientWidth;

        if (track.scrollLeft <= 10) {
            scrollAmount = currentMaxScroll; // Loop to end
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
                    // Trigger reflow for animation if needed
                    setTimeout(() => card.style.opacity = '1', 10);
                } else {
                    card.style.display = 'none';
                    card.style.opacity = '0';
                }
            });
        });
    });
}
