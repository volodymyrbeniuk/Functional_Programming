from lab import honor_roll, average_score
def test_pipeline_and_purity():
 rows=[{"name":" A ","score":95},{"name":"B","score":80}]
 assert honor_roll(rows)==[{"name":"A","score":95.0}]
 assert rows[0]["name"]==" A "
 assert average_score(rows)==87.5
