import pandas as pd


class CodeExecutor:

    def execute(self, df, code: str):

        local_vars = {
            "df": df,
            "pd": pd,
            "result": None
        }

        exec(code, {}, local_vars)

        return local_vars.get("result")


executor = CodeExecutor()