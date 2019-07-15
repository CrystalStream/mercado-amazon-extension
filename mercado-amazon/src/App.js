import React, { useState, useCallback } from 'react'
import './App.css'

function SearchInput(props) {
  const [isSending, setIsSending] = useState(false)
  const getProducts = useCallback(async () => {
    // don't send again while we are sending
    if (isSending) return
    // update state
    setIsSending(true)
    // send the actual request
    const products = await fetchProducts(props.criteria)
    props.onClick(products)
    // once the request is sent, update state again
    setIsSending(false)
  }, [isSending, props.criteria])

  return (
    <>
      <input onChange={e => props.onChange(e.target.value)} value={props.criteria} />
      <button onClick={getProducts}>Search</button>
    </>
  )
}

function ProductList(props) {
  return <>
    <ul>
      {
        props.products && props.products.map((e, i) => {
          return <li key={i}>test</li>
        })
      }
    </ul>
  </>
}

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

function App() {
  const [ searchCriteria, onUpdateCriteria ] = useState('')
  const [ products, onUpdateProductList ] = useState(null)

  return (
    <div className="App">
      <SearchInput onChange={onUpdateCriteria} onClick={onUpdateProductList} criteria={searchCriteria} />
      <ProductList products={products} />
    </div>
  );
}

export default App
