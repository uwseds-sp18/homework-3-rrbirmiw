def create_dataframe(filepath):
    import sqlite3
    import pandas as pd
    import sys
    try:
        conn = sqlite3.connect(filepath)
        query_str = """\
        SELECT video_id, category_id, 'US' as language FROM USvideos
        UNION
        SELECT video_id, category_id, 'CA' as language FROM CAvideos
        UNION
        SELECT video_id, category_id, 'FR' as language FROM FRvideos
        UNION
        SELECT video_id, category_id, 'DE' as language FROM DEvideos
        UNION
        SELECT video_id, category_id, 'GB' as language FROM GBvideos
        ;
        """

        return pd.read_sql_query(query_str, conn)
    except (sqlite3.Error , pd.io.sql.DatabaseError, TypeError) as e:
        raise ValueError("Invalid filepath")
        sys.exit(0)
