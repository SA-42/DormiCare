@router.post("/recommend, response_model = RecommendResponse)
def recommend(req: RecommendRequest) -> RecommendResponse:
  """Return the sleep tips most relevant to the query."""  
  results = recommender.recommend(req.query, top_k=req.top_k)
  return RecommendResponse(query=req.query, results=results)
