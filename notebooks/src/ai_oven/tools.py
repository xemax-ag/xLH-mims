from pydantic_ai import Agent, RunContext
from deps import Deps

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
