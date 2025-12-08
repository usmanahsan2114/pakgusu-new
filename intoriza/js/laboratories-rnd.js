/* Laboratories & R&D - Interactive Components */

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

// --- SECTION 1: RADAR (Lab Risks) ---
const radarData = {
    'particles': {
        title: 'Sample Contamination',
        tag: 'Analytical Integrity',
        desc: 'Preventing cross-contamination in trace analysis and PCR workflows.',
        stat1: '< 0.5 µm', label1: 'Filtration',
        stat2: 'ISO 5', label2: 'Zone'
    },
    'esd': {
        title: 'Chemical Safety',
        tag: 'Fume Control',
        desc: 'Protecting personnel from hazardous fumes and vapors.',
        stat1: '100 fpm', label1: 'Face Velocity',
        stat2: 'Negative', label2: 'Pressure'
    },
    'chemicals': {
        title: 'Chemical Resistance',
        tag: 'Durability',
        desc: 'Surfaces must withstand microbiological stains, acids, and solvents.',
        stat1: 'Epoxy', label1: 'Worktops',
        stat2: 'Phenolic', label2: 'Walls'
    },
    'audits': {
        title: 'GLP / ISO 17025',
        tag: 'Compliance',
        desc: 'Ensuring laboratory environments meet accreditation standards.',
        stat1: 'Annual', label1: 'Validation',
        stat2: 'DQ/IQ/OQ', label2: 'Qual'
    },
    'vibration': {
        title: 'Metrology Stability',
        tag: 'Precision',
        desc: 'Vibration isolation for electron microscopes and balances.',
        stat1: 'VC-E', label1: 'Curve',
        stat2: 'Heavy', label2: 'Base'
    },
    'humidity': {
        title: 'Environmental Stress',
        tag: 'Stability',
        desc: 'Controlling RH for hygroscopic powders and equipment calibration.',
        stat1: '45% ±5%', label1: 'Set Point',
        stat2: 'Tight', label2: 'Tolerance'
    },
    'temp': {
        title: 'Thermal Stability',
        tag: 'Calibration',
        desc: 'Holding temperature constant for dimensional measurement labs.',
        stat1: '20°C ±0.5', label1: 'Temp',
        stat2: 'Soak', label2: 'Time'
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

// --- SECTION 3: CLASSES (BSL / Lab Types) ---
const classData = {
    'iso5': {
        name: 'BSL-3 / High Containment',
        desc: 'For handling indigenous or exotic agents which may cause serious disease.',
        part: 'Directional',
        ach: 'HEPA Out',
        cover: 'Neg Press'
    },
    'iso6': {
        name: 'Analytical Lab (ISO 6)',
        desc: 'Trace metal analysis and ultra-clean research environments.',
        part: '< 1k part',
        ach: '30-40 /hr',
        cover: 'Laminar'
    },
    'iso7': {
        name: 'Microbiology (BSL-2)',
        desc: 'Standard lab for moderate-risk agents. Biosafety cabinets used.',
        part: 'Clean',
        ach: '15-20 /hr',
        cover: 'Mixed'
    },
    'iso8': {
        name: 'General Lab (ISO 8)',
        desc: 'R&D, QA/QC, and teaching laboratories with controlled access.',
        part: 'Controlled',
        ach: '10-15 /hr',
        cover: 'Turbulent'
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
    const sAchLabel = document.querySelector('#spec-ach')?.parentElement?.querySelector('.new-elec-spec-label');


    const chamber = document.getElementById('particle-chamber');

    if (!btns.length) return;

    // Change labels for Lab
    if (sPartLabel) sPartLabel.textContent = 'Airflow Pattern';
    if (sAchLabel) sAchLabel.textContent = 'Exhaust / Recirc';


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
