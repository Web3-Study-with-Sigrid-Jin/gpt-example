from langchain import LLMChain, OpenAI, PromptTemplate, SerpAPIWrapper
from langchain.agents import Tool, ZeroShotAgent

serp_api_wrapper = SerpAPIWrapper()
todo_prompt = PromptTemplate.from_template(
    "You are a planner who is an expert at coming up with a todo list for a given objective. Come up with a todo list for this objective: {objective}"
)
todo_chain = LLMChain(llm=OpenAI(temperature=0), prompt=todo_prompt)

tools = [
    Tool(
        name="Search",
        func=serp_api_wrapper.run,
        description="useful for when you need to answer questions about current events",
    ),
    Tool(
        name="TODO",
        func=todo_chain.run,
        description="useful for when you need to come up with todo lists. Input: an objective to create a todo list for. Output: a todo list for that objective. Please be very clear what the objective is!",
    ),
]

prefix = """You are an AI who performs one task based on the following objective: {objective}.
Take into account these previously completed tasks: {context}."""

suffix = """Question: {task}
{agent_scratchpad}"""

prompt = ZeroShotAgent.create_prompt(
    tools,
    prefix=prefix,
    suffix=suffix,
    input_variables=["objective", "task", "context", "agent_scratchpad"],
)