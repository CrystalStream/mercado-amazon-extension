function fetchProducts(searchCriteria) {
  if (!searchCriteria) return null

  return fetch('http://localhost:5000/api/search?q=' + searchCriteria)
    .then(res => res.json())
    .then(res => {
      if (res.status_code === 200) {
        return res.results
      }
      console.error('Error[404] fetching products: ', res)
      return [[],[]]
    })
    .catch(err => {
      console.error('Error[500] fetching products: ', err)
      return [[],[]]
    })
}

export default {
  fetchProducts
}
