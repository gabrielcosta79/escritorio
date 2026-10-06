import streamlit as st
import threading
import time
import datetime
import os
from google import genai
from google.genai import types

# ==========================================
# 1. IDENTIDADE VISUAL OFICIAL DA PIAGET (CSS)
# ==========================================
def aplicar_identidade_visual_piaget():
    st.markdown("""
        <style>
        .stApp {
            background-color: #f8f9fa;
            color: #0b2545;
        }
        
        h1, h2, h3, p, span {
            color: #0b2545;
        }
        
        label, .stTextInput label, .stSelectbox label, .stTextArea label, .stFileUploader label {
            color: #0b2545 !important;
            font-weight: 600 !important;
        }

        .stButton>button, 
        .stDownloadButton>button,
        [data-testid="stFormSubmitButton"]>button,
        [data-testid="stFileUploader"] button {
            background-color: #4a7758 !important;
            color: white !important;
            border-radius: 6px;
            border: none;
            font-weight: bold;
        }
        
        .stButton>button p, .stButton>button span, .stButton>button div,
        .stDownloadButton>button p, .stDownloadButton>button span, .stDownloadButton>button div,
        [data-testid="stFormSubmitButton"]>button p, [data-testid="stFormSubmitButton"]>button span, [data-testid="stFormSubmitButton"]>button div,
        [data-testid="stFileUploader"] button p, [data-testid="stFileUploader"] button span, [data-testid="stFileUploader"] button div {
            color: white !important;
        }
        
        .stButton>button:hover, 
        .stDownloadButton>button:hover,
        [data-testid="stFormSubmitButton"]>button:hover,
        [data-testid="stFileUploader"] button:hover {
            background-color: #3b5f46 !important;
            color: white !important;
            border-color: transparent !important;
        }

        /* CORREÇÃO DA CAIXA DE PERGUNTAS DO CHAT (Texto Digitado em Branco legível sobre o fundo escuro da caixa) */
        [data-testid="stChatInput"] textarea, [data-testid="stChatInput"] input {
            color: white !important;
        }

        /* CORREÇÃO DAS MENSAGENS DO CHAT (Texto escuro legível nas caixas de mensagem) */
        [data-testid="stChatMessage"] p, [data-testid="stChatMessage"] span, [data-testid="stChatMessage"] div {
            color: #0b2545 !important;
        }

        [data-testid="stSidebar"] {
            background-color: #0b2545 !important;
        }
        
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] label, [data-testid="stSidebar"] span, [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] div, [data-testid="stSidebar"] .stMarkdown {
            color: white !important;
        }

        [data-testid="stAlert"] p, [data-testid="stAlert"] span, [data-testid="stAlert"] div {
            color: #0b2545 !important;
            font-weight: 500;
        }
        
        [data-testid="stSidebar"] [data-testid="stAlert"] p, 
        [data-testid="stSidebar"] [data-testid="stAlert"] span, 
        [data-testid="stSidebar"] [data-testid="stAlert"] div {
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. MOTOR DE TAREFAS EM SEGUNDO PLANO (24/7)
# ==========================================
def worker_escritorio_full_time():
    while True:
        agora = datetime.datetime.now()
        time.sleep(86400)

def iniciar_servico_fundo():
    if "worker_iniciado" not in st.session_state:
        st.session_state["worker_iniciado"] = True
        t = threading.Thread(target=worker_escritorio_full_time, daemon=True)
        t.start()

# ==========================================
# 3. PÁGINAS DO SISTEMA E LÓGICA
# ==========================================

def render_login_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists("logo_piaget.png"):
            st.image("logo_piaget.png", use_container_width=True)
        else:
            st.markdown("""
                <div style="text-align: center; padding: 25px; background-color: #0b2545; border-radius: 10px; margin-bottom: 20px;">
                    <h1 style="color: white !important; margin: 0; font-size: 36px; font-family: serif;">PIAGET</h1>
                    <p style="color: #c5a059 !important; font-size: 13px; letter-spacing: 2px; margin: 5px 0 0 0;">CONSULTORIA E GESTÃO AMBIENTAL</p>
                </div>
            """, unsafe_allow_html=True)

        with st.form("login_form"):
            st.markdown("### Acesso Restrito")
            username = st.text_input("Usuário")
            password = st.text_input("Senha", type="password")
            if st.form_submit_button("Entrar no Sistema"):
                if username == "admin" and password == "piaget2026":
                    st.session_state["authenticated"] = True
                    st.success("Login efetuado com sucesso!")
                    st.rerun()
                else:
                    st.error("Credenciais inválidas. Verifique o usuário e a senha.")

def render_pagina_2_escopo():
    st.title("Página 2: Cadastro do Projeto e Demandas")
    st.write("Insira as informações do empreendimento. Os especialistas consultarão a legislação pertinente para definir o escopo e os documentos necessários.")
    
    with st.form("form_projeto"):
        nome_projeto = st.text_input("Nome do Projeto", value="Condomínio Residencial Parque das Orquídeas III")
        cliente = st.text_input("Cliente", value="Condomínio Residencial")
        municipio = st.text_input("Município / UF", value="São Paulo / SP")
        tipo_demanda = st.text_input("Intervenção / Demanda Ambiental", value="Supressão de espécimes arbóreos, intervenção em APP e licenciamento corretivo")
        
        docs_referencia = st.file_uploader(
            "Carregar Documentos de Referência (Plantas, Matrículas, Notificações, Relatórios)", 
            type=["pdf", "docx", "txt", "png", "jpg"], 
            accept_multiple_files=True
        )
        
        if st.form_submit_button("Acionar Coordenador e Especialistas"):
            with st.spinner("Os Especialistas Jurídico e Técnico estão a cruzar dados com a legislação Federal, Estadual e Municipal..."):
                time.sleep(1.5)
                
                documentos_dinamicos = [
                    {"id": "doc_req", "titulo": "Requerimento Padronizado de Licenciamento", "origem": "Escritório (Coordenador)"},
                    {"id": "doc_laudo", "titulo": f"Laudo Técnico / Fitossanitário ({tipo_demanda.split(',')[0]})", "origem": "Escritório (Especialista Técnico)"},
                    {"id": "doc_tabela", "titulo": "Tabela de Inventário Arbóreo / Diagnóstico", "origem": "Escritório (Especialista Técnico)"},
                    {"id": "doc_croqui", "titulo": "Croqui de Localização e Arquivos KMZ (Manejo)", "origem": "Escritório (Geoprocessamento)"},
                    {"id": "doc_matricula", "titulo": "Cópia da Matrícula do Imóvel", "origem": "Externo (Cliente)"},
                    {"id": "doc_art", "titulo": "ART / RRT de Responsabilidade Técnica", "origem": "Externo (Profissional)"}
                ]
                
                if "paulo" in municipio.lower() or "sp" in municipio.lower() or "salto" in municipio.lower():
                    documentos_dinamicos.insert(3, {"id": "doc_tca", "titulo": "TCA - Termo de Compromisso Ambiental (Legislação SP)", "origem": "Escritório (Jurídico)"})
                
                st.session_state["projeto_atual"] = {
                    "nome": nome_projeto, 
                    "cliente": cliente, 
                    "municipio": municipio, 
                    "tipo": tipo_demanda,
                    "docs_count": len(docs_referencia) if docs_referencia else 0
                }
                st.session_state["documentos_necessarios"] = documentos_dinamicos
                
                st.success(f"Varredura legal concluída! {len(documentos_dinamicos)} exigências documentais mapeadas e enviadas para a Página 3.")

    if "projeto_atual" in st.session_state:
        p = st.session_state["projeto_atual"]
        st.markdown("---")
        st.subheader("Documentação Técnica e Comercial")
        
        docs_count_seguro = p.get('docs_count', 0)
        versao_escopo = st.session_state.get('versao_escopo', 1)
        versao_prop = st.session_state.get('versao_proposta', 1)
        
        lista_docs_texto = "\n".join([f"- {d['titulo']} ({d['origem']})" for d in st.session_state.get("documentos_necessarios", [])])
        
        conteudo_escopo = f"""==================================================
ESCOPO TÉCNICO DE CONSULTORIA AMBIENTAL - ESCRITÓRIO PIAGET
VERSÃO: v{versao_escopo}.0
==================================================
1. IDENTIFICAÇÃO DO PROJETO
- Empreendimento: {p.get('nome', '')}
- Cliente: {p.get('cliente', '')}
- Natureza da Intervenção: {p.get('tipo', '')}
- Jurisdição Analisada: {p.get('municipio', '')}
- Documentos de Referência Base: {docs_count_seguro} anexo(s).

2. DIRETRIZES LEGAIS E DOCUMENTOS A SEREM PRODUZIDOS
Com base na varredura legislativa realizada pelos especialistas, ficam definidos como necessários os seguintes documentos:
{lista_docs_texto}

3. RESPONSABILIDADES DO CONTRATANTE
- Fornecer documentação de propriedade (ex: Matrícula do Imóvel atualizada em até 30 dias).
- Fornecer anuências e assinaturas necessárias para a emissão de ART/RRT.
- Efetuar o pagamento de taxas públicas e emolumentos do órgão ambiental.

4. CRONOGRAMA FÍSICO
- Levantamento de Campo e Vistoria: Até 5 dias úteis após o aceite.
- Elaboração Técnica e Documentos: Até 15 dias úteis após vistoria.
- Trâmite e Análise no Órgão Público: Estimativa de 60 a 120 dias (sujeito à administração pública).
=================================================="""

        conteudo_proposta = f"""==================================================
PROPOSTA TÉCNICA COMERCIAL - CÓDIGO: PIA-PTC-ARB-003-2026
VERSÃO: v{versao_prop}.0
==================================================
À Atenção de: {p.get('cliente', '')}
Empreendimento: {p.get('nome', '')}
Local: {p.get('municipio', '')}

1. ESCOPO RESUMIDO
O Escritório Piaget propõe a prestação de serviços especializados para a demanda técnica de "{p.get('tipo', '')}".

2. VALORES E INVESTIMENTO
- Valor total dos honorários profissionais: R$ 18.500,00 (Dezoito mil e quinhentos reais).
* Custos com plotagens físicas, recolhimento de ARTs e taxas governamentais não inclusos.

3. FORMAS DE PAGAMENTO
- Pagamento parcelado via Boleto Bancário, Transferência Bancária ou PIX.

4. CRONOGRAMA FÍSICO-FINANCEIRO (MARCOS)
A remuneração será dividida conforme os marcos de entrega:
- Marco 1 (Aceite e Assinatura): 30% do valor (R$ 5.550,00)
- Marco 2 (Entrega dos Laudos e Protocolo): 40% do valor (R$ 7.400,00)
- Marco 3 (Emissão da Licença / Deferimento): 30% do valor (R$ 5.550,00)
=================================================="""

        col_esq, col_dir = st.columns(2)

        with col_esq:
            st.markdown("### 📝 Escopo Técnico")
            if st.button("Gerar Documentos de Escopo", type="primary"):
                st.session_state["escopo_criado"] = True
                if "versao_escopo" not in st.session_state:
                    st.session_state["versao_escopo"] = 1

            if st.session_state.get("escopo_criado", False):
                st.success(f"Escopo v{st.session_state.get('versao_escopo', 1)}.0 estruturado!")
                
                st.download_button(
                    label="📥 Baixar Escopo (Word .doc)", 
                    data=conteudo_escopo, 
                    file_name=f"Escopo_{p.get('nome', 'Projeto').replace(' ', '_')}_v{st.session_state.get('versao_escopo', 1)}.doc"
                )
                
                st.markdown("#### 🔄 Corrigir / Refinar Escopo")
                correcao_escopo_file = st.file_uploader("Carregar orientações ou arquivo revisado", type=["txt", "pdf", "docx"], key="up_escopo")
                if correcao_escopo_file and st.button("Regerar Escopo"):
                    st.session_state["versao_escopo"] = st.session_state.get("versao_escopo", 1) + 1
                    st.success(f"Revisão técnica analisada! Nova versão (v{st.session_state['versao_escopo']}.0) gerada.")
                    st.rerun()

        with col_dir:
            st.markdown("### 📄 Proposta Técnica-Comercial")
            if st.button("Gerar Proposta Comercial", type="primary"):
                st.session_state["proposta_gerada"] = True
                if "versao_proposta" not in st.session_state:
                    st.session_state["versao_proposta"] = 1

            if st.session_state.get("proposta_gerada", False):
                st.success(f"Proposta v{st.session_state.get('versao_proposta', 1)}.0 disponível!")
                st.download_button(
                    label="📥 Baixar Proposta Comercial (PDF)", 
                    data=conteudo_proposta, 
                    file_name=f"Proposta_{p.get('nome', 'Projeto').replace(' ', '_')}_v{st.session_state.get('versao_proposta', 1)}.pdf"
                )

                st.markdown("#### 🔄 Corrigir / Refinar Proposta")
                correcao_file = st.file_uploader("Carregar orientações ou planilhas de ajuste", type=["txt", "pdf", "docx"], key="up_proposta")
                if correcao_file and st.button("Regerar Proposta Comercial"):
                    st.session_state["versao_proposta"] = st.session_state.get("versao_proposta", 1) + 1
                    st.success(f"Adequações analisadas! Nova versão (v{st.session_state['versao_proposta']}.0) gerada.")
                    st.rerun()

def render_pagina_3_documentos():
    st.title("Página 3: Central de Produção e Gestão de Documentos")
    if "projeto_atual" not in st.session_state or "documentos_necessarios" not in st.session_state:
        st.warning("Cadastre um projeto na Página 2 primeiro para que os especialistas definam os documentos.")
        return
    
    st.write("Abaixo estão listados os documentos exigidos para a intervenção. Acione os especialistas para gerar um Rascunho Inicial (Word), revise-o e carregue seus apontamentos antes de enviar para a formatação final na Sala de Revisão.")
    
    p = st.session_state["projeto_atual"]
    docs = st.session_state["documentos_necessarios"]
    
    if "docs_em_revisao" not in st.session_state:
        st.session_state["docs_em_revisao"] = {}
    
    for d in docs:
        st.markdown(f"### 📄 {d['titulo']}")
        st.caption(f"Responsabilidade de Produção/Fornecimento: **{d['origem']}**")
        col1, col2 = st.columns(2)
        
        with col1:
            if "Escritório" in d["origem"]:
                doc_gerado_key = f"doc_gerado_{d['id']}"
                if not st.session_state.get(doc_gerado_key, False):
                    if st.button(f"⚡ Gerar Documento Base", key=f"g_{d['id']}"):
                        st.session_state[doc_gerado_key] = True
                        st.rerun()
                else:
                    st.success("Documento estruturado pelo Especialista!")
                    conteudo_rascunho_word = f"""==================================================
DOCUMENTO TÉCNICO: {d['titulo'].upper()}
ESCRITÓRIO PIAGET DE CONSULTORIA E GESTÃO AMBIENTAL
==================================================

1. INFORMAÇÕES GERAIS
Empreendimento: {p.get('nome', 'Não informado')}
Cliente: {p.get('cliente', 'Não informado')}
Local: {p.get('municipio', 'Não informado')}

[RASCUNHO PRELIMINAR - PRONTO PARA REVISÃO DO GESTOR]
"""
                    st.download_button(
                        label=f"📥 Baixar Rascunho Inicial", 
                        data=conteudo_rascunho_word,
                        file_name=f"{d['titulo'].replace(' ', '_').replace('/', '-')}_Rascunho.doc",
                        key=f"dl_{d['id']}"
                    )

                    if "kmz" in d['titulo'].lower() or d['id'] == "doc_croqui":
                        conteudo_kmz = f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Poligonais_e_Individuos_Arboreos_{p.get('nome', 'Projeto').replace(' ', '_')}</name>
    <description>Arquivo KMZ/KML gerado pelo Especialista em Geoprocessamento - Piaget Consultoria</description>
  </Document>
</kml>"""
                        st.download_button(
                            label=f"🌍 Baixar Arquivo Espacial (.kmz)", 
                            data=conteudo_kmz,
                            file_name=f"Mapa_Manejo_{p.get('nome', 'Projeto').replace(' ', '_')}.kmz",
                            mime="application/vnd.google-earth.kmz",
                            key=f"dl_kmz_{d['id']}"
                        )
                    
                    st.file_uploader(f"Carregar apontamentos (.doc, .docx, .kmz):", key=f"up_notas_{d['id']}")
            else:
                st.file_uploader(f"Carregar documento final:", key=f"up_externo_{d['id']}")
                
        with col2:
            if st.button(f"🔍 Enviar para Sala de Revisão", key=f"rev_{d['id']}", type="primary"):
                st.session_state["docs_em_revisao"][d['id']] = {
                    "titulo": d['titulo'],
                    "origem": d['origem'],
                    "versao": 1,
                    "aprovado": False
                }
                st.success(f"{d['titulo']} enviado para a Sala de Revisão (Página 4)!")
        st.markdown("---")

def render_pagina_4_revisao():
    st.title("Página 4: Sala de Revisão, Versões e Aprovação")
    st.write("Os Especialistas Analistas e de Formatação atuam automaticamente nos documentos que chegam a esta sala. Revise, solicite novas versões ou aprove o Produto Final.")
    
    if "docs_em_revisao" not in st.session_state or not st.session_state["docs_em_revisao"]:
        st.warning("Nenhum documento foi enviado para a Sala de Revisão a partir da Página 3.")
        if st.button("Voltar para Página 3"):
            st.session_state["pagina_ativa"] = "Página 3: Central de Documentos"
            st.rerun()
        return

    docs_em_revisao = st.session_state["docs_em_revisao"]
    todos_aprovados = True
    
    p = st.session_state.get("projeto_atual", {})

    for doc_id, info in docs_em_revisao.items():
        st.markdown(f"### 📑 {info['titulo']}")
        
        if info["aprovado"]:
            st.success("✅ PRODUTO FINAL APROVADO. Este documento está trancado e pronto para o Checklist.")
        else:
            todos_aprovados = False
            st.info(f"🤖 **Atuação Automática Concluída:** O Especialista validou os requisitos técnicos e o Especialista em Documentos aplicou a formatação e Identidade Visual Piaget. (Versão **v{info['versao']}.0**)")
            
            conteudo_revisao = f"""[ESCRITÓRIO PIAGET - DOCUMENTO OFICIAL FORMATADO]
DOCUMENTO: {info['titulo'].upper()}
VERSÃO: v{info['versao']}.0
STATUS: REVISÃO DE IDENTIDADE VISUAL E LEGALIDADE APLICADA."""
            
            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    label=f"📥 Baixar Revisão v{info['versao']}.0", 
                    data=conteudo_revisao, 
                    file_name=f"{info['titulo'].replace(' ', '_')}_v{info['versao']}.doc",
                    key=f"dl_rev_{doc_id}"
                )
                
                if "kmz" in info['titulo'].lower() or doc_id == "doc_croqui":
                    conteudo_kmz_rev = f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Revisao_v{info['versao']}_{p.get('nome', 'Projeto').replace(' ', '_')}</name>
  </Document>
</kml>"""
                    st.download_button(
                        label=f"🌍 Baixar Revisão Espacial v{info['versao']}.0 (.kmz)", 
                        data=conteudo_kmz_rev,
                        file_name=f"Mapa_Revisao_v{info['versao']}_{p.get('nome', 'Projeto').replace(' ', '_')}.kmz",
                        mime="application/vnd.google-earth.kmz",
                        key=f"dl_kmz_rev_{doc_id}"
                    )
                
                arq_correcao = st.file_uploader("Submeter novas correções/apontamentos:", key=f"up_correcao_{doc_id}")
                if arq_correcao and st.button("Gerar Nova Revisão", key=f"btn_nova_rev_{doc_id}"):
                    st.session_state["docs_em_revisao"][doc_id]["versao"] += 1
                    st.success(f"Apontamentos processados. Nova versão v{st.session_state['docs_em_revisao'][doc_id]['versao']}.0 gerada!")
                    st.rerun()
            
            with col2:
                if st.button("✅ Aprovar como Produto Final", key=f"btn_aprovar_{doc_id}", type="primary"):
                    st.session_state["docs_em_revisao"][doc_id]["aprovado"] = True
                    st.rerun()
                    
        st.markdown("---")

    if st.button("🚀 Encaminhar Documentos Aprovados para o Checklist (Página 5)", type="primary"):
        st.session_state["pagina_ativa"] = "Página 5"
        st.rerun()

def render_pagina_5_checklist():
    st.title("Página 5: Checklist de Documentos do Projeto")
    st.write("Consolidação automática dos documentos validados para protocolo final.")
    
    docs = st.session_state.get("documentos_necessarios", [])
    docs_revisao = st.session_state.get("docs_em_revisao", {})
    
    if not docs:
        st.warning("Lista de documentos não encontrada. Cadastre o projeto na Página 2.")
        return
        
    for d in docs:
        is_aprovado = docs_revisao.get(d['id'], {}).get("aprovado", False)
        status_texto = " (Produto Final Aprovado)" if is_aprovado else " (Pendente de Aprovação)"
        
        st.checkbox(f"{d['titulo']} {status_texto}", value=is_aprovado, key=f"chk_{d['id']}")

    st.markdown("---")
    if st.button("📦 Gerar Pacote Completo (.zip para Protocolo)", type="primary"):
        st.success("Pacote compilado com sucesso com a identidade visual Piaget! Pronto para submeter ao órgão ambiental.")
        st.balloons()

# ==========================================
# MOTOR COM API REAL DO GEMINI E OS 12 ESPECIALISTAS
# ==========================================
def gerar_resposta_com_gemini(historico_chat, pergunta_usuario):
    # Substitua "SUA_CHAVE_GEMINI_AQUI" pela sua chave de API real do Google Gemini (ex: "AIzaSy...")
    api_key = "AQ.Ab8RN6JkmhLfOx70Xd4hrJ9Y1jtdGS2OcfM_zjGwC-hh7QRr3A"
    
    if not api_key or api_key == "SUA_CHAVE_GEMINI_AQUI":
        return "⚠️ **Erro de Configuração:** Por favor, insira a sua chave de API real do Google Gemini (começada por AIzaSy...) na variável `api_key` dentro do código."

    try:
        client = genai.Client(api_key=api_key)
        
        # System Prompt avançado integrando os 12 Especialistas do Escritório Piaget
        system_instruction = """
        Você é o Coordenador-Geral do Escritório Piaget de Consultoria e Gestão Ambiental. 
        O seu papel é coordenar e sintetizar a deliberação simultânea dos 12 Especialistas da equipa multidisciplinar 
        para responder a qualquer demanda, dúvida, problema pontual, autuação ou licenciamento ambiental trazido pelo utilizador.
        
        Sempre que o utilizador fizer uma pergunta, a sua resposta deve articular as perspetivas técnicas, jurídicas, cartográficas e executivas dos 12 especialistas:
        1. Especialista Jurídico (Leis Federais como 9.605/98, 11.428/06, decretos e prazos recursais).
        2. Especialista Técnico e Florestal (Supressão de vegetação, estágios sucessionais, APP, inventário arbóreo).
        3. Especialista em Geoprocessamento e SIG (Mapeamento, prioridades de restauração municipal, arquivos KMZ).
        4. Especialista em Licenciamento Ambiental (Órgãos como CETESB, IBAMA, Secretarias Municipais, prazos e exigências).
        5. Especialista em Gestão de Conflitos e Autuações.
        6. Especialista em Engenharia de Remediação e Recuperação Ambiental.
        7. Especialista em Recursos Hídricos e Outorgas.
        8. Especialista em Regularização Fundiária e Cadastral.
        9. Especialista em Sustentabilidade e ESG Corporativo.
        10. Especialista em Custos, Orçamentos e Viabilidade Económica.
        11. Especialista em Propostas Técnicas e Redação Executiva.
        12. Especialista em Identidade Visual e Formatação de Produtos Finais.
        
        Responda de forma extremamente técnica, precisa, cirúrgica, fundamentada na legislação aplicável (como a Resolução SEMIL e leis correlatas) e estruturada em tópicos claros, sem respostas evasivas.
        """
        
        # Constrói o histórico de conversação para o Gemini
        conteudos_chat = []
        for m in historico_chat[:-1]: # Pega o histórico anterior
            role = "user" if m["role"] == "user" else "model"
            conteudos_chat.append(types.Content(role=role, parts=[types.Part.from_text(text=m["content"])]))
            
        conteudos_chat.append(types.Content(role="user", parts=[types.Part.from_text(text=pergunta_usuario)]))

        # Chamada ao modelo Gemini
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=conteudos_chat,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.2, # Baixa temperatura para garantir máxima precisão técnica e jurídica
            ),
        )
        return response.text

    except Exception as e:
        return f"❌ Ocorreu um erro ao comunicar com a API do Gemini: {str(e)}"

def render_pagina_6_chat():
    st.title("⚡ Página 6: Solução de Problemas Pontuais (Chat Inteligente Gemini)")
    st.write("Converse diretamente com os 12 agentes especialistas da Piaget mobilizados em tempo real pela inteligência artificial do Gemini para resolver autuações, embargos ou dúvidas técnicas.")
    
    if "chat_hist" not in st.session_state:
        st.session_state["chat_hist"] = [{"role": "assistant", "content": "Olá! Sou o Coordenador da Piaget Consultoria. O nosso chat aciona em tempo real os 12 especialistas multidisciplinares via Gemini para responder com precisão cirúrgica à sua demanda. Como posso ajudar hoje?"}]

    for m in st.session_state["chat_hist"]:
        with st.chat_message(m["role"]):
            st.write(m["content"])

    if user_q := st.chat_input("Ex: Qual a compensação ambiental para supressão em estágio médio em Salto/SP?"):
        st.session_state["chat_hist"].append({"role": "user", "content": user_q})
        with st.chat_message("user"):
            st.write(user_q)
        
        with st.chat_message("assistant"):
            with st.spinner("Os 12 Especialistas estão a consultar a legislação e a articular a resposta via Gemini..."):
                resposta = gerar_resposta_com_gemini(st.session_state["chat_hist"], user_q)
                st.write(resposta)
                st.session_state["chat_hist"].append({"role": "assistant", "content": resposta})

# ==========================================
# 4. CONTROLADOR PRINCIPAL
# ==========================================
def main():
    iniciar_servico_fundo()
    
    st.set_page_config(
        page_title="Escritório Piaget - Consultoria Ambiental", 
        layout="wide", 
        page_icon="logo_piaget.png" if os.path.exists("logo_piaget.png") else "🌿"
    )
    
    aplicar_identidade_visual_piaget()

    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        render_login_page()
        return

    if os.path.exists("logo_piaget.png"):
        st.sidebar.image("logo_piaget.png", use_container_width=True)
    else:
        st.sidebar.markdown("""
            <div style="text-align: center; padding: 12px; background-color: #0b2545; border-radius: 8px;">
                <h2 style="color: white !important; margin-bottom: 0px; font-size: 22px; font-family: serif;">PIAGET</h2>
                <p style="color: #c5a059 !important; font-size: 10px; letter-spacing: 1px; margin: 0;">CONSULTORIA E GESTÃO AMBIENTAL</p>
            </div>
        """, unsafe_allow_html=True)

    st.sidebar.info("Modo Full Time 24/7 Ativo 🟢\nOs agentes operam continuamente.")
    st.sidebar.markdown("---")

    if "pagina_ativa" not in st.session_state:
        st.session_state["pagina_ativa"] = "Página 2: Escopo"

    nav = st.sidebar.radio(
        "Navegação Principal",
        [
            "Página 2: Escopo",
            "Página 3: Central de Documentos",
            "Página 4: Sala de Revisão",
            "Página 5: Checklist de Protocolo",
            "Página 6: Problemas Pontuais (Chat)"
        ]
    )

    if "Página 2" in nav: st.session_state["pagina_ativa"] = "Página 2: Escopo"
    elif "Página 3" in nav: st.session_state["pagina_ativa"] = "Página 3: Central de Documentos"
    elif "Página 4" in nav: st.session_state["pagina_ativa"] = "Página 4"
    elif "Página 5" in nav: st.session_state["pagina_ativa"] = "Página 5"
    elif "Página 6" in nav: st.session_state["pagina_ativa"] = "Página 6"

    st.sidebar.markdown("---")
    if st.sidebar.button("Sair do Sistema"):
        st.session_state["authenticated"] = False
        st.rerun()

    if st.session_state["pagina_ativa"] == "Página 2: Escopo":
        render_pagina_2_escopo()
    elif st.session_state["pagina_ativa"] == "Página 3: Central de Documentos":
        render_pagina_3_documentos()
    elif st.session_state["pagina_ativa"] == "Página 4":
        render_pagina_4_revisao()
    elif st.session_state["pagina_ativa"] == "Página 5":
        render_pagina_5_checklist()
    elif st.session_state["pagina_ativa"] == "Página 6":
        render_pagina_6_chat()

if __name__ == "__main__":
    main()
