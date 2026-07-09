from pathlib import Path
import base64
from datetime import date
import re

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import seaborn as sns

st.set_page_config(page_title="Portfolio Data Analyst", layout="wide")

REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECTS_ROOT = REPO_ROOT / "projets"
DATA_ROOT = REPO_ROOT / "data"

PROJECT_DOMAINS = {
    "EPIC 1": {
        "title": "Analyse & Data Visualisation",
        "us": [2, 8, 9, 10],
        "color": "#2A9D8F",
    },
    "EPIC 2": {
        "title": "Programmation & Analyse avancée",
        "us": [4, 6, 11, 12],
        "color": "#1D3557",
    },
    "EPIC 3": {
        "title": "SQL & Bases de donnees",
        "us": [3, 5],
        "color": "#E07A5F",
    },
    "EPIC 4": {
        "title": "DataViz & Pilotage",
        "us": [7],
        "color": "#F2CC8F",
    },
    "EPIC 5": {
        "title": "Portfolio & Communication",
        "us": [13],
        "color": "#8D99AE",
    },
}

GANTT_DATA = [
    {"us": "US3", "title": "Requetes SQL", "start": 1.0, "duration": 1.25},
    {"us": "US2", "title": "Analyse e-commerce", "start": 2.0, "duration": 2.0},
    {"us": "US5", "title": "Base immobiliere SQL", "start": 3.0, "duration": 2.5},
    {"us": "US7", "title": "Dashboard Power BI", "start": 4.0, "duration": 2.5},
    {"us": "US4", "title": "Etude sante publique", "start": 5.0, "duration": 3.33},
    {"us": "US6", "title": "Optimisation boutique", "start": 6.0, "duration": 2.92},
    {"us": "US8", "title": "Egalite F/H", "start": 7.0, "duration": 2.5},
    {"us": "US9", "title": "Librairie", "start": 8.0, "duration": 3.75},
    {"us": "US10", "title": "Eau potable", "start": 9.0, "duration": 2.92},
    {"us": "US11", "title": "Etude de marche", "start": 10.0, "duration": 3.75},
    {"us": "US12", "title": "Faux billets", "start": 11.0, "duration": 2.92},
    {"us": "US13", "title": "Portfolio", "start": 12.0, "duration": 1.0},
]

FEATURED_PROJECTS = {
    "US6": "Fiabilisation e-commerce: Python, controle qualite et dashboard Streamlit",
    "US7": "Pilotage decisionnel: Power BI, alertes et indicateurs actionnables",
    "US12": "Detection de risque: machine learning, API FastAPI et prediction",
}

DATA_ANALYST_PROOFS = [
    {
        "competence": "Cadrer un besoin metier",
        "preuve": "Projet Bottleneck: rapprochement ERP, Web et table de liaison",
        "indicateur": "3 sources consolidees, 825 produits analyses",
    },
    {
        "competence": "Controler la qualite des donnees",
        "preuve": "Notebook P13 Partie 1 ameliore + scripts Python reutilisables",
        "indicateur": "18 controles qualite, 11 OK, 1 correction stock finalisee",
    },
    {
        "competence": "Produire des KPI exploitables",
        "preuve": "Dashboard et dataviz e-commerce",
        "indicateur": "143 680 EUR de CA calcule, 92 ruptures ou stocks nuls",
    },
    {
        "competence": "Visualiser pour la decision",
        "preuve": "Power BI SANITORAL et graphiques interactifs Bottleneck",
        "indicateur": "Vues par persona, seuil d'alerte superieur a 15%",
    },
    {
        "competence": "Documenter et rendre partageable",
        "preuve": "README, captures, liens publics et tracabilite IA",
        "indicateur": "Documentation consultable comme un espace partageable",
    },
]

COMPETENCY_BLOCKS = [
    {
        "bloc": "Bloc 1",
        "title": "Structurer et gerer les donnees",
        "skills": ["SQL", "modelisation", "qualite", "documentation"],
        "proof": "Base immobiliere, requetes SQL, controles Bottleneck",
    },
    {
        "bloc": "Bloc 2",
        "title": "Identifier, collecter et analyser",
        "skills": ["Python", "Pandas", "EDA", "nettoyage"],
        "proof": "Fiabilisation e-commerce et analyses metier",
    },
    {
        "bloc": "Bloc 3",
        "title": "Visualiser et restituer",
        "skills": ["Power BI", "Streamlit", "storytelling", "KPI"],
        "proof": "Dashboard SANITORAL et dataviz Bottleneck",
    },
    {
        "bloc": "Bloc 4",
        "title": "Piloter un projet data",
        "skills": ["planning", "perimetre", "risques", "feedback"],
        "proof": "Timeline soutenances, mentorat et jalons documentes",
    },
    {
        "bloc": "Specialisation",
        "title": "Statistiques et machine learning",
        "skills": ["classification", "evaluation", "API", "prediction"],
        "proof": "Detection de faux billets avec modele exporte",
    },
]

PROJECT_LABELS = {
    "P1": "Cadrage formation",
    "P2": "Analyse e-commerce",
    "P3": "SQL et requetes",
    "P4": "Sante publique",
    "P5": "Base immobiliere",
    "P6": "Fiabilisation e-commerce",
    "P7": "Dashboard decisionnel",
    "P8": "Egalite F/H",
    "P9": "Librairie",
    "P10": "Eau potable",
    "P11": "Etude de marche",
    "P12": "Detection de faux billets",
    "P13": "Portfolio professionnel",
    "P14": "Stage et bilan",
}

EVENT_WEIGHTS = {
    "Compte-rendu mentorat": 2,
    "Point projet": 1,
    "Transition projet": 2,
    "Soutenance blanche": 3,
    "Reprise demandee": 2,
    "Stage / terrain": 3,
}

US_ICONS = {
    "US2": "📊",
    "US3": "🗄️",
    "US4": "🩺",
    "US5": "🏘️",
    "US6": "⚙️",
    "US7": "📈",
    "US8": "⚖️",
    "US9": "📚",
    "US10": "💧",
    "US11": "🧭",
    "US12": "🛡️",
    "US13": "🧩",
}


def _to_posix(path: Path) -> str:
    return str(path).replace("\\", "/")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _parse_date_from_name(file_name: str) -> tuple[pd.Timestamp | None, str]:
    match = re.search(r"(20\d{6})", file_name)
    if not match:
        return None, "Sans date dans le nom de fichier"

    raw_date = match.group(1)
    parsed_date = pd.to_datetime(raw_date, format="%Y%m%d", errors="coerce")
    if pd.isna(parsed_date):
        return None, f"Date illisible: {raw_date}"

    note = ""
    if file_name.startswith("P2_P3_20261222"):
        parsed_date = pd.Timestamp("2025-12-22")
        note = "Date corrigee pour le mockup: 20261222 semble correspondre a 20251222."
    elif parsed_date.date() > date.today():
        note = "Date future a verifier avant publication."

    return parsed_date, note


def _project_codes_from_name(file_name: str) -> list[str]:
    codes = re.findall(r"P\d+", file_name.upper())
    return sorted(set(codes), key=lambda code: int(code[1:]))


def _classify_timeline_event(file_path: Path) -> str:
    name = file_path.stem.lower()
    suffix = file_path.suffix.lower()

    if "soutenance_blanche" in name:
        return "Soutenance blanche"
    if "a_areprendre" in name or "a-reprendre" in name:
        return "Reprise demandee"
    if name.startswith("stage"):
        return "Stage / terrain"
    if suffix == ".docx":
        return "Compte-rendu mentorat"
    if len(_project_codes_from_name(file_path.name)) > 1:
        return "Transition projet"
    return "Point projet"


@st.cache_data(show_spinner=False)
def _load_timeline_events(data_root: Path) -> pd.DataFrame:
    rows = []
    if not data_root.exists():
        return pd.DataFrame(rows)

    for file_path in sorted(data_root.iterdir(), key=lambda path: path.name):
        if not file_path.is_file():
            continue

        event_date, note = _parse_date_from_name(file_path.name)
        project_codes = _project_codes_from_name(file_path.name)
        if event_date is None or not project_codes:
            continue

        event_type = _classify_timeline_event(file_path)
        project_names = [PROJECT_LABELS.get(code, code) for code in project_codes]
        rows.append(
            {
                "date": event_date,
                "projet": " / ".join(project_codes),
                "projet_label": " / ".join(project_names),
                "type": event_type,
                "preuve": file_path.name,
                "points_qualite": EVENT_WEIGHTS.get(event_type, 1),
                "note": note,
                "extension": file_path.suffix.lower(),
            }
        )

    if not rows:
        return pd.DataFrame(rows)

    events = pd.DataFrame(rows).sort_values(["date", "projet", "preuve"]).reset_index(drop=True)
    events["jalon"] = range(1, len(events) + 1)
    events["points_qualite_cumules"] = events["points_qualite"].cumsum()
    return events


def _build_project_gantt(events: pd.DataFrame) -> pd.DataFrame:
    rows = []
    if events.empty:
        return pd.DataFrame(rows)

    for project_code in sorted(
        {code for value in events["projet"] for code in value.split(" / ")},
        key=lambda code: int(code[1:]) if code[1:].isdigit() else 999,
    ):
        project_events = events[events["projet"].str.contains(project_code, regex=False)]
        start_date = project_events["date"].min()
        end_date = project_events["date"].max()
        rows.append(
            {
                "projet": project_code,
                "projet_label": PROJECT_LABELS.get(project_code, project_code),
                "debut": start_date,
                "fin": end_date,
                "duree_jours": max((end_date - start_date).days, 1),
                "jalons": len(project_events),
                "points_qualite": int(project_events["points_qualite"].sum()),
            }
        )

    return pd.DataFrame(rows)


def _render_timeline_chart(events: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(12, 6.5))
    labels = list(dict.fromkeys(events["projet_label"].tolist()))
    y_positions = {label: index for index, label in enumerate(labels)}
    colors = {
        "Point projet": "#2A9D8F",
        "Transition projet": "#1D3557",
        "Compte-rendu mentorat": "#E07A5F",
        "Soutenance blanche": "#F4A261",
        "Reprise demandee": "#D62828",
        "Stage / terrain": "#6A4C93",
    }

    for event in events.itertuples():
        ax.scatter(
            event.date,
            y_positions[event.projet_label],
            s=90 + event.points_qualite * 35,
            color=colors.get(event.type, "#6B7280"),
            edgecolor="#111827",
            linewidth=0.7,
            alpha=0.9,
        )

    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels)
    ax.set_xlabel("Date")
    ax.set_title("Timeline des jalons documentes")
    ax.grid(axis="x", linestyle="--", alpha=0.25)
    fig.autofmt_xdate()
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)


def _render_gantt_chart(gantt_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(12, 6.5))
    labels = gantt_df["projet_label"].tolist()

    for index, row in enumerate(gantt_df.itertuples()):
        ax.barh(
            index,
            row.duree_jours,
            left=row.debut,
            color="#1D3557",
            edgecolor="#111827",
            alpha=0.86,
        )
        ax.text(row.fin, index, f"  {row.jalons} jalons", va="center", fontsize=9)

    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels)
    ax.set_xlabel("Periode")
    ax.set_title("Gantt reconstruit a partir des preuves datees")
    ax.grid(axis="x", linestyle="--", alpha=0.25)
    ax.invert_yaxis()
    fig.autofmt_xdate()
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)


def _render_competency_mind_map() -> None:
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.axis("off")

    center = (0.0, 0.0)
    ax.scatter(*center, s=2400, color="#1D3557", edgecolor="#111827", linewidth=1.1)
    ax.text(
        *center,
        "Parcours\nData Analyst",
        ha="center",
        va="center",
        color="white",
        fontsize=13,
        fontweight="bold",
    )

    positions = [(-3.7, 1.9), (-3.8, -1.4), (0.4, 2.7), (3.9, 1.0), (3.4, -2.0)]
    colors = ["#2A9D8F", "#457B9D", "#E07A5F", "#F2CC8F", "#8D99AE"]

    for block, position, color in zip(COMPETENCY_BLOCKS, positions, colors):
        ax.plot([center[0], position[0]], [center[1], position[1]], color=color, linewidth=2.1, alpha=0.75)
        ax.scatter(*position, s=1500, color=color, edgecolor="#111827", linewidth=0.9)
        ax.text(
            position[0],
            position[1],
            f"{block['bloc']}\n{block['title']}",
            ha="center",
            va="center",
            fontsize=10,
            fontweight="bold",
            color="#111827",
        )

        skill_x = position[0] + (0.95 if position[0] >= 0 else -0.95)
        align = "left" if position[0] >= 0 else "right"
        ax.text(
            skill_x,
            position[1] - 0.55,
            "\n".join(f"- {skill}" for skill in block["skills"]),
            ha=align,
            va="top",
            fontsize=9,
            color="#374151",
        )

    ax.set_xlim(-5.8, 5.8)
    ax.set_ylim(-3.4, 3.5)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)


def _render_competency_blocks_table() -> None:
    rows = []
    for block in COMPETENCY_BLOCKS:
        rows.append(
            {
                "Bloc": block["bloc"],
                "Competence recruteur": block["title"],
                "Mots-cles": ", ".join(block["skills"]),
                "Preuve portfolio": block["proof"],
            }
        )
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)


def _build_project_competency_matrix() -> pd.DataFrame:
    projects_path = Path(__file__).resolve().parent / "projets_data.md"
    if not projects_path.exists():
        return pd.DataFrame()

    lines = projects_path.read_text(encoding="utf-8").splitlines()
    projects = []
    competences_set = set()
    current_project = None

    for line in lines:
        if line.strip().startswith("### "):
            current_project = re.sub(r"^US\d+\s*[—-]\s*", "", line.strip()[4:])
        if "**Compétences :**" in line and current_project:
            competences = [
                competence.strip()
                for competence in re.split(",|;", line.split("**Compétences :**")[-1])
                if competence.strip()
            ]
            projects.append({"projet": current_project, "competences": competences})
            competences_set.update(competences)

    if not projects:
        return pd.DataFrame()

    matrix = pd.DataFrame(0, index=sorted(competences_set), columns=[project["projet"] for project in projects])
    for project in projects:
        for competence in project["competences"]:
            matrix.loc[competence, project["projet"]] = 1

    return matrix


def _render_project_competency_matrix() -> None:
    matrix = _build_project_competency_matrix()
    if matrix.empty:
        st.info("Aucune matrice competences x projets disponible dans projets_data.md.")
        return

    st.markdown("### Matrice competences x projets developpes")
    st.write(
        "Cette matrice sert de vue de couverture: elle montre quels projets documentent chaque competence, "
        "et complete la timeline qui montre leur progression dans le temps."
    )
    fig, ax = plt.subplots(figsize=(min(13, 1.2 + len(matrix.columns)), min(8.5, 1.2 + len(matrix))))
    sns.heatmap(matrix, annot=True, cmap="Blues", cbar=False, linewidths=0.5, ax=ax)
    ax.set_xlabel("Projets")
    ax.set_ylabel("Competences")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)


def _render_pilotage_mosaic(events: pd.DataFrame, gantt_df: pd.DataFrame) -> None:
    mosaic = [
        ["progress", "progress", "types"],
        ["scope", "quality", "types"],
    ]
    fig, axes = plt.subplot_mosaic(mosaic, figsize=(14, 8), constrained_layout=True)

    progress_df = events.sort_values("date")
    axes["progress"].plot(progress_df["date"], progress_df["jalon"], marker="o", label="Jalons cumules")
    axes["progress"].plot(
        progress_df["date"],
        progress_df["points_qualite_cumules"],
        marker="s",
        label="Score qualitatif cumule",
    )
    axes["progress"].set_title("Progression documentee")
    axes["progress"].grid(axis="y", linestyle="--", alpha=0.25)
    axes["progress"].legend(loc="upper left")
    axes["progress"].tick_params(axis="x", rotation=30)

    scope_df = gantt_df.sort_values("jalons", ascending=True).tail(8)
    axes["scope"].barh(scope_df["projet_label"], scope_df["jalons"], color="#2A9D8F")
    axes["scope"].set_title("Perimetre couvert")
    axes["scope"].set_xlabel("Jalons dates")

    quality_df = gantt_df.sort_values("points_qualite", ascending=False).head(8)
    axes["quality"].bar(quality_df["projet_label"], quality_df["points_qualite"], color="#E07A5F")
    axes["quality"].set_title("Intensite qualitative")
    axes["quality"].set_ylabel("Points")
    axes["quality"].tick_params(axis="x", rotation=45)

    type_counts = events["type"].value_counts().sort_values()
    axes["types"].barh(type_counts.index, type_counts.values, color="#1D3557")
    axes["types"].set_title("Nature des preuves")
    axes["types"].set_xlabel("Nombre")

    st.pyplot(fig, use_container_width=True)


def _render_project_timeline() -> None:
    st.title("Timeline de progression et pilotage")
    st.caption("Mockup recruteur construit a partir des dates de soutenance, mentorat et preuves du dossier data")

    events = _load_timeline_events(DATA_ROOT)
    if events.empty:
        st.warning("Aucun jalon date exploitable trouve dans le dossier data.")
        return

    gantt_df = _build_project_gantt(events)
    first_date = events["date"].min()
    last_date = events["date"].max()
    documented_projects = len(gantt_df)
    planning_days = max((last_date - first_date).days, 1)
    documented_events = len(events)
    quality_points = int(events["points_qualite"].sum())
    estimated_hours = documented_events * 2 + len(events[events["extension"] == ".docx"]) * 1.5

    kpi_cols = st.columns(5)
    kpi_cols[0].metric("Projets suivis", documented_projects)
    kpi_cols[1].metric("Jalons dates", documented_events)
    kpi_cols[2].metric("Periode pilotee", f"{planning_days} jours")
    kpi_cols[3].metric("Score qualitatif", quality_points)
    kpi_cols[4].metric("Charge estimee", f"{estimated_hours:.1f} h")

    st.info(
        "La charge est un proxy de pilotage pour le mockup: 2 h par jalon documente + 1,5 h par compte-rendu. "
        "Elle represente un cout temps, pas un cout financier reel."
    )

    tab_timeline, tab_gantt, tab_pilotage, tab_mindmap, tab_matrix, tab_data = st.tabs(
        ["Timeline", "Gantt", "Pilotage", "Carte mentale", "Matrice competences", "Donnees sources"]
    )

    with tab_timeline:
        _render_timeline_chart(events)
        st.dataframe(
            events[["date", "projet_label", "type", "preuve", "points_qualite", "note"]],
            use_container_width=True,
            hide_index=True,
        )

    with tab_gantt:
        _render_gantt_chart(gantt_df)
        st.dataframe(gantt_df, use_container_width=True, hide_index=True)

    with tab_pilotage:
        st.markdown("### Lecture recruteur")
        st.write(
            "Cette vue montre une capacite a suivre un planning, tenir un perimetre et documenter "
            "les decisions. Les comptes-rendus et jalons servent de preuves de suivi, tandis que "
            "le score qualitatif valorise les moments de feedback, de reprise et de validation."
        )
        _render_pilotage_mosaic(events, gantt_df)

        scope_df = gantt_df[["projet_label", "jalons", "points_qualite", "duree_jours"]].copy()
        scope_df["charge_estimee_h"] = scope_df["jalons"] * 2
        st.markdown("### Perimetre, delai et charge")
        st.dataframe(scope_df, use_container_width=True, hide_index=True)

    with tab_mindmap:
        st.markdown("### Carte mentale des blocs de competences")
        st.write(
            "Cette carte relie le parcours, les blocs de competences et les preuves du portfolio. "
            "Elle complete le Gantt: le planning montre quand les preuves ont ete produites, "
            "la carte montre ce qu'elles demontrent."
        )
        _render_competency_mind_map()
        _render_competency_blocks_table()

    with tab_matrix:
        _render_project_competency_matrix()

    with tab_data:
        suspicious = events[events["note"].astype(bool)]
        if not suspicious.empty:
            st.warning("Dates ou elements a verifier avant publication")
            st.dataframe(suspicious[["date", "projet_label", "preuve", "note"]], use_container_width=True, hide_index=True)

        st.markdown("### Fichiers pris en compte")
        st.dataframe(events[["preuve", "date", "projet_label", "type"]], use_container_width=True, hide_index=True)


def _intro_en_tant_que(role: str) -> str:
    role_clean = role.strip()
    lower = role_clean.lower()

    if lower.startswith(("un ", "une ", "le ", "la ", "les ", "l'", "des ", "du ", "de ", "d'")):
        return f"En tant que {role_clean}"

    if role_clean and role_clean[0].lower() in {"a", "e", "i", "o", "u", "y", "h"}:
        return f"En tant qu'{role_clean}"

    return f"En tant que {role_clean}"


def _extract_streamlit_links(readme_path: Path | None) -> list[str]:
    if readme_path is None or not readme_path.exists():
        return []

    text = _read_text(readme_path)
    links = re.findall(r"https?://[^\s)]+", text, flags=re.IGNORECASE)
    streamlit_links = [link for link in links if "streamlit.app" in link.lower()]
    return sorted(set(streamlit_links))


def _extract_dashboard_links(readme_path: Path | None) -> list[str]:
    if readme_path is None or not readme_path.exists():
        return []

    text = _read_text(readme_path)
    links = re.findall(r"https?://[^\s)]+", text, flags=re.IGNORECASE)

    dashboard_domains = ("streamlit.app", "powerbi.com", "app.powerbi.com", "tableau.com")
    dashboard_links = [link for link in links if any(domain in link.lower() for domain in dashboard_domains)]
    return sorted(set(dashboard_links))


@st.cache_data(show_spinner=False)
def _load_user_story_summaries(backlog_path: Path) -> dict[int, str]:
    if not backlog_path.exists():
        return {}

    text = _read_text(backlog_path)
    summaries: dict[int, str] = {}

    blocks = re.split(r"\n###\s+US", text)
    for block in blocks[1:]:
        us_match = re.match(r"(\d+)", block)
        if not us_match:
            continue

        us_number = int(us_match.group(1))
        role_match = re.search(
            r"\*\*En tant que\*\*\s*(.+?)\s*\*\*je veux\*\*",
            block,
            flags=re.IGNORECASE | re.DOTALL,
        )
        want_match = re.search(
            r"\*\*je veux\*\*\s*(.+?)\s*\*\*afin d['’]?\*\*",
            block,
            flags=re.IGNORECASE | re.DOTALL,
        )
        goal_match = re.search(
            r"\*\*afin d['’]?\*\*\s*(.+?)(?:\s{2,}\n|\n-\s+\*\*Comp|\n\*\*Comp|$)",
            block,
            flags=re.IGNORECASE | re.DOTALL,
        )

        if not role_match or not want_match:
            continue

        role = re.sub(r"\s+", " ", role_match.group(1)).strip(" .")
        want = re.sub(r"\s+", " ", want_match.group(1)).strip(" .")
        intro = _intro_en_tant_que(role)
        sentence = f"{intro}, je veux {want}."

        if goal_match:
            goal = re.sub(r"\s+", " ", goal_match.group(1)).strip(" .")
            sentence = f"{intro}, je veux {want} afin de {goal}."

        summaries[us_number] = sentence

    return summaries


def _extract_us_number(folder_name: str) -> int:
    match = re.match(r"^US(\d+)", folder_name, flags=re.IGNORECASE)
    return int(match.group(1)) if match else 999


def _format_project_title(folder_name: str) -> str:
    parts = folder_name.split("_", 1)
    if len(parts) == 1:
        return folder_name
    us_code = parts[0].upper()
    title = parts[1].replace("_", " ").strip()
    return f"{us_code} - {title}"


def _public_project_title(project: dict) -> str:
    title = project["title"].split(" - ", 1)[-1]
    return title.replace("_", " ").title()


def _find_project_readme(project_dir: Path) -> Path | None:
    candidates = [project_dir / "README.md", project_dir / "readme.md"]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


@st.cache_data(show_spinner=False)
def _list_project_pdfs(project_dir: Path) -> list[Path]:
    return sorted(project_dir.rglob("*.pdf"), key=lambda p: _to_posix(p))


def _epic_for_us(us_number: int) -> str:
    for epic_key, epic_data in PROJECT_DOMAINS.items():
        if us_number in epic_data["us"]:
            return epic_key
    return "Autres projets"


@st.cache_data(show_spinner=False)
def _load_projects() -> list[dict]:
    if not PROJECTS_ROOT.exists():
        return []

    story_summaries = _load_user_story_summaries(REPO_ROOT / "projets_data.md")

    projects = []
    for project_dir in PROJECTS_ROOT.iterdir():
        if not project_dir.is_dir():
            continue

        us_number = _extract_us_number(project_dir.name)
        readme_path = _find_project_readme(project_dir)
        projects.append(
            {
                "folder": project_dir.name,
                "us_number": us_number,
                "us_code": f"US{us_number}" if us_number != 999 else project_dir.name,
                "title": _format_project_title(project_dir.name),
                "epic": _epic_for_us(us_number),
                "project_dir": project_dir,
                "readme": readme_path,
                "pdfs": _list_project_pdfs(project_dir),
                "summary": story_summaries.get(us_number, "Description indisponible."),
                "streamlit_links": _extract_streamlit_links(readme_path),
                "dashboard_links": _extract_dashboard_links(readme_path),
            }
        )

    return sorted(projects, key=lambda p: p["us_number"])


def _render_pdf_links(pdf_path: Path) -> None:
    pdf_bytes = pdf_path.read_bytes()
    encoded_pdf = base64.b64encode(pdf_bytes).decode("utf-8")
    data_url = f"data:application/pdf;base64,{encoded_pdf}"
       # Affiche le PDF dans un iframe
    st.components.v1.html(
        f"""
        <iframe
            src="{data_url}"
            width="100%"
            height="600px"
            style="border: none;">
        </iframe>
        """,
        height=650,  # Ajuste la hauteur selon tes besoins
    )


def _remove_first_markdown_title(readme_text: str) -> str:
    return re.sub(r"^\ufeff?\s*#\s+.*(?:\r?\n)+", "", readme_text, count=1)


def _insert_domain_after_context(readme_text: str, domain_title: str) -> str:
    domain_block = f"\n**Domaine de competence :** {domain_title}\n"
    context_heading = re.search(r"^#{2,3}\s+.*contexte.*$", readme_text, flags=re.IGNORECASE | re.MULTILINE)

    if not context_heading:
        return readme_text + f"\n\n{domain_block}"

    next_heading = re.search(r"^#{1,6}\s+", readme_text[context_heading.end():], flags=re.MULTILINE)
    insert_at = context_heading.end() + next_heading.start() if next_heading else len(readme_text)

    return readme_text[:insert_at] + domain_block + readme_text[insert_at:]


def _render_gantt(projects: list[dict]) -> None:
    gantt_df = pd.DataFrame(GANTT_DATA)
    if gantt_df.empty:
        st.info("Aucune donnee Gantt disponible.")
        return

    us_to_epic = {p["us_code"]: p["epic"] for p in projects}
    gantt_df["epic"] = gantt_df["us"].map(us_to_epic).fillna("Autres projets")

    color_map = {epic: data["color"] for epic, data in PROJECT_DOMAINS.items()}
    color_map["Autres projets"] = "#8D99AE"

    fig, ax = plt.subplots(figsize=(12, 6.5))
    y_labels = [row.title for row in gantt_df.itertuples()]
    y_positions = list(range(len(gantt_df)))

    for idx, row in enumerate(gantt_df.itertuples()):
        ax.barh(
            y=idx,
            width=row.duration,
            left=row.start,
            color=color_map.get(row.epic, "#8D99AE"),
            edgecolor="#1f2937",
            alpha=0.9,
        )

    ax.set_yticks(y_positions)
    ax.set_yticklabels(y_labels, fontsize=9)
    ax.set_xlabel("Semaines")
    ax.set_title("Planning simplifie des projets")
    ax.set_xlim(1, 14)
    ax.set_xticks(range(1, 14))
    ax.grid(axis="x", linestyle="--", alpha=0.25)
    ax.invert_yaxis()
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)


def _open_project(folder_name: str) -> None:
    _set_query_project(folder_name)
    st.session_state["selected_project"] = folder_name
    st.rerun()


def _set_query_project(folder_name: str | None) -> None:
    if hasattr(st, "query_params"):
        if folder_name:
            st.query_params["project"] = folder_name
        else:
            if "project" in st.query_params:
                del st.query_params["project"]
        return

    if folder_name:
        st.experimental_set_query_params(project=folder_name)
    else:
        st.experimental_set_query_params()


def _get_query_project() -> str | None:
    if hasattr(st, "query_params"):
        value = st.query_params.get("project")
        if isinstance(value, list):
            return value[0] if value else None
        return value

    params = st.experimental_get_query_params()
    value = params.get("project")
    if isinstance(value, list):
        return value[0] if value else None
    return value


def _render_portfolio_hub(projects: list[dict]) -> None:
    st.title("Portfolio professionnel Data Analyst")
    st.caption("Selection courte de projets documentes, consultables et orientes recruteur")

    if not projects:
        st.warning("Aucun dossier projet detecte dans le repertoire 'projets'.")
        return

    featured_projects = [project for project in projects if project["us_code"] in FEATURED_PROJECTS]

    st.markdown("### Projets mis en avant")
    st.write(
        "Cette selection montre une progression professionnelle complete: fiabiliser les donnees, "
        "produire des indicateurs utiles, visualiser pour decider et documenter les preuves."
    )

    columns = st.columns(3)
    for index, project in enumerate(featured_projects):
        column = columns[index % 3]
        with column:
            with st.container(border=True):
                icon = US_ICONS.get(project["us_code"], "📁")
                st.markdown(f"**{icon} Projet documente**")
                st.markdown(f"### {_public_project_title(project)}")
                st.caption(FEATURED_PROJECTS[project["us_code"]])
                st.caption(project["summary"])

                if project["readme"]:
                    st.markdown("**Documentation**")
                    st.markdown(f"- 📝 [Lien README](?project={project['folder']})")

                if project["dashboard_links"]:
                    st.markdown("**Dashboards**")
                    for link_index, link in enumerate(project["dashboard_links"], start=1):
                        label = (
                            f"Dashboard {link_index}"
                            if len(project["dashboard_links"]) > 1
                            else "Dashboard"
                        )
                        st.markdown(f"- 🔗 [{label}]({link})")
    st.markdown("### Competences Data Analyst demontrees")
    st.dataframe(pd.DataFrame(DATA_ANALYST_PROOFS), use_container_width=True, hide_index=True)


def _render_home() -> None:
    st.title("Portfolio Data Analyst")
    st.caption("Vitrine recruteur: projets documentes, liens consultables et preuves de competences")
    st.markdown("### Transformer des donnees disperses en decisions fiables")
    st.write(
        "Ce portfolio met en avant une selection courte de projets: qualite des donnees, "
        "dashboard decisionnel et modele predictif. Chaque projet est documente avec objectif, "
        "methode, resultats, competences et preuves consultables."
    )
    st.info("Ouvrez la section Portfolio professionnel dans la navigation pour consulter les 3 projets mis en avant.")

    st.markdown("### Competences Data Analyst demontrees")
    st.dataframe(pd.DataFrame(DATA_ANALYST_PROOFS), use_container_width=True, hide_index=True)
    st.info("La matrice competences x projets est disponible dans Timeline & competences.")


def _render_project_view(project: dict) -> None:
    icon = US_ICONS.get(project["us_code"], "📁")
    st.title(f"{icon} {_public_project_title(project)}")
    st.write(project["summary"])

    col_readme, col_pdf = st.columns([1.05, 0.95], gap="large")

    with col_readme:
        readme_path = project["readme"]
        if readme_path is None:
            st.warning("README introuvable pour ce projet.")
        else:
            readme_content = _read_text(readme_path)
            readme_content = _remove_first_markdown_title(readme_content)
            domain_title = PROJECT_DOMAINS.get(project["epic"], {}).get("title", "Projet documente")
            readme_content = _insert_domain_after_context(readme_content, domain_title)
            st.markdown(readme_content)

        # Affichage du résumé et du lien pour US14 (stage)
        if project["us_code"] == "US14":
            resume_path = project["project_dir"] / "resume_bilan_reflexif.md"
            if resume_path.exists():
                st.markdown("---")
                st.markdown("### 📝 Résumé du bilan réflexif")
                st.markdown(_read_text(resume_path))
            bilan_path = Path(__file__).resolve().parents[1] / "Bilan-Reflexif-de-Stage.pptx"
            if bilan_path.exists():
                st.markdown(f"[📥 Télécharger le bilan réflexif (PPTX)]({bilan_path.as_posix()})")

    with col_pdf:
        st.subheader("🔗 Ressources")
        pdfs = project["pdfs"]

        if project["dashboard_links"]:
            st.markdown("**📈 Liens dashboards**")
            for link_index, link in enumerate(project["dashboard_links"], start=1):
                label = (
                    f"Dashboard {link_index}"
                    if len(project["dashboard_links"]) > 1
                    else "Dashboard"
                )
                st.markdown(f"- 🔗 [{label}]({link})")

        if not pdfs:
            if project["us_code"] == "US13":
                st.info("Gantt simplifie du portfolio")
                _render_gantt([project_item for project_item in projects])
            else:
                st.info("Aucun PDF trouve pour ce projet.")
            return

        if len(pdfs) == 1:
            selected_pdf = pdfs[0]
        else:
            labels = [_to_posix(p.relative_to(project["project_dir"])) for p in pdfs]
            label_to_path = dict(zip(labels, pdfs))
            selected_label = st.selectbox("Choisir un PDF", labels)
            selected_pdf = label_to_path[selected_label]

        _render_pdf_links(selected_pdf)


projects = _load_projects()
project_lookup = {project["folder"]: project for project in projects}

if "selected_project" not in st.session_state:
    st.session_state["selected_project"] = None

query_project = _get_query_project()
if query_project in project_lookup and query_project != st.session_state["selected_project"]:
    st.session_state["selected_project"] = query_project

with st.sidebar:
    st.markdown("## Portfolio")
    st.caption("Parcours recruteur")

    if st.button("Accueil", use_container_width=True):
        _set_query_project(None)
        st.session_state["selected_project"] = None
        st.rerun()

    if st.button("Vitrine projets", use_container_width=True):
        _set_query_project(None)
        st.session_state["selected_project"] = "__portfolio__"
        st.rerun()

    if st.button("Pilotage & competences", use_container_width=True):
        _set_query_project(None)
        st.session_state["selected_project"] = "__timeline__"
        st.rerun()

    st.markdown("### Etudes de cas")
    featured_sidebar_projects = [project for project in projects if project["us_code"] in FEATURED_PROJECTS]
    for project in featured_sidebar_projects:
        project_icon = US_ICONS.get(project["us_code"], "📁")
        button_label = f"{project_icon} {_public_project_title(project)}"
        if st.button(button_label, key=f"featured_{project['folder']}", use_container_width=True):
            _open_project(project["folder"])

    secondary_projects = [
        project
        for project in projects
        if project["us_code"] not in FEATURED_PROJECTS and project["us_code"] != "US13"
    ]
    with st.expander("Autres preuves projet", expanded=False):
        for project in secondary_projects:
            project_icon = US_ICONS.get(project["us_code"], "📁")
            button_label = f"{project_icon} {_public_project_title(project)}"
            if st.button(button_label, key=f"secondary_{project['folder']}", use_container_width=True):
                _open_project(project["folder"])

st.markdown(
    """
    <style>
    .stApp {
        font-size: 1.08rem;
    }
    .stMarkdown p, .stCaption {
        font-size: 1.03rem !important;
        line-height: 1.6;
    }
    h1 {
        font-size: 2.5rem !important;
    }
    h2 {
        font-size: 1.8rem !important;
    }
    h3 {
        font-size: 1.35rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

selected_project_folder = st.session_state["selected_project"]
if selected_project_folder == "__portfolio__":
    _render_portfolio_hub(projects)
elif selected_project_folder == "__timeline__":
    _render_project_timeline()
elif selected_project_folder and selected_project_folder in project_lookup:
    selected_project = project_lookup[selected_project_folder]
    if selected_project["us_code"] == "US13":
        _render_portfolio_hub(projects)
    else:
        _render_project_view(selected_project)
else:
    _render_home()
