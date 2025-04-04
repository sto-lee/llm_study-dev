import enum
from common.database.call_commector import get_connector

########################################################
# 비지니스 영역
########################################################
class SQLs(enum.Enum):
  select_actor_by_title = (enum.auto(), """
    SELECT date, symbol, price, vector 
    FROM stock_vectors 
    ORDER BY date DESC 
    LIMIT 5;
  """, "날짜별 주식 조회")


def excution_by_sql(sql_enum=SQLs.select_actor_by_title.name):
  conn = get_connector()
  sql = SQLs[sql_enum].value[1]
  df_data = conn.query(sql, ttl="10m")
  title_data = SQLs[sql_enum].value[2]
  return df_data, title_data

