#!/usr/bin/env python3
"""
Script de génération des pages villes pour l'annuaire Agence Web France
Génère une page HTML optimisée SEO pour chaque ville
"""

import json
import os
from pathlib import Path

# Configuration
VILLES_JSON = "villes.json"
OUTPUT_DIR = "villes"
TEMPLATE_FILE = "ville_template.html"

def get_departement(zip_code):
    """Extrait le département du code postal"""
    if zip_code.startswith("97"):
        return zip_code[:3]  # DOM-TOM
    return zip_code[:2]

def get_departement_name(dept_code):
    """Retourne le nom du département"""
    departements = {
        "01": "Ain", "02": "Aisne", "03": "Allier", "04": "Alpes-de-Haute-Provence",
        "05": "Hautes-Alpes", "06": "Alpes-Maritimes", "07": "Ardèche", "08": "Ardennes",
        "09": "Ariège", "10": "Aube", "11": "Aude", "12": "Aveyron",
        "13": "Bouches-du-Rhône", "14": "Calvados", "15": "Cantal", "16": "Charente",
        "17": "Charente-Maritime", "18": "Cher", "19": "Corrèze", "2A": "Corse-du-Sud",
        "2B": "Haute-Corse", "21": "Côte-d'Or", "22": "Côtes-d'Armor", "23": "Creuse",
        "24": "Dordogne", "25": "Doubs", "26": "Drôme", "27": "Eure",
        "28": "Eure-et-Loir", "29": "Finistère", "30": "Gard", "31": "Haute-Garonne",
        "32": "Gers", "33": "Gironde", "34": "Hérault", "35": "Ille-et-Vilaine",
        "36": "Indre", "37": "Indre-et-Loire", "38": "Isère", "39": "Jura",
        "40": "Landes", "41": "Loir-et-Cher", "42": "Loire", "43": "Haute-Loire",
        "44": "Loire-Atlantique", "45": "Loiret", "46": "Lot", "47": "Lot-et-Garonne",
        "48": "Lozère", "49": "Maine-et-Loire", "50": "Manche", "51": "Marne",
        "52": "Haute-Marne", "53": "Mayenne", "54": "Meurthe-et-Moselle", "55": "Meuse",
        "56": "Morbihan", "57": "Moselle", "58": "Nièvre", "59": "Nord",
        "60": "Oise", "61": "Orne", "62": "Pas-de-Calais", "63": "Puy-de-Dôme",
        "64": "Pyrénées-Atlantiques", "65": "Hautes-Pyrénées", "66": "Pyrénées-Orientales",
        "67": "Bas-Rhin", "68": "Haut-Rhin", "69": "Rhône", "70": "Haute-Saône",
        "71": "Saône-et-Loire", "72": "Sarthe", "73": "Savoie", "74": "Haute-Savoie",
        "75": "Paris", "76": "Seine-Maritime", "77": "Seine-et-Marne", "78": "Yvelines",
        "79": "Deux-Sèvres", "80": "Somme", "81": "Tarn", "82": "Tarn-et-Garonne",
        "83": "Var", "84": "Vaucluse", "85": "Vendée", "86": "Vienne",
        "87": "Haute-Vienne", "88": "Vosges", "89": "Yonne", "90": "Territoire de Belfort",
        "91": "Essonne", "92": "Hauts-de-Seine", "93": "Seine-Saint-Denis",
        "94": "Val-de-Marne", "95": "Val-d'Oise",
        "971": "Guadeloupe", "972": "Martinique", "973": "Guyane",
        "974": "La Réunion", "976": "Mayotte"
    }
    return departements.get(dept_code, f"Département {dept_code}")

def generate_page_html(ville):
    """Génère le HTML pour une page ville"""
    name = ville["name"]
    zip_code = ville["zip"]
    slug = ville["slug"]
    dept = get_departement(zip_code)
    dept_name = get_departement_name(dept)

    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <title>Agence Web {name} ({zip_code}) - Création de Sites Internet</title>
    <meta name="description" content="Agence web à {name} ({zip_code}). Création de sites internet, développement web et solutions digitales sur mesure dans le {dept_name}. Devis gratuit.">
    <meta name="keywords" content="agence web {name}, création site internet {name}, développement web {zip_code}, {dept_name}">
    <meta name="author" content="Agence Web France">

    <meta property="og:type" content="website">
    <meta property="og:title" content="Agence Web {name} - Création de Sites Internet">
    <meta property="og:description" content="Votre agence web locale à {name} pour la création de sites professionnels">

    <link rel="canonical" href="https://www.agencewebfrance.fr/villes/agence-web-{slug}.html">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <header id="header" class="header-sticky">
        <nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm">
            <div class="container">
                <a class="navbar-brand fw-bold text-primary" href="../index.html">
                    <i class="bi bi-globe2"></i> Agence Web France
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item"><a class="nav-link" href="../index.html">Accueil</a></li>
                        <li class="nav-item"><a class="nav-link" href="../index.html#services">Services</a></li>
                        <li class="nav-item"><a class="nav-link" href="../index.html#about">À Propos</a></li>
                        <li class="nav-item"><a class="nav-link" href="../index.html#portfolio">Portfolio</a></li>
                        <li class="nav-item"><a class="nav-link active" href="../index.html#annuaire">Annuaire</a></li>
                        <li class="nav-item"><a class="nav-link" href="../index.html#contact">Contact</a></li>
                        <li class="nav-item">
                            <a class="nav-link btn btn-primary text-white ms-lg-3 px-4" href="../index.html#contact">Devis Gratuit</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>

    <section class="city-hero section-padding" style="padding-top: 120px; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);">
        <div class="container">
            <nav aria-label="breadcrumb" class="mb-4">
                <ol class="breadcrumb">
                    <li class="breadcrumb-item"><a href="../index.html">Accueil</a></li>
                    <li class="breadcrumb-item"><a href="../index.html#annuaire">Annuaire</a></li>
                    <li class="breadcrumb-item"><a href="../departements/annuaire-departement-{dept}.html">{dept_name}</a></li>
                    <li class="breadcrumb-item active" aria-current="page">{name}</li>
                </ol>
            </nav>

            <div class="row align-items-center">
                <div class="col-lg-7">
                    <h1 class="display-5 fw-bold mb-4">
                        Agence Web à <span class="text-primary">{name}</span>
                    </h1>
                    <p class="lead mb-4">
                        Votre partenaire digital de confiance à {name} ({zip_code}) pour la création de sites internet
                        professionnels et le développement de solutions web sur mesure dans le {dept_name}.
                    </p>
                    <div class="d-flex gap-3 flex-wrap mb-4">
                        <span class="badge bg-primary fs-6 p-2"><i class="bi bi-geo-alt"></i> {name}</span>
                        <span class="badge bg-secondary fs-6 p-2"><i class="bi bi-mailbox"></i> {zip_code}</span>
                        <span class="badge bg-info fs-6 p-2"><i class="bi bi-map"></i> {dept_name}</span>
                    </div>
                    <div class="d-flex gap-3 flex-wrap">
                        <a href="../index.html#contact" class="btn btn-primary btn-lg px-4">
                            <i class="bi bi-envelope"></i> Demander un Devis
                        </a>
                        <a href="tel:+33123456789" class="btn btn-outline-primary btn-lg px-4">
                            <i class="bi bi-telephone"></i> Nous Appeler
                        </a>
                    </div>
                </div>
                <div class="col-lg-5 text-center mt-4 mt-lg-0">
                    <div class="hero-image-placeholder">
                        <i class="bi bi-building display-1 text-primary"></i>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section-padding">
        <div class="container">
            <h2 class="section-title text-center mb-5">Nos Services à {name}</h2>
            <div class="row g-4">
                <div class="col-md-6 col-lg-4">
                    <div class="service-card card h-100 border-0 shadow-sm">
                        <div class="card-body text-center p-4">
                            <div class="service-icon mb-3">
                                <i class="bi bi-brush display-4 text-primary"></i>
                            </div>
                            <h3 class="h5 fw-bold mb-3">Design Web à {name}</h3>
                            <p class="text-muted">
                                Création de designs modernes et sur mesure pour les entreprises de {name} et du {dept_name}.
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4">
                    <div class="service-card card h-100 border-0 shadow-sm">
                        <div class="card-body text-center p-4">
                            <div class="service-icon mb-3">
                                <i class="bi bi-code-slash display-4 text-primary"></i>
                            </div>
                            <h3 class="h5 fw-bold mb-3">Développement Web</h3>
                            <p class="text-muted">
                                Sites vitrine, e-commerce et applications web pour les professionnels de {name}.
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4">
                    <div class="service-card card h-100 border-0 shadow-sm">
                        <div class="card-body text-center p-4">
                            <div class="service-icon mb-3">
                                <i class="bi bi-graph-up-arrow display-4 text-primary"></i>
                            </div>
                            <h3 class="h5 fw-bold mb-3">SEO Local {name}</h3>
                            <p class="text-muted">
                                Référencement local optimisé pour améliorer votre visibilité à {name} et ses environs.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section-padding bg-light">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6 mb-4 mb-lg-0">
                    <h2 class="h3 fw-bold mb-4">Pourquoi choisir notre agence web à {name} ?</h2>
                    <ul class="list-unstyled">
                        <li class="mb-3 d-flex align-items-start">
                            <i class="bi bi-check-circle-fill text-primary me-3 fs-5"></i>
                            <span><strong>Proximité :</strong> Une équipe à votre écoute dans le {dept_name}</span>
                        </li>
                        <li class="mb-3 d-flex align-items-start">
                            <i class="bi bi-check-circle-fill text-primary me-3 fs-5"></i>
                            <span><strong>Expertise :</strong> Plus de 150 projets réalisés en France</span>
                        </li>
                        <li class="mb-3 d-flex align-items-start">
                            <i class="bi bi-check-circle-fill text-primary me-3 fs-5"></i>
                            <span><strong>Sur mesure :</strong> Solutions adaptées aux entreprises de {name}</span>
                        </li>
                        <li class="mb-3 d-flex align-items-start">
                            <i class="bi bi-check-circle-fill text-primary me-3 fs-5"></i>
                            <span><strong>Accompagnement :</strong> Suivi personnalisé et support réactif</span>
                        </li>
                    </ul>
                </div>
                <div class="col-lg-6">
                    <div class="card border-0 shadow">
                        <div class="card-body p-4">
                            <h3 class="h5 fw-bold mb-4 text-center">Demandez votre devis gratuit</h3>
                            <form>
                                <div class="mb-3">
                                    <input type="text" class="form-control" placeholder="Votre nom" required>
                                </div>
                                <div class="mb-3">
                                    <input type="email" class="form-control" placeholder="Votre email" required>
                                </div>
                                <div class="mb-3">
                                    <input type="tel" class="form-control" placeholder="Téléphone">
                                </div>
                                <div class="mb-3">
                                    <textarea class="form-control" rows="3" placeholder="Décrivez votre projet à {name}"></textarea>
                                </div>
                                <button type="submit" class="btn btn-primary w-100">
                                    <i class="bi bi-send"></i> Envoyer ma demande
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="cta-section section-padding bg-primary text-white">
        <div class="container text-center">
            <h2 class="display-6 fw-bold mb-4">Prêt à lancer votre projet web à {name} ?</h2>
            <p class="lead mb-4">Contactez notre équipe dès aujourd'hui pour un devis gratuit et personnalisé.</p>
            <a href="../index.html#contact" class="btn btn-light btn-lg px-5">
                <i class="bi bi-rocket-takeoff"></i> Démarrer mon projet
            </a>
        </div>
    </section>

    <footer class="footer bg-dark text-white py-5">
        <div class="container">
            <div class="row g-4">
                <div class="col-lg-4">
                    <h5 class="fw-bold mb-3"><i class="bi bi-globe2"></i> Agence Web France</h5>
                    <p class="text-white-50">
                        Votre partenaire de confiance pour tous vos projets web à {name} et partout en France.
                    </p>
                </div>
                <div class="col-lg-4">
                    <h5 class="fw-bold mb-3">Navigation</h5>
                    <ul class="list-unstyled">
                        <li class="mb-2"><a href="../index.html" class="text-white-50 text-decoration-none">Accueil</a></li>
                        <li class="mb-2"><a href="../index.html#services" class="text-white-50 text-decoration-none">Services</a></li>
                        <li class="mb-2"><a href="../index.html#annuaire" class="text-white-50 text-decoration-none">Annuaire</a></li>
                        <li class="mb-2"><a href="../index.html#contact" class="text-white-50 text-decoration-none">Contact</a></li>
                    </ul>
                </div>
                <div class="col-lg-4">
                    <h5 class="fw-bold mb-3">Contact</h5>
                    <ul class="list-unstyled text-white-50">
                        <li class="mb-2"><i class="bi bi-geo-alt"></i> Paris, France</li>
                        <li class="mb-2"><i class="bi bi-telephone"></i> +33 1 23 45 67 89</li>
                        <li class="mb-2"><i class="bi bi-envelope"></i> contact@agencewebfrance.fr</li>
                    </ul>
                </div>
            </div>
            <hr class="my-4 bg-white opacity-25">
            <p class="text-center text-white-50 mb-0">&copy; 2024 Agence Web France - Agence Web {name}. Tous droits réservés.</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="../script.js"></script>
</body>
</html>'''

def main():
    print("=" * 60)
    print("Génération des pages villes - Agence Web France")
    print("=" * 60)

    # Créer le dossier de sortie
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"\n✓ Dossier '{OUTPUT_DIR}/' créé")

    # Charger les villes
    with open(VILLES_JSON, 'r', encoding='utf-8') as f:
        villes = json.load(f)

    total = len(villes)
    print(f"✓ {total} villes chargées depuis {VILLES_JSON}")
    print("\nGénération des pages en cours...")

    # Organiser par département pour les stats
    departements = {}

    for i, ville in enumerate(villes, 1):
        dept = get_departement(ville["zip"])
        if dept not in departements:
            departements[dept] = []
        departements[dept].append(ville)

        # Générer la page
        filename = f"agence-web-{ville['slug']}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)

        html_content = generate_page_html(ville)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)

        # Afficher la progression
        if i % 1000 == 0 or i == total:
            percent = (i / total) * 100
            print(f"  [{i}/{total}] {percent:.1f}% - Dernière: {ville['name']}")

    # Générer le fichier JSON des départements pour la homepage
    dept_summary = []
    for dept, villes_dept in sorted(departements.items()):
        dept_summary.append({
            "code": dept,
            "name": get_departement_name(dept),
            "count": len(villes_dept),
            "villes": [{"name": v["name"], "slug": v["slug"], "zip": v["zip"]} for v in villes_dept]
        })

    with open("departements.json", 'w', encoding='utf-8') as f:
        json.dump(dept_summary, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Fichier departements.json créé")
    print(f"\n{'=' * 60}")
    print(f"TERMINÉ !")
    print(f"- {total} pages générées dans /{OUTPUT_DIR}/")
    print(f"- {len(departements)} départements")
    print(f"{'=' * 60}")

if __name__ == "__main__":
    main()
