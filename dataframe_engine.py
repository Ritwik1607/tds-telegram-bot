import pandas as pd


class DataFrameEngine:
    """
    Executes structured operations on a pandas DataFrame.
    """

    def execute(self, df: pd.DataFrame, plan: dict):

        try:
            operation = plan.get("operation")

            if operation == "shape":
                return {
                    "rows": int(len(df)),
                    "columns": int(len(df.columns))
                }

            elif operation == "columns":
                return list(df.columns)

            elif operation == "head":
                n = int(plan.get("n", 5))
                return df.head(n).to_dict(orient="records")

            elif operation == "tail":
                n = int(plan.get("n", 5))
                return df.tail(n).to_dict(orient="records")

            elif operation == "describe":
                return (
                    df.describe(include="all")
                    .fillna("")
                    .to_dict()
                )

            elif operation in ["max", "min", "mean", "median", "sum"]:
                column = plan.get("column")

                if column not in df.columns:
                    return {
                        "error": f"Column '{column}' not found"
                    }

                series = pd.to_numeric(
                    df[column],
                    errors="coerce"
                )

                if operation == "max":
                    return float(series.max())

                elif operation == "min":
                    return float(series.min())

                elif operation == "mean":
                    return float(series.mean())

                elif operation == "median":
                    return float(series.median())

                elif operation == "sum":
                    return float(series.sum())


            elif operation == "count":
                return int(len(df))


            elif operation == "unique":
                column = plan.get("column")

                if column not in df.columns:
                    return {
                        "error": f"Column '{column}' not found"
                    }

                return (
                    df[column]
                    .dropna()
                    .unique()
                    .tolist()
                )


            elif operation == "value_counts":
                column = plan.get("column")

                if column not in df.columns:
                    return {
                        "error": f"Column '{column}' not found"
                    }

                return (
                    df[column]
                    .value_counts()
                    .to_dict()
                )


            elif operation == "sort":

                column = plan.get("column")

                if column not in df.columns:
                    return {
                        "error": f"Column '{column}' not found"
                    }

                ascending = plan.get(
                    "ascending",
                    True
                )

                n = int(
                    plan.get("n", 10)
                )

                return (
                    df.sort_values(
                        column,
                        ascending=ascending
                    )
                    .head(n)
                    .to_dict(orient="records")
                )


            elif operation == "filter":

                column = plan.get("column")
                value = plan.get("value")

                if column not in df.columns:
                    return {
                        "error": f"Column '{column}' not found"
                    }

                return (
                    df[df[column] == value]
                    .to_dict(orient="records")
                )


            elif operation == "groupby":

                group_column = plan.get(
                    "group_column"
                )

                value_column = plan.get(
                    "value_column"
                )

                aggregation = plan.get(
                    "aggregation",
                    "mean"
                )


                if (
                    group_column not in df.columns
                    or value_column not in df.columns
                ):
                    return {
                        "error": "Invalid groupby columns"
                    }


                grouped = (
                    df.groupby(group_column)[value_column]
                    .agg(aggregation)
                )

                return grouped.to_dict()


            else:
                return {
                    "error": f"Unsupported operation: {operation}"
                }


        except Exception as e:

            return {
                "error": str(e)
            }


engine = DataFrameEngine()