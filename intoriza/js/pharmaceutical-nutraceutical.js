/* Pharmaceutical & Nutraceutical - Interactive Components */

document.addEventListener('DOMContentLoaded', () => {
    try { initRadar(); } catch (e) { console.error("Radar Init Error:", e); }
    try { initBlueprint(); } catch (e) { console.error("Blueprint Init Error:", e); }
    try { initClasses(); } catch (e) { console.error("Classes Init Error:", e); }
    try { initCarousel(); } catch (e) { console.error("Carousel Init Error:", e); }
    try { initProductFilters(); } catch (e) { console.error("Product Filter Init Error:", e); }

    // Safety fallback
    setTimeout(() => {
        const loader = document.querySelector('.loading-area');
        if (loader) {
            loader.style.transition = 'opacity 0.5s ease';
            loader.style.opacity = '0';
            setTimeout(() => loader.style.display = 'none', 500);
        }
    }, 2000);
});

// --- SECTION 1: RADAR (Pharma Risks) ---
const radarData = {
    'particles': {
        title: 'Cross-Contamination',
        tag: 'GMP Critical',
        desc: 'Preventing mix-ups and cross-contamination between different drug products.',
        stat1: 'Zero', label1: 'Mix-up',
        stat2: '100%', label2: 'Segregation'
    },
    'esd': {
        title: 'Microbial Control',
        tag: 'Sterility',
        desc: 'Stringent bioburden limits for sterile injectable manufacturing (Annex 1).',
        stat1: '< 1 CFU', label1: 'Grade A',
        stat2: 'Daily', label2: 'Monitoring'
    },
    'chemicals': {
        title: 'Cleaning Validation',
        tag: 'Residue',
        desc: 'Ensuring surfaces can be cleaned to remove active pharmaceutical ingredients (APIs).',
        stat1: 'TOC', label1: 'Limit',
        stat2: 'Visual', label2: 'Clean'
    },
    'audits': {
        title: 'Regulatory Compliance',
        tag: 'FDA / WHO',
        desc: 'Adherence to cGMP, EU GMP Annex 1, and WHO guidelines for facility design.',
        stat1: 'Pass', label1: 'Audit',
        stat2: 'QMS', label2: 'System'
    },
    'vibration': {
        title: 'Containment',
        tag: 'OEB / OEL',
        desc: 'Safe handling of potent compounds (HPAPI) protecting operators and environment.',
        stat1: 'Negative', label1: 'Pressure',
        stat2: 'BIBO', label2: 'Filter'
    },
    'humidity': {
        title: 'Powder Handling',
        tag: 'Hygroscopic',
        desc: 'Humidity control (RH < 30%) for moisture-sensitive powders and tablets.',
        stat1: '30-45%', label1: 'Range',
        stat2: 'Stable', label2: 'Product'
    },
    'temp': {
        title: 'Thermal Mapping',
        tag: 'Stability',
        desc: 'Uniform temperature distribution for product stability and warehousing.',
        stat1: '20-25°C', label1: 'CRT',
        stat2: 'Mapped', label2: 'Area'
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

    // Initial state
    if (pTitle) {
        // Set initial to Microbes or Audit
        const d = radarData['esd']; // Microbes
        pTitle.textContent = d.title;
        pTag.textContent = d.tag;
        pDesc.textContent = d.desc;
        pS1Val.textContent = d.stat1;
        pS1Lab.textContent = d.label1;
        pS2Val.textContent = d.stat2;
        pS2Lab.textContent = d.label2;
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

// --- SECTION 3: CLASSES (GMP Grades) ---
const classData = {
    'iso5': {
        name: 'Grade A (ISO 5)',
        desc: 'Critical zone for high-risk operations like aseptic filling and open ampoules.',
        part: 'Laminar',
        ach: '0.45 m/s', // Velocity usually cited for Grade A
        cover: '100% HEPA'
    },
    'iso6': {
        name: 'Grade B (ISO 5/7)',
        desc: 'Background environment for Grade A zones. Requires aseptic gowning.',
        part: 'Turbulent',
        ach: '> 60 /hr',
        cover: 'High'
    },
    'iso7': {
        name: 'Grade C (ISO 7)',
        desc: 'Clean areas for solution preparation and filling of non-sterile products.',
        part: 'Turbulent',
        ach: '30-40 /hr',
        cover: 'Standard'
    },
    'iso8': {
        name: 'Grade D (ISO 8)',
        desc: 'Handling of components after washing. Secondary packaging and gowning.',
        part: 'Controlled',
        ach: '15-20 /hr',
        cover: 'Low'
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

    if (sPartLabel) sPartLabel.textContent = 'Airflow Pattern';

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
