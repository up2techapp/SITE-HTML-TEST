/**
 * Agence Web France - Scripts JavaScript
 * Interactions et fonctionnalités dynamiques
 */

// ===========================
// Variables globales
// ===========================
let lastScrollTop = 0;
const header = document.getElementById('header');
const scrollTopBtn = document.getElementById('scrollTopBtn');

// ===========================
// Initialisation au chargement de la page
// ===========================
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Site Agence Web France chargé avec succès');

    // Initialiser toutes les fonctionnalités
    initScrollEffects();
    initSmoothScroll();
    initNavbarHighlight();
    initContactForm();
    initAnimationsOnScroll();
    initTypingEffect();
});

// ===========================
// Effets de scroll (header sticky + bouton retour en haut)
// ===========================
function initScrollEffects() {
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        // Header sticky avec effet d'ombre au scroll
        if (scrollTop > 100) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        // Bouton "Retour en haut"
        if (scrollTop > 300) {
            scrollTopBtn.classList.add('show');
        } else {
            scrollTopBtn.classList.remove('show');
        }

        lastScrollTop = scrollTop;
    });

    // Click sur le bouton retour en haut
    scrollTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// ===========================
// Smooth scroll pour les liens d'ancrage
// ===========================
function initSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');

            // Ignorer les liens vides ou #
            if (targetId === '#' || targetId === '') {
                e.preventDefault();
                return;
            }

            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                e.preventDefault();

                // Fermer le menu mobile si ouvert
                const navbarCollapse = document.querySelector('.navbar-collapse');
                if (navbarCollapse.classList.contains('show')) {
                    const bsCollapse = new bootstrap.Collapse(navbarCollapse, {
                        toggle: false
                    });
                    bsCollapse.hide();
                }

                // Calculer la position avec offset pour le header sticky
                const headerHeight = header.offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// ===========================
// Mise en surbrillance du lien actif dans la navbar
// ===========================
function initNavbarHighlight() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link[href^="#"]');

    window.addEventListener('scroll', function() {
        const scrollPosition = window.pageYOffset + 150; // Offset pour le header

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    });
}

// ===========================
// Gestion du formulaire de contact
// ===========================
function initContactForm() {
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            // Validation Bootstrap
            if (!contactForm.checkValidity()) {
                e.stopPropagation();
                contactForm.classList.add('was-validated');
                return;
            }

            // Récupérer les données du formulaire
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                subject: document.getElementById('subject').value,
                message: document.getElementById('message').value
            };

            // Simuler l'envoi du formulaire (à remplacer par un vrai appel API)
            console.log('📧 Formulaire soumis:', formData);

            // Afficher un message de succès
            showNotification('Message envoyé avec succès! Nous vous répondrons dans les plus brefs délais.', 'success');

            // Réinitialiser le formulaire
            contactForm.reset();
            contactForm.classList.remove('was-validated');
        });
    }
}

// ===========================
// Animations au scroll (fade-in)
// ===========================
function initAnimationsOnScroll() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observer les éléments à animer
    const elementsToAnimate = document.querySelectorAll('.service-card, .portfolio-card, .stat-box');
    elementsToAnimate.forEach(element => {
        observer.observe(element);
    });
}

// ===========================
// Effet de typing pour le titre (optionnel)
// ===========================
function initTypingEffect() {
    // Cette fonction peut être activée pour un effet de machine à écrire
    // Actuellement désactivée pour garder un design simple
}

// ===========================
// Système de notifications (Toast)
// ===========================
function showNotification(message, type = 'info') {
    // Créer l'élément de notification
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} notification-toast`;
    notification.innerHTML = `
        <div class="d-flex align-items-center">
            <i class="bi bi-check-circle-fill me-2"></i>
            <span>${message}</span>
        </div>
    `;

    // Ajouter les styles inline
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        z-index: 9999;
        min-width: 300px;
        box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
        animation: slideInRight 0.3s ease-out;
    `;

    // Ajouter au DOM
    document.body.appendChild(notification);

    // Retirer après 5 secondes
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease-in';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 5000);
}

// Ajouter les animations CSS pour les notifications
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }

    .notification-toast {
        border-radius: 10px;
        border: none;
    }
`;
document.head.appendChild(style);

// ===========================
// Gestion des cartes service (hover effects additionnels)
// ===========================
document.querySelectorAll('.service-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-10px) scale(1.02)';
    });

    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) scale(1)';
    });
});

// ===========================
// Gestion des cartes portfolio (hover effects)
// ===========================
document.querySelectorAll('.portfolio-card').forEach(card => {
    card.addEventListener('click', function() {
        // Simuler l'ouverture d'un modal ou redirection
        console.log('🖼️ Projet sélectionné:', this.querySelector('h3').textContent);
        showNotification('Fonctionnalité à venir : Vue détaillée du projet', 'info');
    });
});

// ===========================
// Préchargement et optimisation des images
// ===========================
function preloadImages() {
    // Fonction pour précharger les images si nécessaire
    // Actuellement pas d'images externes, mais prêt pour l'avenir
    console.log('✓ Optimisation des ressources terminée');
}

// ===========================
// Performance monitoring (optionnel)
// ===========================
window.addEventListener('load', function() {
    const loadTime = window.performance.timing.domContentLoadedEventEnd - window.performance.timing.navigationStart;
    console.log(`⚡ Page chargée en ${loadTime}ms`);

    // Google Analytics ou autre tracking pourrait être ajouté ici
});

// ===========================
// Gestion des erreurs globales
// ===========================
window.addEventListener('error', function(e) {
    console.error('❌ Erreur détectée:', e.message);
    // En production, envoyer les erreurs à un service de monitoring
});

// ===========================
// Détection de connexion internet
// ===========================
window.addEventListener('online', function() {
    showNotification('Connexion rétablie', 'success');
});

window.addEventListener('offline', function() {
    showNotification('Connexion internet perdue', 'warning');
});

// ===========================
// Easter egg (optionnel)
// ===========================
let clickCount = 0;
const logo = document.querySelector('.navbar-brand');

if (logo) {
    logo.addEventListener('click', function(e) {
        clickCount++;
        if (clickCount >= 5) {
            console.log('🎉 Easter egg trouvé! Vous avez cliqué 5 fois sur le logo!');
            showNotification('🎉 Easter egg débloqué! Merci de visiter notre site!', 'success');
            clickCount = 0;
        }
    });
}

// ===========================
// Annuaire - Recherche de villes
// ===========================
let villesData = null;
let departementsData = null;

// Charger les données des villes
async function loadVillesData() {
    try {
        const response = await fetch('villes.json');
        villesData = await response.json();
        console.log(`✓ ${villesData.length} villes chargées`);
    } catch (error) {
        console.error('Erreur chargement villes:', error);
    }
}

// Charger les données des départements
async function loadDepartementsData() {
    try {
        const response = await fetch('departements.json');
        departementsData = await response.json();
        console.log(`✓ ${departementsData.length} départements chargés`);
    } catch (error) {
        console.error('Erreur chargement départements:', error);
    }
}

// Initialiser la recherche de villes
function initCitySearch() {
    const searchInput = document.getElementById('citySearch');
    const searchResults = document.getElementById('searchResults');

    if (!searchInput || !searchResults) return;

    let searchTimeout;

    searchInput.addEventListener('input', function() {
        const query = this.value.trim().toLowerCase();

        clearTimeout(searchTimeout);

        if (query.length < 2) {
            searchResults.classList.remove('show');
            searchResults.innerHTML = '';
            return;
        }

        searchTimeout = setTimeout(() => {
            if (!villesData) {
                searchResults.innerHTML = '<div class="p-3 text-muted">Chargement...</div>';
                searchResults.classList.add('show');
                return;
            }

            // Rechercher les villes correspondantes
            const results = villesData
                .filter(v =>
                    v.name.toLowerCase().includes(query) ||
                    v.zip.includes(query)
                )
                .slice(0, 10); // Limiter à 10 résultats

            if (results.length === 0) {
                searchResults.innerHTML = '<div class="p-3 text-muted">Aucune ville trouvée</div>';
                searchResults.classList.add('show');
                return;
            }

            // Afficher les résultats
            searchResults.innerHTML = results.map(v => `
                <a href="villes/agence-web-${v.slug}.html" class="search-result-item text-decoration-none">
                    <span class="city-name">${v.name}</span>
                    <span class="city-zip">${v.zip}</span>
                </a>
            `).join('');
            searchResults.classList.add('show');
        }, 300);
    });

    // Fermer les résultats si on clique ailleurs
    document.addEventListener('click', function(e) {
        if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
            searchResults.classList.remove('show');
        }
    });

    // Navigation clavier
    searchInput.addEventListener('keydown', function(e) {
        const items = searchResults.querySelectorAll('.search-result-item');
        const activeItem = searchResults.querySelector('.search-result-item.active');
        let index = Array.from(items).indexOf(activeItem);

        if (e.key === 'ArrowDown') {
            e.preventDefault();
            if (index < items.length - 1) {
                items.forEach(i => i.classList.remove('active'));
                items[index + 1].classList.add('active');
                items[index + 1].scrollIntoView({ block: 'nearest' });
            }
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            if (index > 0) {
                items.forEach(i => i.classList.remove('active'));
                items[index - 1].classList.add('active');
                items[index - 1].scrollIntoView({ block: 'nearest' });
            }
        } else if (e.key === 'Enter') {
            e.preventDefault();
            if (activeItem) {
                window.location.href = activeItem.getAttribute('href');
            } else if (items.length > 0) {
                window.location.href = items[0].getAttribute('href');
            }
        }
    });
}

// Initialiser les liens de départements
function initDeptLinks() {
    const deptLinks = document.querySelectorAll('.dept-link');
    const modal = document.getElementById('deptModal');
    const modalTitle = document.getElementById('deptModalTitle');
    const modalContent = document.getElementById('deptModalContent');

    if (!modal || !modalTitle || !modalContent) return;

    const bsModal = new bootstrap.Modal(modal);

    deptLinks.forEach(link => {
        link.addEventListener('click', async function(e) {
            e.preventDefault();
            const deptCode = this.getAttribute('data-dept');
            const deptName = this.textContent.trim();

            modalTitle.textContent = deptName;
            modalContent.innerHTML = '<div class="col-12 text-center"><div class="spinner-border text-primary" role="status"></div></div>';
            bsModal.show();

            // Charger les données si pas encore fait
            if (!departementsData) {
                await loadDepartementsData();
            }

            // Trouver le département
            const dept = departementsData.find(d => d.code === deptCode);

            if (dept && dept.villes) {
                modalContent.innerHTML = dept.villes.map(v => `
                    <div class="col-6 col-md-4 col-lg-3">
                        <a href="villes/agence-web-${v.slug}.html">${v.name}</a>
                    </div>
                `).join('');
            } else {
                modalContent.innerHTML = '<div class="col-12 text-center text-muted">Aucune ville trouvée</div>';
            }
        });
    });
}

// Charger les données et initialiser au démarrage
document.addEventListener('DOMContentLoaded', function() {
    loadVillesData();
    initCitySearch();
    initDeptLinks();
});

// ===========================
// Exports pour modules (si nécessaire)
// ===========================
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        showNotification,
        initScrollEffects,
        initSmoothScroll,
        initCitySearch,
        initDeptLinks
    };
}

// Message de bienvenue dans la console
console.log('%c🌐 Agence Web France', 'font-size: 20px; font-weight: bold; color: #0d6efd;');
console.log('%cSite développé avec ❤️ et expertise', 'font-size: 14px; color: #6c757d;');
console.log('%cVous cherchez à créer votre site? Contactez-nous!', 'font-size: 12px; color: #198754;');
