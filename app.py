import autogen

llm_config = {"config_list": [{
    "model": ""
}]}

bob = autogen.AssistantAgent(
    name="bob",
    system_message="you love telling jokes",
    llm_config=llm_config
)

alice = autogen.AssistantAgent(
    name="alice",
    system_message="Criticise the joke and then just reply 'TERMINATE'",
    llm_config=llm_config
)

def termination_message(msg):
    return "TERMINATE" in str(msg.get("content",""))

user_proxy = autogen.AssistantAgent(
    name="user_proxy",
    code_execution_config={"user_docker": False},
    is_termination_msg=termination_message,
    human_input_mode="NEVER"
)

