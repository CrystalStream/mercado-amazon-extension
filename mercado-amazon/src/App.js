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

function Product(props) {
  const { product } = props

  return (
    <>
      <li>
        <img src={product.img} alt={product.name} />
        <p>{ product.name }</p>
        <span>{ product.price }</span>
      </li>
    </>
  )
}

function ProductList(props) {
  const [ mlProducts, amznProducts ] = props.products

  return <>
    <ul>
      {
        mlProducts && mlProducts.map((e, i) => {
          return <Product key={i} product={e}/>
        })
      }
    </ul>
    <ul>
      {
        amznProducts && amznProducts.map((e, i) => {
          return <Product key={i} product={e}/>
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
      <ProductList products={products || [[],[]]} />
    </div>
  );
}

export default App
