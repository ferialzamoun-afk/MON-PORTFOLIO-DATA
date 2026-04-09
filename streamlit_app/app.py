from pathlib import Path
import base64
import re

import streamlit as st

st.set_page_config(page_title="Portfolio Data Analyst", page_icon="📊", layout="wide")

REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECTS_ROOT = REPO_ROOT / "projets"


def _to_posix(path: Path) -> str:
    return str(path).replace("\\", "/")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _find_home_readme() -> Path | None:
    candidates = [
        REPO_ROOT / "projets_data.md",
        REPO_ROOT / "README.md",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def _find_project_readme(project_dir: Path) -> Path | None:
    candidates = [project_dir / "README.md", project_dir / "readme.md"]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


@st.cache_data(show_spinner=False)
def _list_projects() -> list[str]:
    if not PROJECTS_ROOT.exists():
        return []
    projects = [p.name for p in PROJECTS_ROOT.iterdir() if p.is_dir()]

    def _project_sort_key(name: str) -> tuple[int, int, str]:
        # Keep US folders ordered numerically (US2, US3, ..., US13), then others.
        match = re.match(r"^US(\d+)", name, flags=re.IGNORECASE)
        if match:
            return (0, int(match.group(1)), name.lower())
        return (1, 9999, name.lower())

    return sorted(projects, key=_project_sort_key)


@st.cache_data(show_spinner=False)
def _list_pdfs(project_name: str) -> list[str]:
    project_dir = PROJECTS_ROOT / project_name
    if not project_dir.exists():
        return []
    return sorted([_to_posix(p.relative_to(project_dir)) for p in project_dir.rglob("*.pdf")])


def _set_view(kind: str, project: str = "", path: str = "", title: str = "") -> None:
    st.session_state["view"] = {
        "kind": kind,
        "project": project,
        "path": path,
        "title": title,
    }


def _render_pdf(pdf_path: Path) -> None:
    pdf_bytes = pdf_path.read_bytes()
    encoded_pdf = base64.b64encode(pdf_bytes).decode("utf-8")
    pdf_html = f"""
    <embed src="data:application/pdf;base64,{encoded_pdf}" type="application/pdf" width="100%" height="900px" />
    """
    st.markdown(pdf_html, unsafe_allow_html=True)
    st.download_button(
        label="Télécharger le PDF",
        data=pdf_bytes,
        file_name=pdf_path.name,
        mime="application/pdf",
    )


if "view" not in st.session_state:
    _set_view("home")

st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] {
        border-right: 1px solid #d0d7de;
    }
    .sidebar-title {
        font-weight: 700;
        margin-bottom: 0.4rem;
    }
    .sidebar-subtitle {
        color: #57606a;
        margin-bottom: 1rem;
        font-size: 0.9rem;
    }
    .tree-heading {
        margin-top: 0.2rem;
        margin-bottom: 0.6rem;
        font-size: 0.85rem;
        color: #57606a;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }
    .tree-file-note {
        margin-top: 0.2rem;
        margin-bottom: 0.3rem;
        color: #57606a;
        font-size: 0.78rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown('<div class="sidebar-title">MON-PORTFOLIO-DATA</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-subtitle">Navigation style explorateur</div>', unsafe_allow_html=True)

    if st.button("🏠 Accueil", use_container_width=True):
        _set_view("home")

    st.markdown('<div class="tree-heading">Explorateur</div>', unsafe_allow_html=True)

    for project_name in _list_projects():
        project_dir = PROJECTS_ROOT / project_name
        expanded = st.session_state["view"].get("project") == project_name
        with st.expander(project_name, expanded=expanded):
            readme_path = _find_project_readme(project_dir)
            if readme_path and st.button("README.md", key=f"readme_{project_name}", use_container_width=True):
                _set_view(
                    "markdown",
                    project=project_name,
                    path=_to_posix(readme_path),
                    title=f"{project_name} / README.md",
                )

            pdfs = _list_pdfs(project_name)
            if not pdfs:
                st.markdown('<div class="tree-file-note">(aucun PDF)</div>', unsafe_allow_html=True)

            for relative_pdf in pdfs:
                file_name = Path(relative_pdf).name
                label = f"PDF - {file_name}"
                button_key = f"pdf_{project_name}_{relative_pdf}"
                if st.button(label, key=button_key, use_container_width=True):
                    absolute_pdf = _to_posix(project_dir / relative_pdf)
                    _set_view(
                        "pdf",
                        project=project_name,
                        path=absolute_pdf,
                        title=f"{project_name} / {relative_pdf}",
                    )

view = st.session_state["view"]
kind = view.get("kind", "home")

if kind == "home":
    st.title("📊 Portfolio Data Analyst")
    st.caption("Accueil de l'application")
    home_readme = _find_home_readme()
    if home_readme is None:
        st.warning("Aucun fichier d'accueil trouve (projets_data.md / README.md).")
    else:
        st.markdown(f"### {_to_posix(home_readme.relative_to(REPO_ROOT))}")
        st.markdown(_read_text(home_readme))

elif kind == "markdown":
    selected_path = Path(view.get("path", ""))
    st.title("📝 README")
    st.caption(view.get("title", ""))
    if selected_path.exists():
        st.markdown(_read_text(selected_path))
    else:
        st.error("Le fichier Markdown sélectionné n'existe plus.")

elif kind == "pdf":
    selected_path = Path(view.get("path", ""))
    st.title("📄 PDF")
    st.caption(view.get("title", ""))
    if selected_path.exists():
        _render_pdf(selected_path)
    else:
        st.error("Le PDF sélectionné n'existe plus.")

else:
    st.error("Vue non reconnue.")
