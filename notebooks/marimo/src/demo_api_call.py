import marimo

__generated_with = "0.20.1"
app = marimo.App(width="full", sql_output="native")


@app.cell
def _():
    import marimo as mo
    import httpx
    from demo_api_call_models import SearchQuery, SearchResponseData

    return SearchQuery, SearchResponseData, httpx, mo


@app.cell
def _():
    # URL des API-Endpunktes semantische Suche Futuremem
    url = 'https://futuremem-data.xemax.ch/api/v1/query-skills/'
    return (url,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Semantische Suche FUTUREMEM Datenbank
    Die Datenabfrage erfolgt via API-Aufruf
    """)
    return


@app.cell
def _(mo):
    search_query = mo.ui.text_area(placeholder="Eingabe Suchbegriff [mit Tabulator oder CTRL + Enter wird der Request an die API gestartet]")
    search_query
    return (search_query,)


@app.cell
def _(SearchQuery, SearchResponseData, httpx, search_query, url):
    if len(search_query.value) > 0:
        data = SearchQuery(query=search_query.value,
                           language='de',
                           n_results=15,
                          )
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        response = httpx.request(method='POST', url=url, json=data.model_dump(), headers=headers)

        if response.status_code == 200:  # request okay
            # print(response.json())
            search_response_data = SearchResponseData(**response.json())
            #print(search_response_data.model_dump_json(indent=2))
            #print(response.headers['x-process-time'])
            response_text = ''
            for data in search_response_data.data:
                response_text += f'{(data.distance*100.0):0.0f} % | '
                response_text += f'{data.metadatas.level} | '
                response_text += f'{data.document[:120]}<br>\n'
        else:
            response_text = 'connection failure'
    else:
        response_text = 'Bitte Suchbegriff eingeben!'
    return (response_text,)


@app.cell(hide_code=True)
def _(mo, response_text):
    mo.md(f"""
    {response_text}
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
