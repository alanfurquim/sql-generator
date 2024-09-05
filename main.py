"""
Python code used to create SQL statements based on excel files.

Working: Insert
Future Versions: Delete, Update
"""
import pandas as pd


def insert_generator(df, table_name, file_name, step=500):
    """
    This functions creates a SQL Insert code based
    on a pandas dataframe.

    df: pandas dataframe with all data
    table_name: name of the target table
    file_name: name of the file that will be generated
    step: if necessary, split dataframe into smaller parts,
    resulting in multiple smaller SQL insert statements
    """

    insert_statements = []

    for i in range(0, len(df), step):
        df_chunk = df.iloc[i:i + step]

        values_list = []
        for _, row in df_chunk.iterrows():
            values = ', '.join([f"'{str(x)}'" if isinstance(
                x, str) else str(x) for x in row.values])
            values_list.append(f"({values})")

        columns = ', '.join(df.columns)
        values_sql = ',\n'.join(values_list)
        insert_statement = f"INSERT INTO {table_name} ({columns}) VALUES\n{values_sql};\ncommit;\n"
        insert_statements.append(insert_statement)

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write("\n".join(insert_statements))


if __name__ == '__main__':
    df_path = ''
    df = pd.read_excel(df_path)
    table_name = df_path.replace('.xlsx', '').replace('.csv', '')
    file_name = df_path.replace('.xlsx', '').replace('.csv', '') + '.sql'

    # Gerar o arquivo SQL
    insert_generator(df, table_name, file_name)
