from pydantic_ai import Agent, RunContext
from deps import Deps
import requests
import pandas as pd

def set_oven_temperature(ctx: RunContext[Deps], temperature: float) -> bool:
    """
    :param temperature: Einstellung der Backofentemperatur in Grad Celsius.
    Die Temperatur muss zwischen 100 und 250 Grad liegen.
    Die Rückgabe ist True, falls der Backofen die gewünschte Temperatur einstellen kann.
    """
    print(f'=> tool_set_oven_temperature {temperature}')
    set_oven_temperature_opcua(temperature=temperature)
    return True if temperature >= 100 and temperature <= 250 else False

def set_oven_temperature_opcua(temperature: float):
    print(f'=> set_oven_temperature_opcua {temperature}')

def read_hk(ctx: RunContext[Deps], id: str) -> str:
    """
    Gibt die Daten zu den Handlungskompetenzen als DataFrame zurück.
    In den Spalten sind die folgenden Informationen abgelegt:
    - 'id_hk': ID der Handlungskompetenzen
    - 'HK': Titel der Handlungskompetenz
    - 'situation': Beschreibung einer Arbeitssituation der Handlungskompetenz
    - 'ziel': Beschreibung des Ziels der Handlungskompetenz
    :param id: ID der Weiterbildung RS oder TS
    :return: DataFrame mit den Informationen
    """
    print(f'=> read_hk {id}')
    df = pd.read_pickle(f"{id}_HK.pkl")
    json_str = df.to_json(orient="records")
    return json_str

def set_color2rgb(ctx: RunContext[Deps], r: int = 0, g: int = 0, b: int = 0):
    """
    Sets the RGB color remotely by sending a GET request to a predefined URL endpoint.

    This function is used to control RGB color settings by providing specific values
    for red, green, and blue color components. The function sends a request to a fixed
    URL and retrieves the result in JSON format. The function assumes the default URL
    and headers configuration necessary to interact with the endpoint.

    :param r: Red component of the RGB color (default is 0)
    :param g: Green component of the RGB color (default is 0)
    :param b: Blue component of the RGB color (default is 0)
    :return: JSON response from the server containing details of the operation
    :rtype: dict
    """
    print(f'=> set_color2rgb r:{r//10}, g:{g//10}, b:{b//10}')
    url_xlh_base = 'http://192.168.78.55/v1'
    headers = {
        'User-Agent': 'xLH'
    }
    response = requests.request('GET', f'{url_xlh_base}/rgb/wipe/{r//10}/{g//10}/{b//10}/', headers=headers)
    # print(response)
    return response.json()



if __name__ == '__main__':
    from pydantic_ai import Agent
    from pydantic_ai.models.test import TestModel
    from rich import print

    model = TestModel()
    deps: Deps = Deps()
    agent = Agent(
        model=model,
        deps_type=str,
        tools=[set_oven_temperature],
    )
    # result = agent.run_sync(user_prompt='hallo', model=model, deps=deps)
    # for function_tool in model.last_model_request_parameters.function_tools:
    #     print(f'===> {function_tool.name}')
    #     print(function_tool.parameters_json_schema)

    set_oven_temperature_opcua(temperature=315)
