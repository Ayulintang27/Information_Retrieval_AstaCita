import streamlit as st
from component.styles import load_css
from model.retrieval import retrieve_documents


load_css()


def show_pencarian():
    if "selected_news" not in st.session_state:
        st.session_state.selected_news = None

    if "hasil" not in st.session_state:
        st.session_state.hasil = []

    if "query" not in st.session_state:
        st.session_state.query = ""

    st.markdown(
        """
        <div class="eyebrow">Search</div>
        <div class="page-title">Pencarian Berita</div>
        <div class="page-subtitle">
            Temukan topik yang ingin Anda ditelusuri terkait dengan Asta Cita dengan memasukkan kata kunci di bawah ini.
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_query, col_topk = st.columns([3.2, 1])
    with col_query:
        default_query = st.session_state.get("quick_query", "")

        query = st.text_input(
            " ",
            value=default_query,
            placeholder="Masukkan kata kunci..",

        )
    with col_topk:
        top_k = st.selectbox("Top-K", [5, 10, 15])

    if st.button("Cari Berita"):
        st.session_state.hasil = retrieve_documents(
            query,top_k
        )

        st.session_state.query = query
        
    if st.session_state.get("quick_query"):
        st.session_state.hasil = retrieve_documents(query, top_k)
        st.session_state.query = query
        del st.session_state["quick_query"]

    hasil = st.session_state.get("hasil", [])
    query = st.session_state.get("query", "")
    if query and len(hasil) == 0:
        st.warning(
        f'Tidak ditemukan berita untuk "{query}". '
        'Coba gunakan kata kunci lain atau periksa ejaan.'
    )

    if len(hasil) > 0:
            st.session_state.selected_news = None   
            
            st.caption(f'Hasil untuk query: “{query}”')

            for i, item in enumerate(hasil, start=1):

                    st.markdown(
                        f"""
                        <div class="result-card">
                            <div class="result-title">
                                {i}. {item['title']}
                            </div>
                            <div class="result-meta">
                                Similarity {item['score']:.3f}
                            </div>
                            <p class="result-summary">
                                {item['text'][:400]}...
                            </p>
                            <div class="result-meta">
                                Poin Asta Cita: {item['poin_id']}
                            </div>
                                                    """,
                        unsafe_allow_html=True,
                    )
                    if st.button(
                    f"Lihat Detail {i}",
                    key=f"detail_{i}"
                    ):
                        show_detail(item)

@st.dialog("Detail Berita")
def show_detail(item):
    st.session_state.selected_news = item

    st.markdown(
        f"""
        <div class="detail-container">
            <h2 class="detail-title">{item['title']}</h2>
            <div class="detail-badges">
                <span class="detail-badge">Poin Asta Cita: {item['poin_id']}</span>
                <span class="detail-badge">Similarity: {item['score']:.3f}</span>
            </div>
            <hr class="detail-divider">
            <p class="detail-text">{item['text']}</p>
            <div class="detail-source">
                Sumber Berita:
                <a href="{item['url']}" target="_blank" class="detail-link">{item['url']}</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
