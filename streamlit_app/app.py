from pathlib import Path
import base64
import re

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import seaborn as sns

st.set_page_config(page_title="Portfolio Data Analyst", layout="wide")

REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECTS_ROOT = REPO_ROOT / "projets"

EPICS = {
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
    for epic_key, epic_data in EPICS.items():
        if us_number in epic_data["us"]:
            return epic_key
    return "Hors EPIC"


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
    st.components.v1.html(
        f'<a href="{data_url}">📄 Ouvrir la présentation</a>',
        height=28,
    )


def _remove_first_markdown_title(readme_text: str) -> str:
    return re.sub(r"^\ufeff?\s*#\s+.*(?:\r?\n)+", "", readme_text, count=1)


def _insert_epic_after_context(readme_text: str, epic_label: str, epic_title: str) -> str:
    epic_block = f"\n**EPIC :** {epic_label}  \n**Intitule :** {epic_title}\n"
    context_heading = re.search(r"^#{2,3}\s+.*contexte.*$", readme_text, flags=re.IGNORECASE | re.MULTILINE)

    if not context_heading:
        return readme_text + f"\n\n{epic_block}"

    next_heading = re.search(r"^#{1,6}\s+", readme_text[context_heading.end():], flags=re.MULTILINE)
    insert_at = context_heading.end() + next_heading.start() if next_heading else len(readme_text)

    return readme_text[:insert_at] + epic_block + readme_text[insert_at:]


def _render_gantt(projects: list[dict]) -> None:
    gantt_df = pd.DataFrame(GANTT_DATA)
    if gantt_df.empty:
        st.info("Aucune donnee Gantt disponible.")
        return

    us_to_epic = {p["us_code"]: p["epic"] for p in projects}
    gantt_df["epic"] = gantt_df["us"].map(us_to_epic).fillna("Hors EPIC")

    color_map = {epic: data["color"] for epic, data in EPICS.items()}
    color_map["Hors EPIC"] = "#8D99AE"

    fig, ax = plt.subplots(figsize=(12, 6.5))
    y_labels = [f"{row.us} - {row.title}" for row in gantt_df.itertuples()]
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
    ax.set_title("Gantt simplifie - planification des US")
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
    st.title("🧩 US13 - Portfolio")
    st.caption("Vue d'ensemble de vos US avec navigation rapide")

    st.markdown("### 🚀 Acces rapide aux US")
    if not projects:
        st.warning("Aucun dossier projet detecte dans le repertoire 'projets'.")
        return

    columns = st.columns(3)
    for index, project in enumerate(projects):
        column = columns[index % 3]
        with column:
            with st.container(border=True):
                icon = US_ICONS.get(project["us_code"], "📁")
                st.markdown(f"**{icon} {project['us_code']}**")
                st.markdown(f"### {project['title'].split(' - ', 1)[-1].replace('_', ' ').title()}")
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

                st.caption("Ouvrir la US depuis le menu de navigation a gauche.")


def _render_home() -> None:
    st.title("Portfolio Data Analyst")
    st.caption("Page d'accueil")
    st.markdown("### Bienvenue")
    st.write("Utilisez le menu a gauche pour ouvrir vos US.")
    st.info("La vue complete du portfolio est disponible via US13 - Portfolio dans la navigation.")

    # --- Graphe Compétences x Projets (axes inversés) ---
    projets_path = Path("projets_data.md")
    if projets_path.exists():
        with open(projets_path, encoding="utf-8") as f:
            lines = f.readlines()
        projets = []
        competences_set = set()
        current_proj = None
        for line in lines:
            if line.strip().startswith("### "):
                current_proj = line.strip()[4:]
            if "**Compétences :**" in line:
                comp_list = [c.strip() for c in re.split(",|;", line.split("**Compétences :**")[-1])]
                projets.append({"projet": current_proj, "competences": comp_list})
                competences_set.update(comp_list)
        if projets:
            competences = sorted(list(competences_set))
            df = pd.DataFrame(0, index=competences, columns=[p["projet"] for p in projets])
            for p in projets:
                for c in p["competences"]:
                    df.loc[c, p["projet"]] = 1
            st.markdown("### Matrice Compétences x Projets développés")
            import matplotlib.pyplot as plt
            import seaborn as sns
            fig, ax = plt.subplots(figsize=(min(12, 1+len(df.columns)), min(8, 1+len(df))))
            sns.heatmap(df, annot=True, cmap="Blues", cbar=False, linewidths=0.5, ax=ax)
            plt.xlabel("Projets")
            plt.ylabel("Compétences")
            st.pyplot(fig)
        else:
            st.info("Aucun projet trouvé dans projets_data.md.")
    else:
        st.warning("Le fichier projets_data.md est introuvable.")


def _render_project_view(project: dict) -> None:
    icon = US_ICONS.get(project["us_code"], "📁")
    st.write(project["summary"])

    col_readme, col_pdf = st.columns([1.05, 0.95], gap="large")

    with col_readme:
        readme_path = project["readme"]
        if readme_path is None:
            st.warning("README introuvable pour cette US.")
        else:
            readme_content = _read_text(readme_path)
            readme_content = _remove_first_markdown_title(readme_content)
            epic_title = EPICS.get(project["epic"], {}).get("title", "")
            readme_content = _insert_epic_after_context(readme_content, project["epic"], epic_title)
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
                st.info("Aucun PDF trouve pour cette US.")
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
    st.markdown("## 🧭 Navigation")
    if st.button("Accueil", use_container_width=True):
        _set_query_project(None)
        st.session_state["selected_project"] = None
        st.rerun()

    for epic_key, epic_data in EPICS.items():
        label = f"📚 {epic_key} - {epic_data['title']}"
        epic_projects = [p for p in projects if p["epic"] == epic_key]
        if not epic_projects:
            continue

        expanded = any(p["folder"] == st.session_state["selected_project"] for p in epic_projects)
        with st.expander(label, expanded=expanded):
            for project in epic_projects:
                project_icon = US_ICONS.get(project["us_code"], "📁")
                button_label = f"{project_icon} {project['title'].replace('_', ' ')}"
                if st.button(button_label, key=f"sb_{project['folder']}", use_container_width=True):
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
if selected_project_folder and selected_project_folder in project_lookup:
    selected_project = project_lookup[selected_project_folder]
    if selected_project["us_code"] == "US13":
        _render_portfolio_hub(projects)
    else:
        _render_project_view(selected_project)
else:
    _render_home()
