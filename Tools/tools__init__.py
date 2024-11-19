

from Libs.libs import *
from Tools.sport_tool import *


class GetCustomTools():

    tools = []

    def __init__(self, params=None):
        self.params = params
        self.initialize_tools()

    def initialize_tools(self):
        retrieval_toool= StructuredTool.from_function(
            name='Tool_1',
            func=retrieval_tool(self.params),
            description=f"A tool that answers the query about {name}",
            args_schema=QueryInput,
            return_direct=False
        )


      
        self.tools = [retrieval_toool]

    def get_tools(self):
        return self.tools

    def get_tools_names(self):
        return [tool.name for tool in self.tools]
