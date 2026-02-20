import streamlit as st
from app_ui.toolbox.page_config import page_config

page_config(page_title='Demo 1')

#######################################################################################################################

# Initialize chat history
if 'messages_chat' not in st.session_state:
    st.session_state.messages_chat = []

if 'chat_select' not in st.session_state:
    st.session_state.chat_select = ['5.2']

#######################################################################################################################

with st.sidebar:
    st.info(body='Chat mit erweiterten Einstellungen für einfachere Agentenbasierte Chats => '
            'LKN Formulierungen, Miro', icon='ℹ️')

    @st.dialog('Erweiterte Einstellungen Chatbot', width='medium')
    def settings_chatbot(item):
        st.write('''
            Divere Einstellung für den Chataufruf
        ''')
        with st.expander(label='Parameter Chataufruf', expanded=True):

            # options = st.selectbox(
            #     'GPT Modell',
            #     ['5.2', '5.2-mini'],
            #     key='chat_select'
            #     # default=st.session_state.chat_select,
            # )
            # st.write('You selected:', options)
            agree = st.checkbox('I agree', key='chat_checkbox')

        if st.button('Speichern', use_container_width=True):
            st.rerun()


    options = st.selectbox(
        'GPT Modell',
        ['5.2', '5.2-mini'],
        key='chat_select',
        accept_new_options=False,
        # default=st.session_state.chat_select,
    )

    if st.button('Erweiterte Einstellungen', use_container_width=True):
        settings_chatbot('A')

#######################################################################################################################

st.markdown('### Chat erweiterte Einstellungen')

if len(st.session_state.messages_chat) == 0:
    with st.chat_message('assistant'):
        st.write('Hallo 👋')

# Display chat messages from history on app rerun
for message in st.session_state.messages_chat:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
        # st.markdown(message['dummy'])
        if message['role'] == 'user':
            with st.expander(label='Parameter Chataufruf', expanded=False):
                st.write('Auflistung der Parameter für den Chataufruf')
        if message['role'] == 'assistant':
            with st.expander(label='Erweiterte Antwort', expanded=False):
                st.write('Verlinkung der Antwort auf weitere Features (Files, Link, Miro, ...)')

if prompt := st.chat_input('Prompteingabe', ):
    st.session_state.messages_chat.append({'role': 'user', 'content': prompt, 'dummy': 'abcdefg123'})
    response = f'Echo der Antwort: {prompt}'
    st.session_state.messages_chat.append({'role': 'assistant', 'content': response, 'dummy': 'aaaaaaaaaaaaaaaaaa'})

    # with st.chat_message('user'):
    #     st.markdown(prompt)
    #
    # with st.chat_message('assistant'):
    #     st.markdown(response)

    st.rerun()


















# chat_input_style = f'''
#     <style>
#         .stChatInput {{
#           position: fixed;
#           width: 60%;
#           bottom: 1rem;
#         }}
#     </style>
#     '''








