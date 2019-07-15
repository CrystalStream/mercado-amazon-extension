function fetchProducts(searchCriteria) {
  if (!searchCriteria) return null

  return fetch('http://localhost:5000/api/search?q=' + searchCriteria)
    .then(res => res.json())
    .then(res => {
      if (res.status_code === 200) {
        return res.results
      }
      return []
    })
    .catch(err => {
      return [{'message': err}]
    })
}

export default {
  fetchProducts
}
