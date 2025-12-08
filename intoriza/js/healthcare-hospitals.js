/* Healthcare & Hospitals - Interactive Components */

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

// --- SECTION 1: RADAR (Patient Safety Risks) ---
const radarData = {
    'particles': {
        title: 'Airborne Pathogens',
        tag: 'Infection Control',
        desc: 'Bacteria and viruses attached to dust particles can cause surgical site infections (SSI).',
        stat1: '< 10 CFU', label1: 'Bioburden',
        stat2: 'ISO 5/7', label2: 'Standard'
    },
    'esd': {
        title: 'Cross-Contamination',
        tag: 'Patient Safety',
        desc: 'Preventing the spread of infectious agents between isolation rooms and corridors.',
        stat1: 'Negative', label1: 'Pressure',
        stat2: '15 Pa', label2: 'Differential'
    },
    'chemicals': {
        title: 'Sterilization',
        tag: 'VHP / UV-C',
        desc: 'Surfaces must withstand aggressive decontamination agents like Hydrogen Peroxide Vapor.',
        stat1: 'Resistant', label1: 'Panels',
        stat2: 'Seamless', label2: 'Design'
    },
    'audits': {
        title: 'HTM / WHO Compliance',
        tag: 'Regulation',
        desc: 'Meeting strict international healthcare facility standards (HTM 03-01, ISO 14644).',
        stat1: '100%', label1: 'Validation',
        stat2: 'Traceable', label2: 'Records'
    },
    'vibration': {
        title: 'Surgical Precision',
        tag: 'Stability',
        desc: 'Ensuring stable airflow and lighting for microsurgery and imaging equipment.',
        stat1: 'Laminar', label1: 'Flow',
        stat2: 'High Lux', label2: 'Lighting'
    },
    'humidity': {
        title: 'Humidity Control',
        tag: 'Comfort & Safety',
        desc: 'Maintained at 40-60% RH to inhibit bacteria and ensure staff comfort.',
        stat1: '50% ±5%', label1: 'Set Point',
        stat2: 'HVAC', label2: 'Control'
    },
    'temp': {
        title: 'Thermal Control',
        tag: 'Patient Care',
        desc: 'Precise temperature regulation during long surgical procedures.',
        stat1: '18-22°C', label1: 'OT Temp',
        stat2: 'Stable', label2: 'Profile'
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

// --- SECTION 3: CLASSES (Medical Grades) ---
const classData = {
    'iso5': {
        name: 'Ultra Clean (ISO 5)',
        desc: 'Operating Theatres (Ortho/Neuro/Cardiac) & Burn Units.',
        part: '< 1 CFU/m³',
        ach: '> 20 /hr',
        cover: 'Laminar'
    },
    'iso6': {
        name: 'High Dependency (ISO 6)',
        desc: 'Specialized ICUs and Sterile Supply preparation.',
        part: '< 10 CFU/m³',
        ach: '15 - 20 /hr',
        cover: 'HEPA'
    },
    'iso7': {
        name: 'Isolation (ISO 7)',
        desc: 'Infectious Disease Units (Negative Pressure) or Minor Surgery.',
        part: '< 100 CFU/m³',
        ach: '10 - 15 /hr',
        cover: 'Filtered'
    },
    'iso8': {
        name: 'General Ward (ISO 8)',
        desc: 'Clean corridors, recovery rooms, and pharmacy storage.',
        part: '< 200 CFU/m³',
        ach: '6 - 10 /hr',
        cover: 'Basic'
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
    const sCoverLabel = document.querySelector('#spec-cover')?.parentElement?.querySelector('.new-elec-spec-label');


    const chamber = document.getElementById('particle-chamber');

    if (!btns.length) return;

    // Set initial state (ISO 5)
    if (chamber) chamber.classList.add('chamber-density-iso5');
    // Change label for Healthcare
    if (sPartLabel) sPartLabel.textContent = 'Bioburden Limit';
    if (sCoverLabel) sCoverLabel.textContent = 'Airflow Type';

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
