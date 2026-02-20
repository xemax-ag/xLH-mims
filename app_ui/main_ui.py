import streamlit as st

from app_ui.toolbox.page_config import page_config

page_config(page_title='xLH-mims')

try:
    pages = {}

    home = st.Page(page='pages_/home.py', title='Startseite', icon=':material/home:', default=True)
    pages[''] = [home]

    demo = st.Page(page='pages_/demo/demo_1.py', title='Demo: PoC Agent UI',
                   icon=':material/chat_bubble:')
    pages['DEMO'] = [demo]

    settings = st.Page(page='pages_/account/settings.py', title='Einstellungen', icon=':material/settings:')
    pages['BENUTZER'] = [settings]

    pg = st.navigation(pages)
    pg.run()

except Exception as e:
    st.error(e)
    st.title(f'xLH-mims')
    st.stop()

# https://fonts.google.com/icons?icon.query=home
#  https://emojipedia.org/






































# st.title('Chat')
# st.markdown('cookies')
# # st.write(st.context.cookies)
# # st.markdown('headers')
# # st.write(st.context.headers)
#
# client = OpenAI(api_key=config.openai_api_key)
#
# if 'openai_model' not in st.session_state:
#     st.session_state['openai_model'] = 'gpt-5.2'
#
# if 'messages' not in st.session_state:
#     st.session_state.messages = []
#
# for message in st.session_state.messages:
#     with st.chat_message(message['role']):
#         st.markdown(message['content'])
#
# if prompt := st.chat_input('What is up?'):
#     st.session_state.messages.append({'role': 'user', 'content': prompt})
#     with st.chat_message('user'):
#         st.markdown(prompt)
#
#     with st.chat_message('assistant'):
#         stream = client.chat.completions.create(
#             model=st.session_state['openai_model'],
#             messages=[
#                 {'role': m['role'], 'content': m['content']}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         )
#         response = st.write_stream(stream)
#     st.session_state.messages.append({'role': 'assistant', 'content': response})