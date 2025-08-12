from camel.messages import SystemMessage, ChatMessage
from camel.typing import RoleType, ModelType
from camel.agents import ChatAgent

def main():
    system_msg = SystemMessage(
        role_name="Assistant",
        role_type=RoleType.ASSISTANT,
        role="system",
        content="Você é um assistente de programação especializado em Python.",
        meta_dict={}
    )

    agent = ChatAgent(
        system_message=system_msg,
        model=ModelType.CODELLAMA
    )

    user_msg = ChatMessage(
        role_name="User",
        role_type=RoleType.USER,
        role="user",
        content="Como funciona uma função recursiva em Python?",
        meta_dict={}
    )

    response = agent.step(user_msg)
    print("\n🧠 Resposta do modelo local:")
    print(response.msg.content)

if __name__ == "__main__":
    main()
