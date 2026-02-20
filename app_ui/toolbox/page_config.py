import streamlit as st


def logo():
    st.logo(image='https://nextecmedia-api.xemax.ch/static/assets/logo/xemax_logo_claim.svg',
            link="https://xemax.ch",
            icon_image='https://nextecmedia-api.xemax.ch/static/assets/logo/xemax_brain.png')

def set_client_options():
    st.set_option('client.toolbarMode', 'viewer')  # minimal viewer developer
    st.set_option('client.showErrorDetails', True)
    st.set_option('client.showSidebarNavigation', True)


def st_html_optimizer():
    # https://discuss.streamlit.io/t/reduce-white-space-top-of-the-page/21737/6
    st.markdown("""
            <style>
                   .block-container {
                        padding-top: 0.75rem;
                        padding-bottom: 1rem;
                        padding-left: 1rem;
                        padding-right: 1rem;
                    }
            </style>
            """, unsafe_allow_html=True)

    st.markdown(
        """
        <style>
          /* Hide the top-right status/running indicator (and its container) */
          div[data-testid="stStatusWidget"] {
            display: none !important;
          }

          /* If your Streamlit build places it in the toolbar, hide that too */
          // div[data-testid="stToolbar"] {
          //   display: none !important;
          // }
          
        </style>
        """,
        unsafe_allow_html=True,
    )



def page_config(page_title: str = 'UI'):
    set_client_options()
    st.set_page_config(page_title=page_title,
                       page_icon='/static/img/logo/xemax_brain_icon.png',
                       layout='wide',  # 'wide' 'centered', None
                       initial_sidebar_state='expanded',
                       menu_items={
                           'Get Help': 'https://www.xemax.ch',
                           'Report a bug': 'https://www.xemax.ch',
                           'About': 'xemax ag'
                       })
    st_html_optimizer()
    logo()
