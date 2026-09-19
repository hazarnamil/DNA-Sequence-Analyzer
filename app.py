import streamlit as st

# Page Configuration
st.set_page_config(page_title="DNA Sequence Analyzer", page_icon="🧬", layout="centered")

# App Title & Description
st.title("🧬 DNA Sequence Analyzer")
st.write(
    "An interactive web tool to analyze DNA sequences, calculate GC/AT content, and generate RNA & Reverse Complement strands.")

st.divider()

# Input Section
dna_input = st.text_area("Enter DNA Sequence:", value="AATTCCGTA", height=100)

# Process Input
dna = dna_input.strip().upper()

# Analyze Button
if st.button("Analyze Sequence 🚀", type="primary"):
    valid_bases = {'A', 'T', 'C', 'G'}

    # Validation Check
    if not dna or not set(dna).issubset(valid_bases):
        st.error("⚠️ Please enter a valid DNA sequence containing only A, T, C, and G bases.")
    else:
        # Calculations
        length = len(dna)
        count_a = dna.count('A')
        count_t = dna.count('T')
        count_c = dna.count('C')
        count_g = dna.count('G')

        gc_content = ((count_g + count_c) / length) * 100
        at_content = ((count_a + count_t) / length) * 100

        # RNA Transcription
        rna = dna.replace('T', 'U')

        # Reverse Complement
        complement_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        complement = "".join([complement_map[base] for base in dna])
        reverse_complement = complement[::-1]

        # Display Metrics
        st.subheader("📊 Basic Statistics")

        col1, col2, col3 = st.columns(3)
        col1.metric("Sequence Length", f"{length} bp")
        col2.metric("GC Content", f"{gc_content:.2f}%")
        col3.metric("AT Content", f"{at_content:.2f}%")

        st.write("**Nucleotide Base Counts:**")
        col_a, col_t, col_c, col_g = st.columns(4)
        col_a.metric("A", count_a)
        col_t.metric("T", count_t)
        col_c.metric("C", count_c)
        col_g.metric("G", count_g)

        st.divider()

        # Display Output Sequences
        st.subheader("🧪 Output Sequences")
        st.code(f"RNA Sequence        : {rna}", language="text")
        st.code(f"Reverse Complement  : {reverse_complement}", language="text")
        st.code(f"Reverse Comp Length : {len(reverse_complement)} bp", language="text")

        st.success("Analysis completed successfully! ✨")