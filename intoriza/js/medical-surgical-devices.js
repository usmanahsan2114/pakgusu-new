/* Medical & Surgical Devices - Interactive Components */

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

// --- SECTION 1: RADAR (MedTech Risks) ---
const radarData = {
    'particles': {
        title: 'Particulate Matter',
        tag: 'Foreign Body Risk',
        desc: 'Controlling non-viable particles that could cause immune reactions in implants.',
        stat1: 'ISO 7', label1: 'Target',
        stat2: 'Zero', label2: 'Visible'
    },
    'esd': {
        title: 'Bioburden Control',
        tag: 'Pre-Sterilization',
        desc: 'Minimizing microbial load on devices before they enter the sterilization barrier.',
        stat1: '< 100 CFU', label1: 'Standard',
        stat2: 'Routine', label2: 'Test'
    },
    'chemicals': {
        title: 'Sterilization Prep',
        tag: 'Packaging',
        desc: 'Ensuring tyvek pouches and sterile barriers are sealed in clean environments.',
        stat1: 'Validation', label1: 'Seal',
        stat2: 'Integrity', label2: 'Check'
    },
    'audits': {
        title: 'ISO 13485',
        tag: 'Compliance',
        desc: 'Meeting regulatory requirements for Medical Device Manufacturing (QMS).',
        stat1: 'Class I-III', label1: 'Device',
        stat2: 'Yearly', label2: 'Audit'
    },
    'vibration': {
        title: 'Precision Assembly',
        tag: 'Micro-Mechanics',
        desc: 'Stable environments for microscope-aided assembly of catheters and stents.',
        stat1: 'Stable', label1: 'Platform',
        stat2: 'High', label2: 'Acuity'
    },
    'humidity': {
        title: 'Polymer Stability',
        tag: 'Shelf Life',
        desc: 'Humidity control to prevent degradation of bio-absorbable polymers.',
        stat1: '< 30% RH', label1: 'Dry',
        stat2: 'Sealed', label2: 'Area'
    },
    'temp': {
        title: 'Comfort & Cure',
        tag: 'Process',
        desc: 'Temperature control for UV curing adhesives and operator gowning comfort.',
        stat1: '21°C', label1: 'Set',
        stat2: 'Curing', label2: 'Rate'
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
        // Set initial to Bioburden or Audit
        const d = radarData['audits'];
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

// --- SECTION 3: CLASSES (Medical Grades) ---
const classData = {
    'iso5': {
        name: 'Implant Handling (ISO 5)',
        desc: 'Critical zone for exposing bacterial-sensitive implants before packaging.',
        part: 'Laminar',
        ach: '> 240 /hr',
        cover: '100% HEPA'
    },
    'iso6': {
        name: 'Critical Assembly (ISO 6)',
        desc: 'Assembly of complex catheters and valves requiring low particulate counts.',
        part: 'Mixed',
        ach: '50-60 /hr',
        cover: 'High'
    },
    'iso7': {
        name: 'General Assembly (ISO 7)',
        desc: 'Standard environment for most medical device assembly and packaging lines.',
        part: 'Turbulent',
        ach: '30-40 /hr',
        cover: 'Standard'
    },
    'iso8': {
        name: 'Molding / CNC (ISO 8)',
        desc: 'Injection molding (clean room) and component machining areas.',
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

    if (sPartLabel) sPartLabel.textContent = 'Airflow Type';

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
