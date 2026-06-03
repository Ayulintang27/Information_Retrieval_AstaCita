import pandas as pd
import re
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')


#Load Data berita
data = pd.read_csv("data/asta cita skripsi baru.csv", on_bad_lines='warn')
data.info()

df = pd.DataFrame(data[['poin_id','date','title','text']])

# Tahapan cleaning data =========================================================================================================
def cleaning_text(text):
    # Hindari error kalau NaN atau bukan string
    if text is None or not isinstance(text, str):
        return ""

    text_lower = text.lower()

    if 'jadwal sholat' in text_lower:
        return ""

# MENGHAPUS ANGKA
    text = re.sub(r'\d+', ' ', text)

# HEADER BERITA / LOKASI
    text = re.sub(
        r'^[A-Za-z0-9\s\.,]+?\s[-–]\s*',
        '',
        text
)


# MENGHAPUS FORMAT TANGGAL
    text = re.sub(r'\d{1,2}/\d{1,2}/\d{2,4}', '', text)
    text = re.sub(r'\d{1,2}/\d{1,2}', '', text)
    text = re.sub(r'\d{1,2}\s(januari|februari|maret|april|mei|juni|juli|agustus|september|oktober|november|desember)\s?\d{0,4}', '', text, flags=re.IGNORECASE)

# MENGHAPUS JAM
    text = re.sub(r'\d{1,2}:\d{2}:\d{2}', '', text)
    text = re.sub(r'\d{1,2}:\d{2}\s?(wib|wit|wita)?', '', text, flags=re.IGNORECASE)

# MENGHAPUS ELEMEN TAMBAHAN BERITA
    text = re.sub(r'baca juga.*', '', text,flags=re.IGNORECASE)
    text = re.sub(r'halaman selanjutnya.*', '', text,flags=re.IGNORECASE)
    text = re.sub(r'editor.*', '', text,flags=re.IGNORECASE)
    text = re.sub(r'dibaca\s[\d\.,]+\skali','', text, flags=re.IGNORECASE)
    text = re.sub(r'lanjut baca.*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'gulir untuk.*', '', text,flags=re.IGNORECASE)
    text = re.sub(r'advertisement.*', '', text,flags=re.IGNORECASE)

  # TAMBAHAN METADATA BERITA
    text = re.sub(r'sekilas info.*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'kontribusi dari.*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'tim news.*', '', text, flags=re.IGNORECASE)

# MENGHAPUS FOOTER BERITA
    footer_patterns = r'(penulis|phone|editor|reporter|situs resmi|tentang kami|kontak kami|galeri|alamat|all rights reserved|©|email|telp|\.go\.id|share)'
    text = re.split(footer_patterns, text)[0]

# MENGHAPUS SPASI BERLEBIH
    text = re.sub(r'\s+', ' ', text).strip()

# MENGHAPUS SIMBOL DAN SIMBOL KHUSUS
    text = re.sub(r'[^a-zA-Z0-9\s]','', text)

    return text

#MENGHAPUS NOISE
df = df.dropna(subset=['text'])

df = df[
    (df['text'].str.strip() != '') &  # tidak kosong
    (df['text'].str.split().str.len() > 5) &  # minimal kata
    (df['text'].str.len() > 20) &  # minimal karakter

    (~df['text'].str.contains(
        'access denied|cloudflare|security service|blocked|ray id|forbidden|captcha|error|'
        'jadwal sholat|kabupaten|provinsi|kota|'
        'javascript|enable cookies|please wait',
        case=False,
        na=False
    ))
]

# Terapkan ke dataframe
df['clean_text'] = df['text'].apply(cleaning_text)
df = df[df['clean_text'].str.strip() != '']


# Tahapan case folding =========================================================================================================
def case_folding(clean_text):
  if isinstance(clean_text,str):
    lowercase_clean_text =clean_text.lower()
    return lowercase_clean_text
  else:
    return clean_text

df['case_folding'] = df['clean_text'].apply(case_folding)
df = df[df['case_folding'].str.strip() != '']

# Tahapan tokenization =========================================================================================================
from nltk.tokenize import word_tokenize

def tokenize_text(text):
  tokens = word_tokenize(text)
  return tokens

df['tokens'] = df['case_folding'].apply(tokenize_text)

# Tahapan stopword removal =========================================================================================================
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
factory = StopWordRemoverFactory()
# stopword default
stopwords_id = set(factory.get_stop_words())
# tambahan manual
more_stopwords = ['yang', 'dan', 'di', 'ke','jadi','kata']
# gabungkan
stopwords_id.update(more_stopwords)

stopwords_id = set(stopwords_id)

def remove_stopwords(tokens):
    if not isinstance(tokens, list):
        return ""

    filtered = [word for word in tokens if word not in stopwords_id]
    return (filtered)

df['stopword_removal'] = df['tokens'].apply(remove_stopwords)

#data setelah tahapan preprocessing
df_final = df[['poin_id','date','title','text','clean_text','case_folding','stopword_removal']]
df_final.to_csv(
    'data/data_bersih.csv',
    index=False,
    encoding='utf-8-sig'
)

print("Data berhasil disimpan!")