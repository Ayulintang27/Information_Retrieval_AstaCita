
import streamlit as st
from component.styles import load_css
from pages.pencarian import show_pencarian
from pages.dashboard import show_dashboard
load_css()

if "menu" not in st.session_state:
    st.session_state.menu = "HOME"

if "search_input_version" not in st.session_state:
    st.session_state.search_input_version = 0


def clear_search_state() -> None:
    search_input_key = (
        f"search_query_input_{st.session_state.search_input_version}"
    )

    for state_key in (
        "hasil",
        "query",
        "selected_news",
        search_input_key,
        "quick_query",
    ):
        st.session_state.pop(state_key, None)

    st.session_state.search_input_version += 1


def nav_button(label: str, key: str) -> None:
    is_active = st.session_state.menu == key
    if st.button(
        label,
        key=f"nav_{key}",
        type="primary" if is_active else "secondary",
        use_container_width=True,
    ):
        if st.session_state.menu == "PENCARIAN" and key != "PENCARIAN":
            clear_search_state()
        st.session_state.menu = key
        st.rerun()


with st.sidebar:
    st.markdown(
        """
        <div class="brand">
            <div class="brand-badge">📚</div>
            <div>
                <div class="brand-title">Sistem IR</div>
                <div class="brand-subtitle">Asta Cita Explorer</div>
            </div>
        </div>
        
        """,
        unsafe_allow_html=True,
    )

    nav_button("🏠  Home", "HOME")
    nav_button("🔎  Pencarian", "PENCARIAN")
    nav_button("📊  Insight Berita", "DASHBOARD")

st.markdown('<span class="content-anchor"></span>', unsafe_allow_html=True)

if st.session_state.menu == "HOME":
        st.markdown(
            """
            <div class="eyebrow">Beranda</div>
            <div class="page-title">Selamat Datang di Asta Cita Explorer</div>
            <p class="summary-text">
                Asta Cita adalah delapan program dan visi utama pemerintahan Presiden Prabowo Subianto dan Wakil Presiden Gibran Rakabuming Raka 
                untuk mewujudkan Indonesia Maju menuju visi "Indonesia Emas 2045". Delapan program tersebut mencakup:
            </p>
            <ol class="summary-text">
            <li>Memperkokoh ideologi Pancasila, demokrasi, dan hak asasi manusia (HAM);</li>

            <li>
                Menetapkan sistem pertahanan keamanan negara dan mendorong kemandirian bangsa
                melalui swasembada pangan, energi, air, ekonomi kreatif, ekonomi hijau, dan ekonomi biru;
            </li>

            <li>
                Meningkatkan lapangan kerja yang berkualitas, mendorong kewirausahaan,
                mengembangkan industri kreatif, dan melanjutkan pengembangan infrastruktur.
            </li>

            <li>
                Memperkuat pembangunan sumber daya manusia, sains, teknologi, pendidikan,
                kesehatan, prestasi olahraga, kesetaraan gender, serta penguatan peran perempuan,
                pemuda, dan penyandang disabilitas;
            </li>

            <li>
                Melanjutkan hilirisasi dan industrialisasi untuk meningkatkan nilai tambah di dalam negeri;
            </li>

            <li>
                Membangun dari desa dan dari bawah untuk pemerataan ekonomi dan pemberantasan kemiskinan;
            </li>

            <li>
                Memperkuat reformasi politik, hukum, dan birokrasi, serta memperkuat pencegahan
                dan pemberantasan korupsi dan narkoba.
            </li>

            <li>
                Memperkuat penyelarasan kehidupan yang harmonis dengan lingkungan, alam,
                dan budaya, serta peningkatan toleransi antarumat beragama untuk mencapai
                masyarakat yang adil dan makmur.
            </li>
            </ol>    
            </div>
            </div>    
  """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="quick-search-title">Pencarian Cepat</div>',
            unsafe_allow_html=True,
        )

        quick_queries = [
            ("Ketahanan pangan", "ketahanan pangan"),
            ("Kesehatan", "kesehatan"),
            ("Pendidikan", "pendidikan"),
            ("Digitalisasi", "digitalisasi"),
            ("Hilirisasi", "hilirisasi"),
            ("Ekonomi hijau", "ekonomi hijau"),
        ]

        for row_start in range(0, len(quick_queries), 3):
            cols = st.columns([1, 1, 1, 2.4], gap="small")

            for col, (label, query_value) in zip(cols[:3], quick_queries[row_start:row_start + 3]):
                with col:
                    if st.button(
                        label,
                        key=f"quick_{query_value}",
                        use_container_width=True,
                    ):
                        st.session_state.quick_query = query_value
                        st.session_state.menu = "PENCARIAN"
                        st.rerun()
          

elif st.session_state.menu == "PENCARIAN":
        show_pencarian()
elif st.session_state.menu == "DASHBOARD":
        show_dashboard()
        
