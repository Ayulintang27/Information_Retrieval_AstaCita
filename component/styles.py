import streamlit as st

def load_css():

    st.markdown(
        """
        <style>
        :root {
            --bg: #f4f7fb;
            --surface: rgba(255, 255, 255, 0.86);
            --surface-strong: #ffffff;
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --text: #0f172a;
            --muted: #64748b;
            --border: rgba(148, 163, 184, 0.24);
            --shadow: 0 20px 50px rgba(15, 23, 42, 0.08);
        }

        [data-testid="stAppViewContainer"] {
            background:
                radial-gradient(circle at top left, rgba(37, 99, 235, 0.18), transparent 32%),
                linear-gradient(180deg, #f8fbff 0%, var(--bg) 100%);
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        [data-testid="stSidebarNav"] {
            display: none;
        }

        .block-container {
            padding-top: 0.7rem;
            padding-bottom: 1rem;
            padding-left: 2rem;
            padding-right: 2rem;
            max-width: 1380px;
        }
    
        section[data-testid="stSidebar"] {
            background:
                linear-gradient(180deg, rgba(255,255,255,0.96) 0%, rgba(244,247,251,0.96) 100%);
            border-right: 1px solid var(--border);
            padding-top: 0rem;
        }

        section[data-testid="stSidebar"] .block-container {
            padding-top: 0rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 0.85rem;
            margin-bottom: 1.6rem;
            padding-top: 0rem;
            margin-top: -1rem;
        }

        .brand-badge {
            width: 48px;
            height: 48px;
            display: grid;
            place-items: center;
            border-radius: 16px;
            background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
            color: #ffffff;
            font-size: 1.35rem;
            box-shadow: 0 14px 30px rgba(37, 99, 235, 0.28);
        }

        .brand-title {
            color: var(--text);
            font-size: 1.15rem;
            line-height: 1.15;
            font-weight: 800;
            margin: 0;
        }

        .brand-subtitle {
            color: var(--muted);
            font-size: 0.86rem;
            margin-top: 0.15rem;
        }

        .menu-label {
            color: var(--muted);
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.65rem;
        }

        [data-testid="stVerticalBlock"]:has(.content-anchor) {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 32px;
            padding: 2rem;
            min-height: auto;
            box-shadow: var(--shadow);
            backdrop-filter: blur(18px);
        }

        .eyebrow {
            color: var(--primary);
            font-size: 0.8rem;
            font-weight: 800;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 0.6rem;
            padding-top: 0rem;
        }

        .page-title {
            color: var(--text);
            font-size: clamp(2rem, 4vw, 3.2rem);
            line-height: 1.05;
            font-weight: 850;
            letter-spacing: -0.04em;
            margin-bottom: 0.9rem;
        }

        .page-subtitle {
            color: var(--muted);
            font-size: 1.05rem;
            line-height: 1.75;
            max-width: 800px;
            margin-bottom: 1.5rem;
        }

        .summary-title {
            color: var(--text);
            font-size: 1.08rem;
            font-weight: 800;
            margin-bottom: 0.55rem;
        }

        .summary-text {
            color: var(--muted);
            line-height: 1.7;
            margin: 0;
        }

        .tag-list {
            display: flex;
            flex-wrap: wrap;
            gap: 0.55rem;
            margin-top: 0.85rem;
        }

        .tag {
            display: inline-flex;
            align-items: center;
            padding: 0.35rem 0.7rem;
            border-radius: 999px;
            color: var(--primary-dark);
            background: rgba(37, 99, 235, 0.1);
            font-size: 0.84rem;
            font-weight: 700;
        }

        .quick-search-title {
            color: var(--text);
            font-size: 1.35rem;
            line-height: 1.25;
            font-weight: 850;
            margin: 1.4rem 0 1rem;
        }

        .result-card,
        .metric-card {
            background: var(--surface-strong);
            border: 1px solid var(--border);
            border-radius: 22px;
            padding: 1.2rem;
        }

        .metric-wrap {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 1rem;
            margin: 1rem 0 1.5rem;
        }

        .metric-label {
            color: var(--muted);
            font-size: 0.82rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }

        .metric-value {
            color: var(--text);
            font-size: 2rem;
            line-height: 1.2;
            font-weight: 850;
            margin-top: 0.35rem;
        }

        .result-card {
            margin-top: 1rem;
            border-left: 5px solid var(--primary);
        }

        .result-title {
            color: var(--text);
            font-size: 1.15rem;
            font-weight: 750;
            margin-bottom: 0.45rem;
        }

        .result-meta {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            color: var(--primary-dark);
            background: rgba(37, 99, 235, 0.1);
            border-radius: 999px;
            padding: 0.3rem 0.7rem;
            font-size: 0.86rem;
            font-weight: 700;
            margin-bottom: 0.75rem;
        }

        .result-summary {
            color: var(--muted);
            line-height: 1.65;
            margin: 0;
        }

        .stButton > button {
            width: 100%;
            background: #EEF3FF !important;
            border: 1px solid #D9E3FF !important;
            color: #1D4ED8 !important;
            border-radius: 16px;
            min-height: 48px;
            background: rgba(255, 255, 255, 0.7);
            color: var(--text);
            font-weight: 700;
            transition: all 0.18s ease;
            white-space: nowrap !important;

        }

        .stButton > button:hover {
            transform: translateY(-1px);
            border-color: rgba(37, 99, 235, 0.32);
            color: var(--primary-dark);
        }

        .stButton > button[kind="primary"] {
            color: #ffffff;
            border: none;
            background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
            box-shadow: 0 14px 30px rgba(37, 99, 235, 0.25);
            white-space: nowrap !important;

        }

        div[data-baseweb="input"] > div,
        div[data-baseweb="select"] > div {
            border-radius: 16px;
            min-height: 48px;
            border-color: rgba(148, 163, 184, 0.35);
        }

        @media (max-width: 900px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            [data-testid="stVerticalBlock"]:has(.content-anchor) {
                min-height: auto;
            }

            .metric-wrap {
                grid-template-columns: 1fr;
            }
        }

        .hero-mini{
            background: rgba(255,255,255,0.7);
            border: 1px solid rgba(148,163,184,0.18);
            border-radius: 22px;
            padding: 1.2rem 1.5rem;
            margin-bottom: 1.5rem;
            backdrop-filter: blur(12px);
        }

        .hero-eyebrow{
            color:#2563eb;
            font-size:0.82rem;
            font-weight:800;
            letter-spacing:0.08em;
            text-transform:uppercase;
            margin-bottom:0.45rem;
        }

        .hero-title{
            color:#0f172a;
            font-size:1.4rem;
            font-weight:800;
            margin-bottom:0.4rem;
        }

        .hero-subtitle{
            color:#64748b;
            font-size:0.95rem;
            line-height:1.7;
        }

        .main {
             user-select: none;
        }

        *:focus {
            outline: none !important;
            box-shadow: none !important;
        }


        /* ── Dialog overlay — centered ── */
        [data-testid="stDialog"] {
            background: rgba(15, 23, 42, 0.5) !important;
            backdrop-filter: blur(4px) !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            position: fixed !important;
            inset: 0 !important;
        }

        /* ── Dialog panel ── */
        div[data-testid="stDialog"] > div {
            width: min(780px, 90vw) !important;
            max-width: 780px !important;
            max-height: 85vh !important;
            border-radius: 24px !important;
            padding: 2rem 2.5rem !important;
            overflow-y: auto !important;
            background: #ffffff !important;
            box-shadow: 0 32px 80px rgba(15, 23, 42, 0.18) !important;
            margin: auto !important;
            position: relative !important;
            top: unset !important;
            left: unset !important;
            transform: none !important;
        }

        /* ── Detail content inside dialog ── */
        .detail-container {
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 0;
            box-sizing: border-box;
        }

        .detail-eyebrow {
            color: var(--primary);
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 0.75rem;
        }

        .detail-title {
            font-size: clamp(1.4rem, 3vw, 1.9rem);
            font-weight: 800;
            line-height: 1.25;
            color: #0f172a;
            margin-bottom: 1.1rem;
            word-break: break-word;
        }

        .detail-badges {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1.4rem;
        }

        .detail-badge {
            display: inline-flex;
            align-items: center;
            padding: 0.35rem 0.85rem;
            border-radius: 999px;
            background: #eef2ff;
            color: #1d4ed8;
            font-size: 0.85rem;
            font-weight: 700;
        }

        .detail-divider {
            border: none;
            border-top: 1px solid rgba(148, 163, 184, 0.22);
            margin: 0 0 1.4rem;
        }

        .detail-text {
            font-size: 1rem;
            line-height: 1.85;
            color: #374151;
            text-align: justify;
            word-break: break-word;
        }
        div[data-testid="column"]{
        padding-left: 0.2rem !important;
        padding-right: 0.2rem !important;
        }
                </style>
                """,
        unsafe_allow_html=True,
    )
