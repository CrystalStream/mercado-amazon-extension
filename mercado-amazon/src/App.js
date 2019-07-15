import React, { useState } from 'react'
import './App.css'
import { SearchInput, ProductList } from './components'

function App() {
  const [ searchCriteria, onUpdateCriteria ] = useState('')
  const [ products, onUpdateProductList ] = useState([[],[]])

  return (
    <div className="App">
      <SearchInput onChange={onUpdateCriteria} onClick={onUpdateProductList} criteria={searchCriteria} />
      <ProductList products={products} />
    </div>
  );
}

export default App
